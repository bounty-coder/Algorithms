#include<bits/stdc++.h>
using namespace std;

void merg(int arr[],int l,int m,int r)
{
    int i,j,p=m-l+1, q=r-m;
    int left[p],right[q];
    for(i=0;i<p;i++)
    {
        left[i]=arr[l+i];
    }
    for(j=0;j<q;j++)
        right[i]=arr[m+1+j];
    i=0;j=0;
    int k=l;
    while(i<p and j<q)
    {
        if(left[i]<=right[j])
        {
            arr[k]=left[i];
            i++;
        }
        else
        {
            arr[k]=right[j];
            j++;
        }
        k++;
    }
    while (i<p)
    {
        arr[k]=left[i];
        i++;k++;
    }
    while( j< q)
    {
        arr[k]=right[j];
        j++;k++;
    }
}
void mergesort(int arr[],int l,int r)
{
    int m=l+(r-l)/2;
    if(l>=r)
    {   return;
    }
        mergesort(arr,l,m);
        mergesort(arr,m+1,r);
        merg(arr,l,m,r);

}
void printarray(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main()
{
    int arr[]={3,5,1,7,89,55,23,99};
    int n=sizeof(arr)/sizeof(arr[0]);
    cout<<"Enter array:";
    printarray(arr,n);
    mergesort(arr,0,n);
    cout<<"Sorted Array is:";
    printarray(arr,7);
}
