#include<iostream>
using namespace std;
int insertion(int arr[],int n)
{
    int temp;
    for(int i=1;i<n;i++)
    {
        for(int j=0;j<i;j++)
        {
            if(arr[j]>arr[i])
            {
                temp=arr[j];
                arr[j]=arr[i];
                arr[i]=temp;
            }
        }
    }
    return *arr;
}
int main()
{
    int n;
    cout<<"Enter number of element in array:";
    cin>>n;
    int arr[n];
    cout<<"Enter array:";
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    *arr=insertion(arr,n);
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<' ';
    }
}
