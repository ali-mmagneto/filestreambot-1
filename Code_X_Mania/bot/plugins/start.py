# (c) Code-X-Mania

from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram.enums import ParseMode, ChatType, MessageMediaType
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyshorteners import Shortener

@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Banlandın Dostum..**",
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Beni Kullanmak için Kişisel Bloguma katıl yada katılma.. 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Kişisel Blog 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode=ParseMode.HTML
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Bir Hata oluştu..</i> <b> <a href='http://t.me/Adarsh_staus_bot'>CLICK HERE FOR SUPPORT </a></b>",
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="""
<i>👋 Merhaba</i>\n
<i>Sana Telegramda bulunan Dosyaların indirme ve izleme linklerini vereceğim..!<i>\n
<i>Bilgi için /help Kullan..</i>\n\n
<i><b>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</i>\n
<i><u>🔞 Dostum Porno yollama hoş değil.. </u></i>\n
<b>🍃 Bᴏᴛ Made Bʏ: @mmagneto.</b>""",
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton('Owner', url=f"https://t.me/{Var.OWNER_USERNAME}"),
                                                                                       InlineKeyboardButton('Follow ', url='https://github.com/Code-x-Mania') ] ]  ) )
                                                                                       
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sen Banlısın Dostum",
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Botu Kullanabilmek İçin Kişisel Bloguma katıl yada katılma..**!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Kişisel Blog", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Yenile",
                                                     url=f"https://t.me/{Var.APP_NAME}.herokuapp.com/{usr_cmd}") # Chnage ur app name
                            ]
                        ]
                    ),
                    parse_mode=ParseMode.MARKDOWN
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Bir Sorun Oluştu..",
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = Var.URL + 'izle/' + str(log_msg.id)
        online_link = Var.URL + 'indir/' + str(log_msg.id)

        msg_text ="""
<i><u>Linkin Oluşturuldu!</u></i>

<b>📂 Dosya Adı :</b> <i>{}</i>

<b>📦 Dosya Boyutu :</b> <i>{}</i>

<b>📥 İndir :</b> <i>{}</i>

<b> 🖥 İzle  :</b> <i>{}</i>

<b>🚸 Not : Link Süresizdir</b>

<i>© @mmagneto </i>"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🖥STREAM", url=stream_link), #Stream Link
                                                InlineKeyboardButton('Dᴏᴡɴʟᴏᴀᴅ📥', url=online_link)]]) #Download Link
        )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Banlısın Dostum..</i>",
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Botu Kullanmak için Blog Kanalıma katıl veya katılma..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Blog Kanalım", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode=ParseMode.MARKDOWN
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Bir Sorun Oldu.",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True)
            return
   
    await message.reply_text(
       text="https://telegra.ph/Adarsh-10-22-3",
            parse_mode=ParseMode.HTML,
            
          reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🏵 Geliştirici", url="https://t.me/mmagneto")],
                [InlineKeyboardButton("🍺 Kişisel Blog", url="https://t.me/mmagneto3")]
            ]
        )
    )
