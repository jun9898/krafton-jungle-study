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

// 초기화
void init() {
    if (list == NULL) {
        return;
    } else {
        node* cur;
        cur = list;

        while (cur != NULL) {
            list = cur -> next;
            free(cur);
            cur = list;
        }
    }
}

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

void traverse() {
    node* cur = list;
    while (cur != NULL) {
        printf("%d ", cur->data);
        cur = cur -> next;
    }
    printf("\n");
}

int main(void) {

    int arr[9] = {2,4,1,2,6,7,8,3,6};
    int arr_duplicated[18] = { 2,2,1,1,6,2,8,7,6,4,2,5,6,3,7,8,3,9};
    int arr_rmv[4] = {2,9,8,100};

    init();
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); ++i) {
        add(arr[i]);
    }
    printf("After add(nomal) : ");
    traverse();

    init();
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); ++i) {
        ascending_order_add(arr[i]);
    }
    printf("After add(ascending) : ");
    traverse();

    init();
    for (int i = 0; i < sizeof(arr_duplicated) / sizeof(arr_duplicated[0]); ++i) {
        add_unique(arr_duplicated[i]);
    }
    printf("After add(unique) : ");
    traverse();

    for (int i = 0; i < sizeof(arr_rmv) / sizeof(arr_rmv[0]); ++i) {
        remove_node(arr_rmv[i]);
    }
    printf("After remove : ");
    traverse();

    return 0;
}
