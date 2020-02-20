# Competitive-Coding-7

1.)Meeting Rooms II

solved using priority queue

1.first sort the intervals
2.add endinterval if the queue is empty or endinterval is greater than start interval of next index.
3.else just replace the priority end queue index=0 with the present index value of the eninterval of the intervals
4.return the length of the queue 

2.)Kth closest in the matrix(https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

solved using minmum priority queue

1.first added into list and then sort after each elemnt is added
2.then return the kth element in the list
