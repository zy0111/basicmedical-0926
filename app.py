from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
line_bot_api = LineBotApi('R3U/Zs0GeNBvT7MR8jlyeF1vhNoKsV2XBkvYzFHXl5KR3D5dKwkeiCKkf0yb3POlajr0S5/PWGKogr+Wm/BASb3WiNsEHwdZtpE6j+gpg+GcmmtlBiV5UaTFbPsw43MuftA8kBObdICifwhqD2U/TwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7875c1b46b912baf8c35a18ff87af40f')

# 推給你自己 
line_bot_api.push_message('Uf291503081179f3838f2cc820682e27d ', TextSendMessage(text='(後臺訊息)啟動豆芽探索共學ECHO機器人!'))

# 推給某個User
# line_bot_api.push_message('UserID', TextSendMessage(text='(後臺訊息)啟動豆芽探索共學ECHO機器人!'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
