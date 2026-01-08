'''Case A: Small Change
• Target Sum: 4
• Vault Coins: [1, 2, 3]
• Total Ways: 4
o Combinations: {1,1,1,1}, {1,1,2}, {2,2}, {1,3}
Case B: Specific Denominations
• Target Sum: 10
• Vault Coins: [2, 5, 3, 6]
• Total Ways: 5
o Combinations: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5}, {5,5}
Case C: The Impossible Payment
• Target Sum: 5
• Vault Coins: [4]
• Total Ways: 0 (You can't make 5 using only 4-piece coins!)'''

def count_payment_combination(coins,total_sum):
    combinations=[]
    stack=[(0,0,[])]
    
    while stack:
        start_idx,current_sum,possibility=stack.pop()
        if current_sum==total_sum:
            combinations.append(sorted(possibility))
            continue
        elif current_sum>total_sum:
            continue
        for i in range(start_idx,len(coins)):
            if current_sum+coins[i]<=total_sum:
                stack.append((i,current_sum+coins[i],possibility+[coins[i]]))
        
    return len(combinations), combinations

count, combos = count_payment_combination([1, 2, 3], 4)
print(f"Total Ways: {count}")
print(f"Combinations: {combos}")

    
