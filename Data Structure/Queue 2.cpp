#include<iostream>
using namespace std;
class node
{
public:
    int data;
    node *link;
    node(int v)
    {
        data=v;
        link=NULL;
    }
};
class queue
{
public:
    node *front;
    node *rear;
    queue()
    {
        front=NULL;
        rear=NULL;
    }
    void enqueue()
    {
        int v;
        node *nd;
        cout<<"Enter data:";
        cin>>v;
        nd=new node(v);
        nd->data=v;
        if(front==NULL)
        {
            rear=nd;
            front=nd;
            return;
        }
        rear->link=nd;
        rear=nd;
    }
    void dequeue()
    {
        if(front==NULL)
        {
            cout<<"No element.. Underflow!!";
            return;
        }
        node *del=front;
        front=front->link;
        delete del;
    }
    void peek()
    {
        if(front==NULL)
        {
            cout<<"No element in queue";
            return;
        }
        cout<<front->data;
    }
    bool isempty()
    {
        if(front==NULL)
        {
            return true;
        }
        return false;
    }
    void display()
    {
        node *nd;
        nd=front;
        while(nd!=NULL)
        {
            cout<<nd->data<<"->";
            nd=nd->link;
        }
        cout<<"NULL";
    }
};
int main()
{
    queue q;
    int n;
    char y;
    cout<<"\t\t****QUEUE IMPLEMETATION****\n\n";
    do
    {
        cout<<"1.Enqueue:\n"
            <<"2.Dequeue:\n"
            <<"3.Peek:\n"
            <<"4.isempty()\n"
            <<"5.Display\n";
        cin>>n;
        switch(n)
        {
            case 1: q.enqueue();
                    q.display();break;
            case 2: q.dequeue();
                    q.display(); break;
            case 3: q.peek();
                    break;
            case 4: cout<<q.isempty(); break;
            case 5: q.display(); break;
            default:cout<<"\nWrong choice";
        }
        cout<<"\nWant to continue more (y/n):";
        cin>>y;
    }while(y=='y' || y=='Y');
}
