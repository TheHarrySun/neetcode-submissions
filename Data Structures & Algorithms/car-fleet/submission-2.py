class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        combined = sorted(list(zip(position, speed)), reverse = True)
        print(combined)
        for pos, sp in combined:
            time = (target - pos) / sp
            if not stack:
                stack.append(time)
            elif stack[-1] >= time:
                print("less", stack[-1], time)
                continue
            else:
                print(stack[-1], time)
                stack.append(time)
        return len(stack)