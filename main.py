
import requests
from bs4 import BeautifulSoup
import json

print("csidas")
baseUrl = 'https://thuvienphapluat.vn/'
arrLinks =[]
for i in range(500):
    resp = requests.get(baseUrl + '/hoi-dap-phap-luat/tien-te-ngan-hang?page=' + str(i))
    soup = BeautifulSoup(resp.content, "html.parser")
    links = soup.select('.tvpl-main > .row >.col-md-9 >section >.news-card >a')
    for link in links:
     # phân tích dữ liệu lưu trữ vào file json
     newLink = link['href']
     resp1 = requests.get(newLink)
     soup1 = BeautifulSoup(resp1.content, "html.parser")
     dataTimes = soup1.select('.tvpl-main >.d-flex >span')
     dataHeaders = soup1.select('.row >.col-md-9 >article >.row >div >#news-detail>header >h1')
     dataBodys = soup1.select('.row >.col-md-9 >article >.row >div >#news-detail>.news-content>p')
     # mang chua body
     bodys = []
     for dataTime in dataTimes:
        time = dataTime.text
     for dataHeader in dataHeaders:
        header = dataHeader.text
     for dataBody in dataBodys:
        bodys.append(dataBody.text)
     #du lieu moi kieu json
     newData = {
        "time" : time,
        "header": header,
        "answer" : bodys
     }
     with open("data.json", "r") as file:
        content = file.read()
     data = list(json.loads(content))
     data.append(newData)
     newDataJson = json.dumps(data, indent=4)
     with open("data.json", 'w') as file:
        file.write(newDataJson)
     
     
     

     

     
    
        
        

     

    

