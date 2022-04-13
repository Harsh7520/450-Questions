#User function Template for python3

class Solution:
    def merge(self, arr1, arr2, n, m):
        arr1.extend(arr2)
        arr2.clear()
        arr1.sort()
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends
