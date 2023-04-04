import requests
import re 
import random
import datetime
import streamlit as st
from lxml import etree
import pyttsx3 as pt
def panduan(url,t):
    if 'szu' in url:
        paqu_sd(url,t)
    if 'seu' in url:
        paqu_dnd(url,t)
def paqu_sd(url,t):
    import datetime
    SHA_TZ = datetime.timezone(datetime.timedelta(hours=8),name='Asia/Shanghai')
    while True:
        resp=requests.get(url,headers=header)
        resp.encoding='utf-8'
        e=etree.HTML(resp.text)
        time=e.xpath('/html/body/div[3]/div[4]/div[2]/div[2]/ul/li[1]/a/h3/text()')[0]
        title=e.xpath('/html/body/div[3]/div[4]/div[2]/div[2]/ul/li[1]/a/p/text()')[0]
        if '2023-04' in time :
            if '拟录取' in title:
                #如果是这个月出的通知并且含有拟录取字样就提醒我
                pt.speak('已经出录取名单啦')
                pt.speak('已经出录取名单啦')
                pt.speak('已经出录取名单啦')
                from playsound import playsound
                #放歌提醒a
                playsound('D:\CloudMusic\陈军 - 赛马.mp3')
                break
            else:
                st.write('还没出录取名单')
        else:
            now=datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).astimezone(SHA_TZ).strftime('%H:%M:%S')
            st.write(f'{now}  还没出录取名单')
        import time
        #5分钟查一次
        time.sleep(t)
def dnd_detail(url,num,t):
    
    while True:
        import datetime
        SHA_TZ = datetime.timezone(datetime.timedelta(hours=8),name='Asia/Shanghai')
        resp=requests.get(url,headers=header)
        resp.encoding='utf-8'
        e=etree.HTML(resp.text)
        try:  
            key=e.xpath(f'/html/body/div/div/div/div/div/article/div/table/tbody/tr[{num}]/td[3]/p/span/a/text()')[0]
            pt.speak('出名单啦')
            url1=e.xpath(f'/html/body/div/div/div/div/div/article/div/table/tbody/tr[{num}]/td[3]/p/span/a/@href')[0]
            st.write(f'请点击查看：{url1}')
            break
        except:
            now=datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).astimezone(SHA_TZ).strftime('%H:%M:%S')
            st.write(f'{now}  还没出名单，再等等')
        import time
        #5分钟查一次
        time.sleep(t)
def paqu_dnd(url,t):
    resp=requests.get(url,headers=header)
    resp.encoding='utf-8'
    e=etree.HTML(resp.text)
    k=e.xpath('/html/body/div/div/div/div/div/article/div/table/tbody/tr/td[2]/p/span/text()')
    k.insert(0,'请选择')
    xy=st.selectbox('请选择学院',k)
    num=0
    # xueyuan='体育系'
    for x,y in enumerate(k):
        if y==xy:
            # st.write(x+1,y)
            num=x+1
    if xy=='请选择':
        st.stop()
    st.success(dnd_detail(url,num,t))
  
    
  
    
  
user_agent=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36']
header={'user-agent':random.choice(user_agent)}


url=st.text_input('请输入可查询到成绩的网页')
t=st.slider('间隔更新时间选择（默认10秒）',10,7200)
st.write(f'当前选择间隔{t}秒')
if url==None:
    st.warning('请输入可查询到成绩的网页')
    st.stop()
st.success(panduan(url,t))
