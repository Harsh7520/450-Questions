class Solution:
    def minJumps(self, arr, n):
        j=0
        i=arr[0]
        if(arr[0]==0):
            return -1
        elif(n==1):
            return 0
        else:
            j=1
            while(i<n-1):
                j+=1
                if(i+arr[i]<=n-1):
                    i+=arr[i]
                else:
                    i=n-1
            return j

        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
# } Driver Code Ends
