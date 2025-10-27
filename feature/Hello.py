import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="hello", description="التحية")
    async def hello(self, interaction: Interaction):
        print("LOG: Command hello Called")
        await interaction.response.send_message("Hello, World!")