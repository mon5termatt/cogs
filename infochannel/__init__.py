from .infochannel import InfoChannel


async def setup(bot):
    ic_cog = InfoChannel(bot)
    await bot.add_cog(ic_cog)
    await ic_cog.initialize()
