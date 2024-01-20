import asyncio, os, requests, time
from requests import post, get
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from userge import Message, userge

@userge.on_cmd("gofile", about={
    "header": "Uploads File to GoFile.io"})

async def gofile(event):

	msg = await event.reply("**Processing...**")
	# amjana = await event.get_reply_message()
	url_ = event.text.split(" ", 1)[1]

	await msg.edit("Now Uploading to GoFile")
	url = "https://api.gofile.io/getServer"
	r = get(url)

	url2 = f"https://{r.json()['data']['server']}.gofile.io/uploadFile"
	r2 = post(url2, files={'file': open(f'{url_}', 'rb')})
	fileName = r2.json()["data"]["fileName"]
	# fileSize = amjana.file.size
	fileLink = r2.json()["data"]["downloadPage"]

	hmm = f'''File Uploaded successfully !!

**File name:** __{fileName}__
'''

	markup = InlineKeyboardMarkup(
		[[InlineKeyboardButton(text="📦 Link", url=fileLink)]]
	)
	await msg.edit_text(hmm, reply_markup=markup)
