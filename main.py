#pip install --force-reinstall -v "aiogram==2.23.1"


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




bot = Bot(token='7753361066:AAHcpIdZnmbexVt4pbBIArKLGHaVokqO8LU')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="Hall Ticket",url="https://nmuj.digitaluniversity.ac/PreExamV2_DownloadHallTicket_New.aspx")
button2 = InlineKeyboardButton(text="View Result",url="https://nmuj.digitaluniversity.ac/SearchDuplicateResult.aspx?ID=28176")
button3 = InlineKeyboardButton(text="SSBT-WEB", url="https://ssbtweb.com/LogInAlumini.aspx#!")
button4 = InlineKeyboardButton(text="SBBT-Moodle", url="http://elearning.sscoetjalgaon.ac.in/moodle/")
button12 = InlineKeyboardButton(text="Contact Us", url="https://t.me/Pratilkambale")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4, button12)

#  2@@@@@@@@@@@@@@@@@@@

button5 = InlineKeyboardButton(text="OS", callback_data="OS")
button6 = InlineKeyboardButton(text="CN", callback_data="CN")
button7 = InlineKeyboardButton(text="PM", callback_data="PM")
button8 = InlineKeyboardButton(text="NN", callback_data="NN")
button9 = InlineKeyboardButton(text="DAA", callback_data="DAA")

keyboard_inline2 = InlineKeyboardMarkup().add(button5, button6, button7, button8, button9)

button10 = KeyboardButton("who are you ? ", request_contact=True)
button11 = KeyboardButton("Where are you ? ", request_location=True)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("/start", "/Imp_Websites", button10,button11)


@dp.message_handler(commands=["Menu"])
async def random_answer(message: types.Message):
    await message.reply(".\n\n\n@@## MENU ##@@\n1 - /start\n2 - /Notes\n3 - /Imp_Websites\n\n\n\n.",reply_markup=keyboard1)


@dp.message_handler(commands=['start', 'Notes'])
async def welcome(message: types.Message):
    await message.reply_photo("https://pbs.twimg.com/profile_images/1156108760273698821/McSiVnKU_400x400.jpg")
    await message.reply("Hello! Im SSBT Bot,Here is your Imp Notes\n Click here_ /Menu _for Menu",reply_markup=keyboard_inline2)


@dp.message_handler(commands=['IMP_Websites'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im SSBT Bot , Here is IMP Websites", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=["OS", "CN", "PM", "NN", "DAA"])
async def random_value(call: types.CallbackQuery):
    if call.data == "OS":
        await call.message.answer(".\n\n\n\n\n\Wait for 10 seconds\n\n\n\n\n.")
        await call.message.answer_dice("🎲")
        await call.message.answer("UNIT - LAB \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=9159") #lab
        await call.message.answer("UNIT - 1 \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6447") #1
        await call.message.answer("UNIT - 2 \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6448") #2
        await call.message.answer("UNIT - 3.1 \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6449")#3.1
        await call.message.answer("UNIT - 3.2 \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6450")#3.2
        await call.message.answer("UNIT - 4.1 \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6451")#4.1
        await call.message.answer("UNIT - 4.2 \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6452")#4.2
        await call.message.answer("UNIT - 4.3 \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6453")#4.3
        await call.message.answer("UNIT - 5 \nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6454")#5
        await call.message.answer("@@## MENU ##@@\n1 - /start\n2 - /Notes\n3 - /Imp_Websites\n\n\n\n.")


    elif call.data == "CN":
        await call.message.answer(".\n\n\n\n\n\Wait for 10 seconds\n\n\n\n\n.")
        await call.message.answer_dice("🎲")
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=8909") #lab
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=210")#1
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=211")#2
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=418")#3
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=419")#4
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=420")#5
        await call.message.answer("@@## MENU ##@@\n1 - /start\n2 - /Notes\n3 - /Imp_Websites")

    elif call.data == "PM":
        await call.message.answer(".\n\n\n\n\n\Wait for 10 seconds\n\n\n\n\n.")
        await call.message.answer_dice("🎲")
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=5922")#1
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=5915")#2
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=5911")#3
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=5912") #4
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=5913") #5
        await call.message.answer("@@## MENU ##@@\n1 - /start\n2 - /Notes\n3 - /Imp_Websites")

        # await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=1927")
        # await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=1928")
    # await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=1929")
    # await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=1930")
    elif call.data == "NN":
        await call.message.answer(".\n\n\n\n\n\Wait for 10 seconds\n\n\n\n\n.")
        await call.message.answer_dice("🎲")
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6374") #1
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6375") #2
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6377")# 3
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6378")#4
        await call.message.answer_document("http://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=6379")#5
        await call.message.answer("@@## MENU ##@@\n1 - /start\n2 - /Notes\n3 - /Imp_Websites")


    elif call.data == "DAA":
        await call.message.answer(".\n\n\n\n\n\Wait for 10 seconds\n\n\n\n\n.")
        await call.message.answer_dice("🎲")
        await call.message.answer_document("https://github.com/pratikthebos/PR2/archive/refs/heads/main.zip") #1
        await call.message.answer("UNIT 2\nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/resource/view.php?id=744") #2
        await call.message.answer("UNIT 3\nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/folder/view.php?id=1920") #3
        await call.message.answer("UNIT 4\nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/folder/view.php?id=1921") #4
        await call.message.answer("UNIT 5\nhttp://elearning.sscoetjalgaon.ac.in/moodle/mod/folder/view.php?id=1922") #5
        await call.message.answer("@@## MENU ##@@\n1 - /start\n2 - /Notes\n3 - /Imp_Websites")





    else:
        await call.message.answer_document(f"Your message is: ")


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'hi':
        await message.answer('Hello i am SSBT telegram bot')
    elif message.text == 'Youtube':
        await message.reply("Tarkesh")
    else:
        await message.answer("@@## MENU ##@@\n1 - /start\n2 - /Notes\n3 - /Imp_Websites")
    # await message.reply(f"Your message is: {message.text}")


executor.start_polling(dp)