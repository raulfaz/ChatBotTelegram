from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.config import TELEGRAM_TOKEN, logger
from bot.handlers.command_handlers import start, help_command, horario, contacto
from bot.handlers.message_handlers import handle_message
import os

def main():
    # Crear directorio de logs si no existe
    os.makedirs("logs", exist_ok=True)
    
    # Crear la aplicación
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Agregar handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ayuda", help_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("horario", horario))
    application.add_handler(CommandHandler("contacto", contacto))
    
    # Handler para mensajes de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Iniciar el bot
    logger.info("Bot iniciado. Presiona Ctrl+C para detener.")
    application.run_polling()

if __name__ == "__main__":
    main()