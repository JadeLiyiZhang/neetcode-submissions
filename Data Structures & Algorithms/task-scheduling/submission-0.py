class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        table = [0] * 26
        cycles = 0
        for task in tasks:
            table[ord(task) - ord('A')] += 1
        for i in range(len(table)):
            if table[i] != 0:
                heapq.heappush(heap, (-table[i], i))
        while heap:
            cur_round = []
            for i in range(n + 1):
                if heap:
                    count, current = heapq.heappop(heap)
                    count = -count - 1
                    cur_round.append((count, current))
            for i in range(len(cur_round)):
                if cur_round[i][0] != 0:
                    heapq.heappush(heap, (-cur_round[i][0], cur_round[i][1]))
            if heap:
                cycles += n + 1
            else:
                cycles += len(cur_round)
        return cycles
