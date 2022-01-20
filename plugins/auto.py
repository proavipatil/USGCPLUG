from userge.plugins.utils.ocr import ocr_space_file
from userge import userge, Message, Config, pool
from pyrogram import filters

CHANNEL = userge.getCLogger(__name__)


@userge.on_message(filters.user("FastlyWriteClone2Bot") & filters.photo, group=-1)
async def my_auto_bot(message):
    downloaded_file_name = await message.client.download_media(message)
    test_file = await ocr_space_file(downloaded_file_name)
    try:
        ParsedText = test_file["ParsedResults"][0]["ParsedText"]
        await message.reply_text(str(ParsedText).strip().replace("By@FastlyWriteBot","",1))
    except Exception as e_f:
        await CHANNEL.log(e_f)
    os.remove(downloaded_file_name)
    return
