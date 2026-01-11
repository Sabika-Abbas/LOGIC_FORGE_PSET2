import math

def calculate_minimum_speed(piles, k):
    left,right= 1,max(piles)
    result =right
    
    while left<= right:
        mid= (left+right)//2
        total_hours=0
        for bananas in piles:
            total_hours+=math.ceil(bananas/mid)
        
        if total_hours <= k:
            result=mid
            right=mid-1
        else:
            left=mid+1
    
    return result

piles=[5,10,3]        
k=4
speed=calculate_minimum_speed(piles, k)
print("Minimum speed to eat all bananas:", speed)