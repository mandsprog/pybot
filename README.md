# pybot

Wrapper for python-telegram-bot to allow dynamic plug-in architecture, an attempt to make python-telegram-bot more hubottish.

### Execution flow

1. `pybot.py` grabs the message from telegram and sends it to the `brain.py`.

1. The `brain.py` loads in runtime all the `.py` files in the `./memory` folder each time and try to execute a defined method, for example `hear(message.text)`.

1. Each module in `./memory` with that method returns a response, the `brain.py` sends it to the `pybot.py` and it sends the response back to the chat.

* As the methods are dynamically loaded, you can edit and add the files in `./memory` without need to restart `pybot.py`, and they will be reloaded on the next message.

### Install

```
python3 setup.py
```

or

```
pip3 install requests
pip3 install python-telegram-bot
```

### Run

```
python3 pybot.py
```

### License

You may copy, distribute and modify the software provided that modifications are described and licensed for free under `LGPL-3 <https://www.gnu.org/licenses/lgpl-3.0.html>`_. Derivatives works (including modifications or anything statically linked to the library) can only be redistributed under LGPL-3, but applications that use the library don't have to be.
