import discord
import os
import requests 
import json
import random
from replit import db


client = discord.Client()

joemama = ['your mom','teri maa ki','mammi','joe mama','mammi','mummy','maa','mother','mom','I fucked your mom','joemama']

joemama_replies = ['Your mom and your mom jokes, both are overused','atleast im not her biggest dissapointment anymore','joe mama so fat, thanos had to clap', 'joe mama so fat even dora couldnt explore her','I wish ur mum was worth fucking','I dont think necrophilia is something to brag about','HEY! Lets get off moms....i just got off yours', 'Your mum jokes are so old; almost as old as your mum']

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!",
  "keep up"
]

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + ' -' + json_data[0]["a"]
  return(quote)

  
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]
    

def delete_encouragement(index):
  encouragements = db["encouragaments"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements
    

def update_joemamas(message):
  if "joemama" in db.keys():
    joemama = db["joemama"]
    joemama.append(message)
    db["joemama"] = joemama
  else:
    db["joemama"] = [message]
    

def delete_joemama(index1):
  joemama = db["joemama"]
  if len(joemama) > index1:
    del joemama[index1]
    db["joemama"] = joemama
  

@client.event 
async def on_ready():
    print("I'm in")
    print(client.user)
  
@client.event 
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if msg.startswith('!rc'):
    await message.channel.send('hello')
  if msg.startswith('rc inspire me'):
    quote1 = get_quote()
    await message.channel.send(quote1)

  
  if any(word in msg for word in joemama):
    await message.channel.send(random.choice(joemama_replies))

    
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

    
 
    
token = os.environ.get("redcordsecret")
import os
try:
    client.run(token)
except:
    os.system("kill 1")
client.run(token)