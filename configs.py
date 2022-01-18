# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))

    START_TEXT = """
**Hᴇʟʟᴏ {}, I'ᴍ ᴀ Sɪᴍᴘʟᴇ Vɪᴅᴇᴏ Mᴇʀɢᴇʀ Bᴏᴛ!
I Cᴀɴ Mᴇʀɢᴇ Mᴜʟᴛɪᴘʟᴇ Vɪᴅᴇᴏs Iɴᴛᴏ Oɴᴇ Vɪᴅᴇᴏ, Gᴇɴᴇʀᴀᴛᴇ SᴄʀᴇᴇɴSʜᴏᴛs, Gᴇɴᴇʀᴀᴛᴇ Sᴀᴍᴘʟᴇ Vɪᴅᴇᴏ Aɴᴅ Mᴀɴʏ Exᴛʀᴀ Fᴇᴀᴛᴜʀᴇs....!

Cᴏɴғɪɢᴜʀᴇ Tʜᴇ Sᴇᴛᴛɪɴɢs Bᴇғᴏʀᴇ Usɪɴɢ Mᴇʜ...!
Cʜᴇᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs Fᴏʀ Mᴏʀᴇ..! 

🤖 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗔𝗡𝗗 𝗠𝗔𝗧𝗜𝗡𝗔𝗘𝗗 𝗕Y : [KOT DEV](https://t.me/KOT_FREE_DE_LA_HOYA_OFF)**
"""
    ABOUT_TEXT = """
╭──────[@KOT_BOTS]───────〄
│
├ Nᴀᴍᴇ : <a href='https://t.me/KOT_VIDEO_MERGER_BOT'>Vɪᴅᴇᴏ Mᴇʀɢᴇʀ Bᴏᴛ</a>
│
├ Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>Hᴇʀᴏᴋᴜ</a>
│ 
├ Lᴀɴɢᴜᴀɢᴇ : <a href='https://docs.pyrogram.org/'>Pʏᴛʜᴏɴ 3.9.6</a>
│
├ Vᴇʀꜱɪᴏɴ : <a href='https://t.me/KOT_VIDEO_MERGER_BOT</a>
│
├ Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ 1.2.9</a>
│
├ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/KOT_FREE_DE_LA_HOYA_OFF'>✯°• Kᴏᴛ Fʀᴇᴇ Dᴇ Lᴀ Hᴏʏᴀ Oғғ °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪</a>
│
├ Pᴏᴡᴇʀᴇᴅ Bʏ : <a href='https://t.me/KOT_LINKS_TEAM'>Kᴏᴛ Lɪɴᴋs Tᴇᴀᴍ</a>
│
├ Uᴘᴅᴀᴛᴇᴅ Oɴ : [ 19.1.2022 ] 07:09 AM

©️ 𝗕𝗢𝗧 𝗠𝗔𝗧𝗜𝗡𝗔𝗘𝗗 𝗕𝗬 : @KOT_BOTS
"""

    HELP_TEXT = """**Hᴇʟʟᴏ {}, It's too easy to use me..**
 
● Cᴏɴғɪɢᴜʀᴇ Tʜᴇ Sᴇᴛᴛɪɴɢs Bᴇғᴏʀᴇ Usɪɴɢ Mᴇ... 
● Sᴇɴᴅ ᴀ Pʜᴏᴛᴏ Tᴏ Sᴇᴛ Iᴛ As Yᴏᴜʀ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ...
● Sᴇɴᴅ Vɪᴅᴇᴏs Tᴏ Mᴇʀɢᴇ Aᴄᴄᴏʀᴅɪɴɢʟʏ..

  - Aᴛʟᴇᴀsᴛ 𝟸 Vɪᴅᴇᴏs Tᴏ Bᴇ Sᴇɴᴛ Tᴏ Mᴇʀɢᴇ
  - Tʜᴇ Vɪᴅᴇᴏ Fᴏʀᴍᴀᴛs Sʜᴏᴜʟᴅ Bᴇ Mᴘ𝟺, Mᴋᴠ Oʀ WᴇʙM
  - Tʜᴇ Vɪᴅᴇᴏs Sʜᴏᴜʟᴅ Hᴀᴠᴇ Pʀᴏᴘᴇʀ Fɪʟᴇ Nᴀᴍᴇ

● Iғ Yᴏᴜ Aʀᴇ Dᴏɴᴇ Wɪᴛʜ Sᴇɴᴅɪɴɢ Mᴇᴅɪᴀs, Cʟɪᴄᴋ "🔀 Mᴇʀɢᴇ Nᴏᴡ" Tᴏ Mᴇʀɢᴇ
● Tʜᴀᴛ's Iᴛ, Aɴᴅ Rᴇsᴛ Is Mɪɴᴇ Wᴏʀᴋ...

© 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 @KOT_FREE_DE_LA_HOYA_OFF ❤️**
"""
    
    CAPTION = "**__© Merged By @KOT_BOTS ❤️__**"
    PROGRESS = """
╭─────────────────────⍟
│
├⏳ 𝐄𝐓𝐀: {4}
│
├🛠 𝐏𝐞𝐫𝐜𝐞𝐧𝐭𝐚𝐠𝐞 : {0}%
│
├✅ 𝐃𝐨𝐧𝐞: {1}
│
├📡 𝐓𝐨𝐭𝐚𝐥: {2}
│
├🚀 𝐒𝐩𝐞𝐞𝐝: {3}/s
│
╰──────────[🌩️]──────────⍟
"""
