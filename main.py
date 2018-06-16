import gc
import api

telegram = api.TelegramBot('API-KEY')

def message_handler(message):
    if message[2] == '/start':
        telegram.send(message[0], 'Start the bot.')
    else:
        telegram.send(message[0], 'Message received: {}'.format(message[2]))
        
    gc.collect()

telegram.listen(message_handler)

