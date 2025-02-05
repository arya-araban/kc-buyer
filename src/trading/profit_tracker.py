import time
from threading import Thread
from typing import Callable
from sty import fg

from src.constants import DEFAULT_REFRESH_RATE

class ProfitTracker:
    @staticmethod
    def track_profit(price_getter: Callable[[], float], entry_price: float) -> None:
        def tracker():
            start = time.time()
            while True:
                current_price = price_getter()
                profit = round((current_price / entry_price * 100) - 100, 4)
                color = f'{fg.li_green}+' if profit >= 0 else f'{fg.red}'
                print(
                    f'\rTime Elapsed = {fg.blue + str(int(time.time() - start)) + fg.rs} ~ '
                    f'Current Profit = {color + str(profit) + " %" + fg.rs}',
                    end=" "
                )
                time.sleep(DEFAULT_REFRESH_RATE / 2 )  # Sleep to prevent CPU thrashing

        Thread(target=tracker).start()