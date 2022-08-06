def echo(update, context):
msg='Hi, nice to see you!'
context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
update.message.reply_text(text=msg)


updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))
def UserMessage(update: Update, context: CallbackContext):
    if(update.message.text == "Кто ты?"):
        update.message.reply_text("Бот")
    else:
        update.message.reply_text("Не понятно")

        
