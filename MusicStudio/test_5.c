#include<stdio.h>
#include<stdlib.h>
#include <stddef.h>
#define m 3 
#define n 5 
#define MAXN 100

#define False 0
#define True 1

int Allocation[n][m] = {{0,1,0},{2,0,0},{3,0,2},{2,1,1},{0,0,2}} ;   //可用资源，m个资源类型
int Max[n][m] = {{7,5,3},{3,2,2},{9,0,2},{2,2,2},{4,3,3}} ;          // n个进程提交的最大资源需求，n*m矩阵
int Available[m] = {3,3,2};                                          //n个进程已获得的资源，n*m矩阵
int Need[n][m] = {{7,4,3},{1,2,2},{6,0,0},{0,1,1},{4,3,1}} ; 

void ShowData() 
{ 
    int i,j;
    printf("Describe:\n"); 

    printf("Avaliable: ");
    for (j=0;j<m;j++)
    {
        printf("%d ", Avaliable[j]);
    }
    printf("\n");

    printf("|Proc\t|Max\t|Alloc\t|Need\n"); 
    for(i=0;i<n;i++)
    { 
        printf("|%d\t|",i);

        for(j=0;j<m;j++)
        {
            printf("%d ",Max[i][j]);
        }

        printf("\t|"); 

        for(j=0;j<m;j++)
        {
            printf("%d ",Allocation[i][j]);
        }

        printf("\t|");
         
        for(j=0;j<m;j++)
        {
            printf("%d ",Need[i][j]);
        }

        printf("\n");
    } 
}

int Compare(int Work[],int i)
{
    int j;
    for(j=0;j<m;j++)
    {
        if(Work[j]<Need[i][j]) return 0;
    }
    return 1;
}

void Release(int Work[],int i)
{
    int j;
    for(j=0;j<m;j++)
    {
        Work[j]+=Allocation[i][j];
    }
}

int SafeDection() 
{ 
    int i,j,k;
    int Security[MAXN];
    int Work[MAXM];   
    int Finish[MAXN];  

    for (i=0;i<N;i++)
    {
        Finish[i]=False;
    }

    for (j=0;j<M;j++) 
    {
        Work[j]=Avaliable[j];
    } 

    for(i=0,k=0;i<N;i++)
    {  
        if(Finish[i]==False)
        {      
            if(Compare(Work,i)==True)
            {
                Release(Work,i);
                Finish[i]=True;
                Security[k++]=i;
                if(k==N) break;
                i=-1;
            }
        }
    }

    for(i=0;i<N;i++)
    { 
        if(Finish[i]==False)
        { 
            printf("system is not safe!\n");
            return False; 
        } 
    } 
    printf("system is safe!\n");
    printf("safe sequence: "); 
    for(i=0;i<N;i++)
    {
        printf("%d",Security[i]); 
        if(i<N-1) printf("->"); 
    } 
    printf("\n"); 
    return True; 
} 

int main(){
    ShowData();
    return 0;
}
