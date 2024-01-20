import asyncio, os, requests, time
from requests import post, get
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from userge import Message, userge
import json
import shlex
import requests
import subprocess

@userge.on_cmd("go", about={
    "header": "Uploads File to GoFile.io"})

async def gofile(event):
	msg = await event.reply("**Processing...**")
	# amjana = await event.get_reply_message()
	url_ = event.text.split(" ", 1)[1]

	await msg.edit("Now Uploading to GoFile")
	url = "https://api.gofile.io/getServer"
	r = get(url)

	token = None
	folderId = None
	server = r.json()['data']['server']

	cmd = 'curl '
	cmd += f'-F file=@{url_} '
	if token:
		cmd += f'-F token={token} '
	if folderId:
		cmd += f'-F folderId={folderId} '
	cmd += f'https://{server}.gofile.io/uploadFile'
	upload_cmd = shlex.split(cmd)

	out = subprocess.check_output(upload_cmd, stderr=subprocess.STDOUT)
	out = out.decode("UTF-8").strip()

	response = json.loads(out)

	if response["status"] == "ok":
		data = response["data"]

		fileName = data["fileName"]
		fileLink = data["downloadPage"]

		hmm = f'''File Uploaded successfully !!

			**File name:** __{fileName}__
			'''
		markup = InlineKeyboardMarkup(
			[[InlineKeyboardButton(text="📦 Link", url=fileLink)]]
		)
		await msg.edit_text(hmm, reply_markup=markup)

	else:
		await msg.edit_text("Error Occured !")
