#include <bits/stdc++.h>
#include<iostream>
#include <thread>
#include <chrono>
using namespace std;
class Node
{
    public:
        int data;
        Node *link;
};
void create(Node *head,int n)
{
    Node *temp,*sec;
    int i,v;
    cout<<"\nInsert List"<<endl;
    if(head==NULL)
    {
        cout<<"No space, PLEASE FUCK OFF!!";
        return;
    }
    else
    {
        cout<<"Enter data:";
        cin>>v;
        head->data=v;
        temp=head;
        i=1;
        while(i<n)
        {
            sec=new Node();
            cin>>v;
            sec->data=v;
            temp->link=sec;
            temp=sec;
            i++;
        }
        sec=NULL;
        temp->link=sec;
        delete sec;
    }
}
void push(Node* head)
{
    Node *temp;
    temp= new Node();
    int v;
    cout<<"Enter Data:";
    cin>>v;
    temp->data=v;
    temp->link=head;
    head=temp;
}
void enqueue(Node *head)
{
    Node *temp,*sec;
    int v;
    temp=head;
    while(temp->link!=NULL)
    {
        temp=temp->link;
    }
    cout<<"Enter Data:";
    cin>>v;
    sec=new Node();
    sec->data=v;
    temp->link=sec;
}
void dequeue(Node *head)
{
    Node *temp=head;
    if(temp==NULL)
    {
        cout<<"NO elements left";
    }
    else
    {
        if(temp->link!=NULL)
        {
            temp=temp->link;

            head=temp;
        }
        else
        {
            cout<<"Element deleted is "<<head->data;
            delete head;
        }
    }
}
void pop(Node *head)
{
    Node *temp;
    temp=head;
    if(temp==NULL)
    {
        cout<<"NO elements left to pop out";
    }
    else
    {
        while(temp->link->link!=NULL)
        {
            temp=temp->link;
        }
        temp->link=NULL;
    }
}
void printlist(Node* head)
{
    Node* temp;
    cout<<"\n\nLinked List:";
    temp=head;
    if(temp==NULL)
    {
        cout<<"Linked list is empty";
    }
    else
    {
        while(temp!=NULL)
        {
            cout<<temp->data<<"->";
            temp=temp->link;
        }
        cout<<"NULL";
    }
}
int main()
{
    Node *head=NULL,*temp;
    int n,p;
    char y;
    cout<<"Enter the number of elements in Linked List:";
    cin>>n;
    head=new Node();
    create(head,n);
    printlist(head);
    cout.flush();
    this_thread::sleep_for(chrono::seconds(1));
    system("CLS");
    cout<<"\n\t\t******LINKED LIST MENU******\n\n\n";
    do{
            cout<<"1.Insert a new node"<<"\n"
                <<"2.Delete a node"<<"\n"
                <<"3.Display List"<<"\n\n";
            cin>>n;
            switch(n)
            {
                case 1: cout<<"1.Insert the node at head"<<"\n"
                            <<"2.Insert at the end"<<"\n"
                            <<"3.insert after a given node"<<"\n";
                        cin>>p;
                        switch(p)
                        {
                            case 1: push(head);
                                    printlist(head);break;
                            case 2: enqueue(head);
                                    cout<<"\n\nNew Linked is:";
                                    printlist(head);break;
                            case 3:
                                    cout<<"\n\nNew Linked is:";
                            printlist(head);break;
                            default: cout<<"Wrong Choice YOU DUMBASS!!!";
                        }
                        break;
                case 2: cout<<"1.Delete the head"<<"\n"
                            <<"2.Delete the end"<<"\n"
                            <<"3.Delete a specific node"<<"\n";
                        cin>>p;
                        switch(p)
                        {
                            case 1: dequeue(head);
                                    printlist(head); break;
                            case 2: pop(head);
                                    printlist(head);break;
                            case 3: printlist(head); break;
                            default: cout<<"Wrong Choice YOU DUMBASS!!!  {:(";
                        }
                        break;
                case 3: printlist(head);
                        break;
                default: cout<<"Wrong Choice YOU DUMBASS!!!";
            }
    cout<<"\n\nWant to do more operations( Y/N ):";
    cin>>y;
    }while(y=='Y' || y=='y');
}
