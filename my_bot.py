from telegram import Update, ReplyKeyboardMarkup, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, CallbackQueryHandler
from emociones_data import diccionario_emociones, emotions

API_TOKEN = "6602630016:AAEd7FNd9vk3YeyLxA55L2M7AKYbOgCZnlU"

# Estados para el manejo de la conversación
SELECT_GROUP, SELECT_EMOTION, SHOW_INFO = range(3)

def start(update: Update, context: CallbackContext) -> int:
    keyboard = [[InlineKeyboardButton("Agradables", callback_data='Agradables'),
                 InlineKeyboardButton("Desagradables", callback_data='Desagradables')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Hola! Soy una *Ruleta de emociones*\n\n"
        "Selecciona un grupo de emociones:",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN,
    )

    return SELECT_GROUP

def select_group(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    context.user_data["selected_group"] = query.data

    keyboard = [[InlineKeyboardButton(emotion, callback_data=emotion) for emotion in emotions['Agradables']] if query.data == "Agradables" else
                [InlineKeyboardButton(emotion, callback_data=emotion) for emotion in emotions['Desagradables']]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(f"Has seleccionado el grupo de emociones '{context.user_data['selected_group']}'. Ahora elige una emoción:", reply_markup=reply_markup)

    """ Old code for keyboard
    context.user_data["selected_group"] = update.message.text
    update.message.reply_text(
        f"Has seleccionado el grupo de emociones '{context.user_data['selected_group']}'.\n"
        "Ahora elige una emoción:",
        reply_markup=get_emotions_keyboard(context.user_data['selected_group']),
    )
    """
    return SELECT_EMOTION

def select_emotion(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    context.user_data["selected_emotion"] = query.data

    # Obtener información de la emoción
    emotion_info = get_emotion_info(context.user_data['selected_emotion'])

    # Obtener el teclado en línea
    inline_keyboard = get_groups_keyboard()

    # Enviar el mensaje con formato Markdown y teclado en línea
    query.edit_message_text(emotion_info, reply_markup=inline_keyboard, parse_mode='Markdown')


    """Old code
    context.user_data["selected_emotion"] = update.message.text

    # Llamar a una función que devuelva la información de la emoción
    emotion_info = get_emotion_info(context.user_data['selected_emotion'])
    
    update.message.reply_text(
        emotion_info,
        reply_markup=get_groups_keyboard(),
        parse_mode=ParseMode.MARKDOWN,
    )
    """
    return SELECT_GROUP

def get_groups_keyboard():
    groups = [
        [
            InlineKeyboardButton("Agradables", callback_data="Agradables"),
            InlineKeyboardButton("Desagradables", callback_data="Desagradables")
        ]
    ]

    return InlineKeyboardMarkup(groups)


def get_emotions_keyboard(selected_group):
    # Obtén todas las emociones del grupo seleccionado
    all_emotions = emotions[selected_group]

    # Crea botones usando InlineKeyboardButton, 3 botones por línea
    keyboard = [
        [InlineKeyboardButton(emotion, callback_data=emotion) for emotion in all_emotions[i:i+3]]
        for i in range(0, len(all_emotions), 3)
    ]
    
    return InlineKeyboardMarkup(keyboard)



def get_emotion_info(selected_emotion):
    info = diccionario_emociones[selected_emotion]
    if selected_emotion in diccionario_emociones:
        emotion_info = (
            f"Información sobre la emoción *'{selected_emotion} {info['emoji']}'*:\n\n"
            f"*Impulso de acción:* {info['impulso_accion']}\n\n"
            f"*Cuándo está justificada:* {info['si_justificada']}\n\n"
            f"*Cuándo no está justificada:* {info['no_justificada']}\n\n"
            f"*Qué hacer cuando está justificada:* {info['acciones_si_justificada']}\n\n"
            f"*Qué hacer cuando no está justificada:* {info['acciones_no_justificada']}\n\n"
            "Escoger otra emocion ⬇️"
        )
        return emotion_info
    
    else: return f"No se encontró información para la emoción '{selected_emotion}'."


def main():
    updater = Updater(API_TOKEN)

    dp = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECT_GROUP: [CallbackQueryHandler(select_group)],
            SELECT_EMOTION: [CallbackQueryHandler(select_emotion)],
        },
        fallbacks=[],
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
 