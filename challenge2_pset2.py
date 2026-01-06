# - **Example 1:** `arr = [1, 5, 11, 5]` -> Total: 22. Target: 11. **Result: True** (Bag A: [1, 5, 5], Bag B: [11])
# - **Example 2:** `arr = [1, 3, 5]` -> Total: 9. **Result: False** (Cannot split odd weight).

def can_balance_scales(arr):
    bagA=[]
    bagB=[]
    total=sum(arr)
    if total%2!=0:
        return False
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if sum(bagA)<=sum(bagB):
            bagA.append(arr[i])
        else:
            bagB.append(arr[i])

    print(sum(bagA)==sum(bagB))
    print("Bag A: ", bagA)
    print("Bag B: ", bagB)


can_balance_scales([1,5,5,11])
