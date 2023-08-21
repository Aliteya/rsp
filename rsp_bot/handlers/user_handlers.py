from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_kb, game_kb
from servises.servises import get_result, get_win


router: Router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)

@router.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb )

@router.message(F.text==LEXICON_RU['yes_button'])
async def lets(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

@router.message(F.text==LEXICON_RU['no_button'])
async def nou(message: Message):
    await message.answer(text=LEXICON_RU['no'])

@router.message(F.text.in_([LEXICON_RU['rock'], LEXICON_RU['scissors'], LEXICON_RU['paper']]))
async def game_choice(message: Message):
    bot_choice = get_result()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]}' f'- {LEXICON_RU[bot_choice]}')
    wiwi = get_win(message.text, bot_choice)
    await message.answer(LEXICON_RU[wiwi], reply_markup=yes_no_kb)