from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.decorator import check_register

start_router = Router()

@start_router.message(CommandStart())
@check_register
async def command_start_handler(message: Message):
    fullname = html.bold(message.from_user.full_name)
    await message.answer(f"Salom, {fullname}! \n\nRo'yxatdan o'tish uchun 👉 /register ni bosing.")