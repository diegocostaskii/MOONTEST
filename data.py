import os
import requests
from lxml import etree
import json
import bz2

pathList = []
pathList.append(os.path.join(os.path.dirname(__file__), 'wiki1.bz2 '))
pathList.append(os.path.join(os.path.dirname(__file__), 'wiki2.bz2 '))  
pathList.append(os.path.join(os.path.dirname(__file__), 'wiki3.bz2 '))  
pathList.append(os.path.join(os.path.dirname(__file__), 'wiki4.bz2 '))
pathList.append(os.path.join(os.path.dirname(__file__), 'wiki5.bz2 ')) 
pathList.append(os.path.join(os.path.dirname(__file__), 'wiki6.bz2 ')) 
import re



urlList=[]
urlList.append('https://dumps.wikimedia.org/zhwiki/20250201/zhwiki-20250201-pages-articles-multistream1.xml-p1p187712.bz2')
urlList.append('https://dumps.wikimedia.org/zhwiki/20250201/zhwiki-20250201-pages-articles-multistream2.xml-p1p187712.bz2')
urlList.append('https://dumps.wikimedia.org/zhwiki/20250201/zhwiki-20250201-pages-articles-multistream3.xml-p1p187712.bz2')
urlList.append('https://dumps.wikimedia.org/zhwiki/20250201/zhwiki-20250201-pages-articles-multistream4.xml-p1p187712.bz2')
urlList.append('https://dumps.wikimedia.org/zhwiki/20250201/zhwiki-20250201-pages-articles-multistream5.xml-p1p187712.bz2')
urlList.append('https://dumps.wikimedia.org/zhwiki/20250201/zhwiki-20250201-pages-articles-multistream6.xml-p1p187712.bz2')



def parse(bz2_file, jsonl_file, count):
        with bz2.open(bz2_file, 'rb') as bz2_f:
            tree = etree.parse(bz2_f)
            root = tree.getroot()            
        with open(jsonl_file, 'a', encoding='utf-8') as jsonl_f:
            # 遍历每个 page 元素
            ns = root.nsmap[None]
            ns = "{%s}" % ns
            for page in root.findall("{0}page".format(ns)):
                if count<maxCount:
                    # 提取信息
                    title = page.find('{0}title'.format(ns)).text
                    revision = page.find('{0}revision'.format(ns))
                    text_content = revision.find('{0}text'.format(ns)).text
                    text_content = str(text_content)
                    text_content,category = clean_text(text_content)
                    # 构建要写入的字典
                    data = {
                        "meta": {
                            "title": title,
                            "category":category
                        },
                        "text": text_content,
                        
                    }
                    count+=1
                    # 写入JSONL文件
                    json.dump(data,jsonl_f, ensure_ascii=False)
                    jsonl_f.write('\n')

def clean_text(text):

    text = text.replace('\\', '')
    text = text.replace('|', '')
    pattern = r'\[\[Category:([^\]]+)\]\]'
    matches = re.findall(pattern, text)
    category = ''
    for i in matches:
        category = category+str(i)+' '

    text = text.replace('{{', '').replace('}}', '')
    text = text.replace('<', '').replace('>', '').replace('-', '')
    text = text.replace('[', '').replace(']', '')

    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\".*?\"','',text)
    text = re.sub(r'&#.2?','',text)
    text = re.sub(r'\[\[File:.*?\]\]', '', text)
    text = re.sub(r"[a-zA-Z|( )//'.%&*=;:___]", '', text)
    
    pattern = r'\d{14}\+\d{4}'
    text = re.sub(pattern, '', text)
    text = re.sub(r'（）', '', text)
    text = re.sub(r'\d{10,}', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    text = text[0:maxToken]
    
    return text,category



count = 0
maxCount = 1000
maxToken = 512
for i in range(len(pathList)):
    if count < maxCount:
        if not os.path.exists(pathList[i]):
            data_url = urlList[i]
            with open(pathList[i], 'wb+') as f:
                f.write(requests.get(data_url).content)
            parse(pathList[i],'result.jsonl', count)
        else:
            parse(pathList[i],'result.jsonl', count)
