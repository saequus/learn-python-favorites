# LeetCode problem322 Coin Change

# You are given coins of different denominations and a total amount of
# money amount. Write a function to compute the fewest number of coins
# that you need to make up that amount. If that amount of money cannot
# be made up by any combination of the coins, return -1.

# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

print('implementation with regression')


class Coins:
    def __init__(self):
        self.res = None

    def coin_change(self, coins, amount):
        coins.sort(reverse=True)
        self.res = 2 ** 31 - 1
        len_coins = len(coins)

        def helper(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, len_coins):
                if coins[i] <= rem < coins[i] * (self.res-count):
                    helper(i, rem-coins[i], count+1)

        for j in range(len_coins):
            helper(j, amount, 0)
        return self.res if self.res < 2**31-1 else -1



coins = [1, 2, 3, 4, 5]
amount = 6
f = Coins()
print(f.coin_change(coins, amount))
coins2 = [1, 2, 5]
amount2 = 11
print(f.coin_change(coins2, amount2))
coins3 = [1, 3, 5, 9]
amount3 = 21
print(f.coin_change(coins2, amount2))
print('– - – –')


print('naive implementation')


class MyCoins:

    def count_coins(self, coins, amount):
        coins = sorted(coins, reverse=True)
        count = 0
        for i in range(len(coins)):
            current = coins[i]
            while amount - current >= 0:
                amount -= current
                count += 1
        return count if amount == 0 else -1


cu = MyCoins()
print(cu.count_coins(coins, amount))
print(cu.count_coins(coins2, amount2))
print(cu.count_coins(coins3, amount3))
