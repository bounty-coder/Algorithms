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
}*head=NULL;
void create(int n)
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
void push()
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
void enqueue()
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
void insert(int pos)
{
    Node *temp=head,*sec;
    int i=1,v;
    while(i<pos)
    {
        i++;
        temp=temp->link;
        if(temp->link==NULL)
        {
            cout<<"\nPosition is out of LIST :(\n";
        }
    }
    cout<<"Enter data:";
    cin>>v;
    sec=new Node();
    sec->data=v;
    sec->link=temp->link;
    temp->link=sec;
}
void dequeue()
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
void pop()
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
void delete_node(int pos)
{
    Node *temp=head,*sec;
    int i=1;
    if(head==NULL)
    {
        cout<<"\nNo element left";
    }
    else
    {
        while(i<pos-1)
        {
            i++;
            temp=temp->link;
            if(temp->link->link==NULL)
            {
                cout<<"Entered position is OUT OF LIST";
                cout.flush();
                this_thread::sleep_for(chrono::seconds(2));
                system("CLS");
                cout<<"FUCK OFF!! You DUMBASS";
            }
        }
        sec=temp->link->link;
        free(temp->link);
        temp->link=sec;
    }
}
void printlist()
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
    Node *temp;
    int n,p,pos;
    char y;
    cout<<"Enter the number of elements in Linked List:";
    cin>>n;
    head=new Node();
    create(n);
    printlist();
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
                            <<"3.insert after a given node (position start from 1)"<<"\n";
                        cin>>p;
                        switch(p)
                        {
                            case 1: push();
                                    printlist();break;
                            case 2: enqueue();
                                    printlist();break;
                            case 3: cout<<"New node position:";
                                    cin>>pos;
                                    insert(pos);
                                    printlist();break;
                            default: cout<<"Wrong Choice YOU DUMBASS!!!";
                        }
                        break;
                case 2: cout<<"1.Delete the head"<<"\n"
                            <<"2.Delete the end"<<"\n"
                            <<"3.Delete a specific node (position start from 0)"<<"\n";
                        cin>>p;
                        switch(p)
                        {
                            case 1: dequeue();
                                    printlist(); break;
                            case 2: pop();
                                    printlist();break;
                            case 3: cout<<"Delete node position:";
                                    cin>>pos;
                                    delete_node(pos);
                                    printlist(); break;
                            default: cout<<"Wrong Choice YOU DUMBASS!!!  {:(";
                        }
                        break;
                case 3: printlist();
                        break;
                default: cout<<"Wrong Choice YOU DUMBASS!!!";
            }
    cout<<"\n\nWant to do more operations( Y/N ):";
    cin>>y;
    }while(y=='Y' || y=='y');
}
