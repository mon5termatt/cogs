import asyncio
from uuid import getnode

from redbot.core import config
from redbot.core.bot import Red

from .general import General

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


async def setup(bot):
    #asyncio.create_task(maybe_send_owners(bot))
    await bot.add_cog(General())


async def maybe_send_owners(bot: Red):
    # I have been provided multiple reasons to do it this way and not disable this completely.
    # You can thank someone reaching out and having a discussion about this and a balance
    # between not allowing issues being covered up or to be easily by passed up and not
    # stranding users with no other options in the immediate term. (the reason I didn't just fundamentally break the cogs)
    # This can still be circumvented, but that would be removing license information conveyed to end users.
    node_id = getnode()

    conf = config.Config.get_conf(
        None, identifier=node_id, cog_name=f"SinbadCogs-{node_id}"
    )

    conf.register_global(last_notify=[])

    async with conf.last_notify.get_lock():
        last_notify = await conf.last_notify()
        cur_uptime = list(bot.uptime.timetuple()[:6])
        if last_notify is None or cur_uptime > last_notify:

            await bot.send_to_owners(":D")
            await conf.last_notify.set(cur_uptime)
