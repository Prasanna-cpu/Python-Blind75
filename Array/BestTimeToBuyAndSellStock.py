import types


def bestTimeToBuyAndSellStock(prices):
    max_profit = float("-inf")
    min_price = float("inf")

    for p in prices:
        min_price = min(min_price, p)

        max_profit = max(max_profit, abs(p - min_price))

    return max_profit


print(bestTimeToBuyAndSellStock([7, 1, 5, 3, 6, 4]))
