import types
from email.policy import default
from aiogram import html
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, User, ReplyKeyboardRemove
from config import *
from keyboards.defult import share_contact, confirm_button, menu_buttons
from states.register import RegisterState
import psycopg2
from utils.db import session , User
from utils.decorator import check_register

# Model yo'lingiz

register_router = Router()

@register_router.message(Command('register'))
@check_register
async def register_command(message: Message, state: FSMContext):
    await message.answer("To`liq ismingizni kiriting: ")
    await state.set_state(RegisterState.fullname)

@register_router.message(RegisterState.fullname)
async def fullname_handler(message: Message, state: FSMContext):
    fullname = message.text
    await state.update_data(fullname=fullname)  # Ma'lumot state'da saqlanadi
    await message.answer('Telefon raqamingizni yuboring:', reply_markup=share_contact())
    await state.set_state(RegisterState.phone)

@register_router.message(RegisterState.phone)
async def phone_handler(message: Message, state: FSMContext):
    phone_number = message.text
    if message.contact:
        phone_number = message.contact.phone_number

    await state.update_data(phone=phone_number)

    data = await state.get_data()
    fullname = data.get('fullname')
    chat_id = message.chat.id

    user_data = (
        f"Username: {html.bold(message.from_user.username)}\n"
        f"To'liq ismingiz: {html.bold(fullname)}\n"
        f"Telefon raqamingiz: {html.bold(phone_number)}\n"
        f"Chat ID: {html.bold(str(chat_id))}"
    )
    await message.answer(user_data, reply_markup=confirm_button())
    await state.set_state(RegisterState.confirm)

@register_router.message(RegisterState.confirm)
async def confirm_handler(message: Message, state: FSMContext):
    confirm = message.text
    data = await state.get_data()
    fullname = data.get('fullname')
    phone = data.get('phone')

    chat_id = message.chat.id

    if confirm.casefold() == 'ha':
        user = User(fullname=fullname, phone=phone, chat_id=chat_id)
        user.save(session)
        await message.answer(('Botdan foydalanishga xush kelibsiz!') , reply_markup=menu_buttons())
        await state.clear()
    elif confirm.casefold() == 'yo`q':
        await message.answer('Qayta ro`yxatdan o`tish uchun 👉 /register kamandasini bosing',
                             reply_markup=ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.answer('Ha yoki yo`q tugmasini bittasini bosing' , reply_markup=ReplyKeyboardRemove())