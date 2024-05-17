# ETL (Extract, Transform, Load) and Visualization

## About Project
Tentang proyek ETL dengan visualisasi data dan analisis: proyek ini bertujuan untuk mengintegrasikan, membersihkan, dan menganalisis data dari berbagai sumber untuk mendukung pengambilan keputusan yang lebih baik. Dengan menggunakan proses ETL (Ekstraksi, Transformasi, dan Load), data disusun, ditransformasi, dan disajikan secara visual melalui grafik, diagram, dan dashboard interaktif. Ini memungkinkan organisasi untuk memahami pola, tren, dan temuan penting dalam data dengan lebih baik, serta memberikan wawasan yang mendalam untuk pengambilan keputusan yang terinformasi.

## Tech Stacks
Tools dan framework yang digunakan dalam project ini:
- Python
- Library Python: Pandas, sqlite3, os, OpenAI, requests, numpy, json, re, seaborn, matplotlib.pyplot, plotly.express, BeautifulSoup, sklearn, mysql.connector, csv, dotenv.
- Jupyter Notebook
- Google Cloud Storage atau Google Firebase
- Google BigQuery
- GitHub
- CSV
- JSON 
- MySQL
- XML
- DB
- API
- Apache Airflow

## Architecture Diagram
![Arsitektur Diagram ETL](Architecture-Diagram-ETL.png)

## Setup 
Berikut langkah-langkah untuk memproses setiap data:

### Langkah 1: Persiapan Environment
**Instalasi Library dan Tools**:
   - Persiapkan instalasi Python beserta pustaka yang diperlukan seperti Pandas, sqlite3, OpenAI, requests, json, re, seaborn, matplotlib.pyplot, plotly.express, BeautifulSoup, sklearn, dan env.
   - Siapkan Jupyter Notebook untuk analisis interaktif.

### Langkah 2: Ekstraksi Data
**Sumber Data**:
   - Kumpulkan data dari berbagai sumber seperti CSV, JSON, XML, API, dan database.

**Tools untuk Ekstraksi data**:
   - Unduh file data dari [sumber](https://github.com/yudhaislamisulistya/mini-project-de-alta).
   - Gunakan library Pandas untuk membaca file CSV dan JSON.
   - Gunakan BeautifulSoup untuk parsing data XML.
   - Gunakan requests untuk mendapatkan data dari API.
   - Gunakan sqlite3 atau SQLAlchemy untuk mengakses database.

### Langkah 3: Transformasi Data
**Transformasi Data**:
   - Mengubah Tipe Data (Changing Data Types)
   - Menguraikan Tanggal (Parsing Dates)
   - Menangani Encoding File (Handling File Encodings)
   - Menghapus Outliers (Removing Outliers)
   - Penskalaan Fitur (Scaling Features)
   - Membuat Variabel Dummy (Creating Dummy Variables)
   - Rekayasa Fitur (Engineering Features)

### Langkah 4: Load Data
**Google Cloud Storage atau Google Firebase**:
   - Simpan data yang sudah diproses ke dalam Google Cloud Storage atau Google Firebase untuk backup.

### Langkah 5: Analisis dan Visualisasi Data
**Analisis Data**:
   - Gunakan Pandas untuk analisis data di Jupyter Notebook.

**Visualisasi Data**:
   - Gunakan seaborn dan matplotlib untuk visualisasi data di Jupyter Notebook.
   - Gunakan plotly.express untuk visualisasi interaktif.

### Langkah 6 : Process to Apache Airflow
**Proses**:
   - Buatlah sebuah file DAG di Apache Airflow.
   - Jalankan DAG menggunakan airflow standalone di sistem operasi Linux.
   - Konfigurasikan scheduler di Airflow untuk menjalankan proses ETL secara berkala.

### Kesimpulan
Proyek ini memungkinkan organisasi untuk memahami pola, tren, dan temuan penting dalam data dengan lebih baik melalui proses ETL yang komprehensif dan visualisasi data yang informatif.


# ETL Pipeline and Visualization

## About Project
Project ini memiliki tujuan untuk melakukan ETL (Extract, Transform, Load). Dengan melakukan proses pengekstrakan data dari berbagai sumber kemudian digabungkan menjadi satu dataset. Dataset tersebut dilakukan proses Cleaning dan Tranformasi. Kemudian hasilnya akan diupload ke data warehouse (Cloud Storage dan Database). Setelah itu dialukasn proses Visualisasi Data dari data tersebut untuk mendapatkan insight dari model prediksi biaya total proyek Bank Dunia.

## Tech Stacks
Daftar tools dan framework yang digunakan dalam project ini:
- Python
- Library in Python: Pandas, sqlite3, requests, json, re, seaborn, matplotlib.pyplot, plotly.express, Levenshtein, BeautifulSoup, sklearn, google cloud, sqlalchemy, airflow, openai
- Jupyter Notebook
- Google Cloud Storage
- MySQL
- API World Bank
- XML
- JSON 
- CSV
- DB
- Apache Airflow
- other

## Architecture Diagram
 ![ETL Diagram](https://github.com/rayhanrere008/rayhan-qalby-r-DE-Mini-Project/blob/main/image/ETL_Architecture_Diagram.png?raw=true)

## Setup 
### Langkah 1: Persiapan Lingkungan
Pastikan Anda telah menginstal Tools dan Library yang diperlukan:
- Python
- Pandas (untuk melakukan ETL)
- Matplotlib, Plotly.express, Seaborn (untuk visualisasi)
- Google Cloud dan Sqlalchemy (untuk load to warehouse)
- Others (yang telah disebutkan pada bagian 'Tech Stacks')

### Langkah 2: Ekstraksi Data
1. Unduh file data yang diberikan dari [sumber](https://github.com/yudhaislamisulistya/mini-project-de-alta) yang ditentukan.
2. Simpan file data yang berupa csv, json, db, xml, dll di direktori proyek Anda.
3. Buka lingkungan pengembangan Python (seperti Jupyter Notebook atau IDE Python).
4. Import Library yang diperlukan
5. Buat skrip Python untuk membaca atau ekstraksi file data yang diunduh menggunakan Pandas.

### Langkah 3: Transformasi Data
1. Buat skrip Python untuk melakukan transformasi data sesuai kebutuhan proyek, seperti pembersihan data, penggabungan data, penyesuaian tipe data, Menguraikan Tanggal (Parsing Dates), Menangani Encoding File (Handling File Encodings), Menghapus Outliers (Removing Outliers), Penskalaan Fitur (Scaling Features), Membuat Variabel Dummy (Creating Dummy Variables), Rekayasa Fitur (Engineering Features), dsb.

### Langkah 4: Load Data to Warehouse
1. Buat skrip Python untuk menyimpan data yang telah diolah ke dalam format yang sesuai (misalnya, file CSV).
2. Buat Bucket di Google Cloud Storage (implementasikan IAM dan Service Accountnya)
3. Buat Database di MySQL (misal menggunakan RDBMS : Dbeaver)
4. Buatlah skrip untuk melakukan proses load ke Google Cloud Storage dan Database

### Langkah 5: Visualisasi Data
1. Gunakan Pandas untuk membaca data yang telah diolah
2. Gunakan Matplotlib, Plotly.express, Seaborn  untuk membuat visualisasi data yang relevan berupa analisis statistik deskriptif, analisis korelasi, analisis distribusi, analisis tren, analisis perbandingan, atau analisis lain yang informatif. Diagram bisa berupa diagram batang, diagram lingkaran, atau plot garis.
3. Sertakan judul yang jelas dan label sumbu untuk memperjelas visualisasi.

### Langkah 6 : Implementation AI
1. Buat key openai di Naga AI
2. Masukkan key di file .env
3. Buat script integrasi dengan key dan function prompt AI
4. Masukkan prompt AI tentang analisis tren, distribusi, korelasi, dan perbandingan dari dataset final
5. Menampilkan hasil prompt AI

### Langkah 7 : Apache Airflow
Dalam project ini juga menerapkan proses ETL menggunakan apache airflow namun hanya pada bagian extract population_data from API dan load data final to Google Cloud Storage. Stepnya :
1. Install Apache Airflow
2. Put DAG file to dag folder
3. Jalankan Airflow
4. Cek hasilnya di Airflow UI (localhost:8080)

### Kesimpulan
Dengan mengikuti langkah-langkah di atas, Anda dapat melakukan proyek ETL dan visualisasi data secara lokal menggunakan Python dan tools yang sesuai. Pastikan untuk menyesuaikan langkah-langkah ini sesuai dengan kebutuhan dan karakteristik proyek Anda.

Selamat mengerjakan proyek!!