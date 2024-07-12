### Pendahuluan
BMKG menyediakan data terbuka untuk diakses publik untuk meningkatkan transparansi, akuntabilitas, dan artisipasi masyarakat. Data yang tersedia yakni :
- Data Prakiraan Cuaca, Data ini berisi informasi seperti suhu udara, kelembapan, arah dan kecepatan angin, serta kondisi cuaca dengan format CSV (Comma Separated Values)
- Data Gempa Bumi, Data ini berisi Informasi mengenai kejadian gempa bumi di seluruh wilayah Indonesia. Data ini mencakup gempa bumi dengan magnitudo 5.0 ke atas, gempa bumi yang dirasakan, dan gempa bumi berpotensi tsunami. Data tersedia dalam format XML, JSON, dan JPG

Data-data ini dapat diakses melalui portal data BMKG, dan pengguna diwajibkan untuk mencantumkan BMKG sebagai sumber data jika digunakan dalam aplikasi atau sistem lainnya​ (Data Terbuka BMKG)​.
### Penggunaan
Untuk mengakses salah satu data terbuka bmkg kita dapat menggunakan bahasa pemrograman Python sebagai request kita ke data terbuka bmkg dengan menggunakan library request, untuk menginstall library python kita dapat menggunakan command prompt dan pastikan anda memiliki versi pip yang terbaru ```python -m pip install requests```

Setelah library request terinstall anda dapat memahami kode dibawah ini

```
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
```
