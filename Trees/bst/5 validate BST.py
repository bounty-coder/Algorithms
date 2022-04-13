class Solution:
    # @param A : root node of tree
    # @return an integer

    def isValidBST(self, A):
        lrange=float("-inf")
        rrange=float("inf")
        
        def validate(A, lrange,rrange):
            if A is None:
                return True
            
            x=A.val
            if x<=lrange or x>=rrange:
                return False

            return validate(A.left,lrange,x) and validate(A.right,x,rrange)

        if validate(A,lrange,rrange):
            return 1
        return 0