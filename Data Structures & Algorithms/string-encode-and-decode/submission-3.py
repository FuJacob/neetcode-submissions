class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        ptr = 0
        while ptr < len(s):
            start = ptr
            while s[ptr] != '#':
                ptr +=1
            length = int(s[start:ptr])
            ptr +=1
            decoded.append(s[ptr:ptr+length])
            ptr += length
        return decoded

