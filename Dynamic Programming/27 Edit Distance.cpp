// Given two strings str1 and str2.
//Return the minimum number of operations required to convert str1 to str2.
// The possible operations are permitted:

// Insert a character at any position of the string.
// Remove any character from the string.
// Replace any character from the string with any other character.

// Input: str1 = "geek", srt2 = "gesek"
// Output: 1
// Explanation: One operation is required, inserting 's' between two 'e'.

/* 
  1. Base conditions:
    -    If str1 and str2 are NULL "", then 0
    -    If str1 is "" and str2!=empty, then str2.length()
    -    If str1!=empth and str2 is "", then str1.length()
  2. If both not empty:
    -    if str1[i]==str[j], then check for earlier elements 
         i.e. (i-1,j-1), whatever be the edit distance for them it'll be the answer.
    -    else check for min([i-1][j],[i-1][j-1],[i][j-1]) and add 1 to it.
*/
int editDistance(string str1, string str2){
    int n = str1.length();
    int m = str2.length();
    vector<vector<int>> dp(n+1,vector<int>(m+1,0));

    for(int i=0;i<n+1;i++){
        for(int j=0;j<m+1;j++){
            if(i==0 && j==0){
                dp[i][j]=0;
            }
            else if(i==0){
                dp[i][j]=j;
            }
            else if(j==0){
                dp[i][j]=i;
            }
            else if(str1[i-1]==str2[j-1]){
                dp[i][j]=dp[i-1][j-1];
            }
            else{
                dp[i][j]=min({dp[i-1][j],dp[i-1][j-1],dp[i][j-1]})+1;
            }
        }
    }
    return dp[n][m];
}
