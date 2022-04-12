
class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        for i in range(n):
            if(arr[i]<=k):
                arr[i]+=k
            else:
                arr[i]-=k
        m = min(arr)
        ma = max(arr)
        return (ma-m)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
