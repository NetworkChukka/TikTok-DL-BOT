from telegram import ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)
import requests
import os
import logging

# ◇─────────────────────────────────────────────────────────────────────────────────────◇


# TikTok Downloader API
API = 'https://api.g99solutions.com/tiktok?url='

# Your BOT Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# TikTok Video URL Types , You Can Add More to This :)
TikTok_Link_Types= ['https://m.tiktok.com','https://vt.tiktok.com','https://tiktok.com','https://www.tiktok.com']

# ParseMode Type For All Messages
_ParseMode=ParseMode.MARKDOWN


# ◇─────────────────────────────────────────────────────────────────────────────────────◇

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def start_handler(update, context):
    update.message.reply_text('[🏖 TikTok Download bot 🏖](https://github.com/NetworkChukka/TikTok-DL-BOT)\n\n[Anonymous Devalopers </> 🇱🇰](https://t.me/ehivpnssh) \n [❤RESPECT MY MASTER❤](https://t.me/networkchukka)',parse_mode=_ParseMode)
    update.message.reply_sticker('CAACAgIAAxkBAAEEyOFiieuJYGSQY9dC-wvkecW4-5LyvwAC1AoAAuhO8Uh29Jn8lOf2iiQE')
    update.message.reply_text(' SEND YOUR TIKTOK LINK IT WAS EASY \n ඔයාගේ ටික්ටොක් ලින්ක් එක එවන්න ඒක ලේසියි \n  FOR MORE DETAILS /about',parse_mode=_ParseMode)
def about_handler(update, context):
    update.message.reply_sticker('CAACAgIAAxkBAAEEyONiieuu2qxx3LDoulmlzpTuFUI7IAACVgEAAhZCawpxwIcFYMakhSQE')
    update.message.reply_text('[🏖 GITHUB REPO 🏖](https://github.com/NetworkChukka/TikTok-DL-BOT)\n\n[Anonymous Devalopers </> 🇱🇰](https://t.me/ehivpnssh) \n\n THANK YOU FOR SINGLE DEVALOPERS API ',parse_mode=_ParseMode)
    
# ◇─────────────────────────────────────────────────────────────────────────────────────◇

# Download Task
def Download_Video(Link,update, context):
    message=update.message
    req=None
    no_watermark=None
    watermark=None

    status_msg=message.reply_text('🚀 DOᗯᑎᒪOᗩᗪIᑎG Video TO Sᕮᖇᐯᕮᖇ ....')
    status_sticker=message.reply_sticker('CAACAgIAAxkBAAEEyOViievWm_t-hsYevrQB0aUPsEzZ4wACugADMNSdEYTXxIjEUGdWJAQ')

    # Getting Download Links Using API
    try:
       req=requests.get(API).json()
       no_watermark=req['no_watermark']
       watermark= req['watermark']
       print('Download Links Generated \n\n\n'+str(req)+'\n\n\n')
    except:
        print('Download Links Generate Error !!!')
        status_msg.edit_text('⁉️ TikTok Downloader API Error !!! Report To Developer : @networkchukka')
        status_sticker.delete()
        return
    
    caption_text="""◇───────────────◇

✅ Successfully Downloaded {} Video 🔰

🔰 Powerd by : [🏖 TikTok Download API 🏖](https://github.com/Single-Developers/API)
[🔥 ANONYMOUS DEVALOPERS </> ](https://t.me/ehivpnssh) 

◇───────────────◇"""
    
    # Uploading Downloaded Videos to Telegram
    print('Uploading Videos')
    status_msg.edit_text('☘️ 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚝𝚘 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖....')
    message.reply_video(video=no_watermark,supports_streaming=True,caption=caption_text.format('No Watermark'),parse_mode=_ParseMode)
    message.reply_video(video=watermark,supports_streaming=True,caption=caption_text.format('Watermark'),parse_mode=_ParseMode)

    # Task Done ! So, Deleteing Status Messages
    status_msg.delete()
    status_sticker.delete()

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def incoming_message_action(update, context):
    message=update.message
    if any(word in str(message.text) for word in TikTok_Link_Types):
        context.dispatcher.run_async(Download_Video,str(message.text),update,context)

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def main() -> None:
    """Run the bot."""
  
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher


    # Commands Listning
    dispatcher.add_handler(CommandHandler('start', start_handler, run_async=True))
    dispatcher.add_handler(CommandHandler('about', about_handler, run_async=True))

    # Message Incoming Action
    dispatcher.add_handler( MessageHandler(Filters.text, incoming_message_action,run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main() # 😁 Start

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

# Example For https://github.com/Single-Developers/API/blob/main/tiktok/Note.md

# https://t.me/SL_Developers
# https://t.me/SingleDevelopers

# ◇─────────────────────────────────────────────────────────────────────────────────────◇
