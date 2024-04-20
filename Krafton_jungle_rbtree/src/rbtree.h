#ifndef _RBTREE_H_
#define _RBTREE_H_

#include <stddef.h>

typedef enum { RBTREE_RED, RBTREE_BLACK } color_t;	// 색깔은 red또는 black으로만 설정

typedef int key_t;	// key의 자료형은 int로 선언

typedef struct node_t {
  color_t color;	// 노드 색
  key_t key;		// 노드 값
  struct node_t *parent, *left, *right;	// 노드 부모, 왼쪽 자식, 오른쪽 자식
} node_t;

typedef struct {
  node_t *root;	// 루트노드
  node_t *nil;  // 경계노드
} rbtree;

rbtree *new_rbtree(void);		// 트리 생성
void delete_rbtree(rbtree *);	// 할당된 메모리 해제

node_t *rbtree_insert(rbtree *, const key_t);		// 노드 삽입
node_t *rbtree_find(const rbtree *, const key_t);	// 노드 찾기
node_t *rbtree_min(const rbtree *);					// 트리의 최솟값 찾기
node_t *rbtree_max(const rbtree *);					// 트리의 최댓값 찾기
int rbtree_erase(rbtree *, node_t *);				// 노드 삭제

int rbtree_to_array(const rbtree *, key_t *, const size_t);	// 오르차순 정렬

#endif