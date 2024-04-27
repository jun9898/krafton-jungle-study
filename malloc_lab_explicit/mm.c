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

static void *find_fit(size_t asize);
static void *coalesce(void *bp);
static void place(void *bp, size_t allocated_size);
static void *extend_heap(size_t words);

static void remove_free_block(void *bp);
static void put_free_block(void *bp);

// Basic constants and macros
#define WSIZE               4                                                       // word = 4 byte
#define DSIZE               8                                                       // double word = 8 byte
#define CHUNKSIZE           (1 << 12)                                               // chunk size = 2^12 = 4096

#define MAX(x, y)           ((x) > (y) ? (x) : (y))                                 // x와 y 중 큰 값을 반환

// Pack a size and allocated bit into a word
#define PACK(size, alloc)   ((size) | (alloc))                                      // 크기 비트와 할당 비트를 통합해 header 및 footer에 저장할 수 있는 값 리턴

// Read and write a word at address p
#define GET(p)              (*(unsigned int *)(p))                                  // p가 참조하는 word를 읽어서 리턴 ((void*)라서 type casting 필요)
#define PUT(p, val)         (*(unsigned int *)(p) = (val))                          // p가 가리키는 word에 val 저장

// Read the size and allocated fields from address p
#define GET_SIZE(p)         (GET(p) & ~0x7)                                         // 사이즈 (뒤에 세자리 없어짐 -> 할당 여부와 무관한 사이즈를 반환)
#define GET_ALLOC(p)        (GET(p) & 0x1)                                          // 할당 여부 (마지막 한자리, 즉 할당 여부만 가지고 옴)

// Given block ptr bp, compute address of its header and footer
#define HDRP(bp)            ((char *)(bp) - WSIZE)                                  // 해당 블록의 header 주소를 반환 (payload 시작점인 bp에서 헤더 크기인 1 word를 뺀 값)
#define FTRP(bp)            ((char *)(bp) + GET_SIZE(HDRP(bp)) - DSIZE)             // 해당 블록의 footer 주소를 반환 (payload 시작점인 bp에서 블록 사이즈를 더한 뒤 2 word를 뺀 값)

// Given block ptr bp, compute address of next and previous blocks
#define NEXT_BLKP(bp)       ((char *)(bp) + GET_SIZE(((char *)(bp) - WSIZE)))       // 다음 블록의 bp를 반환 (현재 bp에서 해당 블록의 크기를 더해준 값)
#define PREV_BLKP(bp)       ((char *)(bp) - GET_SIZE(((char *)(bp) - DSIZE)))       // 이전 블록의 bp를 반환 (현재 bp에서 이전 블록의 크기를 빼준 값 -> DSIZE를 빼야 이전 블록의 정보를 가져올 수 있음!!)

/* single word (4) or double word (8) alignment */
// 정렬할 크기
#define ALIGNMENT 8

// **Explicit**
#define PRED_FREEP(bp)      (*(void **)(bp))                                        // 이전 가용 블록의 주소
#define SUCC_FREEP(bp)      (*(void **)(bp + WSIZE))                                // 다음 가용 블록의 주소

static char *heap_listp = NULL;         // 메모리 힙의 시작 주소
static char *free_listp = NULL;         // 가용 블록 리스트의 시작 부분

/* 
 * mm_init - initialize the malloc package.
 */
int mm_init(void)
{   
    // 기존 초기화는 4WSIZE면 됐지만 SUCC, PRED 포인터 추가로 6WSIZE
    if ((heap_listp = mem_sbrk(6 * WSIZE)) == (void *) -1) 
        return -1;
    // 공갈워드
    PUT(heap_listp, 0);     // 프롤로그 헤더 - 전체 사이즈가 커져서 * 2 해줘야함
    PUT(heap_listp + (1 * WSIZE), PACK(2 * DSIZE, 1));    // 프롤로그 PRED 포인터
    PUT(heap_listp + (2 * WSIZE), NULL);     // 프롤로그 SUCC 포인터
    PUT(heap_listp + (3 * WSIZE), NULL);     // 프롤로그 푸터 - 탐색 일관성 유지용
    PUT(heap_listp + (4 * WSIZE), PACK(2 * DSIZE, 1));        // 에필로그 헤더
    PUT(heap_listp + (5 * WSIZE), PACK(0, 1));
    free_listp = heap_listp + DSIZE;
    if (extend_heap(CHUNKSIZE/DSIZE) == NULL)
        return -1;
    return 0;
}

static void *extend_heap(size_t words) {
    char *bp;
    size_t size;

    // words가 홀수면 패딩 추가해주기
    size = (words % 2) ? (words + 1) * WSIZE : words * WSIZE;
    // brk 포인터 를 뒤로 밀어준다
    if ((bp = mem_sbrk(size)) == (void *)-1) {
        return NULL;
    }
    
    PUT(HDRP(bp), PACK(size, 0));
    PUT(FTRP(bp), PACK(size, 0));
    // 에필로그 헤더 세팅
    PUT(HDRP(NEXT_BLKP(bp)), PACK(0, 1));

    return coalesce(bp);
}

/* 
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    size_t asize;
    size_t extendsize;
    void *bp;

    if (size <= 0)
        return NULL;
    
    if (size <= DSIZE)
        asize = 2*DSIZE;
    else
        asize = DSIZE * ((size + (DSIZE) + (DSIZE - 1)) / DSIZE);
    
    if ((bp = find_fit(asize)) != NULL) {
        place(bp, asize);
        return bp;
    }

    extendsize = MAX(asize, CHUNKSIZE);
    if ((bp = extend_heap(extendsize/WSIZE)) == NULL)
        return NULL;
    place(bp, asize);
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

static void *coalesce(void *bp) {
    // 앞뒤 메모리가 사용중인지
    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp)));
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
    size_t size = GET_SIZE(HDRP(bp));

    // 전체적으로 연결 끊어주기만 추가해주면 됨
    if (prev_alloc && !next_alloc) {   // case2
        remove_free_block(NEXT_BLKP(bp));
        size += GET_SIZE(HDRP(NEXT_BLKP(bp)));
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
    }

    else if (!prev_alloc && next_alloc) {   // case3
        remove_free_block(PREV_BLKP(bp));
        size += GET_SIZE(HDRP(PREV_BLKP(bp)));
        bp = PREV_BLKP(bp);
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
    }

    else if (!prev_alloc && next_alloc) {    // case4
        remove_free_block(PREV_BLKP(bp));
        remove_free_block(NEXT_BLKP(bp));
        size += GET_SIZE(HDRP(PREV_BLKP(bp))) + GET_SIZE(FTRP(NEXT_BLKP(bp)));
        bp = PREV_BLKP(bp);
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
    }
    // 새로 추가된 가용 블록 리스트 처음에 넣어주기
    put_free_block(bp);
    return bp;
}


// void *mm_realloc(void *ptr, size_t size) {
//     if (ptr == NULL) {
//         return mm_malloc(size);
//     }
//     if (size == 0) {
//         mm_free(ptr);
//         return NULL;
//     }
//     size_t new_size = size + DSIZE;
//     void *oldptr = ptr;
//     void *newptr;
//     size_t original_size = GET_SIZE(HDRP(oldptr));
//     // 만약 즉시 할당 가능하면 pointer return
//     if (new_size <= original_size) {
//         return oldptr;
//     } else {
//         // 다음 블록 사이즈 확인
//         size_t next_size = original_size + GET_SIZE(HDRP(NEXT_BLKP(oldptr)));
//         // 다음 블록이 allocated 되어있지 않고 size의 합이 할당 가능한 영역이라면
//         if (!GET_ALLOC(HDRP(NEXT_BLKP(oldptr))) && (new_size <= next_size)) {
//             // allocated
//             PUT(HDRP(oldptr), PACK(next_size, 1));
//             PUT(FTRP(oldptr), PACK(next_size, 1));
//             return oldptr;
//         } else {
//             // 만약 기존 데이터에 할당이 불가능하다면
//             newptr = mm_malloc(new_size);
//             if (newptr == NULL) {
//                 return NULL;
//             }
//             memmove(newptr, oldptr, new_size);
//             mm_free(oldptr);
//             oldptr = NULL;
//             return newptr;
//         }
//     }
// }

void *mm_realloc(void *ptr, size_t size) {
    void *oldptr = ptr;
    void *newptr;
    size_t copySize;                        // 새 메모리 블록에 복사해야 할 데이터의 크기
    
    newptr = mm_malloc(size);               // 요청한 사이즈만큼 블록 할당
    if (newptr == NULL)
        return NULL;
    
    copySize = GET_SIZE(HDRP(oldptr));      // 이전 블록 사이즈를 copySize에 저장
    
    if (size < copySize)                    // 요청한 size가 원래 크기보다 작다면,
        copySize = size;                    // 기존 메모리 블록에서 일부만 복사해야 하므로 copySize를 요청한 크기로 설정
    
    memcpy(newptr, oldptr, copySize);       // 이전 블록에서 copySize만큼의 데이터를 새 블록에 복사
    mm_free(oldptr);                        // 기존 블록 free
    return newptr;                                          
}



static void *find_fit(size_t asize) {
    void *bp;
    // 모든 리스트에서 가용중인 리스트는 에필로그 헤더밖에 없음
    for (bp = free_listp; GET_ALLOC(HDRP(bp)) != 1; bp = SUCC_FREEP(bp)) {
        if (asize <= GET_SIZE(HDRP(bp))) {
            return bp;
        }
    }
    return NULL;
}


static void place(void* bp, size_t allocated_size) {
    size_t curr_size = GET_SIZE(HDRP(bp));
    // 데이터를 할당함으로 list에서 지워야함
    remove_free_block(bp);
    // Case 1. 남는 부분이 최소 블록 크기(16 bytes) 이상일 때 -> 블록 분할
    if ((curr_size - allocated_size) >= (2 * DSIZE)) {          // 남는 블록이 최소 블록 크기(16 bytes) 이상일 때 
        PUT(HDRP(bp), PACK(allocated_size, 1));                 // Header -> size와 allocated(1) 설정
        PUT(FTRP(bp), PACK(allocated_size, 1));                 // Footer -> size와 allocated(1) 설정
        bp = NEXT_BLKP(bp);                                     // bp 위치를 다음 블록 위치로 갱신
        // 블록 분할
        PUT(HDRP(bp), PACK(curr_size - allocated_size, 0));     // 남은 공간의 Header -> 남는 size와 free(0) 설정
        PUT(FTRP(bp), PACK(curr_size - allocated_size, 0));     // 남은 공간의 Footer -> 남는 size와 free(0) 설정
        // 분할된 값을 list에 추가
        put_free_block(bp);
    }
    // Case 2. 남는 부분이 최소 블록 크기(16 bytes) 미만일 때 -> 블록 분할 필요 X
    else {
        PUT(HDRP(bp), PACK(curr_size, 1));                      // 분할할 필요가 없다면, 그냥 할당
        PUT(FTRP(bp), PACK(curr_size, 1));
    }
}

static void put_free_block(void *bp) {
    // 기존 free_listp의 후임자로 bp를 설정해준다.
    SUCC_FREEP(bp) = free_listp;
    PRED_FREEP(bp) = NULL;
    PRED_FREEP(free_listp) = bp;
    free_listp = bp;
}

static void remove_free_block(void *bp) {
    // 처음으로 할당되어 있는 메모리의 연결을 끊어줄때
    if (bp == free_listp) {
        // 후임자의 전임자 연결 끊기
        PRED_FREEP(SUCC_FREEP(bp)) = NULL;
        free_listp = SUCC_FREEP(bp);
    } else {
        // 연결 끊어주기
        SUCC_FREEP(PRED_FREEP(bp)) = SUCC_FREEP(bp);
        PRED_FREEP(SUCC_FREEP(bp)) = PRED_FREEP(bp);
    }
}