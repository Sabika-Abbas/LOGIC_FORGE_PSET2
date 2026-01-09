'''
climbing mountain to nth sep in possible combinations
'''


def count_ways_to_summit(n):
    combinations=[]
    queue=[[1],[2]]
    while queue:
        current_path=queue.pop()
        current_sum=sum(current_path)
        if current_sum==n:
            combinations.append(current_path)
        elif current_sum<n:
            queue.append(current_path+[1])
            queue.append(current_path+[2])
    return combinations

combos = count_ways_to_summit(4)
print(f"Combinations: {combos}")
print(f"Number of ways: {len(combos)}")