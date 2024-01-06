// Stack in cpp STL
/* push(element) - insert element, 
   pop() - deleted top element
   top() - displays top element
   empty() - checks if stack is empty
*/

// Stack Sorting will include, similar to bubble sort
// code from line60
//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

class SortedStack{
public:
	stack<int> s;
	void sort();
};

void printStack(stack<int> s)
{
    while (!s.empty())
    {
        printf("%d ", s.top());
       	s.pop();
    }
    printf("\n");
}

int main()
{
int t;
cin>>t;
while(t--)
{
	SortedStack *ss = new SortedStack();
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
	int k;
	cin>>k;
	ss->s.push(k);
	}
	ss->sort();
	printStack(ss->s);
}
}
// } Driver Code Ends


/*The structure of the class is
class SortedStack{
public:
	stack<int> s;
	void sort();
};
*/

/* The below method sorts the stack s 
you are required to complete the below method */
void stackinsert(stack<int> &s,int &temp){
   if(s.empty() || temp>=s.top()){
       s.push(temp);
       return;
   }
   int temp2=s.top();
   s.pop();
   stackinsert(s,temp);
   s.push(temp2);
   return;
}

void SortedStack :: sort()
{
    if(s.empty()){
       return;
    }
    
    int temp=s.top();
    s.pop();
    sort();
    stackinsert(s,temp);
    return;
}
