import discord
from vote import Vote

TOKEN = 'yourtokenhere'

client = discord.Client()

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

    await member.guild.text_channels[0].send(embed = embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-vote') and '(' in message.content and ')' in message.content:
            question = message.content[message.content.find('(')+1:message.content.find(')')]
            options = message.content[message.content.find(')')+2:].split()
            
            if len(options) <= 1:
                await message.channel.send('Você precisa dar mais de 1 opção.')
                return

            if len(options) > 10:
                await message.channel.send('Não é possivel fazer uma votação com mais de 10 opções.')
                return

            if len(options) == 2 and options[0] == 'sim' and options[1] == 'não':
                reactions = ['✅', '❌']
            else:
                reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

            description = []
            for x, option in enumerate(options):
                description += '\n {} {}'.format(reactions[x], option)
            embed = discord.Embed(title=question, description=''.join(description))
            react_message = await message.channel.send(embed=embed)
            for reaction in reactions[:len(options)]:
                await react_message.add_reaction(reaction)

    elif message.content.startswith('-vote'):
        await message.channel.send('Digite um tópico entre parêntesis, exemplo:\n -vote (tópico aqui) opção1 opção2 opção3')

client.run(TOKEN)