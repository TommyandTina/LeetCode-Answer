#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct Stack {
    struct TreeNode* data[10000];
    int top;
};

void push(struct Stack* stack, struct TreeNode* node) {
    stack->data[stack->top++] = node;
}

struct TreeNode* pop(struct Stack* stack) {
    return stack->data[--stack->top];
}

bool isEmpty(struct Stack* stack) {
    return stack->top == 0;
}

int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    struct Stack stack;
    stack.top = 0;
    int* result = (int*)malloc(10000 * sizeof(int));
    *returnSize = 0;
    if (root != NULL) {
        push(&stack, root);
    }
    while (!isEmpty(&stack)) {
        struct TreeNode* node = pop(&stack);
        result[(*returnSize)++] = node->val;
        if (node->right != NULL) {
            push(&stack, node->right);
        }
        if (node->left != NULL) {
            push(&stack, node->left);
        }
    }
    return result;
}

int main() {
    struct TreeNode n1, n2, n3;
    n1.val = 1; n1.left = NULL; n1.right = &n2;
    n2.val = 2; n2.left = &n3; n2.right = NULL;
    n3.val = 3; n3.left = NULL; n3.right = NULL;
    int returnSize;
    int* result = preorderTraversal(&n1, &returnSize);
    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }
    free(result);
    return 0;
}
