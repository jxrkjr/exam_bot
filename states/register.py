from aiogram.fsm.state import State , StatesGroup

class RegisterState(StatesGroup):
    fullname = State()
    phone = State()
    confirm = State()
class TransferState(StatesGroup):
    phone_number = State()
    summa = State()
    confirm = State()