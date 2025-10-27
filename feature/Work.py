import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Work(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="work", description="التأكد من العمل")
    async def work(self, interaction: Interaction):
        print("LOG: Command work Called")
        await interaction.response.send_message("ياعم شغال")
