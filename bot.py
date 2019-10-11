from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters


TG_TOKEN = "892905402:AAGQoR7AEDmA7GK-GexbUDcvva_kC6Bcd8w"

def message_handler(bot: Bot, update: Update):
	user = update.effective_user
	if user:
		name = user.first_name
	else:
		name = 'Аноним'

	text = update.effective_message.text
	reply_text = f'Привет, {name}!\n\n {text}'

	bot.send_message(
		chat_id=update.effective_message.chat_id,
		text=reply_text,
	)


def main():
        print('Start')
	bot = Bot(
		token-TG_TOKN,
	)
	updater = Updater(
		bot=bot,
	)

	hendler = MessageHandler(Filters.all, message_handler)
	updater.dispatcher.add_hendler(hendler)

	updater.start_polling()
	updater.idle()
        print('Finish')
        
	if __name__ == '__main__':
		main()

