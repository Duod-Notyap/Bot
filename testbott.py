import discord

TOKEN = 'NDk3Mjg2ODUwMzIzNDE1MDQx.Dpc-GA.JkTmPuavdjxirmGbMWP6D2IrYd0'

client = discord.Client()
str = ""
@client.event
async def on_message(message):
    global str

    if message.author == client.user:
        return



@client.event
async def on_ready():
    global str
    print(client.user.name)
    print("ready!")
    str = input("input:")


client.run(TOKEN)
