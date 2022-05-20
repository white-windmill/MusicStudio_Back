#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 100
int n,l,r;
typedef struct node 
{
    int data,lchild,rchild;
}
btree;
btree t[MAX];
void create() 
{
    int i,lc,rc;
    scanf("%d",&n);
    for (i=1;i<=n;i++) 
    {
        scanf("%d%d",&lc,&rc);
        t[i].data=i;
        t[i].lchild=lc;
        t[i].rchild=rc;
    }
}
int dfs(int i) 
{
    if(t[i].data==0)
            return 0;
    if(t[i].lchild==0&&t[i].rchild==0)
            return 1; else 
    {
        l=dfs(t[i].lchild);
        r=dfs(t[i].rchild);
        if(l>r)
                    return l+1; else
                    return r+1;
    }
}
int main() 
{
    memset(t,0,sizeof(t));
    create();
    printf("%dn",dfs(1));
    return 0;
}