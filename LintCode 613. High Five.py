"""
There are two properties in the node student id and scores, 
to ensure that each student will have at least 5 points, 
find the average of 5 highest scores for each person.

Example

Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

Return 
"""
'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        map = {}
        for r in results:
            if r.id not in map:
                map[r.id] = []
            heapq.heappush(map[r.id], r.score)
            if len(map[r.id]) > 5:
                heapq.heappop(map[r.id])
        result = {}
        for id, score in map.items():
            result[id] = sum(score)/5.0

        return result