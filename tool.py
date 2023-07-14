import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from jamo import h2j, j2hcj



#해당 카테고리가 있는 주소를 넣으면 그 카테고리에 있는 토큰과 이미지를 가져오는 함수
def get_text(url):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    elements_text = soup.select('.s-expression')
    #elements_image = soup.select('.s-img')


    li = []

    for i in range(len(elements_text)):
        try:
            li.append(elements_text[i].text)
        except:
            print(f"{i}번째 데이터에 오류가 있습니다")

    return li


def get_image(url):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    #elements_text = soup.select('.s-expression')
    elements_image = soup.select('.s-img')


    li = []

    for i in range(len(elements_image)):
        try:
            li.append(elements_image[i]['src'])
        except:
            print(f"{i}번째 데이터에 오류가 있습니다")

    return li


def make_df(li_text,li_image):
    df_temp = pd.DataFrame({'text':li_text,
                            'image':li_image})

    return df_temp



# text = "저는 집에 가고 싶어요"
# jamo_str = j2hcj(h2j(text))


def extract_consonant(text):
    return j2hcj(h2j(text))[-1]



def is_noun(a):
    length = len(a)
    if length <= 2:
        return '명사'
    else:
        if extract_consonant(a) == 'ㅁ':
            return '명사'
        else:
            return '0'
        

def extract_verb(url):

    li_food_text = get_text(url)
    li_food_image = get_image(url)

    df_food = make_df(li_food_text,li_food_image)

    id = []
    for i in range(df_food.shape[0]):
        temp = df_food.iloc[i,0]
        if temp[-1] =="요":
            id.append(i)

    df_food_id=df_food.iloc[id] 

    return df_food_id