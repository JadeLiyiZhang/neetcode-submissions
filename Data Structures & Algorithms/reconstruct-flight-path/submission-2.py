class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mapping = defaultdict(list)
        stops = set()
        # construct the graph
        for start, end in tickets:
            mapping[start].append(end)
        
        for dest in mapping.values():
            dest.sort(reverse=True)
        
        path = []
        
        def dfs(node):
            if len(path) == len(tickets) + 1:
                return

            while sorted(mapping[node]):
                neighbor = mapping[node].pop()
                dfs(neighbor)
            path.append(node)

        dfs("JFK")
        return path[::-1]