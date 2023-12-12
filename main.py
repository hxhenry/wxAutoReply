
from wxauto import *
import time
import pyautogui
import pyperclip
 
msg='1'
# 获取当前微信客户端
wx = WeChat()
user = 'A新人通知'
# 获取会话列表
wx.GetSessionList()
 
def reply_message_if_send_key_word(user, key_words, reply_message):
    #wx.LoadRecentMessage(1)
    msgs = wx.GetAllMessage
    message_value = [msg[1] for msg in msgs]
    for index, msg in enumerate(msgs):
        if msg[0] in key_words:
            
            print("*"*20)
            if reply_message not in message_value[index:]:
                print(f"将自动回复以下语句:{reply_message}")
                
                
                def send():
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')
 
                def send_msg(friend):
                    for i in range(1):
                        send()
                        time.sleep(0.001)
                if __name__ == '__main__':
                    send_msg(user)
            else:
                pass
            print("*"*20)
 
if __name__ == '__main__':
    user = 'A新人通知'
    key_word1 = 'vivan'
    key_word2 = 'sandy'
    key_word3 = 'jennie'
    key_word4 = 'Bunny'
    key_word5 = 'Yuumi'
    key_word6 = 'Kaylee'
    key_word7 = 'Cris'
    key_words = [key_word1,key_word2,key_word3,key_word4,key_word5,key_word6, key_word7]
    reply_message = '1'
 
    while True:
        reply_message_if_send_key_word(user=user, key_words=key_words ,reply_message=reply_message)
        time.sleep(0.001)
