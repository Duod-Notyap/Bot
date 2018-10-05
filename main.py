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
badwords = ["fuck", "shit", "dammit", "damn", "crap", "bitch", "fuq", "fuk", "feck", "fook", "dicc", "dick", "ass", "darn", "shoot", "heck", "shoot", "effin", "bish", "hell", "eff", "cock"]
p1 = {"p":"", "hp": 30}
p2 = {"p":"", "hp": 30}


repcounters = []
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

with open('REPS.txt') as b:
    for line in b.readlines():
        print(line)
        person = line.split("\'p\': ")[1].split(",")[0]
        num = int(line.split("\'rep\': ")[1].split("}")[0])
        repcounters.append({"p":person.replace("\'", ""), "rep":num})

with open('triviaqfile.txt') as n:
    for line in n.readlines():
        q = line.split("[[[")
        trivialist.append({"q":q[0], "ans":q[1]})
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
                        os.remove("badwordspeople.txt")
                        badwordfile = open("badwordspeople.txt", "w+")
                        for badperson in badwordpeople:
                            badwordfile.write(str(badperson))
                        badwordfile.close()
                        return
                badwordpeople.append({"p": message.author.id, "num": 1})
                await message.channel.send("tsk tsk you've cursed {} times now".format(badwordpeople[-1]["num"]))
        os.remove("badwordspeople.txt")
        badwordfile = open("badwordspeople.txt", "w+")
        for badperson in badwordpeople:
            badwordfile.write(str(badperson))
        badwordfile.close()




#rep counter
    if message.author.roles[-1].permissions.administrator == True:
        if message.content.startswith("-rep"):
            for person in repcounters:
                if person["p"] == message.content.split(" ")[1]:
                    print(person)
                    person["rep"] -= 5
                    await message.channel.send("OOF your rep is now {}".format(str(person["rep"])))
                    os.remove("reps.txt")
                    repfile = open("reps.txt", "w+")
                    for person in repcounters:
                        repfile.write(str(person))
                    repfile.close()
                    return
            repcounters.append({"p":message.content.split(" ")[1], "rep": 35})
            await message.channel.send("OOF your rep is now {}".format(str(repcounters[-1]["rep"])))
            os.remove("reps.txt")
            repfile = open("reps.txt", "w+")
            for person in repcounters:
                repfile.write(str(person))
            repfile.close()
        elif message.content.startswith("+rep"):
            for person in repcounters:
                if person["p"] == message.content.split(" ")[1]:
                    print(person)
                    person["rep"] += 5
                    await message.channel.send("YAY your rep is now {}".format(str(person["rep"])))
                    os.remove("reps.txt")
                    repfile = open("reps.txt", "w+")
                    for person in repcounters:
                        repfile.write(str(person))
                    repfile.close()
                    return
            repcounters.append({"p":message.content.split(" ")[1], "rep": 35})
            await message.channel.send("YAY your rep is now {}".format(str(repcounters[-1]["rep"])))
            os.remove("reps.txt")
            repfile = open("reps.txt", "w+")
            for person in repcounters:
                repfile.write(str(person))
            repfile.close()
    print("this shouldnt print on a -rep: {}".format(message.content))
    print(str(repcounters))

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

#y e e t
    if "yeet" in message.content.lower():
        await message.channel.send("***YEET***")

#alexa play despayeeto
    if message.content.startswith("^sad"):
        await message.channel.send("This is so sad alexa play despayeeto")


#returns url to source code
    if message.content.startswith("^source"):
        await message.channel.send("https://github.com/Duod-Notyap/Bot/blob/master/main.py")
#lets users check their reps
    if message.content.startswith("^myrep"):
        for person in repcounters:
            if person["p"] == "<@{}>".format(str(message.author.id)):
                await message.channel.send("Your rep is {}".format(person["rep"]))
                return
        await message.channel.send("You don't have a rep counter so its most likely at the base 40")

    if message.content.startswith("^clear") and message.author.roles[-1].permissions.administrator == True:
        msgs = []
        mesgtodel = int(message.content.split(" ")[1])
        async for x in message.channel.history():
            msgs.append(x)
        await message.channel.delete_messages(msgs)

#log readiness of bot
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#run the bot
client.run(TOKEN)
