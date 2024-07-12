import requests
url = f'https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json'
headers = {
    'User-Agent': 'application.json'
}
response = requests.get(url,headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')
