# Jarvis the Nutritionist - Wit version

This is a test version of *Jarvis-the-nutritionist* with a [wit.ai](https://wit.ai) integration using [pywit](https://github.com/wit-ai/pywit), a Python library for wit.

## Installation

Create a virtual environment with Python 3.5 (or 3.4)

	virtualenv -p /usr/bin/python3.5 venv

Enter the virtual environment

	source venv/bin/activate

Install dependencies

	pip install --upgrade pip
	pip install -r requirements.txt


## Run

It is possible to run the bot in two different ways:

- in a terminal to test the commands directly with [wit.ai](https://wit.ai)
- on Facebook Messenger to test the full experience

For both of these, you have to copy the `.env.bk` file and name it `.env`. Then edit the `.env` file and write the correct tokens.

The variables in this file have to be on your environment variables. To add them on Linux, type :

    export $(cat .env)


### In Terminal

To run the bot in interactive mode in the terminal, `terminal_mode` variable (line 8 of bot.py) must be set to `True`. Then just launch the python file `bot.py` with the following command :

    python bot.py


### On Messenger

To use it directly on Messenger, set the `terminal_mode` to `False`. Then you need to setup a Facebook page first. You can follow the [Messenger Platform setup guide](https://developers.facebook.com/docs/messenger-platform/quickstart).

After setting up the page, run the bot with :

    python bot.py

Then you have to subscribe your page to the webhook `https://<your_host>/webhook` (note: you must have a valid SSL certificate).

Hint : you can use [ngrok](https://ngrok.com), to test in localhost.


## Contribute

It is possible to contribute !

Please follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) code convention ;)