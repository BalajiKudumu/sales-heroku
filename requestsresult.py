import requests
url='http://localhost:5000/predict_api'
r=requests.post(url,json={"rate":0,"sales_in_first_month":2,'sales_in_second_month':500})
print(r.json())