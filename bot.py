import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8771929884:AAGx1OITXVv_-kqZpL5-AVn1rHvK8kyia8c"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello👋, How Are You ? 🚀")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is my own Bot. 😎")

async def thanks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Thank you—that was my duty. 😎")

app = ApplicationBuilder().token(8771929884:AAGx1OITXVv_-kqZpL5-AVn1rHvK8kyia8c).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("thanks", thanks))

app.run_polling()
