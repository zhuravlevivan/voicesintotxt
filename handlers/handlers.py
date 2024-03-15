import os
from config import bot
from aiogram import types
from pydub import AudioSegment
import speech_recognition


async def oga2wav(filename):
    # Конвертация формата файлов
    new_filename = filename.replace('.oga', '.wav')
    audio = AudioSegment.from_file(filename)
    audio.export(new_filename, format='wav')
    return new_filename


async def recognize_speech(oga_filename):
    # Перевод голоса в текст + удаление использованных файлов
    wav_filename = await oga2wav(oga_filename)
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.WavFile(wav_filename) as source:
        wav_audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(wav_audio, language='ru')
    except Exception as e:
        return str(e)

    if os.path.exists(oga_filename):
        os.remove(oga_filename)

    if os.path.exists(wav_filename):
        os.remove(wav_filename)

    return text


async def download_file(bot, file_id):
    # Скачивание файла, который прислал пользователь
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    filename = file_id + file_info.file_path
    filename = filename.replace('/', '_')
    with open(filename, 'wb') as f:
        f.write(downloaded_file.getvalue())
    return filename


async def start_cmd(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет')


async def transcript(message: types.Message):
    # Функция, отправляющая текст в ответ на голосовое
    filename = await download_file(bot, message.voice.file_id)
    text = await recognize_speech(filename)
    if text:
        await bot.send_message(message.chat.id, text)
    else:
        await bot.send_message(message.chat.id, 'enjoy the silence')
