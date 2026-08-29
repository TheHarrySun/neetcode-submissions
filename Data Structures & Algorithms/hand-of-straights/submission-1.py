class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = defaultdict(int)
        for card in hand:
            freq[card] += 1
        
        for i in range(len(hand)):
            if freq[hand[i]] != 0:
                for j in range(groupSize):
                    freq[hand[i] + j] -= 1
                    if freq[hand[i] + j] < 0:
                        return False
        for _, val in freq.items():
            if val != 0:
                return False 
        return True