import json
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

restime = []
OK=[]
class Restime():
    def API(self,URL2,param):

        try:
            r = requests.get(URL2, json=param, timeout=10)
            r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
        except requests.RequestException as e:
            print(e)
        else:
            js = json.dumps(r.json())
            return [r.json(), r.elapsed.total_seconds(),js]

    def circulation(self,num,URL2,param):

        for i in range(num):

            restime.append(Restime.API(URL2,param)[1]) #超时时间列表集合
            if json.loads(Restime.API(URL2, param)[2])["msg"]=='ok':
                OK.append(json.loads(Restime.API(URL2, param)[2])["msg"])
                logger.info('请求第' + str(i+1) + '次，请求'+json.loads(Restime.API(URL2, param)[2])["msg"]+',状态码：'+json.loads(Restime.API(URL2, param)[2])["status"])
            else:
                logger.info('请求第' + str(i+1) + '次，请求' + json.loads(Restime.API(URL2, param)[2])["msg"] + ',状态码：' +
                            json.loads(Restime.API(URL2, param)[2])["status"])

        print('测试次数：',num)
        print('响应次数：', len(restime))
        print('正常响应次数：', len(OK))
        print('总响应最大时长：', max(restime))
        print('总响应最小时长：', min(restime))
        print('总响应时长：', sum(restime))
        print('平均响应时长：', sum(restime) / len(restime))



if __name__ == '__main__':
    Restime=Restime()

    num=10#压力测试次数
    URL2 = 'https://appapi.5i5j.com/appapi/community/5/v1/allinfo'  #地址
    param = {"uid":"7782413","communityid":338855,"cityid":"5"} #参数
    Restime.API(URL2,param)


    Restime.circulation(num,URL2,param)

    # input('Press Enter to exit...')

    # r = requests.post(URL2,json=param)
    # print(r.text)