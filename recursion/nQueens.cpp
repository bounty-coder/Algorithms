#include <iostream>
#include <vector>

using namespace std;

// Checks if placing a queen at row `row` and column `col` is safe
bool isSafe(vector<int>& queens, int row, int col) {
    // Check for attacks in the same column
    for (int i = 0; i < row; i++) {
        if (queens[i] == col) {
            return false;
        }
    }

    // Check for attacks in the diagonal directions
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (queens[i] == j) {
            return false;
        }
    }

    for (int i = row, j = col; i >= 0 && j < queens.size(); i--, j++) {
        if (queens[i] == j) {
            return false;
        }
    }

    return true;
}

// Recursively solves the n-queens problem
void solveNQueens(vector<int>& queens, int row, int n, vector<vector<int>>& solutions) {
    // If all rows have been placed, a solution has been found
    if (row == n) {
        solutions.push_back(queens);
        return;
    }

    // Try placing a queen in each column of the current row
    for (int col = 0; col < n; col++) {
        // If placing a queen at the current column is safe, place it and solve for the next row
        if (isSafe(queens, row, col)) {
            queens[row] = col;
            solveNQueens(queens, row + 1, n, solutions);
            queens[row] = -1; // Backtrack
        }
    }
}

int main() {
    int n;
    cout << "Enter the board size (n): ";
    cin >> n;

    // Create a vector to store the column positions of queens
    vector<int> queens(n, -1);
    vector<vector<int>> solutions;
    solveNQueens(queens, 0, n, solutions);

    cout << "Number of solutions: " << solutions.size() << endl;
    for (const auto& solution : solutions) {
        for (int queen : solution) {
            cout << queen + 1 << " ";
        }
        cout << endl;
    }

    return 0;
}
