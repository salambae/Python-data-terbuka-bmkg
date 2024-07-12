# Cara mengakses data terbuka BMKG dengan Python
## Pendahuluan
BMKG menyediakan data terbuka untuk diakses publik untuk meningkatkan transparansi, akuntabilitas, dan artisipasi masyarakat. Data yang tersedia yakni :
- Data Prakiraan Cuaca, Data ini berisi informasi seperti suhu udara, kelembapan, arah dan kecepatan angin, serta kondisi cuaca dengan format CSV (Comma Separated Values)
- Data Gempa Bumi, Data ini berisi Informasi mengenai kejadian gempa bumi di seluruh wilayah Indonesia. Data ini mencakup gempa bumi dengan magnitudo 5.0 ke atas, gempa bumi yang dirasakan, dan gempa bumi berpotensi tsunami. Data tersedia dalam format XML, JSON, dan JPG

Data-data ini dapat diakses melalui portal data BMKG, dan pengguna diwajibkan untuk mencantumkan BMKG sebagai sumber data jika digunakan dalam aplikasi atau sistem lainnya​ (Data Terbuka BMKG)​.
## Penggunaan
Untuk mengakses salah satu data terbuka bmkg kita dapat menggunakan bahasa pemrograman Python sebagai request kita ke data terbuka bmkg dengan menggunakan library request, untuk menginstall library python kita dapat menggunakan command prompt dan pastikan anda memiliki versi pip yang terbaru ```python -m pip install requests```

Setelah library request terinstall, semisal kita ingin mengakses data gempa terbaru di Indonesia kita dapat memahami kode dibawah ini :

```Python
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

### Penjelasan kode diatas :
- Menggunakan library request, pada baris pertama ```import request```, kita mengimpor library request yang memungkinkan kita untuk melakukan HTTP request
- Mendefinisikan URL Endpoint dengan menambahkan variabel ```url = f'https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json'```
- Melakukan HTTP Get Request, fungsi sintaks ```response = request.get(url,headers=headers)``` yakni Kita melakukan GET request bersamaan dengan headers ke URL yang telah kita siapkan.
- Mencetak dan memproses respon, fungsi sintaks ```if response.status_code == 200:``` adalah memeriksa apakah request berhasil dilakukan dengan memeriksa status code respons. Status code 200 menunjukkan request berhasil, apabila status code menunjukkan code selain 200 maka python akan mencetak error beserta error code
- Apabila request berhasil, kita akan mengambil data json dari respon dan menyimpannya ke dalam variabel ```data = response.data()```
- Mencetak data json mentah ke konsol

Dengan menggunakan kode diatas, anda dapat mengintegrasikan data cuaca dari BMKG ke dalam aplikasi atau proyek Python kamu untuk menampilkan informasi cuaca terkini atau prakiraan cuaca sesuai dengan area yang kamu pilih.

## Referensi
https://data.bmkg.go.id/gempabumi/
