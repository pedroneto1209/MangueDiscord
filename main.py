import discord

TOKEN = 'NzI3MzA4Mjk2MDA4MjM3MjE4.Xvp9WQ.5M1fnSOF465U0SfAa5_rOwTZjc8'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(member):

    embed = discord.Embed(title = f'Bem-vindo ao {member.guild}!!', colour = discord.Colour.gold())
    boasvindas = f'''
        Ei {member.mention} Aguarde até a sua entrevista!!\nIremos te chamar quando for a hora\n
        Entre no canal de espera e desligue seu microfone até sua vez!
    '''

    embed.set_image(url = 'https://media.tenor.com/images/34a26802bf0a04f190b4195ed1f9b0a8/tenor.gif')
    embed.add_field(name = 'Gente nova entrando no Mangue :)', value=f'{boasvindas}\n\n')
    channel = client.get_channel(575381401814302720)

    await member.guild.text_channels[0].send(embed = embed)
    await member.setVoiceChannel(channel)

client.run(TOKEN)