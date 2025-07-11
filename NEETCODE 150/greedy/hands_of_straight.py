# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# Link: https://leetcode.com/problems/hand-of-straights/

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False

        count = {}

        for card in hand:
            count[card] = 1 + count.get(card, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            minHand = minH[0]

            # Try to build a group of size `groupSize` starting from `minCard`
            for i in range(minHand, minHand + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    # We are done using this card, so we should remove it from the heap
                    # But! The card we're removing must be the smallest remaining card.
                    # If it's not on top of the heap, it means we skipped cards
                    # and formed groups out of order → invalid
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True