import requests

#url = "https://tiendas.axoft.com/api/Aperture/Price?pageSize=500&pageNumber=1&filter=1"
#response = requests.get(api_url, params={"accesstoken":})

url="https://tiendas.axoft.com/api/Aperture/"
pricesResource="Price?pageSize=500&pageNumber=%%pageNumber%%&filter=1"
productResource="Product?pageSize=500&pageNumber=1&filter=%%sku%%"
accesstoken="1b527354-2481-4f92-b2f9-208056e615a4_12236"
#accesstoken="f91c69e5-51d5-4c2b-9a0c-6000299788c2_12685"
startDate="2022-10-04T08:00:00"
threads=500

response = requests.get(url, params={'pricesResource':pricesResource,"accesstoken":accesstoken,"productResource":productResource,"startDate":startDate,"threads":500})

response.json()

print(response.json())

