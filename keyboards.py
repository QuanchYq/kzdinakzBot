from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    myinfo = KeyboardButton('🌟 Мен жайлы')
    reviews = KeyboardButton('🎓 Шәкірттер')
    pay = KeyboardButton('💳 Төлем')
    сourse = KeyboardButton('📚 Интенсив')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(myinfo, reviews, pay, сourse)
    return keyboard

def admin_menu():
    add_access = KeyboardButton('🔑 Доступ беру')
    myinfo = KeyboardButton('🌟 Мен жайлы')
    reviews = KeyboardButton('🎓 Шәкірттер')
    сourse = KeyboardButton('📚 Интенсив')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(add_access, myinfo, reviews, сourse)
    return keyboard

def people():
    #add inline keyboard
    buttons = [[InlineKeyboardButton(text='1.Гүлсім', callback_data='gulsim')],
                [InlineKeyboardButton(text='2. Жайна', callback_data='zhaina')],
                [InlineKeyboardButton(text='3. Inkar', callback_data='inkar')],
                [InlineKeyboardButton(text='4. Жанат', callback_data='zhanat')],
                [InlineKeyboardButton(text='5. Назерке', callback_data='nazerke')]
                ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def Gulsim():
    buttons = [[InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/kosmetics.kz/')],
                [InlineKeyboardButton(text='TikTok', url='https://www.tiktok.com/@sakura_kosmetic?_t=8bdAkGAu6tx&_r=1')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return keyboard

def Zhaina():
    buttons = [[InlineKeyboardButton(text='Instagram', url='https://instagram.com/nka_studio?igshid=YmMyMTA2M2Y=')],
                [InlineKeyboardButton(text='TikTok', url='https://www.tiktok.com/@bra89_8?_t=8bdAcuGXzyI&_r=1')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return keyboard

def Inkar():
    buttons = [[InlineKeyboardButton(text='TikTok', url='https://www.tiktok.com/@bakitkizi.inkar?_t=8bdAX1cnCFy&_r=1')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return keyboard

def Zhanat():
    buttons = [[InlineKeyboardButton(text='Instagram', url='https://instagram.com/zhanat__shop?igshid=YmMyMTA2M2Y=')],
                [InlineKeyboardButton(text='TikTok', url='https://www.tiktok.com/@zhanat_shop?_t=8bdAUFPPbT3&_r=1')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return keyboard

def Nazerke():
    buttons = [[InlineKeyboardButton(text='Instagram', url='https://instagram.com/nka_studio?igshid=YmMyMTA2M2Y=')],
                [InlineKeyboardButton(text='TikTok', url='https://www.tiktok.com/@nkastudioo?_t=8bdAYsQPfiX&_r=1')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return keyboard 

def pay_pay():
    buttons = [[InlineKeyboardButton(text='Ақпарат қалдыру', callback_data='info')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

                

    



