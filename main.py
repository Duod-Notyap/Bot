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
@client.event
async def on_message(message):
    global badwordpeople
    global lookingforans
    trivq = 0

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


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
