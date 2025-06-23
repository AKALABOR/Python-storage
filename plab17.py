import json
import os
import logging
from threading import Lock
from json import JSONDecodeError

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = '8153800687:AAFz6tdtz6pfszMhBLLN9Dpcuba3SmH45E8'

class Assistant:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.lock = Lock()
        self._load_notes()

    def _load_notes(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f)
            self.notes = []
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.notes = json.load(f)
                if not isinstance(self.notes, list):
                    raise JSONDecodeError("not a list", "", 0)
        except (JSONDecodeError, ValueError):
            self.notes = []
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _save_notes(self):
        with self.lock:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def add_note(self, note: str):
        self.notes.append(note)
        self._save_notes()

    def list_notes(self):
        return list(self.notes)

    def search_notes(self, keyword: str):
        kw = keyword.lower()
        return [n for n in self.notes if kw in n.lower()]

def console_interface():
    a = Assistant()
    while True:
        cmd = input("Команда (/add, /list, /search, /exit): ").strip()
        if cmd == "/add":
            note = input("Введіть текст нотатки: ").strip()
            if note:
                a.add_note(note)
                print("Нотатку додано.")
            else:
                print("Порожня нотатка не зберігається.")
        elif cmd == "/list":
            notes = a.list_notes()
            if not notes:
                print("Нотаток немає.")
            else:
                for idx, n in enumerate(notes, 1):
                    print(f"{idx}. {n}")
        elif cmd == "/search":
            kw = input("Введіть ключове слово для пошуку: ").strip()
            if kw:
                found = a.search_notes(kw)
                if not found:
                    print("Нічого не знайдено.")
                else:
                    for idx, n in enumerate(found, 1):
                        print(f"{idx}. {n}")
            else:
                print("Ключове слово порожнє.")
        elif cmd == "/exit":
            break
        else:
            print("Невідома команда.")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
assistant = Assistant()

class AddNoteState(StatesGroup):
    waiting_for_note = State()

class SearchNoteState(StatesGroup):
    waiting_for_keyword = State()

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    text = (
        "Вітаю! Я ваш асистент.\n"
        "/add – додати нотатку\n"
        "/list – показати всі нотатки\n"
        "/search – пошук за ключовим словом"
    )
    await message.reply(text)

@dp.message_handler(commands=["add"])
async def cmd_add(message: types.Message):
    await message.reply("Введіть текст нотатки:")
    await AddNoteState.waiting_for_note.set()

@dp.message_handler(state=AddNoteState.waiting_for_note, content_types=types.ContentTypes.TEXT)
async def process_add_note(message: types.Message, state: FSMContext):
    note = message.text.strip()
    if note:
        assistant.add_note(note)
        await message.reply("Нотатку додано.")
    else:
        await message.reply("Порожня нотатка не зберігається.")
    await state.finish()

@dp.message_handler(commands=["list"])
async def cmd_list(message: types.Message):
    notes = assistant.list_notes()
    if not notes:
        await message.reply("Нотаток немає.")
    else:
        text = "\n".join(f"{i+1}. {n}" for i, n in enumerate(notes))
        await message.reply(text)

@dp.message_handler(commands=["search"])
async def cmd_search(message: types.Message):
    await message.reply("Введіть ключове слово для пошуку:")
    await SearchNoteState.waiting_for_keyword.set()

@dp.message_handler(state=SearchNoteState.waiting_for_keyword, content_types=types.ContentTypes.TEXT)
async def process_search_note(message: types.Message, state: FSMContext):
    kw = message.text.strip()
    if kw:
        found = assistant.search_notes(kw)
        if not found:
            await message.reply("Нічого не знайдено.")
        else:
            text = "\n".join(f"{i+1}. {n}" for i, n in enumerate(found))
            await message.reply(text)
    else:
        await message.reply("Ключове слово порожнє.")
    await state.finish()

@dp.message_handler()
async def unknown(message: types.Message):
    await message.reply("Невідома команда. Використайте /help.")

if __name__ == "__main__":
    mode = input("Виберіть режим (console/telegram): ").strip().lower()
    if mode == "console":
        console_interface()
    elif mode == "telegram":
        executor.start_polling(dp, skip_updates=True)
    else:
        print("Невірний режим. Запустіть програму ще раз.")
