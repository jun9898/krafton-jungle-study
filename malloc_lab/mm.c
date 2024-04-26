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


// 답지
void *mm_realloc(void *ptr, size_t size)
{
    if (ptr == NULL)
    {
        return mm_malloc(size);
    }
    if (size == 0)
    {
        mm_free(ptr);
        return NULL;
    }
    void *oldptr = ptr;
    void *newptr;
    size_t copySize = GET_SIZE(HDRP(oldptr));
    if (size + DSIZE <= copySize)
    {
        return oldptr;
    }
    else
    {
        size_t next_size = copySize + GET_SIZE(HDRP(NEXT_BLKP(oldptr)));
        if (!GET_ALLOC(HDRP(NEXT_BLKP(oldptr))) && (size + DSIZE <= next_size))
        {
            PUT(HDRP(oldptr), PACK(next_size, 1));
            PUT(FTRP(oldptr), PACK(next_size, 1));
            return oldptr;
        }
        else
        {
            newptr = mm_malloc(size + DSIZE);
            if (newptr == NULL)
            {
                return NULL;
            }
            memmove(newptr, oldptr, size + DSIZE); // Corrected memcpy size using MIN macro
            mm_free(oldptr);
            return newptr;
        }
    }
}

/*
 * mm_realloc - Implemented simply in terms of mm_malloc and mm_free
 */
// void *mm_realloc(void *ptr, size_t size) {
//     void *oldptr = ptr;
//     void *newptr;
//     size_t original_size = GET_SIZE(HDRP(oldptr));  // 원본 사이즈
//     size_t new_size;                 // 새로운 사이즈

//     if (size <= DSIZE)
//         new_size = 2*DSIZE;
//     else
//         new_size = DSIZE * ((size + (DSIZE) + (DSIZE - 1)) / DSIZE);

//     // 만약 새로운 크기가 원래 크기보다 작다면, 기존 블록을 그대로 사용
//     if (new_size <= original_size) {
//         // 분할 체크
//         place(oldptr, new_size);
//         return oldptr;
//     }

//     // 만약 새로운 크기가 원래 크기보다 크다면 메모리 영역을 확장
//     int flag;
//     size_t tmp_size;
//     do {
//         tmp_size = GET_SIZE(HDRP(ptr));
//         PUT(HDRP(ptr), PACK(tmp_size, 0));
//         PUT(FTRP(ptr), PACK(tmp_size, 0));
//         flag = realloc_coalesce(ptr);
//     } while(flag != 0);


//     size_t realloc_coalesce_size = GET_SIZE(HDRP(ptr));
//     if (new_size <= realloc_coalesce_size) {
//         place(ptr, new_size);
//         memmove(ptr, oldptr, original_size);
//         return ptr;
//     }

//     // 만약 새로운 크기도 부족하다면
//     newptr = mm_malloc(size);
//     if (newptr == NULL) {
//         return NULL; // 할당 실패
//     }

//     // 이전 데이터 복사
//     memmove(newptr, oldptr, original_size);

//     // 이전 메모리 블록 해제
//     mm_free(oldptr);
//     return newptr;
// }


// 표준
// void *mm_realloc(void *ptr, size_t size)
// {

//     void *oldptr = ptr;
//     void *newptr;
//     size_t copySize;
    
//     newptr = mm_malloc(size);
//     if (newptr == NULL)
//       return NULL;
//     copySize = GET_SIZE(HDRP(oldptr));
//     if (size < copySize)
//       copySize = size;
//     memcpy(newptr, oldptr, copySize);
//     mm_free(oldptr);
//     return newptr;
// }

static int realloc_coalesce(void *bp) {
    // 앞뒤 메모리가 사용중인지
    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp)));
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
    size_t size = GET_SIZE(HDRP(bp));

    if (prev_alloc && next_alloc) {         // case1
        printf("==============test=================");
        return 0;
    }

    else if (prev_alloc && !next_alloc) {   // case2
        size += GET_SIZE(HDRP(NEXT_BLKP(bp)));
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
        return 1;
    }

    else if (!prev_alloc && next_alloc) {   // case3
        size += GET_SIZE(HDRP(PREV_BLKP(bp)));
        PUT(FTRP(bp), PACK(size, 0));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));
        bp = PREV_BLKP(bp);
        return 1;
    }

    else {                                  // case4
        size += GET_SIZE(HDRP(PREV_BLKP(bp))) + GET_SIZE(FTRP(NEXT_BLKP(bp)));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));
        PUT(FTRP(NEXT_BLKP(bp)), PACK(size, 0));
        bp = PREV_BLKP(bp);
        return 1;
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
static void *find_fit(size_t asize) {
    void *bp;
    // 에필로그 헤더는 size가 0임으로 해당 조건에 걸림
    for (bp = heap_listp; GET_SIZE(HDRP(bp)) > 0; bp = NEXT_BLKP(bp)) {
        if (!GET_ALLOC(HDRP(bp)) && (asize <= GET_SIZE(HDRP(bp)))) {
            return bp;
        }
    }
    return NULL;
}


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
// static void *find_fit(size_t asize) {

//     void *bp;
//     void *old_ptr = next_listp;

//     for (bp = next_listp; GET_SIZE(HDRP(bp)) > 0; bp = NEXT_BLKP(bp)) {
//         if (!GET_ALLOC(HDRP(bp)) && (asize <= GET_SIZE(HDRP(bp)))) {
//             next_listp = NEXT_BLKP(bp);
//             return bp;
//         }
//     }

//     for (bp = heap_listp; bp < old_ptr; bp = NEXT_BLKP(bp)) {
//         if (!GET_ALLOC(HDRP(bp)) && (asize <= GET_SIZE(HDRP(bp)))) {
//             next_listp = NEXT_BLKP(bp);
//             return bp;
//         }
//     }
//     return NULL;
// }


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













