#include "rbtree.h"

#include <stdio.h>
#include <stdlib.h>

// 왼쪽 회전
void left_rotate(rbtree *T, node_t *cur_node)
{
	node_t *target_node = cur_node->right;
	cur_node->right = target_node->left;
	if (target_node->left != T->nil)
	{
		target_node->left->parent = cur_node;
	}
	target_node->parent = cur_node->parent;
	// 만약 현재 노드가 root였다면
	if (cur_node->parent == T->nil)
	{
		T->root = target_node;
		// 만약 cur 노드가 parant 기준 왼쪽에 존재하면
	}
	else if (cur_node == cur_node->parent->left)
	{
		cur_node->parent->left = target_node;
		// 만약 cur 노드가 parant 기준 오른쪽에 존재하면
	}
	else
	{
		cur_node->parent->right = target_node;
	}
	target_node->left = cur_node;
	cur_node->parent = target_node;
}

void right_rotate(rbtree *T, node_t *cur_node)
{
	node_t *target_node = cur_node->left;
	cur_node->left = target_node->right;
	if (target_node->right != T->nil)
	{
		target_node->right->parent = cur_node;
	}
	target_node->parent = cur_node->parent;
	// 만약 현재 노드가 root였다면
	if (cur_node->parent == T->nil)
	{
		T->root = target_node;
		// 만약 cur 노드가 parant 기준 왼쪽에 존재하면
	}
	else if (cur_node == cur_node->parent->left)
	{
		cur_node->parent->left = target_node;
		// 만약 cur 노드가 parant 기준 오른쪽에 존재하면
	}
	else
	{
		cur_node->parent->right = target_node;
	}
	target_node->right = cur_node;
	cur_node->parent = target_node;
}

rbtree *new_rbtree(void)
{
	rbtree *p = (rbtree *)malloc(sizeof(rbtree));
	if (p == NULL)
	{
		perror("Failed to allocate memory for RB tree");
		exit(EXIT_FAILURE);
	}
	// TODO: initialize struct if needed
	p->nil = (node_t *)malloc(sizeof(rbtree));

	if (p->nil == NULL)
	{
		perror("Failed to allocate memory for sentinel node");
		exit(EXIT_FAILURE);
	}

	p->nil->color = RBTREE_BLACK;

	p->root = p->nil;

	return p;
}

void delete_rbtree_recursive(node_t *node, node_t *nil) {
	if (node == nil) {
		return;
	}
	delete_rbtree_recursive(node->left, nil);
	delete_rbtree_recursive(node->right, nil);
	free(node);
}

void delete_rbtree(rbtree *t)
{
	delete_rbtree_recursive(t->root, t->nil);
	free(t->nil);
	free(t);
}

void rbtree_insert_fixup(rbtree *t, node_t *new_node)
{
	while (new_node->parent->color == RBTREE_RED)
	{
		// 만약 부모 노드가 할아버지 노드 기준 왼쪽에 있을때
		if (new_node->parent == new_node->parent->parent->left)
		{
			node_t *uncle_node = new_node->parent->parent->right;
			// 만약 RB트리 부모와 삼촌 노드가 모두 RED일때 쭈왑
			if (uncle_node->color == RBTREE_RED)
			{
				new_node->parent->color = RBTREE_BLACK;
				new_node->parent->parent->color = RBTREE_RED;
				uncle_node->color = RBTREE_BLACK;
				new_node = new_node->parent->parent;
				// 바꿨으면 다시 반복문 초기화
				continue;
				// 만약 다른색이고 할아버지 노드와 부모 노드가 꺾여있다면
			}
			if (new_node == new_node->parent->right)
			{
				new_node = new_node->parent;
				// 펴주기
				left_rotate(t, new_node);
			}
			new_node->parent->color = RBTREE_BLACK;
			new_node->parent->parent->color = RBTREE_RED;
			right_rotate(t, new_node->parent->parent);
		}
		// 만약 부모 노드가 할아버지 노드 기준 오른쪽에 있을때
		else
		{
			node_t *uncle_node = new_node->parent->parent->left;
			// 만약 RB트리 부모와 삼촌 노드가 모두 RED일때 쭈왑
			if (uncle_node->color == RBTREE_RED)
			{
				new_node->parent->color = RBTREE_BLACK;
				new_node->parent->parent->color = RBTREE_RED;
				uncle_node->color = RBTREE_BLACK;
				new_node = new_node->parent->parent;
				// 바꿨으면 다시 반복문 초기화
				continue;
				// 만약 다른색이고 할아버지 노드와 부모 노드가 꺾여있다면
			}
			else if (new_node == new_node->parent->left)
			{
				new_node = new_node->parent;
				// 펴주기
				right_rotate(t, new_node);
			}
			// 색 바꾸고 전환
			new_node->parent->color = RBTREE_BLACK;
			new_node->parent->parent->color = RBTREE_RED;
			left_rotate(t, new_node->parent->parent);
		}
	}
	t->root->color = RBTREE_BLACK;
}

node_t *rbtree_insert(rbtree *t, const key_t key)
{
	node_t *new_node = (node_t *)malloc(sizeof(node_t));
	new_node->color = RBTREE_RED;
	new_node->key = key;
	new_node->left = new_node->right = t->nil;

	node_t *cur_node = t->root;
	node_t *prev_node = t->nil;

	while (cur_node != t->nil)
	{
		prev_node = cur_node;
		if (new_node->key < cur_node->key)
		{
			cur_node = cur_node->left;
		}
		else
		{
			cur_node = cur_node->right;
		}
	}
	new_node->parent = prev_node;
	// 만약 바로 반복문에 탈출했다면 루트라는 뜻
	if (prev_node == t->nil)
	{
		t->root = new_node;
	}
	else if (new_node->key < prev_node->key)
	{
		prev_node->left = new_node;
	}
	else
	{
		prev_node->right = new_node;
	}
	// 노드 삽입 후 트리 재정렬
	rbtree_insert_fixup(t, new_node);
	// TODO: implement insert
	return t->root;
}

node_t *rbtree_find(const rbtree *t, const key_t key) 
{
	node_t *cur_node = t->root;
	while (cur_node->key != key && cur_node != t->nil)
	{
		if (key < cur_node->key)
		{
			cur_node = cur_node->left;
		}
		else
		{
			cur_node = cur_node->right;
		}
	}
	if (cur_node == t->nil) {
		return NULL;
	}
	return cur_node;
}

node_t *rbtree_min(const rbtree *t)
{
	// TODO: implement find
	return t->root;
}

node_t *rbtree_max(const rbtree *t)
{
	// TODO: implement find
	return t->root;
}

int rbtree_erase(rbtree *t, node_t *p)
{
	// TODO: implement erase
	return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n)
{
	// TODO: implement to_array
	return 0;
}
