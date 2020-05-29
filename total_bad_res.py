import pandas as pd
from sqlalchemy import  create_engine

from settings import citys

engine = create_engine('mysql+mysqlconnector://root:admin123456@10.2.1.92/autotest?charset=utf8')

#step1 获取数据源
# sql='select * from response_time'
# df=pd.read_sql_query(sql,engine)
# print(df.shape)

#step2 导出数据源
# df.to_excel('bad_res.xlsx')

# step3 使用pandas处理数据
df =pd.DataFrame(pd.read_excel('bad_res.xlsx'))
print(df.shape)

'''
数据重组
分出城市，测试环境
url中只保留接口地址部分
'''
#通过接口地址 区分出城市
for city in citys:
    city_id =city['city_id']
    city_name=city['name']

    df.loc[df['request_url'].str.contains('/%s/'%city_id),'city']='%s'%city_name

#通过接口地址 区分出测试环境 线上|预生产
df.loc[df['request_url'].str.contains('https://appapi.5i5j.com/'),'test_env']='appapi'
df.loc[df['request_url'].str.contains('https://appts.5i5j.com/'),'test_env']='appts'

#分割接口地址，去掉 域名，只保留url地址
df.replace(r'https://appapi.5i5j.com/','',regex=True,inplace=True)
df.replace(r'https://appts.5i5j.com/','',regex=True,inplace=True)


'''
统计结果
'''
#按城市统计 超时接口数量

#按测试环境统计，超时接口数量

#按接口统计，哪个接口超时次数最多？

#接时间统计，上午还是下午容易响应超时

#周一至周日来统计，哪一天最容易接口超时