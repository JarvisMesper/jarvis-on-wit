import sys, os
from wit import Wit

from actions import wit,forecast

terminal_mode = True

if terminal_mode:
    if len(sys.argv) != 2:
        print('usage: python ' + sys.argv[0] + ' <wit-token>')
        exit(1)
    access_token = sys.argv[1]

actions = {
    'send': wit.send,
    'getForecast': forecast.get_forecast,
}

if terminal_mode:
    client = Wit(access_token=access_token, actions=actions)
    client.interactive()
