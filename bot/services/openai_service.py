import openai
from bot.config import OPENAI_API_KEY, logger
from bot.data.knowledge_base import REPUESTOS_INFO

# Configurar la API de OpenAI
openai.api_key = OPENAI_API_KEY

async def get_openai_response(user_message):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Eres un asistente virtual para una tienda de repuestos automotrices. Usa esta información para responder: {REPUESTOS_INFO}. Sé amable y profesional. Si no sabes algo, sugiere que contacten a la tienda. No inventes información que no esté en la base de conocimientos."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error con OpenAI: {e}")
        return "Lo siento, estoy experimentando problemas técnicos. Por favor, inténtalo de nuevo más tarde o contacta directamente con nuestra tienda."