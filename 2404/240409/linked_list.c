#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//
// Created by 전병준 on 24. 4. 9.
//
typedef struct NODE{
    int data;
    struct NODE* next;
} node;

node* list;

// append_left 방식
void add(int key) {
    node *new_node;
    new_node = (node *) malloc(sizeof(node)); //    노드의 크기만큼 메모리 할당 및 노드 생성
    new_node->data = key;
    new_node->next = NULL;

    if (list == NULL) {
        list = new_node;
    } else {
        new_node->next = list;
        list = new_node;
    }
}

// 정렬하며 노드를 삽입하는 방법
void ascending_order_add(int key) {
    node *new_node; // 노드 초기화
    new_node = (node *) malloc(sizeof(node)); //    노드의 크기만큼 메모리 할당 및 노드 생성
    new_node->data = key;
    new_node->next = NULL;

    if (list == NULL) { // list가 비어있으면
        list = new_node;
    } else {
        node* cur = list; // 첫번째 노드
        node* prev = NULL;

        if (cur -> data > new_node -> data) { // 만약 새로 추가한 노드가 가장 작은 수를 가졌으면
            new_node -> next = cur;
            list = new_node;
        } else {
            while (cur != NULL && cur -> data < new_node -> data) {
                prev = cur;
                cur = cur-> next;
            }
            if (cur != NULL) {
                new_node -> next = cur;
                prev -> next = new_node;
            } else {
                prev -> next = new_node;
            }
        }
    }
}

// unique key값만 추가하는 로직
void add_unique(int key) {
    node *new_node; // 노드 초기화
    new_node = (node *) malloc(sizeof(node)); //    노드의 크기만큼 메모리 할당 및 노드 생성
    new_node->data = key;
    new_node->next = NULL;

    if (list == NULL) { // 만약 list가 비어있으면
        list = new_node;
    } else {
        node* cur = list; // 현재 노드

        while (cur != NULL) {
            if (cur -> data == key) {
                return;
            }
            cur = cur -> next;
        }

        new_node -> next = list;
        list = new_node;
    }
}

bool remove_node(int key) {

    if (list == NULL) {
        return false;
    }

    if (list -> data == key) { // 첫번째 요소가 key와 일치하면
        node* cur = list;
        list = list -> next;
        free(cur);
        return true;
    }
    else {
        node* cur = list -> next;
        node* prev = list;
        while (cur != NULL && cur -> data != key) {
            prev = cur;
            cur = cur -> next;
        }
        if (cur == NULL) return false; // 만약 탐색을 마쳤는데 일치하는 값이 없으면

        prev -> next = cur -> next;
        free(cur);
        return true;
    }
}

int main(void) {
//    단순히 값을 추가
//    add(10);
//    add(20);
//    add(30);
//    add(40);
//    add(50);
//    add(60);

//    오름차순으로 값을 추가
//    ascending_order_add(50);
//    ascending_order_add(20);
//    ascending_order_add(30);
//    ascending_order_add(10);
//    ascending_order_add(90);
//    ascending_order_add(70);

//    unique key값만 추가
//    add_unique(10);
//    add_unique(10);
//    add_unique(10);
//    add_unique(10);
//    add_unique(10);
//    add_unique(10);
//    add_unique(10);
//    add_unique(10);
//    add_unique(10);

    node* curr = list;
    while(curr != NULL) {
        printf("%d\n", curr->data);
        curr = curr->next;
    }
    return 0;
}
