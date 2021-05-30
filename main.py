import discord
from discord import user
import requests
import json, random
from DB import create_user, create_table, delete_user, create_transaction
import DB

client = discord.Client()
token = "ODQ4MTQ1NzIyMTI5MzgzNDM1.YLIXQQ.9QAPx5L62mAqsPiupeVuFYddKJ0"
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_typing(channel, user, when):
#     print("send DM to typing user")
#     await user.send('''  Send before you think twice.
#     {}
#     {}
#     '''.format(channel.name, when))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    author = message.author
    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$createUser'):

        create_user(author.id,author.name)
        await message.channel.send("Successful create USER {}".format(author.name))



    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if msg.startswith("$DM"):
        await message.author.send("HI")

    if msg.startswith("$whoami"):
        res = '''
        id: {}
        name :{}
        guild: {}
        status: {}
        role: {}
        '''.format(author.id, author.name, author.guild, author.status, author.roles)
        await author.send(res)

    if msg.startswith('$roles'):
        role_name = [role.name for role in author.roles]
        res = '''
        role_names : {}
        '''.format(role_name)

        if 'manager' in role_name:
            res +="\n You're a fucking manger!!"
        await message.channel.send(res)

    if msg.startswith('$add'):
        user_id = author.id
        token = msg.split(' ')[1]
        res_messsage = DB.add_token(user_id, token)
        await message.channel.send(res_messsage)

    if msg.startswith('$tokens'):
        user_id = author.id
        tokens = DB.select_token(user_id)
        await message.author.send('''>>> ```markdown
        Hi you still have ##{}
        ```
        '''.format(tokens))



@client.event
async def on_member_join(member):
    await member.send('Private message')

client.run(token)
