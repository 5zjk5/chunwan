import requests
import re
import csv
import pandas as pd


def create_csv():
    '''
    创建保存 csv
    :return:
    '''
    with open('../data/晚会信息.csv','w+',encoding='utf8',newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['中文名','外文名','别名','国家/地区','类型','主持人','制作公司',
                     '首播时间','播出频道','播出时间','导演','播出状态','在线播放平台',
                     '届数'])


def get_html(url):
    '''
    请求获取 html
    :param url:
    :return:
    '''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    response.encoding = 'utf8'
    return response.text


def get_info(html):
    '''
    提取数据
    :param html:
    :return:
    '''
    # 中文名
    chinaName = re.findall('<dt class="basicInfo-item name">中文名</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html,re.S)
    if chinaName == []:
        chinaName = ''
    else:
        chinaName = chinaName[0]
    # 外文名
    englishName = re.findall('<dt class="basicInfo-item name">外文名</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if englishName == []:
        englishName = ''
    else:
        englishName = englishName[0]
    # 别名
    otherName = re.findall('<dt class="basicInfo-item name">别&nbsp;&nbsp;&nbsp;&nbsp;名</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if otherName == []:
        otherName = ''
    else:
        otherName = otherName[0]
    # 国家/地区
    loc = re.findall('<dt class="basicInfo-item name">国家/地区</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if loc == []:
        loc = ''
    else:
        loc = loc[0]
    # 类型
    type = re.findall('<dt class="basicInfo-item name">类&nbsp;&nbsp;&nbsp;&nbsp;型</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if type == []:
        type = ''
    else:
        type = type[0]
    # 主持人
    zhuchi = re.findall('<dt class="basicInfo-item name">主持人</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if zhuchi == []:
        zhuchi = ''
    else:
        zhuchi = zhuchi[0]
    # 制作公司
    company= re.findall('<dt class="basicInfo-item name">制作公司</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if company == []:
        company = ''
    else:
        company = company[0]
    # 首播时间
    startTime = re.findall('<dt class="basicInfo-item name">首播时间</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if startTime == []:
        startTime = ''
    else:
        startTime = startTime[0]
    # 播出频道
    pingdao = re.findall('<dt class="basicInfo-item name">播出频道</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if pingdao == []:
        pingdao = ''
    else:
        pingdao = pingdao[0]
    # 播出时间
    bochu = re.findall('<dt class="basicInfo-item name">播出时间</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if bochu == []:
        bochu = ''
    else:
        bochu = bochu[0]
    # 导演
    daoyan = re.findall('<dt class="basicInfo-item name">导&nbsp;&nbsp;&nbsp;&nbsp;演</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if daoyan == []:
        daoyan = ''
    else:
        daoyan = daoyan[0]
    # 播出状态
    zhuangtai = re.findall('<dt class="basicInfo-item name">播出状态</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if zhuangtai == []:
        zhuangtai = ''
    else:
        zhuangtai = zhuangtai[0]
    # 在线播放平台
    pingtai = re.findall('<dt class="basicInfo-item name">在线播放平台</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if pingtai == []:
        pingtai = ''
    else:
        pingtai = pingtai[0]
    # 届数
    jieshu = re.findall('<dt class="basicInfo-item name">届&nbsp;&nbsp;&nbsp;&nbsp;数</dt>.*?<dd class="basicInfo-item value">(.*?)</dd>',html, re.S)
    if jieshu == []:
        jieshu = ''
    else:
        jieshu = jieshu[0]

    return [chinaName,englishName,otherName,loc,type,zhuchi,company,
            startTime,pingdao,bochu,daoyan,zhuangtai,pingtai,jieshu]


def write_to_csv(info):
    '''
    保存进 csv
    :param info:
    :return:
    '''
    with open('../data/晚会信息.csv','a+',encoding='utf8',newline='') as f:
        wr = csv.writer(f)
        wr.writerow(info)


def clean_data():
    df = pd.read_csv('../data/晚会信息.csv')
    df['中文名'] = df['中文名'].map(lambda x: x.replace('\n', ''))
    df['外文名'] = df['外文名'].map(lambda x: x.replace('\n', ''))
    df['别名'] = df['别名'].astype(str)
    df['别名'] = df['别名'].map(lambda x: x.replace('\n', ''))
    df['别名'] = df['别名'].map(loc)
    df['国家/地区'] = df['国家/地区'].astype(str)
    df['国家/地区'] = df['国家/地区'].map(lambda x: x.replace('\n', ''))
    df['国家/地区'] = df['国家/地区'].map(loc)
    df['类型'] = df['类型'].map(lambda x: x.replace('\n', ''))
    df['类型'] = df['类型'].map(loc)
    df['主持人'] = df['主持人'].map(lambda x: x.replace('\n', ''))
    df['主持人'] = df['主持人'].map(loc)
    df['主持人'] = df['主持人'].map(loc)
    df['制作公司'] = df['制作公司'].astype(str)
    df['制作公司'] = df['制作公司'].map(lambda x: x.replace('\n', ''))
    df['制作公司'] = df['制作公司'].map(loc)
    df['首播时间'] = df['首播时间'].astype(str)
    df['首播时间'] = df['首播时间'].map(lambda x: x.replace('\n', ''))
    df['播出频道'] = df['播出频道'].astype(str)
    df['播出频道'] = df['播出频道'].map(lambda x: x.replace('\n', ''))
    df['播出频道'] = df['播出频道'].map(loc)
    df['播出时间'] = df['播出时间'].astype(str)
    df['播出时间'] = df['播出时间'].map(lambda x: x.replace('\n', ''))
    df['导演'] = df['导演'].astype(str)
    df['导演'] = df['导演'].map(lambda x: x.replace('\n', ''))
    df['导演'] = df['导演'].map(loc)
    df['播出状态'] = df['播出状态'].astype(str)
    df['播出状态'] = df['播出状态'].map(lambda x: x.replace('\n', ''))
    df['在线播放平台'] = df['在线播放平台'].astype(str)
    df['在线播放平台'] = df['在线播放平台'].map(lambda x: x.replace('\n', ''))
    df['在线播放平台'] = df['在线播放平台'].map(loc)
    df['届数'] = df['届数'].astype(str)
    df['届数'] = df['届数'].map(lambda x: x.replace('\n', ''))

    df.to_csv('../data/晚会信息.csv',index=False)


def loc(s):
    '''
    数据清洗专用
    :param s:
    :return:
    '''
    if 'sup' in s:
        s = re.findall('(.*?)<sup class',s)
        return s
    elif '</a>' in s:
        s = re.findall('>(.*?)</a>',s)
        return s
    else:
        return s


if __name__ == '__main__':
    create_csv()
    for y in range(1983,2022):
        url = 'https://baike.baidu.com/item/{}年中央电视台春节联欢晚会'.format(str(y))
        html = get_html(url)
        info = get_info(html)
        write_to_csv(info)
    clean_data()
