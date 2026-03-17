from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8514910182:AAF46lVUOLAFluX0_XqrCfLA0hulcQWXUm4"
CHANNEL_LINK = "https://t.me/+CRv_8bjodDQ0ZmU1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Official Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("I Joined 👍", callback_data="joined")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "Welcome to 𝐐𝐔𝐎𝐓𝐄𝐗_𝐀𝐋𝐏𝐇𝐀_𝐋𝐄𝐆𝐄𝐍𝐃! 📊🇮🇳\n\n"
        "Daily market insights, charts, and educational trading setups.\n"
        "Tap the buttons below 👇\n\n"
        "⚠️ Disclaimer:\n"
        "We do NOT provide investment advice.\n"
        "All market analysis is ONLY for educational purposes."
    )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "joined":
        await query.message.reply_text(
            "✅ Thank you for joining!\n\n"
            "You will now receive daily market insights and educational trading setups.\n\n"
            "Stay tuned! 📈"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
