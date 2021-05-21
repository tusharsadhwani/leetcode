class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:
        time = 1
        while True:
            selected_memory = memory1 if memory1 >= memory2 else memory2

            if selected_memory < time:
                return [time, memory1, memory2]
            
            if memory1 >= memory2:
                memory1 -= time
            else:
                memory2 -= time
            
            time += 1


tests = [
    (
        (2,2,),
        [3,1,0],
    ),
    (
        (8,11,),
        [6,0,4],
    ),
]