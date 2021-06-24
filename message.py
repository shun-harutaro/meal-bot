from linebot import LineBotApi
from linebot.models import TextSendMessage
import setting

CHANNEL_ACCESS_TOKEN = setting.CHANNEL_ACCESS_TOKEN
USER_ID = setting.USER_ID
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def push():
    message = TextSendMessage(text="てすと")
    linebot.push_message(USER_ID, message=messages)

push()
