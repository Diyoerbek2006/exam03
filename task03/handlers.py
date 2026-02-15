from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from image_service import ImageService


class Handlers:
    def __init__(self):
        self.image_service = ImageService()

    def start_command(self, update, context):
        keyboard = [
            [
                InlineKeyboardButton("Dog", callback_data="dog"),
                InlineKeyboardButton("Cat", callback_data="cat"),
                InlineKeyboardButton("Fox", callback_data="fox"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            "Qaysi hayvon rasmini ko'rmoqchisiz?",
            reply_markup=reply_markup
        )

        
    def button_handler(self, update, context):
        query = update.callback_query  
        query.answer()

        animal = query.data
        image_url = self.image_service.fetch_random_image(animal)

        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=image_url
        )

        keyboard = [
            [
                InlineKeyboardButton("🐶 Dog", callback_data="dog"),
                InlineKeyboardButton("🐱 Cat", callback_data="cat"),
                InlineKeyboardButton("🦊 Fox", callback_data="fox"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_reply_markup(reply_markup=reply_markup)


    def dog_command(self, update, context):
        image_url = self.image_service.fetch_random_image("dog")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)

    def cat_command(self, update, context):
        image_url = self.image_service.fetch_random_image("cat")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)

    def fox_command(self, update, context):
        image_url = self.image_service.fetch_random_image("fox")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)
