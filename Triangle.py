def minimumTotal(self, triangle: List[List[int]]) -> int:
        DP = []
        for row in range(len(triangle)):
            DP.append([])
            for number in range(len(triangle[row])):
                DP[row].append(float("inf"))
            
        DP[0][0] = triangle[0][0]
        print(DP)
        for row in range(1, len(triangle)):
            for num in range(len(triangle[row])):
                if (num == 0):
                    parents = [num]
                elif (num == len(triangle[row]) - 1):
                    parents = [num - 1]
                else:
                    parents = [num - 1, num]
                for parent in parents:
                    DP[row][num] = min(triangle[row][num] + DP[row-1][parent], DP[row][num])
        return min(DP[len(triangle) - 1])
