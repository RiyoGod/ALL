import openai
from pyrogram import Client, filters
from AnonXMusic import app  # Import the app instance from the main bot file

# Set up OpenAI API key
openai.api_key = "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"

# Function to get AI response
async def get_ai_response(prompt: str):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # You can change this to "gpt-4" or another model if you prefer
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Command handler for /ai {prompt}
@app.on_message(filters.command("ai") & filters.group)
async def ai_command(client, message):
    # Extract the prompt from the command
    prompt = message.text.split(None, 1)  # This splits the text to get the actual prompt
    if len(prompt) < 2:
        await message.reply_text("Please provide a prompt for me to assist you.")
        return

    prompt = prompt[1]  # Get the prompt after the command

    # Send message to the AI (ChatGPT) and get the response
    ai_response = await get_ai_response(prompt)

    # Send the AI response back to the chat
    await message.reply_text(f"<b>Kiyomi AI<\b>: {ai_response}")
