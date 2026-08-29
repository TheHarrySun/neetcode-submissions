class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = []
        second = []
        third = []
        for i, triplet in enumerate(triplets):
            x, y, z = triplet
            if x == target[0] and y <= target[1] and z <= target[2]:
                first.append(triplet)
            if x <= target[0] and y == target[1] and z <= target[2]:
                second.append(triplet)
            if x <= target[0] and y <= target[1] and z == target[2]:
                third.append(triplet)
        return len(first) > 0 and len(second) > 0 and len(third) > 0