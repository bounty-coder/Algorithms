#include<iostream>
using namespace std;
void printarray(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
int merg(int arr[],int l,int m,int r,int n)
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
    while(i<p || j<q)
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
    printarray(arr,n);
}
int mergesort(int arr[],int l,int r,int n)
{
    int m=l+(r-l)/2;
    if(l>=r)
        {return;}

        mergesort(arr,l,m,n);
        mergesort(arr,m+1,r,n);
        merg(arr,l,m,r,n);

}

int main()
{
    int n,i;
    cout<<"Enter number of element:";
    cin>>n;
    int arr[n];
    cout<<"Enter array:";
    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    mergesort(arr,0,n-1,n);
    cout<<"Sorted Array is:";
    printarray(arr,n);
}
