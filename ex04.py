import requests

response = requests.get('http://192.168.0.123:7888/home')
if response.status_code==200:
    data=response.json()
    print('이름 국어 영어 수학 총점 평균')
    for i in data:
        tot = i['국어']+i['영어']+i['수학']
        avg = tot//3
        print(i['이름'], i['국어'], i['영어'], i['수학'], tot, avg)
