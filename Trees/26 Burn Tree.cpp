/*
1) Find Target and Parent: Create a map to store parent-child relationships while searching for the target node using BFS.
2) Initialize BFS: Start BFS from the target node, keeping track of visited nodes and time.
3) Explore Neighbors: In each BFS iteration, explore the node's left, right, and parent if not visited.
4) Update Max Time: Update the maximum time if a new node is visited.
5) Return Max Time: The final maximum time is the minimum time to burn the entire tree.
*/

//User function Template for C++

/*
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution {
  public:
pair<Node*, unordered_map<Node*, Node*> > findTargetAndParent(Node* root, int target) {
    unordered_map<Node*, Node*> parent;
    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        Node* curr = q.front();
        q.pop();

        if (curr->data == target) {
            return make_pair(curr, parent);
        }

        if (curr->left) {
            parent[curr->left] = curr;
            q.push(curr->left);
        }
        if (curr->right) {
            parent[curr->right] = curr;
            q.push(curr->right);
        }
    }
    return make_pair(nullptr, parent);
}

int minTime(Node* root, int target) {
    pair<Node*, unordered_map<Node*, Node*> > result = findTargetAndParent(root, target);
    Node* targetNode = result.first;
    unordered_map<Node*, Node*> parent = result.second;

    if (!targetNode) {
        return -1; // Target not found
    }

    queue<pair<Node*, int> > q;
    unordered_set<Node*> visited;

    q.push(make_pair(targetNode, 0));
    visited.insert(targetNode);

    int maxTime = 0;

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            Node* node = q.front().first;
            int time = q.front().second;
            q.pop();

            maxTime = max(maxTime, time);

            if (node->left && visited.find(node->left) == visited.end()) {
                q.push(make_pair(node->left, time + 1));
                visited.insert(node->left);
            }
            if (node->right && visited.find(node->right) == visited.end()) {
                q.push(make_pair(node->right, time + 1));
                visited.insert(node->right);
            }
            if (parent.find(node) != parent.end() && visited.find(parent[node]) == visited.end()) {
                q.push(make_pair(parent[node], time + 1));
                visited.insert(parent[node]);
            }
        }
    }

    return maxTime;
}
};
