import os
from importlib import import_module
from pathlib import Path

import hikari
import lightbulb

def create_bot() -> lightbulb.Bot:
    with open("./secrets/token") as f:
        token = f.read().strip()
    
    bot = lightbulb.Bot(token=token, prefix="!")

    commands = Path("./rhyho_bot/commands").glob("*.py")
    for c in commands:
        mod = import_module(f"rhyho_bot.commands.{c.stem}")
        com = mod.__dict__[f'{c.stem}'.title()]
        bot.add_slash_command(com)

    return bot

if os.name != 'nt':
    import uvloop

    uvloop.install()

if __name__ == "__main__":
    create_bot().run()