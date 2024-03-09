//usage of streamstring

//it is a stream class operating on strings.
// Operator >> Extracts formatted data.
// Operator << Inserts formatted data.

//if ss is streamstring object having 
//ss("My name is anthony gonsalves")
//ss<<s;
//cout<<s; =>  My

#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    stringstream ss(str);
    vector<int> x;
    string i;
    while(getline(ss,i,',')){
        x.push_back(stoi(i));
    }
    return x;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    return 0;
}
