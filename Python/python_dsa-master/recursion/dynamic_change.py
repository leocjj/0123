#!/usr/bin/python3
"""
Make change using the fewest number of coins
Dynamic programming is used for a situation in which the greedy method fails
"""


def make_change(coin_values, change, min, coins_used):
    # Make change using the fewest number of coins
    for cents in range(change + 1):
        count = cents
        new_coin = 1
        for j in [c for c in coin_values if c <= cents]:
            if min[cents - j] + 1 < count:
                count = min[cents - j] + 1
                new_coin = j
        min[cents] = count
        coins_used[cents] = new_coin
    return min[change]


def print_coins(coins_used, change):
    # Print the coins used
    coin = change
    while coin > 0:
        current = coins_used[coin]
        print(current)
        coin -= current

if __name__ == '__main__':
    amount = 63
    coin_list = [1, 5, 10, 21, 25]
    coins_used = [0] * (amount + 1)
    coin_count = [0] * (amount + 1)

    print('Making change for', amount, 'requires', end=' ')
    print(make_change(coin_list, amount, coin_count, coins_used), 'coins')
    print('They are:')
    print_coins(coins_used, amount)
    print('The coins used are:')
    print(coins_used)

    amount = 33
    coin_list = [1, 5, 8, 10, 25]
    coins_used = [0] * (amount + 1)
    coin_count = [0] * (amount + 1)

    print('Making change for', amount, 'requires', end=' ')
    print(make_change(coin_list, amount, coin_count, coins_used), 'coins')
    print('They are:')
    print_coins(coins_used, amount)
    print('The coins used are:')
    print(coins_used)
