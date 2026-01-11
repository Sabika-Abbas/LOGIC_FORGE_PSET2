# - **Example 1:** `arr = [1, 5, 11, 5]` -> Total: 22. Target: 11. **Result: True** (Bag A: [1, 5, 5], Bag B: [11])
# - **Example 2:** `arr = [1, 3, 5]` -> Total: 9. **Result: False** (Cannot split odd weight).

def can_balance_scales(arr):
    total=sum(arr)
    
    if total%2 != 0:
        return False, [], []
    
    target=total//2
    n=len(arr)
    
    dp=[[False] * (target+1) for _ in range(n+1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, target + 1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    
    if not dp[n][target]:
        return False, [], []
    
    bagA=[]
    bagB=[]
    i, j=n,target
    
    while i>0 and j>0:
        if dp[i-1][j]:
            bagB.append(arr[i-1])
            i-=1
        elif j>=arr[i-1] and dp[i-1][j-arr[i-1]]:
            bagA.append(arr[i-1])
            j-=arr[i-1]
            i-=1
    
    while i>0:
        bagB.append(arr[i-1])
        i-=1
    
    return True, bagA, bagB

print(can_balance_scales([1, 5, 11, 5])) 