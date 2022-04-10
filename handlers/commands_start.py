from aiogram import types
from misc import dp,bot
import asyncio
content = -1001620327594

@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    await update.approve()
    await asyncio.sleep(20)
    await bot.copy_message(chat_id=update.from_user.id , from_chat_id= content, caption= """Возраста постарше и помладше💋
Все есть в наличии😋😋

Пиши мне в личку, @karinka77_tg хочу доступ❗️

🔮Buy access - @karinka77_tg""", message_id= 2)


