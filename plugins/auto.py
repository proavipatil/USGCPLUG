from userge.plugins.utils.ocr import ocr_space_file
from userge import userge, Message, Config, pool
from pyrogram import filters

CHANNEL = userge.getCLogger(__name__)


@userge.on_message(filters.user("FastlyWriteClone2Bot") & filters.photo, group=-1)
async def my_auto_bot(client, message):
    try:
        downloaded_file_name = await client.download_media(message)
        test_file = await ocr_space_file(downloaded_file_name)
        ParsedText = test_file["ParsedResults"][0]["ParsedText"]
        await message.reply_text(ParsedText.split("\r")[0])
    except Exception as e_f:
        await CHANNEL.log(e_f)
    os.remove(downloaded_file_name)
    return
