import openai
from AnonXMusic import app
from pyrogram import filters

# Set your OpenAI API Key
openai.api_key = "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"

@app.on_message(filters.command("ai") & (filters.group | filters.private))
async def ai_command(client, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ.")
    
    prompt = message.text.split(None, 1)[1]
    await message.reply_text("ᴛʜɪɴᴋɪɴɢ...")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply_text = response["choices"][0]["message"]["content"]
        await message.reply_text(f"ᴋɪʏᴏᴍɪ ᴀɪ: {reply_text}")
    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ: {str(e)}")
