// Your task is to implement the function strstr. 
// The function takes two strings as arguments (s,x) and 
// locates the occurrence of the string x in the string s. 
// The function returns an integer denoting the first occurrence of the string x in s (0 based indexing).

// Note: You are not allowed to use inbuilt function.

// Input 1:  s = GeeksForGeeks, x = Fr
// Output:  -1

// Inout 2:  s = GeeksForGeeks, x = For
// Output:  5

// Input 3: s = QeYncKvfuYvWzGCxIpltSyycfQ, x = ycfQ
// Output:  22

int strstr(string s, string x) {
    int n = s.length(); // Length of the main string
    int m = x.length(); // Length of the substring to find
    int j = 0, k = 0; // j is the index for substring, k is the starting index of the match in the main string
    bool first = true; // Flag to check if it's the first matching character

    for (int i = 0; i < n; i++) {
        // If the entire substring has been matched
        if (j == m) {
            return k; // Return the starting index of the match
        }

        // If characters match, proceed with the next character
        if (s[i] == x[j]) {
            if (first) {
                k = i; // Save the starting index of the match
                first = false; // Set the flag to false after the first match
            }
            j++; // Move to the next character in the substring
        }
        // If the current character matches the first character of the substring
        // but it's not the first match, reset the substring index
        else if (s[i] == x && !first) {
            j = 1; // Start matching from the second character of the substring
            k = i; // Update the starting index of the match
        }
        // If characters do not match, reset the substring index and flag
        else {
            j = 0; // Reset the substring index
            first = true; // Reset the flag
        }
    }

    // Check if the substring was matched at the end of the loop
    if (j == m) {
        return k; // Return the starting index of the match
    }

    return -1; // Return -1 if the substring is not found
}
