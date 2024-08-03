// A celebrity is a person who is known to all but does not know anyone at a party.
//   A party is being organized by some people.  
//   A square matrix mat is used to represent people at the party such that 
// if an element of row i and column j is set to 1 it means ith person knows jth person. 
//   You need to return the index of the celebrity in the party, 
//   if the celebrity does not exist, return -1.

// Note: Follow 0-based indexing.

// Input: mat[][] = [[0 1 0],
//                 [0 0 0], 
//                 [0 1 0]]
// Output: 1
// Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity. 

//Take the sum of row, which will be >= col-1
// then check for the same row and its sum should be 0(celebrity doesn;t know anyone).
int celebrity(vector<vector<int> >& mat) {
    int m=mat.size();
    if(m<=0){
        return -1;
    }
    int n=mat[0].size();
    for(int i=0;i<n;i++){
        int x=0;
        for(int j=0;j<m;j++){
            if(mat[j][i]==1){
                x+=1;
            }
        }
        if(x>=m-1){
            int y=0;
            for(int k=0;k<n;k++){
                if(mat[i][k]==1){
                    y+=1;
                }
            }
            if(y==0)
            return i;
        }
    }
    return -1;
}

//In Python
/*
def celebrity(self, M, n):
    for i in range(n):
        sum_row=sum(M[i])
        sum_col=0
        for r in M:
            sum_col+=r[i]
            
        if sum_row==0 and sum_col==n-1:
            return i
    return -1
*/
