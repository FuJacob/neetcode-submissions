class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        res = ""
        if not strs: return ""
        for s in strs:
            sizes.append(len(s))
        for idx, sz in enumerate(sizes):
            res+= str(sz)
            if idx != len(sizes) -1:
                 res += ","
        res+="#"

        for s in strs:
            res+=s
        return res

    def decode(self, s: str) -> List[str]:
        if not s: return []
        end = 0
        lens = s
        for idx, c in enumerate(s):
            if c == "#":
                lens = lens[:idx]
                end = idx + 1
                break
        lens = lens.split(",")
        print(lens)
        ans = []
        for i in range(len(lens)):
            ans.append(s[end:end+ int(lens[i])])
            end = end+int(lens[i])
        return ans

