import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to MOG Crypto Bot!\nUse /help to see commands."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Begin\n"
        "/help - Commands\n"
        "/signal - Get trading signal\n"
        "/price BTC - Check Bitcoin price\n"
        "/catalog - View items\n"
        "/order - How to order\n"
        "/delivery - Delivery info\n"
        "/contact - Contact info\n"
        "/about - About MOG Atelier"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Send like this:\n/price BTC")
        return
    
    symbol = context.args[0].upper()
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"

    try:
        data = requests.get(url).json()
        if "price" in data:
            await update.message.reply_text(f"{symbol} Price: ${data['price']}")
        else:
            await update.message.reply_text("Invalid symbol.")
    except:
        await update.message.reply_text("Market data unavailable.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 **AUTO SIGNAL**\nBUY BTC/USDT\nEntry: 1\nTP: 2\nSL: -1"
    )

async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "MOG Atelier Catalog:\nTrading Class — ₦50,000"
    )

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("To order, send: /contact")

async def delivery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Delivery available nationwide.")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Contact:\nPrince (MOG Atelier)\nWhatsApp: 09012345678"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("MOG Atelier — Premium Trading & Fashion Brand.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("catalog", catalog))
app.add_handler(CommandHandler("order", order))
app.add_handler(CommandHandler("delivery", delivery))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("about", about))

app.run_polling()
