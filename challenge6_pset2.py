class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 2))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

def maximize_freelance_profit(deadlines, profits):
    if not deadlines:
        return [0, 0]
    
    jobs = sorted(zip(profits, deadlines), reverse=True)
    max_deadline = max(deadlines)
    dsu = DSU(max_deadline + 1)
    
    total_jobs = 0
    total_profit = 0
    
    for profit, dl in jobs:
        slot = dsu.find(dl)
        if slot > 0:
            total_jobs += 1
            total_profit += profit
            dsu.union(slot, slot - 1)
    
    return [f"{total_jobs} jobs", f"{total_profit} profit"]

Deadlines = [4, 1, 1, 1]
Profits = [20, 10, 40, 30]
result = maximize_freelance_profit(Deadlines, Profits)
print("Total jobs done and total profit:", result)
