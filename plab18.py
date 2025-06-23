from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import json
import os

API_TOKEN = '8153800687:AAFz6tdtz6pfszMhBLLN9Dpcuba3SmH45E8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

DATA_FILE = "notes.json"

def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_notes(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привіт! Я бот для нотаток. Введіть /help, щоб дізнатися більше.")

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "/addnote – додати нотатку\n"
        "/listnotes – переглянути нотатки\n"
        "/deletenote – видалити нотатку\n"
        "/info – про бота\n"
        "/exit – завершити роботу"
    )

@dp.message(Command("info"))
async def info(message: Message):
    await message.answer("Цей бот дозволяє створювати, переглядати та видаляти особисті нотатки.")

@dp.message(Command("exit"))
async def exit_cmd(message: Message):
    await message.answer("Дякую за використання бота. До зустрічі!")

@dp.message(Command("addnote"))
async def add_note(message: Message):
    await message.answer("Напишіть текст нотатки:")

    @dp.message()
    async def get_note_text(msg: Message):
        user_id = str(msg.from_user.id)
        notes = load_notes()
        notes.setdefault(user_id, []).append(msg.text)
        save_notes(notes)
        await msg.answer("Нотатку збережено!")
        dp.message.unregister(get_note_text)

@dp.message(Command("listnotes"))
async def list_notes(message: Message):
    user_id = str(message.from_user.id)
    notes = load_notes().get(user_id, [])
    if notes:
        reply = "\n".join(f"{idx+1}. {note}" for idx, note in enumerate(notes))
        await message.answer(f"Ваші нотатки:\n{reply}")
    else:
        await message.answer("У вас ще немає нотаток.")

@dp.message(Command("deletenote"))
async def delete_note(message: Message):
    await message.answer("Введіть номер нотатки для видалення:")

    @dp.message()
    async def get_index(msg: Message):
        try:
            index = int(msg.text) - 1
            user_id = str(msg.from_user.id)
            notes = load_notes()
            if user_id in notes and 0 <= index < len(notes[user_id]):
                removed = notes[user_id].pop(index)
                save_notes(notes)
                await msg.answer(f"Нотатку '{removed}' видалено.")
            else:
                await msg.answer("Невірний номер нотатки.")
        except ValueError:
            await msg.answer("Введіть число.")
        dp.message.unregister(get_index)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
