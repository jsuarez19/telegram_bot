from telegram import Update, ReplyKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, CallbackQueryHandler
from emociones_data import diccionario_emociones, emotions

API_TOKEN = "6602630016:AAEd7FNd9vk3YeyLxA55L2M7AKYbOgCZnlU"

# Estados para el manejo de la conversación
SELECT_GROUP, SELECT_EMOTION, SHOW_INFO = range(3)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Hola! Soy una *ruleta de emociones*\n"
        "Selecciona un grupo de emociones:",
        reply_markup=get_groups_keyboard(),
        parse_mode=ParseMode.MARKDOWN,
    )

    return SELECT_GROUP

def select_group(update: Update, context: CallbackContext) -> int:
    context.user_data["selected_group"] = update.message.text
    update.message.reply_text(
        f"Has seleccionado el grupo de emociones '{context.user_data['selected_group']}'.\n"
        "Ahora elige una emoción:",
        reply_markup=get_emotions_keyboard(context.user_data['selected_group']),
    )

    return SELECT_EMOTION

def select_emotion(update: Update, context: CallbackContext) -> int:
    context.user_data["selected_emotion"] = update.message.text

    # Llamar a una función que devuelva la información de la emoción
    emotion_info = get_emotion_info(context.user_data['selected_emotion'])

    update.message.reply_text(
        emotion_info,
        reply_markup=get_groups_keyboard(),
        parse_mode=ParseMode.MARKDOWN,
    )

    return SELECT_GROUP

def get_groups_keyboard():
    groups = [["Agradables", "Desagradables"]]

    reply_markup = ReplyKeyboardMarkup(groups, one_time_keyboard=True)
    return reply_markup


def get_emotions_keyboard(selected_group):
    keyboard = [[emotion] for emotion in emotions[selected_group]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    return reply_markup


def get_emotion_info(selected_emotion):
    info = diccionario_emociones[selected_emotion]
    emotion_info = (
        f"Información sobre la emoción *'{selected_emotion} {info['emoji']}'*:\n"
        f"*Impulso de acción:* {info['impulso_accion']}\n"
        f"*Cuándo está justificada:* {info['si_justificada']}\n"
        f"*Cuándo no está justificada:* {info['no_justificada']}\n"
        f"*Qué hacer cuando está justificada:* {info['acciones_si_justificada']}\n"
        f"*Qué hacer cuando no está justificada:* {info['acciones_no_justificada']}"
    )

    return emotion_info

def main():
    updater = Updater(API_TOKEN)

    dp = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECT_GROUP: [MessageHandler(Filters.text & ~Filters.command, select_group)],
            SELECT_EMOTION: [MessageHandler(Filters.text & ~Filters.command, select_emotion)],
        },
        fallbacks=[],
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
 