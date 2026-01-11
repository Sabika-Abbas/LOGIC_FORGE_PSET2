class DSU:
    def __init__(self, n):
        self.parent=list(range(n + 1))
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)]=self.find(y)

def maximize_freelance_profit(deadlines, profits):
    jobs = sorted(zip(profits, deadlines), reverse=True)
    max_deadline = max(deadlines)
    dsu = DSU(max_deadline)
    
    total_jobs = 0
    total_profit = 0
    
    for profit, dl in jobs:
        slot = dsu.find(dl)
        if slot > 0:
            total_jobs += 1
            total_profit+=profit
            dsu.union(slot, slot-1)
    
    return [total_jobs, total_profit]