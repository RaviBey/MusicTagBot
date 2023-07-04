from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from youtubesearchpython.__future__ import VideosSearch

import config
from FallenMusic import BOT_MENTION, BOT_NAME, app
from FallenMusic.Helpers import gp_buttons, pm_buttons
from FallenMusic.Helpers.dossier import *


@app.on_message(filters.command(["start"]) & ~filters.forwarded)
@app.on_edited_message(filters.command(["start"]) & ~filters.forwarded)
async def fallen_st(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        if len(message.text.split()) > 1:
            cmd = message.text.split(None, 1)[1]
            if cmd[0:3] == "inf":
                m = await message.reply_text("🔎")
                query = (str(cmd)).replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                for result in (await results.next())["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["channel"]["link"]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                searched_text = f"""
➻ **Məlumatı izləyin** 

📌 **Başlıq :** {title}

⏳ **Müddət :** {duration} ᴍɪɴᴜᴛᴇs
👀 **Baxışlar :** `{views}`
⏰ **Dərc olunub :** {published}
🔗 **Link :** [Youtube-da izləyin]({link})
🎥 **Kanal :** [{channel}]({channellink})

💖 Axtarış dəstəklənir {BOT_NAME}"""
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="You Tube", url=link),
                            InlineKeyboardButton(
                                text="Dəstək", url=config.SUPPORT_CHAT
                            ),
                        ],
                    ]
                )
                await m.delete()
                return await app.send_photo(
                    message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=key,
                )
        else:
            await message.reply_photo(
                photo=config.START_IMG,
                caption=PM_START_TEXT.format(
                    message.from_user.first_name,
                    BOT_MENTION,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
            )
    else:
        await message.reply_photo(
            photo=config.START_IMG,
            caption=START_TEXT.format(
                message.from_user.first_name,
                BOT_MENTION,
                message.chat.title,
                config.SUPPORT_CHAT,
            ),
            reply_markup=InlineKeyboardMarkup(gp_buttons),
        )
@app.on_callback_query(filters.regex("tagbutton"))
async def tagbutton(_, query: CallbackQuery):
    await query.edit_message_text(f"──────────────────────\n{query.from_user.mention} kömək “📚 Əmrlər„ bunlardır.⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**㋡⇰ /tag “səbəb„ - 5-li Tag Atışları.**\n**㋡⇰ /etag “səbəb„ - Emoji ilə etiketlər.**\n**㋡⇰ /stag “səbəb„ - Söz'lü Tag etiketlər.**\n**㋡⇰ /tektag “səbəb„ - Üzvləri Tək-Tək etiketlər.**\n**㋡⇰ /usta “səbəb„ - usta Tag Bot'una aid Tag etiketlər.**\n**㋡⇰ /admins “səbəb„ - İdarəçilər Tək-Tək etiketlər.**\n**㋡⇰ /cancel - Tag Ələməyi Dayandır.**\n──────────────────────", 
    reply_markup=InlineKeyboardMarkup([
    [
    InlineKeyboardButton("◄◐ Geri", callback_data="fallen_home"),
    InlineKeyboardButton("🚀 Dəstək", url=config.SUPPORT_CHANNEL)
    ]]))
