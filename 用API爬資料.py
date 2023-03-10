import urllib.request as request
import json    #因為此筆資料是用json儲存的
src = 'https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire'
with request.urlopen(src) as response:
    data = json.load(response)   #利用json模組處理json

#將公司名稱列表出來
clist = data['result']['results']
for i in clist:
    print(i['公司名稱'])

#將公司名稱整理出來並寫成一個檔案
with open('company_name.txt','w',encoding='utf-8') as file:
    for i in clist:
        file.write(i['公司名稱'] + '\n')
