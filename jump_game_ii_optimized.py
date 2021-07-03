class Solution(object):
    def jump(self, nums: list[int]) -> int:
        # As we just need to reach last index, the number at last position doesn't matter
        nums.pop()

        if len(nums) == 0:
            return 0

        jumps = 1
        next_jump_max = current_jump_max = nums[0]
        for index, num in enumerate(nums):
            next_jump_max = max(next_jump_max, index + num)

            # If we reach the point where our current number of jumps isn't enough.
            # That is because we've reached the maximum value the current jump could've
            # reached, and the iteration is still going on. So we know we need to do another jump.
            # Then, `next_jump_max` becomes the max we can reach in `jumps+1` number of jumps.
            if index == current_jump_max:
                jumps += 1
                current_jump_max = next_jump_max

                # Optional optimization: if current_jump_max is already
                # bigger than maximum index, we don't need to iterate any further
                if current_jump_max >= len(nums):
                    break

        return jumps


tests = [
    (
        ([2, 3, 1, 1, 4],),
        2,
    ),
    (
        ([2, 3, 0, 1, 4],),
        2,
    ),
    (
        ([1, 1, 1, 1],),
        3,
    ),
]
