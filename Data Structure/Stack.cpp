#include<iostream>
using namespace std;
class node{
public:
    int data;
    node *link;
}*top=NULL;
void push()
{
    node *temp;
    int v;
        temp=new node();
        cout<<"Enter data:";
        cin>>v;
        temp->data=v;
        temp->link=top;
        top=temp;

}
void pop()
{
    if(top==NULL)
    {
        cout<<"Stack Underflow!!\n";
    }
    else
    {
        top=top->link;
    }
}
void peep()
{
    if(top==NULL)
    {
        cout<<"Stack OVERFLOW!! \nNo space available";
    }
    else
    {
        cout<<"\nTop element is "<<top->data;
    }
}
void printlist()
{
    node *temp;
    temp=top;
    if(top==NULL)
    {
        cout<<"Nothing to display";
    }
    else
    {
        cout<<"Stack element :";
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
    int c;
    char y;
    top=new node();
    cout<<"\t\t****STACK IMPLEMENTATION****\n\n";
    do
    {
        cout<<"1.Push in stack\n"
        <<"2.Pop in stack\n"
        <<"3.Peep\n4.Display Stack"<<endl;
        cin>>c;
        switch(c)
        {
            case 1: push();
                    printlist();break;
            case 2: pop();
                    printlist(); break;
            case 3: peep();break;
            case 4: printlist(); break;
            default: cout<<"Wrong Choice";
        }
        cout<<"Want to continue: (y/n)";
        cin>>y;
    }while(y=='y' || y=='Y');
}
