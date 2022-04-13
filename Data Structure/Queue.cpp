#include<iostream>
using namespace std;
class node
{
public:
    int data;
    node *link;
}*frnt=NULL,*rear=NULL;
void queu()
{
    if()

}
void dequeue()
{

}
void display()
{

}
int main()
{
    head=new node();
    int n;
    char ch;
    cout<<"\t\t****QUEUE IMPLEMENTATION****\n\n";
    do
    {
        cout<<"1.Queue element\n"
            <<"2.Dequeue element\n"
            <<"3.Display Queue\n";
        cin>>n
        switch(n)
        {
            case 1: queu();
                    display();break;
            case 2: dequeue();
                    display(); break;
            case 3: display(); break;
            default:cout<<"\nWrong choice";
        }
        cout<<"\nWant to continue more (y/n):";
        cin>>ch;
    }while(y=='y' || y=='Y');
}
