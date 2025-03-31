import openai
from pyrogram import Client, filters
from AnonXMusic import app  

openai.api_key = "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"

async def get_ai_response(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"<b>ᴇʀʀᴏʀ:</b> {str(e)}"

@app.on_message(filters.command(["ai", "kiyomi"]) & filters.text)
async def ai_command(_, message):
    prompt = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    if not prompt:
        return await message.reply_text("<b>ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ.</b>")

    ai_response = await get_ai_response(prompt)
    response_text = f"<b>ᴋɪʏᴏᴍɪ ᴀɪ</b>\n\n{ai_response}"
