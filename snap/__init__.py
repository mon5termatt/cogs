from redbot.core.bot import Red
from .stafftools import Stafftools


def setup(bot: Red):
    tools = Stafftools(bot)
    await bot.add_cog(tools)
