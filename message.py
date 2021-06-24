from linebot import LineBotApi
from linebot.models import TextSendMessage
import setting

CHANNEL_ACCESS_TOKEN = setting.CHANNEL_ACCESS_TOKEN
USER_ID = setting.USER_ID
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def push():
    f = open('', 'r')
    content = f.read()
    f.close()
    messages = TextSendMessage(text=content)
    line_bot_api.push_message(USER_ID, messages)

push()
