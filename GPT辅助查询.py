from config.yml_DATA import *
from revChatGPT.V1 import Chatbot
#注要有chatgpt才可以访问到并且使用时要科学上网
#Access Token获取网址https://chat.openai.com/api/auth/session

chatbot = Chatbot(config={"access_token":GPT_access_token},conversation_id=GPT_convo_id)
for i in chatbot.get_conversations():
    print(i['id'])

