#include<iostream>
using namespace std;
int swap(int *a,int *b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
int quicksort(int arr[],int low,int high)
{
    if(low<high)
    {
        int pivot=arr[high];/*Taking last element as pivot*/
        int j=low-1,temp;
        for(int i=low;i<high;i++)
        {
            if(arr[i]<pivot)
            {
                ++j;
                swap(&arr[i],&arr[j]);
            }
        }
        swap(&arr[j+1],&arr[high]);
        quicksort(arr,low,j);
        quicksort(arr,j+2,high);
    }
    return *arr;
}


int main()
{
    int n,i;
    cout<<"Enter number of elements:";
    cin>>n;
    int arr[n];
    cout<<"Enter array:";
    for(i=0;i<n;++i)
    {
        cin>>arr[i];
    }
    *arr=quicksort(arr,0,n-1);
    cout<<"Sorted array:";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<' ';
    }
}
