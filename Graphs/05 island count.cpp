// This is same as python one, but with a little but different approach

void dfs(vector<vector<char>> &grid, vector<vector<bool>> &visited, int i, int j,int n,int m){
        if(i<0 || i>=n) return;
        if(j<0 || j>=m) return;
        // if(!visited[i][j])  return;
        visited[i][j]=true;
        for(int x=-1;x<=1;x++){
            for(int y=-1;y<=1;y++){
                int row = x+i;
                int col = y+j;
                if(row<0 || row>=n)continue;
                if(col<0 || col>=m)continue;
                if(!visited[row][col] && grid[row][col]=='1'){
                    dfs(grid,visited,row,col,n,m);
                }
            }
        }
        return;
    }
    
    // Function to find the number of islands.
    int numIslands(vector<vector<char>>& grid) {
        int count=0;
        int n=grid.size();
        int m=grid[0].size();
        vector<vector<bool>> visited(n,vector<bool>(m,false));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]=='0'){
                    visited[i][j]=true;
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(!visited[i][j]){
                    dfs(grid,visited,i,j,n,m);
                    count++;
                }
            }
        }
        return count;
    }
