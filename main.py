from os import link
from pyrogram import Client
import asyncio
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import random


list = []
converter = []

API_ID = 17158127
API_HASH = 'd1a5974070430293b64fde5339591447'
Token = '5615677984:AAGmN2mEaKzp5dYKLlR3s92YORbuSKV_5jQ' #token del bot

bot = Client('session', api_id=API_ID, api_hash=API_HASH, bot_token=Token)

@bot.on_message()
async def message_handler(client: Client, message: Message):
    msg: str = str(message.text)
    send = message.reply
    username = message.from_user.username
    name = message.from_user.first_name

    if msg.startswith('/start'):
        await send(f'Hola {name} envie un txt para convertirlo')

    if not '/' in msg:
        txt = await message.download()
        with open(txt, "rb") as f:
            msg = f.read().decode("UTF-8")
            for i in msg.split('\n'):
                list.append(i)
            for i in list:
                i = i.split('\t')[-1]
                a = 'https://repotematico.uo.edu.cu/sites/default/files/Paquete_contenido/' + i 
                converter.append(a)       
            namet = str(random.randint(11111,9999999)) + '.txt'
            with open(namet, 'w') as txt:
                progress = None;progress_args = None
                links_str = '' 
                for item in converter:
                    links_str += item+'\n'
                txt.write(links_str);txt.close()
                await message.reply_document(namet,progress=progress, progress_args=progress_args)
                list.clear();converter.clear()   
print('init')
bot.run()        
     
