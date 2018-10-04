import random
import discord
import os

TOKEN = 'NDk1NDgzMDc3NjI0MDcwMTU0.Dpbbgw.t-EC7fYCMezsHb1D-_Hd4tq6X3A'

badwordpeople = []
lookingforans ={"stat":False, "q":1}
trivialist = [
{"q":"What do Sea Cucumbers use as a self defense mechanism?", "ans":"organs"},
{"q":"Who was the 16th president of the United States of America", "ans":"Abraham Lincoln"}
]
client = discord.Client()
badwords = ["fuck", "shit", "dammit", "damn", "crap", "bitch", "fuq", "fuk", "feck", "fook", "dicc", "dick", "ass", "darn", "shoot", "heck", "shoot", "effin", "bish", "hell"]
p1 = {"p":"", "hp": 30}
p2 = {"p":"", "hp": 30}
battlestatus = False
'''
async def battle_start(message):
    await message.channel.send("BATTLE START!")
    battling=True
    return battling
'''
'''
async def battle_end(message):
    await message.channel.send("THE BATTLE IS OVER")
    battling = False
    return battling
'''
#grab the saved word counters
with open('badwordspeople.txt') as e:
    for line in e.readlines():
        print(line)
        person = int(line.split("\'p\': ")[1].split(",")[0])
        num = int(line.split("\'num\': ")[1].split("}")[0])
        badwordpeople.append({"p":person, "num":num})

#initialize the funfacts
with open('funfactgallery.txt') as f: # Tim added these two lines
    funfactgallery = f.readlines()    # ''

#do on a new message
@client.event
async def on_message(message):
    #set globally accessible variables
    global badwordpeople
    global lookingforans
    trivq = 0
    global battlestatus
    dmg = 0
    global p1
    global p2

#make the bot not respond to itself
    if message.author == client.user:
        return

# ^die command returns "HECKIN' dies"
    if message.content.startswith('^die'):
        msg = 'HECKIN\' *dies*'.format(message)
        await message.channel.send(msg)
        print("Me: " + msg)

#Swear counter
    if message.author.roles[-1].permissions.administrator != True:
        for word in badwords:
            if " {}".format(word) in message.content.lower() or message.content.lower().startswith(word):
                await message.channel.send("THAS A BAD WORD AND A NONO")
                for curser in badwordpeople:
                    if curser["p"] == message.author.id:
                        print("trigger counter")
                        curser["num"] += 1
                        await message.channel.send("tsk tsk you've cursed {} times now".format(curser["num"]))
                        return
                badwordpeople.append({"p": message.author.id, "num": 1})
                await message.channel.send("tsk tsk you've cursed {} times now".format(badwordpeople[-1]["num"]))
        os.remove("badwordspeople.txt")
        badwordfile = open("badwordspeople.txt", "w+")
        for badperson in badwordpeople:
            badwordfile.write(str(badperson))
        badwordfile.close()

#trivia system, implementing as a file is on the todo list
    if message.content.startswith("^trivia"):
        trivq = random.randint(0, len(trivialist)-1)
        await message.channel.send(trivialist[trivq]["q"])
        lookingforans={"stat":True, "q":trivq}
        print(lookingforans)

    if trivialist[lookingforans["q"]]["ans"].lower() in message.content.lower() and lookingforans["stat"] == True:
        await message.channel.send("Correct!")
        lookingforans["stat"] = False

    if lookingforans["stat"] == True:
        print(trivialist[lookingforans["q"]]["ans"].lower())
        print(message.content)

#LiterallySatan is the best
    if message.content.lower().startswith("who is the best bot"):
        await message.channel.send("ME ME ME")

#funfact system code thanks to Jauq  https://github.com/Jauq
    if message.content.startswith("^funfact"):              # Tim added these 4
        fnum = random.randint(0, len(funfactgallery)-1)     # ''
        await message.channel.send(funfactgallery[fnum])    # ''
        print("funfact haha")
                       # ''

#this works, people spam it too fast and it canbt process and variables dont update changes blah blah its getting overloaded
    '''
    if message.content.startswith("^battle") and len(message.content.split(" ")) > 2:
        battlestatus = await battle_start(message)
        p1={"p":message.content.split(" ")[1].replace("!", ""), "hp":30}
        p2={"p":message.content.split(" ")[2].replace("!", ""), "hp":30}
        print(p1)
        print(p2)
        print(message.author.mention)
        return
    elif message.content.startswith("^battle"):
        await message.channel.send("Incorrect syntax, please specify 2 users")
        print(battlestatus)

    if (("<@{}>".format(message.author.id) == p2["p"]) and battlestatus):
        print("p2 trigger")
        dmg = random.randint(0, 10)
        p1["hp"] -= dmg
        await message.channel.send(message.author.mention + " HIT " + p1["p"] + " FOR " + str(dmg) + "DAMAGE!")
        if dmg >=7:
            await message.channel.send("THATS A LOTTA DAMAGE")
        if p1["hp"] <=0:
            battlestatus = await battle_end(message)
            await message.channel.send(message.author.mention + "WINS!!!!!")
    elif (("<@{}>".format(message.author.id) == p1["p"]) and battlestatus):
        print("p1 trigger")
        dmg = random.randint(0, 10)
        p2["hp"] -= dmg
        await message.channel.send(message.author.mention + " HIT " + p2["p"] + " FOR " + str(dmg) + "DAMAGE!")
        if dmg >=7:
            await message.channel.send("THATS A LOTTA DAMAGE")
        if p2["hp"] <=0:
            battlestatus = False
            await message.channel.send(message.author.mention + "WINS!!!!!")
    dmg = 0
    print(message.author.mention)
    '''
#y e e t
    if "yeet" in message.content.lower():
        await message.channel.send("***YEET***")

#alexa play despayeeto
    if message.content.startswith("^sad"):
        await message.channel.send("This is so sad alexa play despayeeto")

#returns url to source code
    if message.content.startswith("^source"):
        await message.channel.send("https://github.com/Duod-Notyap/Bot/blob/master/main.py")

    if message.content.startswith("^clear"):
        message.channel.delete_messages(int(message.content.split(" ")[1]))

#log readiness of bot
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#run the bot
client.run(TOKEN)
