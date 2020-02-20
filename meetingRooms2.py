import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sortintervals = sorted(intervals)
        endqueue = []
        roomalloted = 0
        for i in sortintervals:
            if endqueue == [] or endqueue[0] > i[0] :
                heapq.heappush(endqueue, i[1])
                roomalloted += 1
            else:
                heapq.heapreplace(endqueue, i[1])
        return roomalloted 