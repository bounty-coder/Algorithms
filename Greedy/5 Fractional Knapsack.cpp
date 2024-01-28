// https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

/*Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
    Input:
  N = 3, W = 50
  value[] = {60,100,120}
  weight[] = {10,20,30}
  Output:
  240.000000  */

// we can cut the items, that means we can take the items in ratio.. in whatever ratio we want.

#include <bits/stdc++.h>
using namespace std;

struct Item{
    int value;
    int weight;
};


struct Item{
    int value;
    int weight;
};
class Solution
{
    public:
    double fractionalKnapsack(int W, Item arr[], int n)
    {
        vector<pair<double,int>> ratio;
        for(int i=0;i<n;i++){
            double x = (double)arr[i].value/arr[i].weight;
            ratio.push_back(make_pair(x,i));
        }
        sort(ratio.rbegin(),ratio.rend()); // sort in descending order
    
        double knap=0;
        for(int i=0;i<n && W>0;i++){
            if(W>=arr[ratio[i].second].weight){
                knap+=arr[ratio[i].second].value;
                W-=arr[ratio[i].second].weight;
            }
            else{
                knap+=W*ratio[i].first;
                W-=W;
            }
        }
        return knap;
    }
};

int main()
{
	int t;
	//taking testcases
	cin>>t;
	cout<<setprecision(6)<<fixed;
	while(t--){
	    //size of array and weight
		int n, W;
		cin>>n>>W;
		
		Item arr[n];
		//value and weight of each item
		for(int i=0;i<n;i++){
			cin>>arr[i].value>>arr[i].weight;
		}
		
		//function call
		Solution ob;
		cout<<ob.fractionalKnapsack(W, arr, n)<<endl;
	}
    return 0;
}
