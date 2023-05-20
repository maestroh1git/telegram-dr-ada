from unittest import TestCase, mock
from telegram import Update, Message, User, Chat
from handlers.start_handler import start
from main import generate_start_message

class TestStartHandler(TestCase):
    @mock.patch('telegram.Bot.send_message')
    def test_start_command(self, mock_send_message):
        bot = mock.Mock()
        user = User(id=1, first_name="Test", is_bot=False)
        chat = Chat(id=1, type="private")
        message = Message(message_id=1, date=None, chat=chat, from_user=user)
        update = Update(update_id=1, message=message)
        context = mock.Mock()  # We can use a Mock object for the context too

        start(update, context)

        # Check that the message text is what we expect
        mock_send_message.assert_called_once_with(chat_id=chat.id, text=generate_start_message(user.first_name))
