class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins_needed = [0 for _ in range(amount+1)]
        for amt in range(1, amount+1):
            min_coins_needed = -1

            for coin in coins:
                rest_amount = amt - coin
                if rest_amount < 0:
                    continue

                coins_for_rest = coins_needed[rest_amount]
                if coins_for_rest == -1:
                    continue

                if min_coins_needed == -1:
                    min_coins_needed = coins_for_rest + 1
                    continue

                min_coins_needed = min(min_coins_needed, coins_for_rest+1)

            coins_needed[amt] = min_coins_needed

        return coins_needed[-1]


tests = [
    (
        ([1, 2, 5], 11,),
        3,
    ),
    (
        ([2], 3,),
        -1,
    ),
    (
        ([1], 1,),
        1,
    ),
    (
        ([1], 2,),
        2,
    ),
]
