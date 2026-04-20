from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("About ℹ️", callback_data="about")],
        [InlineKeyboardButton("Help 📖", callback_data="help")],
        [InlineKeyboardButton("Thanks ❤️", callback_data="thanks")],
        [InlineKeyboardButton("All Paid Batch ❤️", callback_data="all_batch")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Hello 👋 Choose an option:", reply_markup=reply_markup)

# BUTTON CLICK HANDLE
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_text("This is my own Bot 😎")

    elif query.data == "help":
        await query.edit_message_text("Use commands:\n/start\n/about\n/thanks")

    elif query.data == "thanks":
        await query.edit_message_text("Thank you—that was my duty 😎")

    elif query.data == "all_batch":
        await query.edit_message_text("👉 All Paid Batches Link:\nhttps://t.me/+TaRk_JVdzmIyMTY9")

# COMMANDS
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is my own Bot 😎")

async def thanks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Thank you—that was my duty 😎")

async def batch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 All Paid Batches:\n\n👉 https://t.me/+TaRk_JVdzmIyMTY9"
    )

# APP

app = ApplicationBuilder().token("8771929884:AAGx1OITXVv_-kqZpL5-AVn1rHvK8kyia8c").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("thanks", thanks))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(CommandHandler("batch", batch))

app.run_polling()
