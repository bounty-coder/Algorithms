#include<iostream>
using namespace std;
int selection(int arr[],int n)
{
    int temp,m,k;
    for(int i=0;i<n;i++)
    {
        m=arr[i];k=i;
        for(int j=i+1;j<n;j++)
        {
            if(m>arr[j])
            {
                m=arr[j];
                k=j;
            }
        }
        temp=arr[i];
        arr[i]=arr[k];
        arr[k]=temp;
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
    *arr=selection(arr,n);
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<' ';
    }
}
