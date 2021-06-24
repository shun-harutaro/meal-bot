from linebot import LineBotApi
from linebot.models import TextSendMessage
from datetime import datetime
import setting

CHANNEL_ACCESS_TOKEN = setting.CHANNEL_ACCESS_TOKEN
USER_ID = setting.USER_ID
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def date2file():
    utc_now = datetime.utcnow()
    d = utc_now.day
    h = utc_now.hour
    t = ''
    f = ''
    if (h == 0):
        t = 'm'
    elif (h == 4):
        t = 'l'
    elif (h == 9):
        t = 'd'
    f = str(d) + '-' + t
    return f

def push():
    filename = date2file()
    f = open('content/'+filename, 'r')
    content = f.read()
    f.close()
    messages = TextSendMessage(text=content)
    line_bot_api.push_message(USER_ID, messages)
push()
