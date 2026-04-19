class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = deque([(0,'0000')])
        dirs = []

        if '0000' in visited:
            return -1

        for i in range(4):
            dirs.append((i,-1))
            dirs.append((i,1))

        while q:
            num, state = q.popleft()
            if "".join(state) == target:
                return num
            for idx, dr in dirs:
                new_state = state[0:idx] + str((int(state[idx]) + dr) % 10) + state[idx+1:]
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((num+1, new_state))
        return -1
