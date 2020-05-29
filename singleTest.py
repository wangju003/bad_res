import requests

url = 'https://appapi.5i5j.com/appapi/rent/5/v1/dklist'
data={"hid":23966781}

url2='https://appapi.5i5j.com/appapi/community/5/v1/allinfo'
data2={"uid":"7782413","communityid":338855,"cityid":"5"}

url3='https://appapi.5i5j.com/appapi/home/5/info'
data3={}

token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjEifQ.eyJpc3MiOiJ6aGFuZ3NhbiIsImp0aSI6IjEiLCJpYXQiOjE1NzY4MTA4NDksImF1ZCI6IntcInVpZFwiOlwiNjMxMjI4NlwiLFwibG9naW5uYW1lXCI6bnVsbCxcIm5pY2tuYW1lXCI6XCJcXHU3NTFmXFx1NGVhN1wiLFwiZW1haWxcIjpudWxsLFwiZ2VuZGVyXCI6bnVsbCxcInJlZ2lvblwiOm51bGwsXCJjaXR5XCI6bnVsbCxcImhlYWRpbWdcIjpudWxsLFwiaW52aXRpbmdjb2RlXCI6bnVsbCxcInJlZ2RhdGVcIjpcIjE1NTM0OTY2MzJcIixcInN0YXR1c1wiOjEsXCJwYXNzV29yZFwiOlwiNzIxOTk2YTQxMjU0MjY0NTE1OTRkNDI0NTc5MjMzMjhcIixcInNhbHRcIjpcIjNVMWVjNFwifSIsInN1YiI6InN1YmplY3QifQ.KZFAOXnRKnkxCd9Q9cdvfy2jF1HvIoD_rx00Z2L0RZE'
headers = {'token':token}

r = requests.post(url2,json=data2)
print(r.text)