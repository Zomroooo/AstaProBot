# AI Chat (C) 2020-2021 by @Aceladi

import emoji
import re
import aiohttp
from googletrans import Translator
from pyrogram import filters
from aiohttp import ClientSession
from SiestaRobot import BOT_USERNAME as bu
from SiestaRobot import BOT_ID, pbot, arq
from SiestaRobot.ex_plugins.chatbot import add_chat, get_session, remove_chat
from SiestaRobot.utils.pluginhelper import admins_only, edit_or_reply
from SiestaRobot.modules.language import gs

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = Translator()


async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


async def fetch(url):
    try:
        async with aiohttp.Timeout(1.0):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    try:
                        data = await resp.json()
                    except:
                        data = await resp.text()
            return data
    except:
        print("AI response Timeout")
        return


ewe_chats = []
en_chats = []


@pbot.on_message(filters.command(["chatbot", f"chatbot@{bu}"]) & ~filters.edited & ~filters.bot & ~filters.private)
@admins_only
async def hmm(_, message):
    global ewe_chats
    if len(message.command) != 2:
        await message.reply_text("I only recognize /chatbot on and /chatbot off only")
        message.continue_propagation()
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("Kaguya AI Already Activated In This Chat")
            return
        await lel.edit(f"Kaguya AI Actived by {message.from_user.mention()} for users in {message.chat.title}")

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("Kaguya AI Was Not Activated In This Chat")
            return
        await lel.edit(f"Kaguya AI Deactivated by {message.from_user.mention()} for users in {message.chat.title}")

    elif status == "EN" or status == "en" or status == "english":
        if not chat_id in en_chats:
            en_chats.append(chat_id)
            await message.reply_text(f"English AI chat Enabled by {message.from_user.mention()}")
            return
        await message.reply_text(f"English AI Chat Disabled by {message.from_user.mention()}")
        message.continue_propagation()
    else:
        await message.reply_text("I only recognize `/chatbot on` and `chatbot off` only")


@pbot.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        return
    if not message.reply_to_message:
        return
    try:
        senderr = message.reply_to_message.from_user.id
    except:
        return
    if senderr != BOT_ID:
        return
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("Kaguya", "Aco")
        test = test.replace("Kaguya", "Aco")
        test = test.replace("My god is @Aceladi", "I'm a Christian")
        test = test.replace("16", "9")
        test = test.replace("@Aceladi is my husbando.", "I'm single.")
        test = test.replace("My husbando is @Aceladi", "I'm single.")
        test = test.replace("@NexusXSupport", "Siestabot.ai")
        test = test.replace("I live in @NexusXSupport.", "I live in San Francisco, California.")
        test = test.replace("I was created by @Aceladi", "I made myself")
        test = test.replace(
            "Hello there I am Siesta...nice to meet u",
            "Hi, my friend! Do you want me to tell you a joke?")
        test = test.replace("Aceladi is my owner", "Have the control right.")
        test = test.replace(
            "Hi, My name is Kaguya Nice to meet you.",
            "Hi, my friend, what can I do for you today?")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "Siesta")
        response = response.replace("aco", "siesta")
        response = response.replace("Luna", "Siesta")
        response = response.replace("luna", "siesta")
        response = response.replace("I'm a Christian", "My god is @Aceladi")
        response = response.replace("9", "16")
        response = response.replace("I'm married to my job.", "I'm married with @Aceladi")
        response = response.replace("I'm single.", "My husband is @Aceladi")
        response = response.replace("Siestabot.ai", "@NexusXSupport")
        response = response.replace("I live in San Francisco, California.", "I live in @NexusXSupport.")
        response = response.replace("I made myself", "I was Created by @Aceladi")
        response = response.replace(
                "Hi, my friend! Do you want me to tell you a joke?",
                "Hello there I am Siesta...nice to meet u")
        response = response.replace("Have the control right.", "@saint_foire is my owner.")
        response = response.replace(
                "Hi, my friend, what can I do for you today?",
                "Hi, My name is Kaguya Nice to meet you")

        pro = response
        try:
            await pbot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return

    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
        try:
            lan = translator.detect(rm)
            lan = lan.lang
        except:
            return
        test = rm
        if not "en" in lan and not lan == "":
            try:
                test = translator.translate(test, dest="en")
                test = test.text
            except:
                return
        # test = emoji.demojize(test.strip())

        test = test.replace("Siesta", "Aco")
        test = test.replace("Siesta", "Aco")
        test = test.replace("My god is @saint_foire", "I'm a Christian")
        test = test.replace("16", "9")
        test = test.replace("@saint_foire is my husband.", "I'm single.")
        test = test.replace("@machinaxsupport", "Siestabot.ai")
        test = test.replace("I live in @machinaxsupport.", "I live in San Francisco, California")
        test = test.replace("I was created by @saint_foire", "I made myself")
        test = test.replace(
            "Hello there I am Siesta...nice to meet u",
            "Hi, my friend! Do you want me to tell you a joke?")
        test = test.replace("@saint_foire is my owner", "Have the control right.")
        test = test.replace(
            "Hi, My name is Siesta Nice to meet you.",
            "Hi, my friend, what can I do for you today?")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "Siesta")
        response = response.replace("aco", "siesta")
        response = response.replace("Luna", "Siesta")
        response = response.replace("luna", "siesta")
        response = response.replace("I'm a Christian", "My god is @saint_foire")
        response = response.replace("9", "16")
        response = response.replace("I'm married to my job.", "I'm married with @saint_foire")
        response = response.replace("I'm single.", "My husband is @saint_foire")
        response = response.replace("Siestabot.ai", "@machinaxsupport")
        response = response.replace("I live in San Francisco, California.", "I live in @machinaxsupport.")
        response = response.replace("I made myself", "I was Created by @saint_foire")
        response = response.replace(
                "Hi, my friend! Do you want me to tell you a joke?",
                "Hello there I am Siesta...nice to meet u")
        response = response.replace("Have the control right.", "@saint_foire is my owner.")
        response = response.replace(
                "Hi, my friend, what can I do for you today?",
                "Hi, My name is Siesta Nice to meet you")
        pro = response
        if not "en" in lan and not lan == "":
            try:
                pro = translator.translate(pro, dest=lan)
                pro = pro.text
            except:
                return
        try:
            await pbot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return


@pbot.on_message(filters.text & filters.private & ~filters.edited & filters.reply & ~filters.bot)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return
    test = test.replace("Siesta", "Aco")
    test = test.replace("Siesta", "Aco")
    test = test.replace("My god is @saint_foire", "I'm a Christian")
    test = test.replace("16", "9")
    test = test.replace("@saint_foire is my husband.", "I'm single.")
    test = test.replace("@machinaxsupport", "Siestabot.ai")
    test = test.replace("I live in @machinaxsupport.", "I live in San Francisco, California.")
    test = test.replace("I was created by @saint_foire", "I made myself")
    test = test.replace(
        "Hello there I am Siesta...nice to meet u",
        "Hi, my friend! Do you want me to tell you a joke?")
    test = test.replace("@saint_foire is my owner", "Have the control right.")
    test = test.replace(
        "Hi, My name is Siesta Nice to meet you.",
        "Hi, my friend, what can I do for you today?")

    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Aco", "Siesta")
    response = response.replace("aco", "siesta")
    response = response.replace("Luna", "Siesta")
    response = response.replace("luna", "siesta")
    response = response.replace("I'm a Christian", "My god is @saint_foire")
    response = response.replace("9", "16")
    response = response.replace("I'm married to my job.", "I'm married with @saint_foire")
    response = response.replace("I'm single.", "My husband is @saint_foire")
    response = response.replace("Siestabot.ai", "@machinaxsupport")
    response = response.replace("I live in San Francisco, California.", "I live in @machinaxsupport")
    response = response.replace("I made myself", "I was Created by @saint_foire")
    response = response.replace(
            "Hi, my friend! Do you want me to tell you a joke?",
            "Hello there I am Siesta...nice to meet u")
    response = response.replace("Have the control right.", "@saint_foire is my owner.")
    response = response.replace(
            "Hi, my friend, what can I do for you today?",
            "Hi, My name is Siesta Nice to meet you")

    pro = response
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, dest=lan)
        pro = pro.text
    try:
        await pbot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


@pbot.on_message(filters.regex("Siesta|siesta|robot|SIESTA|vain") & ~filters.bot & ~filters.via_bot  & ~filters.forwarded & ~filters.reply & ~filters.channel & ~filters.edited)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return

    # test = emoji.demojize(test.strip())

    test = test.replace("Siesta", "Aco")
    test = test.replace("Siesta", "Aco")
    test = test.replace("My god is @saint_foire", "I'm a Christian")
    test = test.replace("16", "9") 
    test = test.replace("@saint_foire is my husband.", "I'm single.")
    test = test.replace("@machinaxsupport", "Siestabot.ai")
    test = test.replace("I live in @machinaxsupport.", "I live in San Francisco, California.")
    test = test.replace("I was created by @saint_foire", "I made myself")
    test = test.replace(
        "Hello there I am Siesta...nice to meet u",
        "Hi, my friend! Do you want me to tell you a joke?")
    test = test.replace("@saint_foire is my owner", "Have the control right.")
    test = test.replace(
        "Hi, My name is Siesta Nice to meet you.",
        "Hi, my friend, what can I do for you today?")
    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Aco", "Siesta")
    response = response.replace("aco", "siesta")
    response = response.replace("Luna", "Siesta")
    response = response.replace("luna", "siesta")
    response = response.replace("I'm a Christian", "My god is @saint_foire")
    response = response.replace("I'm married to my job.", "I'm married with @saint_foire")
    response = response.replace("9", "16") 
    response = response.replace("I'm single.", "My husband is @saint_foire")
    response = response.replace("Siestabot.ai", "@machinaxsupport")
    response = response.replace("I live in San Francisco, California.", "I live in @machinaxsupport.")
    response = response.replace("I made myself", "I was Created by @saint_foire")
    response = response.replace(
            "Hi, my friend! Do you want me to tell you a joke?",
            "Hello there I am Siesta...nice to meet u")
    response = response.replace("Have the control right.", "@saint_foire is my owner.")
    response = response.replace(
            "Hi, my friend, what can I do for you today?",
            "Hi, My name is Siesta Nice to meet you")

    pro = response
    if not "en" in lan and not lan == "":
        try:
            pro = translator.translate(pro, dest=lan)
            pro = pro.text
        except Exception:
            return
    try:
        await pbot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


def helps(chat):
    return gs(chat, "chatbot_help")

__mod_name__ = "Chatbot"
