from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def share_contact():
    keyboards = [
        [
           KeyboardButton(text='📲 Telefon ulashish' , request_contact=True),
        ]
    ]
    kbs = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder=('Tugamadan foydalaning!'))
    return kbs
def confirm_button():
    keyboards = [

        [
            KeyboardButton(text=('Ha')),
            KeyboardButton(text=('Yoq'))
        ],

    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder=('Tugamadan foydalaning!'))
    return kb
def menu_buttons():
    keyboards = [
        [
            KeyboardButton(text=('Pul otkazish')),
            KeyboardButton(text=('Tarixni ko`rish'))
        ],
        [
            KeyboardButton(text=('Qidirish')),
        ]
    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards,
                             resize_keyboard=True,
                             input_field_placeholder=('Tugamadan foydalaning!'))
    return kb


