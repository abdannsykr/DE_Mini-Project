# ETL (Extract, Transform, Load) and Visualization

## About Project
Tentang proyek ETL dengan visualisasi data dan analisis: Proyek ini bertujuan untuk menjalankan proses ETL (Extract, Transform, Load) pada berbagai sumber data guna menyusun satu tabel yang bersih dan konsisten. Ini menjadi bagian penting dalam pembangunan model prediksi biaya total proyek Bank Dunia, Populasi, Populasi Pedesaan, GDP, GDP Per Capita, Akses Listrik. Langkah pertama adalah mengekstrak data dari file CSV, JSON, XML, basis data, dan API World Bank. Kemudian, dilakukan proses transformasi data termasuk penggabungan, pembersihan, penyesuaian tipe data, imputasi data yang hilang, penghapusan duplikasi, pembuatan variabel dummy, penggantian nilai, penghapusan outliers, penskalaan fitur, dan rekayasa fitur. Setelah transformasi selesai, data dimuat ke dalam basis data atau penyimpanan cloud. Selain itu, proyek juga melibatkan visualisasi data dan analisis statistik untuk memahami karakteristik dan tren dalam dataset yang digunakan. Penggunaan alat dan teknologi seperti Python, Pandas, Numpy, Matplotlib, Seaborn, Plotly, serta layanan seperti Google Cloud Storage atau Google Firebase, SQLite, dan API World Bank sangat mendukung terlaksananya proyek ini. Dengan proses ETL ini, data disusun, diubah, dan disajikan secara visual melalui grafik, diagram, dan dashboard interaktif, memungkinkan organisasi untuk memahami pola, tren, dan temuan penting dalam data dengan lebih baik.

## Tech Stacks
Tools dan framework yang digunakan dalam project ini:
- Python
- Library Python: Pandas, sqlite3, string, OpenAI, requests, json, re, seaborn, matplotlib.pyplot, plotly.express, BeautifulSoup, sklearn, SQLite3, env.
- Jupyter Notebook
- Google Cloud Storage atau Google Firebase
- Google BigQuery
- GitHub
- MySQL
- API World Bank
- XML
- JSON 
- CSV
- DB

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

### Kesimpulan
Proyek ini memungkinkan organisasi untuk memahami pola, tren, dan temuan penting dalam data dengan lebih baik melalui proses ETL yang komprehensif dan visualisasi data yang informatif.