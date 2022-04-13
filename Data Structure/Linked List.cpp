#include<iostream>
using namespace std;
class node{
    public:
        int data;
        node *link;
};
int main()
{
    int n,a;
    node *head=NULL;
    node *second= NULL;
    node *third= NULL;
    cout<<"/t/t/tLINKED LIST/n/n/n";
    head= new node();
    cout<<"Enter data:";
    cin>>a;
    head->data=a;
    second= new node();
    third= new node();
    head->link=second;
    cout<<"Enter data:";
    cin>>a;
    second->data=a;
    second->link= third;
    cout<<"Enter data:";
    cin>>a;
    third->data=a;
    third->link= NULL;
    node *temp;
    temp=head;
    while(temp!=NULL)
    {
        cout<<temp->data;
        temp=temp->link;
    }
}
