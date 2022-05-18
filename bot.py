# id: [CENSORED_ID]
# token: [CENSORED_TOKEN]
# perms: 100352
# https://discordapp.com/oauth2/authorize?client_id=[CENSORED_ID]&scope=bot&permissions=100352

import discord
import cv2
import random
import os
import requests
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pytesseract

client = discord.Client()

@client.event
async def on_ready():       # called on initial call
    print( f"Logged in as { client.user }" )

@client.event   
async def on_message( message ):    # everytime a message is sent
    # print its data
    print( f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "i'm" in message.content.lower()[0:3]:
        await message.channel.send("Hi " +message.content.lower()[4:]+ " I'm dad")
    if "im" in message.content.lower()[0:2]:
        await message.channel.send("Hi " +message.content.lower()[3:]+ " I'm dad")

    if "🐱" in message.content.lower():     # special emojis
        await message.channel.send( "m e o w" )
    if "<:brr:760646744181702676>" in message.content.lower():
        await message.channel.send( "m e o w" )
    if "☢️" in message.content.lower():
        await message.channel.send( "Of course, the whole point of a Doomsday Machine is lost, if you *keep* it a *secret*! Why didn't you tell the world, EH?" )
    if "🐶" in message.content.lower():     # special emojis
        if random.randint( 0, 1 ) == 0:
            await message.channel.send( "w o o f" )
        else:
            await message.channel.send( "g r r" )
    if "🐍" in message.content.lower():     # special emojis
        await message.channel.send( "h i s s" )
    if "🐟" in message.content.lower():     # special emojis
        await message.channel.send( "g l u b" )
    if "🐦" in message.content.lower():     # special emojis
        await message.channel.send( "t w e e t" )
    if "<:grr_bby_grr:760962346830004244>" in message.content.lower():
        await message.channel.send( "***grr***" )
    if "<:chainsawwaifu:758312251513634826>" in message.content.lower():
        await message.channel.send( "_haha chainsaw go_ ***brrrr***" )
    if "🐮" in message.content.lower():
        await message.channel.send( "m o o" )
    if "🦑" in message.content.lower():
        await message.channel.send( "g l u b  g l u b" )
    if "🐭" in message.content.lower():
        await message.channel.send( "s q u e a k" )
    if "🐡" in message.content.lower():
        await message.channel.send( "🥕" )
    if "🎺" in message.content.lower():
        await message.channel.send( "t o o t" ) 
    if "🥶" in message.content.lower():
        await message.channel.send( "b r r r r" )
    if "😡" in message.content.lower():
        await message.channel.send( "a n g e r" )
    if "👯‍" in message.content.lower():
        await message.channel.send( "o o o h l a l a :yum:" )

    if "strangelove" in message.content.lower():
        await message.channel.send( "Hello, +help for help!" )

    if "+help" == message.content.lower():
        await message.channel.send( "Avalible:\n\t+help\n\t+place <yourx> <youry> #<html color tag>\n\t+place <yourx> <youry> <black/white/red/orange/yellow/green/blue/magenta/purple/brown/teal/grey/gray/lime/aqua/pink>\n\t+viewplace\n\t🐱\n\t☢" )
   
    if message.attachments:
        for e in message.attachments:
            if e.url.endswith(("png", "jpg")):
                loc = str(random.randint(0,10000000)) + ".png"
                img_data = requests.get(e.url).content
                sp = e.url.split("/")
                fn = sp[len(sp) - 2] + "-" + sp[len(sp) - 1]
                with open(f"{loc}", "ab") as handler:
                    handler.write(img_data)
                    print(f"Downloaded {e.url} to {loc}")
                img = cv2.imread( loc )
                bbox, label, conf = cv.detect_common_objects(img)
                strout = ""
                if len( label ) > 0:
                    for l in label: 
                        strout += l 
                        strout += ", "
                    strout = strout[0:len( strout ) - 2]
                    await message.channel.send( "I think there are: " + strout )
                data = pytesseract.image_to_string(cv2.imread(loc), lang='eng', config='--psm 6')
                if not "@" in data:
                    await message.channel.send( data )
                os.system( "rm " + loc )


    if "+viewplace" == message.content.lower():
        file = discord.File( "place.png", filename = "place.png" )
        await message.channel.send( "place.png", file = file )
    if "+place" in message.content.lower()[ :6 ]:
        temp = message.content.lower().split( " " )
        if len( temp ) == 4:
            try:
                y = int( temp[ 1 ] )
                x = int( temp[ 2 ] )
                oldtemp3 = temp[ 3 ]
                temp[ 3 ] = temp[ 3 ].replace( "#", "" )
                if oldtemp3 == temp[ 3 ]:   #is color name
                    if temp[ 3 ] == "black":
                        red = 0    
                        green = 0
                        blue = 0
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "white":
                        red = 255
                        green = 255
                        blue = 255
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "red":
                        red = 255
                        green = 0
                        blue = 0
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "orange":
                        red = 255
                        green = 136
                        blue = 0
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "yellow":
                        red = 255
                        green = 200
                        blue = 0
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "green":
                        red = 0
                        green = 128
                        blue = 0
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "blue":
                        red = 0
                        green = 0
                        blue = 255
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "magenta":
                        red = 255
                        green = 0
                        blue = 255
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "purple":
                        red = 100
                        green = 0
                        blue = 160
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "secret":
                        red = 18
                        green = 255
                        blue = 170
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "brown":
                        red = 120
                        green = 74
                        blue = 0
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "teal":
                        red = 0
                        green = 80
                        blue = 80
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "lime":
                        red = 0
                        green = 255
                        blue = 0
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "grey" or temp[ 3 ] == "gray":
                        red = 128
                        green = 128
                        blue = 128
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "aqua":
                        red = 0
                        green = 255
                        blue = 255
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    elif temp[ 3 ] == "pink":
                        red = 255
                        green = 192
                        blue = 203
                        img = cv2.imread( "place.png" )
                        if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                            raise
                        img[ x, y ] = [ blue, green, red ]
                        cv2.imwrite( "place.png", img )
                        file = discord.File( "place.png", filename = "place.png" )
                        await message.channel.send( "place.png", file = file )
                    else:
                        raise
                else:   #hexcode specified
                    red = int( temp[ 3 ][0:2], 16 )     
                    green = int( temp[ 3 ][ 2:4 ], 16 )
                    blue = int( temp[ 3 ][ 4:6 ], 16 )
                    img = cv2.imread( "place.png" )
                    if img.shape[ 0 ] < x or img.shape[ 1 ] < y:
                        raise
                    img[ x, y ] = [ blue, green, red ]
                    cv2.imwrite( "place.png", img )
                    file = discord.File( "place.png", filename = "place.png" )
                    await message.channel.send( "place.png", file = file )
            except:
                await message.channel.send( "It seems you have sent an invalid message." )
        else:
            await message.channel.send( "It seems you have sent an invalid message." )

client.run( open(os.path.dirname(os.path.abspath(__file__)) + '/configuration/token.txt', 'r').read() )     # ew
