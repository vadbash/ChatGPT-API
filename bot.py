import requests
import telebot
from telebot import types
import openai
import os

#bot connect
bot = telebot.TeleBot('TG_bot_token')

#chatgpt api connect
API_KEY = 'Chatgpt_api_key'
openai.api_key = f'{API_KEY}'

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("ChatGPT")
    markup.add(btn1)
    bot.reply_to(message, "Hello, click chatGPT and write one question", reply_markup=markup)

    @bot.message_handler(regexp="ChatGPT")
    def send_welcome(message):
        msg = bot.send_message(message.chat.id, text="Type your question")
        bot.register_next_step_handler(msg, define)

    def ask_gpt(prompt, model="text-davinci-002", max_tokens=150, temperature=0.5):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        answer = response.choices[0].text.strip()
        return answer
    #Main function
    def define(message):
        message_text = str(message.text)
        prompt = message_text
        answer = ask_gpt(prompt)

        #output
        bot.send_message(message.chat.id, text=f"{answer}")
        bot.send_message(message.chat.id, text=f"Whant other question? Click ChatGPT one more time")
        print(answer)
    

bot.infinity_polling()

