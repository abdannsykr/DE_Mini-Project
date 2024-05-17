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
![Alt-Text](https://github.com/abdannsykr/DE_Mini-Project/blob/main/Architecture_Diagram.jpg)

## Setup 
Berikut langkah-langkah untuk memproses setiap data:

### Langkah 1: Persiapan Environment
**Instalasi Library dan Tools**:
   - Persiapkan instalasi Python beserta pustaka yang diperlukan seperti Pandas, sqlite3, OpenAI, requests, json, re, seaborn, matplotlib.pyplot, plotly.express, BeautifulSoup, sklearn, dan env.
   - Siapkan Jupyter Notebook untuk analisis interaktif.

### Langkah 2: Ekstraksi Data
**Sumber Data**:
   - Kumpulkan data dari berbagai sumber seperti CSV, JSON, XML, Database(DB), dan API.

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

### Langkah 6 : Proses ke Apache Airflow
**Proses**:
   - Buatlah sebuah file DAG di Apache Airflow.
   - Jalankan DAG menggunakan airflow standalone di sistem operasi Linux.
   - Untuk melihat hasilnya, buka 'localhost:8080' di web browser.

### Kesimpulan
Proyek ini memungkinkan organisasi untuk memahami pola, tren, dan temuan penting dalam data dengan lebih baik melalui proses ETL yang komprehensif dan visualisasi data yang informatif.