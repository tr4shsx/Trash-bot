# Open-source totalmente editável
# Chat bot: telegram
# Versão Atual 1.1.0
# Código desenvolvido por @Tr4shpxdm


# Importações
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep

# Configurações
bot = telebot.TeleBot("TOKEN_BOT")

# Créditos Terminal
sleep(2)
print('Create by @Tr4shpxdm')
print('www.github.com/tr4shpxdm')

# Botões
def menu_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("CANAL", url="https://t.me/nome"))
    return markup

#Início de Menus e comandos 

@bot.message_handler(commands=['start'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text

    menu = f'Olá, eu sou um bot para estudos e desenvolvimento'
    bot.send_message(chat_id=bid, text=menu, reply_markup=menu_markup())

# Inicialização do bot
bot.polling(timeout=987886875)