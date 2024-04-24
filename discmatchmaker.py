import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = ";", help_command = None, intents = intents)


@bot.event
async def on_ready():
    print(f'Bot está online e conectado como {bot.user}')


@bot.command()
async def montar_times(ctx):
    nomes = []

    for i in range(10):
        await ctx.send(f'Digite o nome do jogador {i + 1}: ')
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author)
        nomes.append(msg.content)

    random.shuffle(nomes)

    tamanho_times = len(nomes) // 2
    time1 = nomes[:tamanho_times]
    time2 = nomes[tamanho_times:]

    await ctx.send('Times montados com sucesso!')
    await ctx.send('Time 1: ' + ', '.join(time1))
    await ctx.send('Time 2: ' + ', '.join(time2))

bot.run('MTIzMDc3MDE0NDY2NjQ1MjA1OA.GCRqIo.chRvp0E1Rg70hLC1f3hBfLN83KzZ5sdR3Amvyw')
