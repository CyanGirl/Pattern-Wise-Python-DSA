'''
Link: https://leetcode.com/problems/bus-routes/description/
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
'''

from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        
        # This question asks for minimum buses. so thats a hint for: each BFS level = each bus
        # so we go by buses. Means, we cover one bus and its all stops entirely which starts with the source,
        # then go to the next bus which can be connected by any of the curstops we have. until we reach target

        # we first see for each stops, how many different buses we have from there
        busStops= defaultdict(set)
        for busnum, stops in enumerate(routes):
            for stop in stops: busStops[stop].add(busnum)

        
        totalbus=-1
        q=[source]
        visited = set([source])

        while q:
            n = len(q)
            totalbus+=1

            for _ in range(n):
                curstop=q.pop(0)
                if curstop==target: return totalbus

                # traverse all the stops which can be reached by buses from this stop
                for busnum in busStops.get(curstop,[]):

                    # check for all the stops which can be reached by the  current bus
                    for stop in routes[busnum]:
                        if stop in visited: continue
                        visited.add(stop)
                        q.append(stop)

                    routes[busnum]=[] # since we have already visited all the stops by this bus

        return -1


