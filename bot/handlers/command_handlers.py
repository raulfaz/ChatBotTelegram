from telegram import Update
from telegram.ext import ContextTypes
from bot.config import logger

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Usuario {update.effective_user.id} inició el bot")
    await update.message.reply_text(
        "¡Bienvenido a Repuestos Automotrices Faz! 🔧🚗\n\n"
        "Puedo ayudarte con:\n"
        "• Información sobre nuestros productos\n"
        "• Horarios de atención\n"
        "• Consultas técnicas básicas\n\n"
        "¿En qué puedo ayudarte hoy?"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Estos son los comandos disponibles:\n"
        "/start - Iniciar la conversación\n"
        "/ayuda - Mostrar esta ayuda\n"
        "/horario - Ver nuestro horario de atención\n"
        "/contacto - Obtener información de contacto\n\n"
        "También puedes preguntarme directamente sobre repuestos específicos."
    )

async def horario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕒 Nuestro horario de atención es:\n"
        "• Lunes a Viernes: 8:00 a 18:00\n"
        "• Sábados: 9:00 a 13:00\n"
        "• Domingos: Cerrado"
    )

async def contacto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Información de contacto:\n"
        "• Teléfono: 0968174810\n"
        "• Dirección: Av. Quevedo\n"
        "• Sitio web: www.repuestosautomotrices.com\n"
        "• Email: info@repuestosautomotrices.com"
    )