from redbot.core import commands, checks
from redbot.core import Config


class Scheduler(commands.Cog):

    @checks.admin_or_permissions()
    @commands.command()
    async def exampleCommand(self, ctx: commands.Context, *args: str):
        if not args:
            return await ctx.send_help()
        return await ctx.send(args)

    @checks.admin_or_permissions()
    @commands.command()
    async def addEvent(self, ctx: commands.Context, *args: str):
        if not args:
            return await ctx.send_help()
        return await ctx.send("Wait while I add " + args + "to the schedule")
