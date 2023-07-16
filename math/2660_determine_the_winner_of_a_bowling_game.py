from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def caldulateScore(results: List[int]):
            score = 0
            for i, result in enumerate(results):
                if (i >= 1 and results[i - 1] == 10) or (i >= 2 and results[i - 2] == 10):
                    score += result * 2
                else:
                    score += result
            return score

        player1_score = caldulateScore(player1)
        player2_score = caldulateScore(player2)

        if player1_score > player2_score:
            return 1
        elif player2_score > player1_score:
            return 2
        else:
            return 0


sol = Solution()
res = sol.isWinner([4, 10, 7, 9], [6, 5, 2, 3])
