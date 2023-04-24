import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv
from aiogram.dispatcher.filters.state import State, StatesGroup 
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from aiogram.utils.markdown import text, bold, italic, code, pre, hlink, hbold 
from aiogram.dispatcher.filters import Text
from keyboards import main_menu, admin_menu, people, Gulsim, Zhaina, Inkar, Zhanat, Nazerke, pay_pay
from libs import isAdmin, add_user, isAdminUsername, add_user_username
import json
import os
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	


load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

token_bot = os.getenv('TOKEN')

storage = MemoryStorage()

# Replace YOUR_TOKEN with your bot token
bot = Bot(token=token_bot,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

Admins = [695064750]



class FormStates(StatesGroup):
    name = State()
    surname = State()
    company_type = State()
    instagram_link = State()


# Left date
# Define the starting message in Kazakh
start_message = """
<b>Сәлеметсізбе!</b> 🎉

<b>Интенсивке</b> қош келдіңіз! 🤖📚

Курс туралы көбірек білу үшін <b>"Интенсив"</b> түймесін басыңыз - сізді бағдарлама және шәкірттер туралы мәліметтер күтеді. 📝💡

Жаңа білім мен жетістікке жету жолын бастауға дайынсыз ба? 👍💪
"""

# Define the handler for the /start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id in Admins:
        await bot.send_message(chat_id=message.chat.id, text=start_message,
                           reply_markup=admin_menu())
    else :
        await bot.send_message(chat_id=message.chat.id, text=start_message,
                           reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == '🌟 Мен жайлы')
async def about_me(message: types.Message):
    photo = open('images/dina.jpg', 'rb')

    text = '''
<b>👋 Сәлем</b>. <i>Мені оқырмандарым <b>Дина</b> деп атайды.</i> 🤗

🙍‍♀️ <b>Жасы 29-да.</b> 
🌏 <b>Алматы</b> қаласында туылған
. 🏙

<i>2012 — 2013 жж</i> 
<b>Шыңжаң педагогикалық университеті.</b>

<i>2013−2014 жж</i> 
<b>Tongji University - Қытай тілі курстары</b>

<i>2014−2016 жж</i> 
<b>қытай & ағылшын тілдерінің мұғалімі</b>

<i>2016−2020 жж</i> 
<b>Фудан университеті - Бакалавр</b>

<i>2020−2023 жж</i> 
<b>ТикТок эксперт</b>

'''
    await bot.send_photo(chat_id=message.chat.id, photo=photo , caption=text, parse_mode='HTML')

@dp.message_handler(lambda message: message.text == '🎓 Шәкірттер')
async def add_review(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Шәкірттерді қосу үшін біздің каналымызға жіберіңіз',
                           reply_markup=people())

@dp.callback_query_handler(lambda c: c.data == 'gulsim')
async def gulsim(callback_query: types.CallbackQuery):
    photo_gulsim = open('images/gulsim.jpeg', 'rb')
    text = """
👩: <b>Гүлсим</b>

🏆: <i>💄🌟 Корей косметикасы мен парфюмериясында жетекші сәтті бизнес.</i>

<i>🏢💼 Өзінің 3 қабатты жалға берілетін ғимараты.</i>

<i>📈 Instagram-да 18,2 мың данада жазылушысы бар.</i>

<i>👗👠 Киім мен аяқ киімдерді сату магазынын ашу пландары бар!</i>
    """
    photo = open('images/gulsim.jpeg', 'rb')
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo , caption=text, parse_mode='HTML', reply_markup=Gulsim())

@dp.callback_query_handler(lambda c: c.data == 'zhaina')
async def zhaina(callback_query: types.CallbackQuery):
    photo = open('images/zhaina.jpg', 'rb')
    text = """
👩: <b>Жайна</b>

🏆: <i>👙  Іш киім, пижама және пенюар дүкені.</i>

<i>📈 TikTok-та 31 мың жазылушы бар.</i>

<i>🌍 Бүкіл әлем бойынша жеткізу.</i>

"""
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo , caption=text, parse_mode='HTML', reply_markup=Zhaina())


@dp.callback_query_handler(lambda c: c.data == 'inkar')
async def inkar(callback_query: types.CallbackQuery):
    photo = open('images/inkar.jpg', 'rb')
    text = """
👩: <b>Инкар</b>

🏆: <i>👜 Сөмкелер, аяқ киім және косметика дүкені.</i>

<i>📈 8-мыңнан астам жазылушылар.</i>

"""
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo , caption=text, parse_mode='HTML', reply_markup=Inkar())

@dp.callback_query_handler(lambda c: c.data == 'zhanat')
async def inkar(callback_query: types.CallbackQuery):
    photo = open('images/zhanat.jpg', 'rb')
    text = """
👩: <b>Жанат</b>

🛍️: <i>Көйлек мен сумкаларды сату дүкені.</i>

📈: <i>Instagram-да 15-мыңнан астам жазылушысы бар.</i>
"""
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo , caption=text, parse_mode='HTML', reply_markup=Zhanat())

@dp.callback_query_handler(lambda c: c.data == 'nazerke')
async def inkar(callback_query: types.CallbackQuery):
    photo = open('images/nazerke.jpg', 'rb')
    text = """
👩: <b>Назерке</b>

🛍️: <i>Қазақстандық мерч: худи, свитшоттар, жүйрік.</i>

🌍: <i>Әлем бойынша жеткізу.</i>

📈: <i>Instagram-да 48 мың данадан астам жазылушысы бар.</i>
"""
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo , caption=text, parse_mode='HTML', reply_markup=Nazerke())



@dp.message_handler(lambda message: message.text == '💳 Төлем')
async def pay(message: types.Message):
    text = """
👋 Біздің <b>Интенсивімізге</b> қосылыңыз! 🤩

💰 <i>Төмендегі сілтемені пайдаланып, <b>Интенсивке</b> жазылыңыз!:</i>
<u>📎 https://pay.kaspi.kz/pay/96v0sicr</u>

✅ Төлемнен кейін өзіңіз жайлы ақпарат қалдырыңыз! 🙌
    """
    await bot.send_message(message.chat.id,text, parse_mode='HTML', reply_markup=pay_pay(), disable_web_page_preview=True)

@dp.callback_query_handler(lambda c: c.data == 'info')
async def name(callback_query: types.CallbackQuery, ):
    await FormStates.name.set()
    await callback_query.message.edit_text("💭 Атыңызды теріңіз")


@dp.message_handler(state=FormStates.name)
async def ask_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FormStates.surname.set()
    await message.answer("👤 Тегіңізді теріңіз")

@dp.message_handler(state=FormStates.surname)
async def ask_company_type(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('ТОО'))
    keyboard.add(KeyboardButton('ИП'))
    keyboard.add(KeyboardButton('Басқа'))
    await FormStates.company_type.set()
    await message.answer("Выберите тип вашей компании", reply_markup=keyboard)

@dp.message_handler(Text(equals=['ТОО', 'ИП', 'Басқа']), state=FormStates.company_type)
async def ask_instagram_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_type'] = message.text
    await FormStates.instagram_link.set()
    await message.answer("Инстаграм линкіңізді теріңіз")

@dp.message_handler(state=FormStates.instagram_link)
async def finish_form(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['instagram_link'] = message.text
        form_data = data
    await state.finish()
    await message.answer("Форма толтырылды!", reply_markup=main_menu())
    CREDENTIALS_FILE = 'courses.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

    httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 

    spreadsheetId = '1RM7f67tIk_cfua6vN1pauR7VhEiS62zFsLgWj-i9gYc'
    raw = [
        [form_data['name'],form_data['surname'],form_data['company_type'],form_data['instagram_link']]
    ]
    body = {
        'values' : raw
    }

    results = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId,
        range="Лист1",
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()




class response(StatesGroup):
    response = State()

@dp.message_handler(lambda message: message.text == '🔑 Доступ беру' )
async def admin_only(message: types.Message):
    await response.response.set()
    user_id = message.from_user.id
    if user_id in Admins:
        await message.answer('🔓 Доступ беру үшін пайдаланушынын никін енгізіңіз.')
    else:
        await message.answer('🗝️ Сіздің құқығыңыз жоқ!')

@dp.message_handler(state=response.response)
async def echo(message: types.Message, state: FSMContext):
    text = """
🎉 <b>Интенсивқа сәтті жазылдыңыз!</b> 🎉

<b>📅 Күні:</b><i> 2023 жылғы 15 мамыр</i>
<b>🕐 Уақыты:</b> <i>10: 00 - 16: 00</i>
<b>📍 Орын:</b><i>"Планета" Конференц-залы</i>

<b>Уақытында келуді және қарқындылық үшін барлық қажетті материалдарды алып жүруді ұмытпаңыз. Біз сізді күтеміз және сабағымызды бастауға дайынбыз! 💪 👨‍🏫    
    </b>
"""
    if message.from_user.id in Admins:
        if message.text:
            async with state.proxy() as data:
                data['user_id'] = ''
                user_mes = message.text
                await add_user(user_mes)
                await bot.send_message(chat_id=user_mes, text=text)
            await state.finish()
        else:
            await message.answer('Қате ID, қайтадан көріңіз')
    else:
        await message.answer('🔓 Сіздің құқығыңыз жоқ!')



@dp.message_handler(lambda message: message.text == '📚 Интенсив')
async def course(message: types.Message):
    text = """
<b>Интенсивтан не күтуге болады? 🎉</b>

<i>
• <b>Аптасына 3 рет 2 сағаттан, TikTok-та аккаунтыңызды дамыту ⏰</b>.

• <b>Алғашқы 1000 оқырман жинау📈💯</b>.

• <b>Тікелей эфирде оқырман ұстап қалу👥💬</b>.

• <b>TikTok-та сатуды үйрену! 🤑</b>

• <b>TikTok-та сатуға болатын товарлар тізімі</b>

• <b>Қандай әрекеттер Тикток банға әкеледі?🔍</b>.

• <b>TikTok-та нишаңызды жүргізу.</b>.

• <b>🔝 TikTok-та сатылымды 2х көбейту жолдары.</b>.</i>

<b>✅"Өткен интенсивімізден табыс жетілген шәкірттердің мәліметтерін алу үшін <u>🎓 Шәкірттер</u> батырмасын басыңыз.</b>"
"""
    await bot.send_message(message.chat.id, text, parse_mode='HTML')

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
