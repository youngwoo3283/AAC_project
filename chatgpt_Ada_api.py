import openai


openai.api_key = "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"


# chatgpt가 제공하는 모델 확인 코드
# import os
# import openai
# #openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.Model.list())

# -------------------------------------------------------------------------------------------------------

# 문장을 입력하면 답을 받는 형식
# messages = []
# while True:
#     content = input("User: ")
#     messages.append({'role':'user','content':content})

#     completion = openai.ChatCompletion.create(
#         #model = 'text-davinci-003',
#         model = 'gpt-3.5-turbo',
#         messages = messages
#     )

#     chat_response = completion.choices[0].message.content
#     print(f'ChatGPT: {chat_response}')
#     messages.append({"role":"assistant","content":chat_response})
#------------------------------------------------------------------------------------------------------------

# 데이터 프레임의 여러 토큰을 랜덤하게 입력받으면 답을 받는 형식

import pandas as pd
import numpy as np
import random

messages = []

df_집_동사_검토반영 = pd.read_csv('df_집_동사_검토반영.csv')
df_집_명사_검토반영 = pd.read_csv('df_집_명사_검토반영.csv')

for i in range(5):
    #id_1 = random.randint(0,df_집_동사_검토반영.shape[0])
    content = f"{df_집_동사_검토반영.iloc[i,0]},{df_집_명사_검토반영.iloc[i,0]}을 사용해서 자연스러운 1개의 문장을 만들어줘"
    messages.append({'role':'user','content':content})

    completion = openai.ChatCompletion.create(
        #model = 'text-davinci-003',
        model = 'gpt-3.5-turbo',
        messages = messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response},{df_집_동사_검토반영.iloc[i,0]},{df_집_명사_검토반영.iloc[i,0]}')
    messages.append({"role":"assistant","content":chat_response})



# while True:
#     content = input("User: ")
#     messages.append({'role':'user','content':content})

#     completion = openai.ChatCompletion.create(
#         #model = 'text-davinci-003',
#         model = 'gpt-3.5-turbo',
#         messages = messages
#     )

#     chat_response = completion.choices[0].message.content
#     print(f'ChatGPT: {chat_response}')
#     messages.append({"role":"assistant","content":chat_response})



# ------------------------------------------------------------------------------------------------------------

# prompt = '축구,쉬는시간,하고싶어요라는 단어로 문장을 만들어줘'

# response = openai.Completion.create(engine = 'gpt-3.5-turbo',
#                                     prompt = prompt,
#                                     max_tokens=50)


# print(response.choices[0].text)

#----------------------------------------------------------------------------------------------------------------







