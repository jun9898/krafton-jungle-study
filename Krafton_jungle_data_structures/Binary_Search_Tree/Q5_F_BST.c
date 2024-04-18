//////////////////////////////////////////////////////////////////////////////////

/* CE1007/CZ1007 Data Structures
Lab Test: Section F - Binary Search Trees Questions
Purpose: Implementing the required functions for Question 5
		 Implementing 'remove node' operation for BST*/
//////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>

//////////////////////////////////////////////////////////////////////////////////

typedef struct _bstnode{
	int item;
	struct _bstnode *left;
	struct _bstnode *right;
} BSTNode;   // You should not change the definition of BSTNode

typedef struct _stackNode{
	BSTNode *data;
	struct _stackNode *next;
}StackNode; // You should not change the definition of StackNode

typedef struct _stack
{
	StackNode *top;
}Stack; // You should not change the definition of Stack

///////////////////////// function prototypes ////////////////////////////////////

// You should not change the prototypes of these functions
void postOrderIterativeS2(BSTNode *root);

void insertBSTNode(BSTNode **node, int value);

void push(Stack *stack, BSTNode *node);
BSTNode *pop(Stack *s);
BSTNode *peek(Stack *s);
int isEmpty(Stack *s);
void removeAll(BSTNode **node);
BSTNode* removeNodeFromTree(BSTNode *root, int value);

///////////////////////////// main() /////////////////////////////////////////////

int main()
{
	int c, i;
	c = 1;

	//Initialize the Binary Search Tree as an empty Binary Search Tree
	BSTNode * root;
	root = NULL;

	printf("1: Insert an integer into the binary search tree;\n");
	printf("2: Print the post-order traversal of the binary search tree;\n");
	printf("3: Print the remove node from tree;\n");
	printf("0: Quit;\n");


	while (c != 0)
	{
		printf("Please input your choice(1/2/3/0): ");
		scanf("%d", &c);

		switch (c)
		{
		case 1:
			printf("Input an integer that you want to insert into the Binary Search Tree: ");
			scanf("%d", &i);
			insertBSTNode(&root, i);
			break;
		case 2:
			printf("The resulting post-order traversal of the binary search tree is: ");
			postOrderIterativeS2(root); // You need to code this function
			printf("\n");
			break;
		case 3:
			printf("Input an integer that you want to delete into the Binary Search Tree: ");
			scanf("%d", &i);
			postOrderIterativeS2(root); // You need to code this function
			break;
		case 0:
			removeAll(&root);
			break;
		default:
			printf("Choice unknown;\n");
			break;
		}

	}

	return 0;
}

//////////////////////////////////////////////////////////////////////////////////
void makeStack(Stack *s, BSTNode *cur) {
	if (cur == NULL) {
		return;
	}
	makeStack(s, cur->left);
	makeStack(s, cur->right);
	push(s, cur);
}

void postOrderIterativeS2(BSTNode *root)
{
	// use two stack
	Stack *s1 = (Stack *) malloc(sizeof(Stack));
	Stack *s2 = (Stack *) malloc(sizeof(Stack));

	s1->top = NULL;
	s2->top = NULL;

	makeStack(s1, root);

	while (s1->top != NULL) {
		push(s2, pop(s1));
	}

	while (s2->top != NULL) {
		printf("%d ", pop(s2)->item);
	}

	free(s1);
	free(s2);
}

BSTNode* findMinValue(BSTNode* node) {
    BSTNode* curr = node;
    while (curr->left != NULL) {
        curr = curr->left;
    }
    return curr;
}

BSTNode* removeNodeFromTree(BSTNode *root, int value)
{
    /* add your code here */
    // 1. 트리가 비어있다면 NULL 반환
    if (root == NULL)
        return NULL;
    // 2. 삭제할 노드 탐색 (재귀)
    if (value < root->item) {
        root->left = removeNodeFromTree(root->left, value);
    }
    else if (value > root->item) {
        root->right = removeNodeFromTree(root->right, value);
    }
    // 3. 삭제할 노드 찾았으면,
    else {
        // 3-1. 삭제할 노드의 자식이 없으면 걍 삭제 ㄱ
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }
        // 3-2. 삭제할 노드의 자식이 1개면?? 맞나??
        else if (root->left == NULL) {
            BSTNode* tmp = root->right;
            free(root);
            return tmp;
        }
        else if (root->right == NULL) {
            BSTNode* tmp = root->left;
            free(root);
            return tmp;
        }
        // 3-3. 삭제할 노드의 자식이 2개면,
        else {
            // 오른쪽 최솟값 올리고
            BSTNode* tmp = findMinValue(root->right);
            root->item = tmp->item;     // 값 갱신
            root->right = removeNodeFromTree(root->right, tmp->item);   // 오른쪽에서 재귀적으로 삭제 작업
        }
    }
    return root;
}

///////////////////////////////////////////////////////////////////////////////

void insertBSTNode(BSTNode **node, int value){
	if (*node == NULL)
	{
		*node = malloc(sizeof(BSTNode));

		if (*node != NULL) {
			(*node)->item = value;
			(*node)->left = NULL;
			(*node)->right = NULL;
		}
	}
	else
	{
		if (value < (*node)->item)
		{
			insertBSTNode(&((*node)->left), value);
		}
		else if (value >(*node)->item)
		{
			insertBSTNode(&((*node)->right), value);
		}
		else
			return;
	}
}

//////////////////////////////////////////////////////////////////////////////////

void push(Stack *stack, BSTNode * node)
{
	StackNode *temp;

	temp = malloc(sizeof(StackNode));

	if (temp == NULL)
		return;
	temp->data = node;

	if (stack->top == NULL)
	{
		stack->top = temp;
		temp->next = NULL;
	}
	else
	{
		temp->next = stack->top;
		stack->top = temp;
	}
}


BSTNode * pop(Stack * s)
{
	StackNode *temp, *t;
	BSTNode * ptr;
	ptr = NULL;

	t = s->top;
	if (t != NULL)
	{
		temp = t->next;
		ptr = t->data;

		s->top = temp;
		free(t);
		t = NULL;
	}

	return ptr;
}

BSTNode * peek(Stack * s)
{
	StackNode *temp;
	temp = s->top;
	if (temp != NULL)
		return temp->data;
	else
		return NULL;
}

int isEmpty(Stack *s)
{
	if (s->top == NULL)
		return 1;
	else
		return 0;
}


void removeAll(BSTNode **node)
{
	if (*node != NULL)
	{
		removeAll(&((*node)->left));
		removeAll(&((*node)->right));
		free(*node);
		*node = NULL;
	}
}
