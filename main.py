import random
import discord
import os
import time

TOKEN = 'NDk1NDgzMDc3NjI0MDcwMTU0.Dpbbgw.t-EC7fYCMezsHb1D-_Hd4tq6X3A'

badwordpeople = []
lookingforans ={"stat":False, "q":1}
trivialist = []
client = discord.Client()
badwords = ["fuck", "shit", "dammit", "damn", "crap", "bitch", "fuq", "fuk", "feck", "fook", "dicc", "dick", "ass", "effin", "bish", "eff", "cock", "fack", "fak", "fek", "nigger", "owo", "uwu"]
p1 = {"p":"", "hp": 30}
p2 = {"p":"", "hp": 30}
muted = []

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
        msg = 'HECKIN\' *dies*'
        await message.channel.send(msg)
        print("Me: " + msg)

#Swear counter
    if message.author.roles[-1].permissions.administrator != True and message.author.id != 237948713123708939:
        for word in badwords:
            strbad = message.content.lower()
            if word in strbad:
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
                    if len(message.content.split(" ")) >= 3:
                        person["rep"] -= int(message.content.split(" ")[2])
                    if len(message.content.split(" ")) == 2:
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
                    if len(message.content.split(" ")) >= 3:
                        person["rep"] += int(message.content.split(" ")[2])
                    if len(message.content.split(" ")) == 2:
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
        elif message.content.startswith("=rep"):
            for person in repcounters:
                if person["p"] == message.content.split(" ")[1]:
                    print(person)
                    person["rep"] = int(message.content.split(" ")[2])
                    await message.channel.send("Your rep is now {}".format(str(person["rep"])))
                    os.remove("reps.txt")
                    repfile = open("reps.txt", "w+")
                    for person in repcounters:
                        repfile.write(str(person))
                    repfile.close()
                    return
            repcounters.append({"p":message.content.split(" ")[1], "rep": 35})
            await message.channel.send("Your rep is now {}".format(str(repcounters[-1]["rep"])))
            os.remove("reps.txt")
            repfile = open("reps.txt", "w+")
            for person in repcounters:
                repfile.write(str(person))
            repfile.close()

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
        await message.channel.send("https://github.com/Duod-Notyap/Bot/")
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
        await message.channel.delete_messages(await message.channel.history(limit=mesgtodel).flatten())

    if message.content.startswith("^allreps") and message.author.roles[-1].permissions.administrator == True:
        for i in repcounters:
            await message.channel.send("{} has {} rep".format(i["p"], str(i["rep"])))

#mutes a person
    if message.content.lower().startswith("^mute") and message.author.roles[-1].permissions.administrator == True:
        messagesplit = message.content.split(" ")
        messagesplit[1] = messagesplit[1].replace("!", "")
        if len(messagesplit) == 2:
            muted.append({"name":int(messagesplit[1][2:-1]), "time":9999999999999999, "start":time.time()})
            await message.channel.send("{} got muted FOREVER".format(messagesplit[1]))
            return;
        muted.append({"name":int(messagesplit[1][2:-1]), "time":int(messagesplit[2]), "start":time.time()})
        await message.channel.send("Oops {} just got muted for {} seconds!".format(messagesplit[1], messagesplit[2]))

#test if a person is muted and stop the message
    for user in muted:
        if user["name"] == message.author.id and time.time()-user["start"]<user["time"]:
            await message.delete()

#remove an ended muting
    for user in muted:
        if time.time()-user["start"]>user["time"]:
            muted.remove(user)

    if message.content.startswith("^detime"):
        await message.channel.send("It is currently {} despacitos since the epoch".format(str(int(time.time() / 227))))

    if message.author.roles[-1].permissions.administrator == True and message.content.startswith("^unmute"):
        splitted = message.content.split(" ")
        for user in muted:
            splitted[1] = splitted[1].replace("!", "")
            print("{} : {} : {}".format(splitted[1], splitted[1][2:-1], user["name"]))
            if int(splitted[1][2:-1]) == user["name"]:
                muted.remove(user)
                await message.channel.send("{} unmuted".format(splitted[1]))

#log readiness of bot
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#run the bot
client.run(TOKEN)
