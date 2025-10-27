import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
from feature.Hello import Hello
from feature.Join import Join
from feature.Leave import Leave
from feature.Tazker import StartTazker
from feature.Test import Test
from feature.Work import Work

load_dotenv()
intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")
    try:
        await bot.sync_all_application_commands()
        await bot.sync_application_commands()
        print(f"✅ Slash Commands Synced!")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

def init_features():
    bot.add_cog(Test(bot))
    bot.add_cog(Work(bot))
    bot.add_cog(Hello(bot))
    bot.add_cog(Join(bot))
    bot.add_cog(Leave(bot))
    bot.add_cog(StartTazker(bot))


# main
init_features()
bot.run(os.getenv("DISCORD_TOKEN"))