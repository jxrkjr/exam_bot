from aiogram import Router, F

from aiogram.fsm.context import FSMContext
from keyboards.defult import confirm_button, menu_buttons
from aiogram.types import Message, ReplyKeyboardRemove

from states.register import TransferState
from utils.db import User, session

menu_router = Router()
@menu_router.message(F.text == 'Pul otkazish')
async def pul_otkazish(message: Message, state: FSMContext):
    await message.answer(
        'Pul o`tkazmoqchi bo`lgan odamni chat idni  kiriting(masalan 123456789)',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(TransferState.phone_number)


@menu_router.message(TransferState.phone_number)
async def phone_number_handler(message: Message, state: FSMContext):
    phone_number = message.text
    user = User()
    if user.check_phone(phone_number, session):
        await message.answer('Summani kiriting:')
        await state.update_data(phone_number=phone_number)  # 📍 Saqlaymiz
        await state.set_state(TransferState.summa)          # 📍 Keyingi state
    else:
        await message.answer('To‘g‘ri raqam kiriting')


@menu_router.message(TransferState.summa)
async def sum_handler(message: Message, state: FSMContext):
    summa = message.text
    user = User()
    datas = await state.get_data()
    phone_number = datas['phone_number']
    if user.check_summa(phone_number, summa, session):
        await message.answer('Tasdiqlaysizmi?', reply_markup=confirm_button())
        await state.update_data(summa=summa)  # 📍 Summani ham saqlaymiz
        await state.set_state(TransferState.confirm)
    else:
        await message.answer('Mablag‘ yetarli emas, boshqa summa kiriting')


@menu_router.message(TransferState.confirm)
async def confirm_handler(message: Message, state: FSMContext):
    confirm = message.text
    datas = await state.get_data()
    phone_number = datas['phone_number']
    summa = datas['summa']
    if confirm.lower() == 'ha':
        user2 = User()
        user2.transfer(phone_number, message.chat.id, summa, session)
        await message.answer('Pul muvaffaqiyatli o‘tkazildi!', reply_markup=menu_buttons())
    elif confirm.lower() == 'yoq':
        await message.answer('Bosh menyuga qaytdingiz', reply_markup=menu_buttons())
    await state.clear()