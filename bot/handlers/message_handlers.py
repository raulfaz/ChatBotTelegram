from telegram import Update
from telegram.ext import ContextTypes
from bot.services.openai_service import get_openai_response
from bot.config import logger

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_id = update.effective_user.id
    
    logger.info(f"Usuario {user_id} envió: {user_message}")
    
    # Mostrar mensaje de "escribiendo..."
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    # Obtener respuesta de OpenAI
    response = await get_openai_response(user_message)
    
    # Responder al usuario
    await update.message.reply_text(response)
    logger.info(f"Respondido a usuario {user_id}")