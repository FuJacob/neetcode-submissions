class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        deadends_set = set(deadends)
        q = deque([(0,['0','0','0','0'])])
        dirs = []
        if '0000' in deadends_set:
            return -1

        for i in range(4):
            dirs.append((i,-1))
            dirs.append((i,1))

        while q:
            num, state = q.popleft()
            if "".join(state) == target:
                return num
            for idx, dr in dirs:
                new_state = state[:]
                new_state[idx] = str(int(new_state[idx]) + dr)
                if int(new_state[idx]) > 9:
                    new_state[idx] = '0'
                elif int(new_state[idx]) < 0:
                    new_state[idx] = '9'
                new_state_str = "".join(new_state)
                if new_state_str not in deadends_set and new_state_str not in visited:
                    visited.add(new_state_str)
                    q.append((num+1, new_state))
        return -1
