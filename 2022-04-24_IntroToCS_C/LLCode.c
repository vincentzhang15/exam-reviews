#include <stdio.h>
#include <stdlib.h>

typedef struct LLNode
{
    int data;
    struct LLNode *next;
} LLNode;


LLNode *newNode(int data)
{
    LLNode *n = (LLNode *)calloc(1, sizeof(LLNode));
    n->data = data;
    n->next = NULL;
    return n;
}

void printLL(LLNode *h)
{
    printf("=============== LL ==========\n");
    if(!h) { printf("NULL\n"); return; }
    for(LLNode *n=h; n; n=n->next)
    {
        if(!h) printf("null\n");
        else printf("DATA: %d\n", n->data);
    }
    printf("============================\n");
}

LLNode *insertHead(LLNode *h, int data)
{
    LLNode *n= newNode(data);
    if(!h) return n;

    n->next = h;
    return n;
}

LLNode *insertTail(LLNode *h, int data)
{
    LLNode *n= newNode(data);
    if(!h) return n;

    LLNode *i=h;
    for(;i->next;i=i->next) {}
    i->next = n;
    return h;
}

int length(LLNode *h)
{
    int i=0;
    for(;h;i++,h=h->next) {}
    return i;
}

LLNode *insertPos(LLNode *h, int data, int pos)
{
    LLNode *n= newNode(data);
    if(!h) return n;
    if(pos<=0) {h=insertHead(h, data); return h;}
    int len = length(h);
    if(pos>=len) {h=insertTail(h, data); return h;}
    
    LLNode *p =h;
    for(int i=0; i<pos-1; i++, p=p->next) {}
    n->next = p->next;
    p->next = n;
    return h;
}

void deleteNode(LLNode *n)
{
    if(!n) return;
    n->next = NULL;
    free(n);
    n = NULL;
    return;
}
LLNode *deleteHead(LLNode *h)
{
    if(!h) return NULL;
    LLNode *t = h->next;
    deleteNode(h);
    return t;
}

LLNode *deleteTail(LLNode *h)
{
    if(!h) return NULL;

    LLNode *p = h;
    LLNode *i = h->next;
    if(!i)
    {
        deleteNode(p);
        return h;
    }

    for(;i->next; i=i->next) {}
    deleteNode(i);
    p->next = NULL;
    return h;
}

LLNode *deletePos(LLNode *h, int pos)
{
    if(!h) return NULL;
    if(pos<=0) {h=deleteHead(h); return h;}
    int len = length(h);
    if(pos >= len) {h=deleteTail(h); return h;}

    LLNode *t = h;
    for(int i=0; i<pos-1; i++, t=t->next) {}
    LLNode *n = t->next;
    t->next = t->next->next;
    deleteNode(n);    
    return h;
}

LLNode *deleteData(LLNode *h, int data)
{
    if(!h) return NULL;
    if(h->data == data) { LLNode *t = h->next; deleteHead(h); return t; }

    LLNode *p = h;
    LLNode *c = h->next;
    for(;c;p=p->next, c=c->next)
    {
        if(c->data == data)
        {
            p->next = c->next;
            deleteNode(c);
            return h;
        }
    }
    return h;
}

LLNode *deleteAll(LLNode *h)
{
    while(h)
    {
        LLNode *t = h->next;
        deleteNode(h);
        h =t;
    }
    return h;
}

LLNode *reverse(LLNode *h)
{
    if(!h || !h->next) return h;
    LLNode *p = NULL;
    LLNode *c = h;
    LLNode *n = NULL;
    while(c)
    {
        n = c->next;
        c->next = p;
        p = c;
        c = n;
    }
    return p;
}

void split(LLNode *h, LLNode **a, LLNode **b)
{
    LLNode *mid = h;
    LLNode *end = h->next;

    while(end)
    {
        end = end ->next;
        if(end)
        {
            end = end->next;
            mid = mid->next;
        }
    }

    *a = h;
    *b = mid->next;
    mid->next = NULL;
}
LLNode *merge(LLNode *a, LLNode *b)
{
    LLNode *h = NULL;

    if(!a) return b;
    if(!b) return a;

    if(a->data > b->data)
    {
        h = b;
        h->next = merge(a, b->next);
    }
    else
    {
        h =a ;
        h->next = merge(a->next, b);
    }

    return h;
}
LLNode *mergeSort(LLNode *h)
{
    if(!h || !h->next) return h;

    LLNode *a = NULL;
    LLNode *b = NULL;


    split(h, &a, &b);
    a = mergeSort(a);
    b = mergeSort(b);
    h = merge(a, b);
    return h;
}

int main(void)
{
    printf("PROGRAM START\n");
    LLNode *head = NULL;
    /*
    LLNode *head = insertPos(NULL, 1, 100);


    head = insertPos(head, 2, 100);
    head = insertPos(head, 3, -22);
    printLL(head);
    
    head = deleteAll(head);
    printLL(head);

    head = insertPos(head, 1, 0);
    head = insertPos(head, 2, 1);
    head = insertPos(head, 3, 2);
    head = insertPos(head, 4, 1);
    printLL(head);

    head = deletePos(head, -11);
    printLL(head);

    head = deletePos(head, 1);
    printLL(head);

    head = deletePos(head, 100);
    printLL(head);

    head = deleteAll(head);
    printLL(head);


    head = insertPos(head, 1, 0);
    head = insertPos(head, 2, 1);
    printLL(head);

    head = reverse(head);
    printLL(head);

    head = deleteAll(head);
    printLL(head);
    */

    head = insertPos(head, 1, 0);
    head = insertPos(head, 2, 1);
    head = insertPos(head, 3, 2);
    head = insertPos(head, 4, 3);
    head = insertPos(head, 5, 3);
    //printLL(head);

    head = reverse(head);
    printLL(head);

    head = mergeSort(head);
    printLL(head);

    printf("PROGRAM END\n");

    return 0;
}