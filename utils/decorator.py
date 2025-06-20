from keyboards.defult import menu_buttons
from utils.db import User, session



def check_register(func):
    async def wrapper(*args, **kwargs):
        message = args[0]
        chat_id = message.chat.id
        if User.check_register(session, chat_id):
            await message.answer(('Botdan foydalanishga xush kelibsiz!'), reply_markup=menu_buttons())
        else:
            if func.__name__ == 'register_start':
                await func(message, kwargs.pop('state'))
            else:
                await func(message)

    return wrapper


