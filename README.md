# Discord Python Bot

This repository was created for the sole reason of being as 'a basic template' a discord bot.

What does it do? (WIP)

![image](https://user-images.githubusercontent.com/64602039/120628210-15229780-c46d-11eb-9969-a8f7599c6705.png)

# Requirements

**Python 3.5.3 or higher(3.8) is required.**

Install Python on https://www.python.org/.

If you're new to Python, that's great! However, it is highly suggested to start
off learning Python, it is an easy, simple and useful programming language. It
is never late to begin coding! You don't need a computer science degree for that.

**discord.py module**

```bash
# Linux/macOS
python3 -m pip install -U discord.py

# Windows (on cmd, after you've installed Python)
py -3 -m pip install -U discord.py
```

**py-cord module**
```bash
# Linux/macOS
python3 -m pip install -U py-cord --pre

# Windows (on cmd)
py -3 -m pip install -U py-cord --pre
```
Run the bot
```bash
# Linux
python3 bot.py

# Windows
py bot.py
```
**A text editor**

There are many available text editors you can find on the web. I'd recommend
using **atom.io**, but any text editor will do! Even the regular Notepad, but
don't use it, *just don't*.

# Troubleshooting
`No module named discord`
```bash
pip install discord
```

If you encounter an `Import/Module error` after running the bot, try 
```bash
# Linux
pip install --upgrade --no-deps --force-reinstall pycord

# Windows
py -m pip install --upgrade --no-deps --force-reinstall pycord
```

# Notes
Slash commands work immediately if the guild ids are provided, otherwise it will be considered as "public slash command" and it will take up an hour to work.

Read the comments in `bot.py`, make any changes that you wish. Have fun!
