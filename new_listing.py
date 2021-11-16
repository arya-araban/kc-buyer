import time
from rsrcs.coin_lib import keyboard_buy, buy_on_time

# TUNABLE PARAMETERS
DESIRED_TIME_UTC = "09:00:01"  # Put this the time in which the coin will be releasing
COIN_NAME = "WNXM"

USDT_AMOUNT = 26  # amount of usdt to buy with. make sure this is less than your current USDT balance
RELEASE_OFFSET_PERCENTAGE = 3  # offset percentage to buy higher ie 1 means 1% higher. 0 means no price offset
KEYBOARD_OFFSET_PERCENTAGE = 2

# around 10 to 50 percent for world premiers, and 1 to 5 for normal new listings.


def main():
    buy_on_time(COIN_NAME, USDT=USDT_AMOUNT, offset=RELEASE_OFFSET_PERCENTAGE,
                desired_time_utc=DESIRED_TIME_UTC)

    keyboard_buy(COIN_NAME, USDT=USDT_AMOUNT, offset=KEYBOARD_OFFSET_PERCENTAGE)


if __name__ == "__main__":
    main()
