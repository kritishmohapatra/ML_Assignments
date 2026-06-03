
'''https://docs.langchain.com/oss/python/langchain/overview
https://docs.langchain.com/oss/python/langchain/quickstart
https://docs.langchain.com/oss/python/releases/changelog'''
import threading
from bs4 import BeautifulSoup
import requests

url=[
    'https://docs.langchain.com/oss/python/langchain/overview',
'https://docs.langchain.com/oss/python/langchain/quickstart',
'https://docs.langchain.com/oss/python/releases/changelog'

]

def fetch_c(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.content, 'html.parser')
    print(f"fetched{len(soup.text)} char from {url}")
threads=[]
for ul in url:
    thread=threading.Thread(target=fetch_c, args=(ul,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("dONE")