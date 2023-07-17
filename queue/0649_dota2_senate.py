from collections import deque


class Solution:
    # Greedy
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        s, banned = set(), [False] * n
        ban_d = ban_r = 0
        while len(s) != 1:
            s = set()
            for i, p in enumerate(senate):
                if banned[i]:
                    continue
                if p == 'R':
                    if ban_r > 0:
                        ban_r -= 1
                        banned[i] = True
                    else:
                        ban_d += 1
                        s.add('R')
                else:
                    if ban_d > 0:
                        ban_d -= 1
                        banned[i] = True
                    else:
                        ban_r += 1
                        s.add('D')
        return 'Radiant' if s.pop() == 'R' else 'Dire'

    # Queue
    def predictPartyVictory2(self, senate: str) -> str:
        n, R, D = len(senate), deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r, d = R.popleft(), D.popleft()
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)

        return 'Radiant' if R else 'Dire'
