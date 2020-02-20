class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    
        smallestqueue = []
        if(matrix == None or len(matrix)==0):
            return smallestqueue
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                smallestqueue.append(matrix[i][j])
                smallestqueue.sort()
        print(smallestqueue)
        return smallestqueue[k-1]