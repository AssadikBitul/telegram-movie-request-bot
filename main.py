import telebot
import os

BOT_TOKEN = os.getenv("8459480039:AAGLopg5z80AIBS5cMDFTyDNxXGxkTJksfc")
ADMIN_ID = int(os.getenv("1803063154"))

bot = telebot.TeleBot(BOT_TOKEN)

# User sends any text → movie request
@bot.message_handler(func=lambda m: True)
def movie_request(message):
    username = message.from_user.username or "Unknown"
    user_id = message.from_user.id
    text = message.text

    # Send confirmation to user
    bot.reply_to(message,
                 "🎬 আপনার মুভি রিকোয়েস্ট রিসিভ হয়েছে!\n⏳ এডমিন শীঘ্রই চেক করবে।")

    # Send to admin
    admin_msg = (
        f"📥 *New Movie Request Received*\n\n"
        f"👤 User: @{username}\n"
        f"🆔 ID: {user_id}\n"
        f"🎬 Movie: {text}"
    )
    bot.send_message(ADMIN_ID, admin_msg, parse_mode="Markdown")

bot.infinity_polling()
