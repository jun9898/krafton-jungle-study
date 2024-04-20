#include "rbtree.h"

#include <limits.h>
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
			} if (new_node == new_node->parent->right)
			{
				new_node = new_node->parent;
				// 펴주기
				left_rotate(t, new_node);
			}
			new_node->parent->color = RBTREE_BLACK;
			new_node->parent->parent->color = RBTREE_RED;
			right_rotate(t, new_node->parent->parent);
		}
		else
		{
			node_t *uncle_node = new_node->parent->parent->left;
			if (uncle_node->color == RBTREE_RED)
			{
				new_node->parent->color = RBTREE_BLACK;
				new_node->parent->parent->color = RBTREE_RED;
				uncle_node->color = RBTREE_BLACK;
				new_node = new_node->parent->parent;
				continue;
			}
			else if (new_node == new_node->parent->left)
			{
				new_node = new_node->parent;
				right_rotate(t, new_node);
			}
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
    // TODO: implement find
    node_t *cur = t->root;
    while (cur != t->nil)
    {
        if (cur->key == key)
        {
            return cur;
        }
        else if (cur->key < key)
        {
            cur = cur->right;
        }
        else
        {
            cur = cur->left;
        }
    }
    return NULL;
}

node_t *smallest_value(node_t *cur_node, node_t *nil)
{
    if (cur_node == nil) {
        return nil;
    }
    node_t *left_node = smallest_value(cur_node->left, nil);
    node_t *right_node = smallest_value(cur_node->right, nil);

    if (left_node == nil && right_node == nil) {
        return cur_node;
    }

    node_t *smallest = cur_node;
    if (left_node != nil && left_node->key < smallest->key) {
        smallest = left_node;
    }
    if (right_node != nil && right_node->key < smallest->key) {
        smallest = right_node;
    }

    return smallest;
}

node_t * greatest_value(node_t *cur_node, node_t *nil)
{
    if (cur_node == nil) {
        return cur_node;
    }
    node_t *left_node = greatest_value(cur_node->left, nil);
    node_t *right_node = greatest_value(cur_node->right, nil);

    if (cur_node->key >= left_node->key && cur_node->key >= right_node->key)
        return cur_node;
    else if (left_node->key >= cur_node->key && left_node->key >= right_node->key)
        return left_node;
    else
        return right_node;
}

node_t *rbtree_min(const rbtree *t)
{
    node_t* res_node = smallest_value(t->root, t->nil);
	return res_node;
}

node_t *rbtree_max(const rbtree *t)
{
    node_t* res_node = greatest_value(t->root, t->nil);
	return res_node;
}

void rb_transplant(rbtree *t, node_t *u, node_t *v){
    // 만약 삭제 노드가 root면
    if (u->parent == t->nil) {
        t->root = v;
    // 부모기준 왼쪽이면
    } else if (u == u->parent->left) {
        u->parent->left = v;
    // 부모기준 오른쪽이면
    } else {
        u->parent->right = v;
    }
    // 양방향 매핑
    v->parent = u->parent;
    // 최종 삭제는 밖에서
}

node_t * find_successor(node_t *cur_node, node_t *nil) {
    cur_node = cur_node->right;
    while (cur_node->left != nil) {
        cur_node = cur_node->left;
    }
    return cur_node;
}

void rbtree_erase_fixup(rbtree *t, node_t *x) {
    while (x != t->root && x->color == RBTREE_BLACK) {
        // 대체 노드가 왼쪽에 있을때
        if (x == x->parent->left) {
            node_t *w = x->parent->right;
            // 삼촌 노드의 색이 빨강일 경우 부모와 삼촌 노드의 색을 바꾸고 왼쪽으로 rotate
            if (w->color == RBTREE_RED) {
                w->color = RBTREE_BLACK;
                x->parent->color = RBTREE_RED;
                left_rotate(t, x->parent);
                // 회전 후 삼촌 노드의 위치를 재조정
                w = x->parent->right;
            }
            if (w->left->color == RBTREE_BLACK && w->right->color == RBTREE_BLACK) {
                w->color = RBTREE_RED;
                x = x->parent;
            // 만약 왼쪽 red 오른쪽 black이면
            } else {
                if (w->right->color == RBTREE_BLACK) {
                    // 색 변경
                    w->left->color = RBTREE_BLACK;
                    w->color = RBTREE_RED;
                    // 돌리고 오른 자식이 red가 되게끔 만든다.
                    right_rotate(t, w);
                    w = x->parent->right;
                }
                // 최종적으로 오른쪽 자식이 red일때 작업을 수행 "깜부깜"
                w->color = x->parent->color;
                x->parent->color = RBTREE_BLACK;
                w->right->color = RBTREE_BLACK;
                left_rotate(t, x->parent);
                // 깜깜부가 수행되면 사실상 노드의 정렬이 끝났다고 봐도 무방함
                x = t->root;
            }   
        // 대체 노드가 오른쪽에 있을때 -> 정반대
        } else {
            node_t *w = x->parent->left;
            // 삼촌 노드의 색이 빨강일 경우 부모와 삼촌 노드의 색을 바꾸고 왼쪽으로 rotate
            if (w->color == RBTREE_RED) {
                w->color = RBTREE_BLACK;
                x->parent->color = RBTREE_RED;
                right_rotate(t, x->parent);
                // 회전 후 삼촌 노드의 위치를 재조정
                w = x->parent->left;
            }
            if (w->left->color == RBTREE_BLACK && w->right->color == RBTREE_BLACK) {
                w->color = RBTREE_RED;
                x = x->parent;
            // 만약 왼쪽 red 오른쪽 black이면
            } else {
                if (w->left->color == RBTREE_BLACK) {
                    // 색 변경
                    w->right->color = RBTREE_BLACK;
                    w->color = RBTREE_RED;
                    // 돌리고 오른 자식이 red가 되게끔 만든다.
                    left_rotate(t, w);
                    w = x->parent->left;
                }
                // 최종적으로 오른쪽 자식이 red일때 작업을 수행 "깜부깜"
                w->color = x->parent->color;
                x->parent->color = RBTREE_BLACK;
                w->left->color = RBTREE_BLACK;
                right_rotate(t, x->parent);
                // 깜깜부가 수행되면 사실상 노드의 정렬이 끝났다고 봐도 무방함
                x = t->root;
            }   
        }
    }
    // 트리는 무조건 black
    x->color = RBTREE_BLACK;
}

int rbtree_erase(rbtree *t, node_t *z)
{
    node_t *y = z;
    // 최초 target node 색깔 저장
    color_t y_original_color = y->color;
    // 대체 노드 초기화
    node_t *x;
    // 자식이 하나만 있는 경우
    if (z->left == t->nil) {
        x = z->right;
        rb_transplant(t, z, z->right);
    } else if (z->right == t->nil) {
        x = z->left;
        rb_transplant(t, z, z->left);
    } else {
        // 후임자 탐색
        y = find_successor(z, t->nil);
        y_original_color = y->color;
        // 한번밖에 안들어가면 대체할 노드는 그대로
        x = y->right;
        // 만약 edge가 내려갔으면
        if (y->parent == z) {
            x->parent = y;
        } else {
            // 후임자의 오른쪽을 기존 후임자 노드 위치로 이동
            rb_transplant(t, y, y->right);
            // 후임자와 target node의 위치를 swap할 준비
            y->right = z->right;
            y->right->parent = y;
        }
        // target node와 후임자의 노드를 swap
        rb_transplant(t, z, y);
        // target의 속성을 물려받음
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }
    // 자유
    free(z);
    
    // 대참사 발생
    if (y_original_color == RBTREE_BLACK) {
        // 대체 노드부터 fixup
        rbtree_erase_fixup(t, x);
    }
	return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n)
{
	// TODO: implement to_array
	return 0;
}


void rbtree_to_print(node_t *t, node_t *nil)
{
    // TODO: implement to_print
    if (t == nil)
    {
        printf("노드 바닥이에용\n");
        return;
    }
    printf("key = %d, color = %d \n", t->key, t->color);
    rbtree_to_print(t->left, nil);
    rbtree_to_print(t->right, nil);
}