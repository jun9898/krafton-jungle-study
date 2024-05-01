/*
 * mm-naive.c - The fastest, least memory-efficient malloc package.
 * 
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free.
 *
 * NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your solution.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>

#include "mm.h"
#include "memlib.h"

/* single word (4) or double word (8) alignment */
#define ALIGNMENT 8

/* rounds up to the nearest multiple of ALIGNMENT */
#define ALIGN(size) (((size) + (ALIGNMENT - 1)) & ~0x7)

#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))

/*********************************************************
 * NOTE TO STUDENTS: Before you do anything else, please
 * provide your team information in the following struct.
 ********************************************************/
team_t team = {
    /* Team name */
    "ateam",
    /* First member's full name */
    "Harry Bovik",
    /* First member's email address */
    "bovik@cs.cmu.edu",
    /* Second member's full name (leave blank if none) */
    "",
    /* Second member's email address (leave blank if none) */
    ""
};

/* 
 * mm_init - initialize the malloc package.
 */
int mm_init(void)
{   
    if ((heap_listp = mem_sbrk(4*WSIZE)) == (void *) -1) 
        return -1;
    // 공갈워드
    PUT(heap_listp, 0);
    // 프롤로그 헤더
    PUT(heap_listp + (1*WSIZE), PACK(DSIZE, 1));
    // 프롤로그 헤더2 - 탐색 일관성 유지용
    PUT(heap_listp + (2*WSIZE), PACK(DSIZE, 1));
    // 에필로그 헤더
    PUT(heap_listp + (3*WSIZE), PACK(0, 1));
    // 탐색 시작점 설정
    heap_listp += (2*WSIZE);

    // next_fit을 위한 포인터 설정
    next_listp = heap_listp;

    if (extend_heap(CHUNKSIZE/WSIZE) == NULL)
        return -1;
    return 0;
}

/* 
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    size_t asize;
    size_t extendsize;
    char *bp;

    if (size == 0)
        return NULL;
    
    if (size <= DSIZE)
        asize = 2*DSIZE;
    else
        asize = DSIZE * ((size + (DSIZE) + (DSIZE - 1)) / DSIZE);
    
    if ((bp = find_fit(asize)) != NULL) {
        place(bp, asize);

        // next_fix을 위한 설정
        next_listp = bp;

        return bp;
    }

    extendsize = MAX(asize, CHUNKSIZE);
    if ((bp = extend_heap(extendsize/WSIZE)) == NULL)
        return NULL;
    place(bp, asize);

    // next_fix을 위한 설정
    next_listp = bp;

    return bp;
}

/*
 * mm_free - Freeing a block does nothing.
 */
void mm_free(void *bp)
{
    size_t size = GET_SIZE(HDRP(bp));

    PUT(HDRP(bp), PACK(size, 0));
    PUT(FTRP(bp), PACK(size, 0));
    coalesce(bp);
}


void *mm_realloc(void *ptr, size_t size) // 재할당
{
    if (ptr == NULL) // 입력 포인터가 NULL이면, 입력 사이즈만큼 새롭게 할당 (예외처리)
    {
        return mm_malloc(size);
    }
    
    if (size == 0) // 입력 사이즈가 0이면, 입력 포인터의 블록을 해제 (예외처리)
    {
        mm_free(ptr);
        return NULL;
    }

    void *oldptr = ptr;
    size_t original_size = GET_SIZE(HDRP(oldptr)); // 재할당하려는 블록의 사이즈
    
    if (size + DSIZE <= original_size) // (재할당 하려는 블록 사이즈 + 8 bytes(Header + Footer)) <= 현재 블록 사이즈
    {
        return oldptr; // 현재 블록에 재할당해도 문제 없기 때문에, 포인터만 반환
    }
    else // (재할당 하려는 블록 사이즈 + 8 bytes) > 현재 블록 사이즈
         // 경우에 따라서 인접 Free block을 활용하는 방안과, 새롭게 할당하는 방안을 이용해야 함
    {
        size_t next_size = original_size + GET_SIZE(HDRP(NEXT_BLKP(oldptr))); // 현재 블록 사이즈 + 다음 블록 사이즈 = next_size
        size_t prev_size = GET_SIZE(HDRP(PREV_BLKP(oldptr))); // 이전 블록 사이즈

        if (!GET_ALLOC(HDRP(NEXT_BLKP(oldptr))) && (size + DSIZE <= next_size)) 
        // 다음 블록이 Free block이고, (재할당 하려는 블록의 사이즈 + 8 bytes) <= (현재 블록 사이즈 + 다음 블록 사이즈)
        // 현재 블록과 다음 블록을 하나의 블록으로 취급해도 크기의 문제가 발생하지 않음
        // malloc을 하지 않아도 됨 -> 메모리 공간 및 시간적 이득을 얻을 수 있음
        {
            PUT(HDRP(oldptr), PACK(next_size, 1)); // 현재 블록의 Header Block에, (현재 블록 사이즈 + 다음 블록 사이즈) 크기와 Allocated 상태 기입
            PUT(FTRP(oldptr), PACK(next_size, 1)); // 현재 블록의 Footer Block에, (현재 블록 사이즈 + 다음 블록 사이즈) 크기와 Allocated 상태 기입
            next_listp = oldptr; // next_fit 사용을 위한 포인터 동기화
            return oldptr;
        }
        else if (!GET_ALLOC(HDRP(PREV_BLKP(oldptr))) && (size + DSIZE <= prev_size + original_size))
        // 이전 블록이 Free block이고, (재할당 하려는 블록의 사이즈 + 8 bytes) <= (이전 블록 사이즈 + 현재 블록 사이즈)
        // 이전 블록과 현재 블록을 하나의 블록으로 취급해도 크기의 문제가 발생하지 않음
        // malloc을 하지 않아도 됨 -> 메모리 공간 및 시간적 이득을 얻을 수 있음
        {
            void *prev_ptr = PREV_BLKP(oldptr); // 이전 블록의 bp
            
            memmove(prev_ptr, oldptr, original_size); // 이전 블록의 bp로 현재 block의 메모리 영역을 옮긴다
            PUT(HDRP(prev_ptr), PACK(prev_size + original_size, 1)); // 이전 블록의 Header Block에, (이전 블록 사이즈 + 현재 블록 사이즈) 크기와 Allocated 상태 기입
            PUT(FTRP(prev_ptr), PACK(prev_size + original_size, 1)); // 이전 블록의 Footer Block에, (이전 블록 사이즈 + 현재 블록 사이즈) 크기와 Allocated 상태 기입
            next_listp = prev_ptr; // next_fit 사용을 위한 포인터 동기화
            return prev_ptr;
        }
        else if (!GET_ALLOC(HDRP(NEXT_BLKP(oldptr))) && !GET_ALLOC(HDRP(PREV_BLKP(oldptr))) && (size + DSIZE <= next_size + original_size + prev_size))
        // 이전 블록과 다음 블록이 모두 Free block, (재할당 하려는 블록의 사이즈 + 8 bytes) <= (이전 블록 사이즈 + 현재 블록 사이즈 + 다음 블록 사이즈)
        // 이전 블록과 현재 블록과 다음 블록을 하나의 블록으로 취급해도 크기의 문제가 발생하지 않음
        // malloc을 하지 않아도 됨 -> 메모리 공간 및 시간적 이득을 어등ㄹ 수 있음
        {
            void *prev_ptr = PREV_BLKP(oldptr); // 이전 블록의 bp

            memmove(prev_ptr, oldptr, original_size); // 이전 블록의 bp로 현재 block의 메모리 영역을 옮긴다
            PUT(HDRP(prev_ptr), PACK(prev_size + original_size + next_size, 1)); // 이전 블록의 Header Block에, (이전 블록 사이즈 + 현재 블록 사이즈 + 다음 블록 사이즈) 크기와 Allocated 상태 기입
            PUT(FTRP(prev_ptr), PACK(prev_size + original_size + next_size, 1)); // 이전 블록의 Footer Block에, (이전 블록 사이즈 + 현재 블록 사이즈 + 다음 블록 사이즈) 크기와 Allocated 상태 기입
            next_listp = prev_ptr; // next_fit 사용을 위한 포인터 동기화
            return prev_ptr;
        }
                
        else // 위 케이스에 모두 해당되지 않아, 결국 malloc을 해야 하는 경우
        {
            void *newptr;
            newptr = mm_malloc(size + DSIZE); // (할당하려는 크기 + 8 bytes)만큼 새롭게 할당
            if (newptr == NULL) // 새로 할당한 주소가 NULL일 경우 (예외처리)
            {
                return NULL;
            }
            memmove(newptr, oldptr, size + DSIZE); // payload 복사
            next_listp = newptr; // next_fit 사용을 위한 포인터 동기화
            mm_free(oldptr); // 기존의 블록은 Free block으로 바꾼다
            return newptr; // 새롭게 할당된 주소의 포인터를 반환
        }
    }
}

static void *coalesce(void *bp) {
    // 앞뒤 메모리가 사용중인지
    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp)));
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
    size_t size = GET_SIZE(HDRP(bp));

    if (prev_alloc && next_alloc) {         // case1

        // next_fix을 위한 설정
        next_listp = bp;

        return bp;
    }

    else if (prev_alloc && !next_alloc) {   // case2
        size += GET_SIZE(HDRP(NEXT_BLKP(bp)));
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
    }

    else if (!prev_alloc && next_alloc) {   // case3
        size += GET_SIZE(HDRP(PREV_BLKP(bp)));
        PUT(FTRP(bp), PACK(size, 0));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));
        bp = PREV_BLKP(bp);
    }

    else {                                  // case4
        size += GET_SIZE(HDRP(PREV_BLKP(bp))) + GET_SIZE(FTRP(NEXT_BLKP(bp)));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));
        PUT(FTRP(NEXT_BLKP(bp)), PACK(size, 0));
        bp = PREV_BLKP(bp);
    }

    // next_fix을 위한 설정
    next_listp = bp;

    return bp;
}

static void *extend_heap(size_t words) {
    char *bp;
    size_t size;

    // words가 홀수면 패딩 추가해주기
    size = (words % 2) ? (words + 1) * WSIZE : words * WSIZE;
    // brk 포인터 를 뒤로 밀어준다
    if ((long)(bp = mem_sbrk(size)) == -1)
        return NULL;
    
    PUT(HDRP(bp), PACK(size, 0));
    PUT(FTRP(bp), PACK(size, 0));
    // 에필로그 헤더 세팅
    PUT(HDRP(NEXT_BLKP(bp)), PACK(0, 1));

    return coalesce(bp);

}

// FIRST_FIT
// static void *find_fit(size_t asize) {
//     void *bp;
//     // 에필로그 헤더는 size가 0임으로 해당 조건에 걸림
//     for (bp = heap_listp; GET_SIZE(HDRP(bp)) > 0; bp = NEXT_BLKP(bp)) {
//         if (!GET_ALLOC(HDRP(bp)) && (asize <= GET_SIZE(HDRP(bp)))) {
//             return bp;
//         }
//     }
//     return NULL;
// }


// BEST_FIT
// static void *find_fit(size_t asize) {
//     void *bp;
//     void *best_p = NULL;
//     size_t min_size = SIZE_MAX;
//     // 에필로그 헤더는 size가 0임으로 해당 조건에 걸림
//     for (bp = heap_listp; GET_SIZE(HDRP(bp)) > 0; bp = NEXT_BLKP(bp)) {
//         if (!GET_ALLOC(HDRP(bp)) && (asize <= GET_SIZE(HDRP(bp))) && (min_size > GET_SIZE(HDRP(bp)))) {
//             best_p = bp;
//         }
//     }
//     if (best_p != NULL) {
//         return best_p;
//     } else {
//         return NULL;
//     }
// }


// NEXT_FIT
static void *find_fit(size_t asize) {

    void *bp;
    void *old_ptr = next_listp;

    for (bp = next_listp; GET_SIZE(HDRP(bp)) > 0; bp = NEXT_BLKP(bp)) {
        if (!GET_ALLOC(HDRP(bp)) && (asize <= GET_SIZE(HDRP(bp)))) {
            next_listp = NEXT_BLKP(bp);
            return bp;
        }
    }

    for (bp = heap_listp; bp < old_ptr; bp = NEXT_BLKP(bp)) {
        if (!GET_ALLOC(HDRP(bp)) && (asize <= GET_SIZE(HDRP(bp)))) {
            next_listp = NEXT_BLKP(bp);
            return bp;
        }
    }
    return NULL;
}


static void place(void* bp, size_t allocated_size) {
    size_t curr_size = GET_SIZE(HDRP(bp));
    // Case 1. 남는 부분이 최소 블록 크기(16 bytes) 이상일 때 -> 블록 분할
    if ((curr_size - allocated_size) >= (2 * DSIZE))            // 남는 블록이 최소 블록 크기(16 bytes) 이상일 때
    {
        PUT(HDRP(bp), PACK(allocated_size, 1));                 // Header -> size와 allocated(1) 설정
        PUT(FTRP(bp), PACK(allocated_size, 1));                 // Footer -> size와 allocated(1) 설정
        bp = NEXT_BLKP(bp);                                     // bp 위치를 다음 블록 위치로 갱신
        // 블록 분할
        PUT(HDRP(bp), PACK(curr_size - allocated_size, 0));     // 남은 공간의 Header -> 남는 size와 free(0) 설정
        PUT(FTRP(bp), PACK(curr_size - allocated_size, 0));     // 남은 공간의 Footer -> 남는 size와 free(0) 설정
    }
    // Case 2. 남는 부분이 최소 블록 크기(16 bytes) 미만일 때 -> 블록 분할 필요 X
    else
    {
        PUT(HDRP(bp), PACK(curr_size, 1));                      // 분할할 필요가 없다면, 그냥 할당
        PUT(FTRP(bp), PACK(curr_size, 1));
    }
}