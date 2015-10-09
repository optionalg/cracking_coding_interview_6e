"""
Question:
Given a list of stock prices as follows:
stock_prices = [10, 3, 5, 9, 1, 5]

Find the best days (buy_index, sell_index) to buy and sell your stock
in order to maximize the return.

You cannot sell before you buy: e.g. in the above example you cannot
choose to sell for price 10 and buy for price 1 because day 4 comes
after day 0.
"""


def buy(prices):
    b_buy = 0
    b_sell = 0
    for buy_day in range(0, len(prices) - 1):
        for sell_day in range(buy_day, len(prices) - 1):
            if prices[sell_day] - prices[buy_day] < prices[b_sell] - prices[b_buy]:
                b_sell = sell_day
                b_buy = buy_day
    return (b_buy, b_sell)


def buy_linear_time(prices):
    b_buy = 0
    b_sell = 0
    lowest = 0
    for day in range(0, len(prices)):
        if prices[day] < prices[lowest]:
            lowest = day
            # get the current best return    # get the updated best return
        if prices[b_sell] - prices[b_buy] < prices[day] - prices[lowest]:
            b_buy = lowest
            b_sell = day

    return(b_buy, b_sell)
