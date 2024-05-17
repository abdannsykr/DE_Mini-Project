import pandas as pd
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.utils.dates import days_ago

# Define function to extract data from API
def extract_population_data():
    try:
        url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=30000"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()[1]  # Memilih bagian data dari JSON
            data_world_bank = pd.DataFrame(data)
            columns = ['country.value', 'countryiso3code', 'indicator.id', 'indicator.value', 'date', 'value']
            data_world_bank = pd.json_normalize(data)[columns]
            data_world_bank.columns = ['Country Name', 'Country Code', 'Indicator Code', 'Indicator Name', 'Year', 'Population']
            print("Data berhasil diambil dari API.")
            return data_world_bank
        else:
            print("Error:", response.status_code)
            return None
    except Exception as e:
        print("Terjadi kesalahan:", str(e))
        return None
    
# Define default arguments for the DAG
default_args = {
    'owner': 'abdan',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 17),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

# Define DAG parameters
dag = DAG(
    'load_data_API_from_airflow',
    default_args=default_args,
    description='This DAG is responsible for fetching data from an API using Airflow',
    schedule_interval='@daily',
)

# Define task to extract data from API
ekstrak_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

# Set task dependencies
ekstrak_data_task
