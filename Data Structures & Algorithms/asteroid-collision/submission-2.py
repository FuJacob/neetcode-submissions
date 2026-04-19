class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for asteroid in asteroids:
            destoryed = False
            while stack and stack[-1] > 0 and asteroid < 0:
                top = abs(stack[-1])
                if abs(asteroid) >= top:
                    stack.pop()
                    if abs(asteroid) == top:
                        destoryed = True
                        break
                else:
                    destoryed = True
                    break
            if not destoryed:
                stack.append(asteroid)
        return stack
                
                






        