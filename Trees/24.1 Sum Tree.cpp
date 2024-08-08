// Given a Binary Tree. Check for the Sum Tree for every node except the leaf node. Return true if it is a Sum Tree otherwise, return false.

// A SumTree is a Binary Tree where the value of a node is equal to the sum of the nodes present in its left subtree and right subtree. An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf node is also considered a Sum Tree.

bool isSumTree(Node* root) {
    if(root==NULL){
        return true;
    }
    if(!root->left && !root->right){
        return true;
    }
    
    bool left = isSumTree(root->left);
    if(!left) return false;
    bool right = isSumTree(root->right);
    if(!right) return false;
    
    int l=0,r=0;
    
    if(root->left){
        if(!root->left->left && !root->left->right){
            l=root->left->data;
        }else{
            l=2*(root->left->data);
        }
    }
    if(root->right){
        if(!root->right->left && !root->right->right){
            r=root->right->data;
        }else{
            r=2*(root->right->data);
        }
    }
    if(l+r==root->data){
        return true;
    }
    else{
        return false;
    }
}
