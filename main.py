import random
import discord
TOKEN = ''
#template code made by devdungeon.com\
badwordpeople = []
lookingforans ={"stat":False, "q":1}
triviatuple = [
{"q":"What do Sea Cucumbers use as a self defense mechanism?", "ans":"organs"},
{"q":"Who was the 16th president of the United States of America", "ans":"Abraham Lincoln"}
]
client = discord.Client()
badwords = ["fuck", "shit", "dammit", "damn", "crap", "bitch", "fuq", "fuk"]


async def battle_start(message):
    await message.channel.send("BATTLE START!")
    battling=True
    return battling

async def battle_end(message):
    await message.channel.send("THE BATTLE IS OVER")
    battling = False
    return battling

with open('funfactgallery.txt') as f: # Tim added these two lines
    funfactgallery = f.readlines()    # ''
@client.event
async def on_message(message):
    global badwordpeople
    global lookingforans
    trivq = 0
    battlestatus = False
    dmg = 0
    p1={}
    p2={}

    if message.author == client.user:
        return

    if message.content.startswith('^die'):
        msg = 'HECKIN\' *dies*'.format(message)
        await message.channel.send(msg)
        print("Me: " + msg)


    for word in badwords:
        if word in message.content:
            await message.channel.send("THAS A BAD WORD AND A NONO")
            '''
            for person in badwordpeople:
                if message.author == person["user"]:
                    person["num"] += 1
                    await message.channel.send("swear count: " + str(person["num"]))
                    return
            persontemp = badwordpeople[len(badwordpeople)] = {"user": message.author, "num": 1}
            await message.channel.send("swear count: " + str(persontemp["num"]))
            del persontemp
            '''

    if message.content.startswith("^trivia"):
        trivq = random.randint(0, len(triviatuple)-1)
        await message.channel.send(triviatuple[trivq]["q"])
        lookingforans={"stat":True, "q":trivq}
        print(lookingforans)

    if triviatuple[lookingforans["q"]]["ans"].lower() in message.content.lower() and lookingforans["stat"] == True:
        await message.channel.send("Correct!")
        lookingforans["stat"] = False

    if lookingforans["stat"] == True:
        print(triviatuple[lookingforans["q"]]["ans"].lower())
        print(message.content)
    print(lookingforans["stat"])

    if message.content.lower().startswith("who is the best bot"):
        await message.channel.send("ME ME ME")

    if message.content.startswith("^funfact"):              # Tim added these 4
        fnum = random.randint(0, len(funfactgallery)-1)     # ''
        await message.channel.send(funfactgallery[fnum])    # ''
        print("funfact haha")                               # ''

    if message.content.startswith("^battle") and len(message.content.split(" ")) > 2:
        battlestatus = await battle_start(message)
        p1={"p":message.content.split(" ")[1], "hp":30}
        p2={"p":message.content.split(" ")[2], "hp":30}
        print(p1)
        print(p2)
        print(message.author.mention)
        return
    elif message.content.startswith("^battle"):
        await message.channel.send("Incorrect syntax, please specify 2 users")

    if message.author.mention == p2["p"] and battlestatus==True:
        print("p2 trigger")
        dmg = random.randint(0, 10)
        p1["hp"] -= dmg
        await message.channel.send(message.author.mention + " HIT " + p1["p"] + " FOR " + str(dmg) + "DAMAGE!")
        if dmg >=7:
            await message.channel.send("THATS A LOTTA DAMAGE")
        if p1["hp"] <=0:
            battlestatus = await battle_end()
            await message.channel.send(message.author.mention + "WINS!!!!!")
    elif message.author.mention == p1["p"] and battlestatus==True:
        print("p1 trigger")
        dmg = random.randint(0, 10)
        p2["hp"] -= dmg
        await message.channel.send(message.author.mention + " HIT " + p2["p"] + " FOR " + str(dmg) + "DAMAGE!")
        if dmg >=7:
            await message.channel.send("THATS A LOTTA DAMAGE")
        if p2["hp"] <=0:
            battlestatus = await battle_end()
            await message.channel.send(message.author.mention + "WINS!!!!!")
    dmg = 0
    print(message.author.mention)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
