import random
import csv
from datetime import datetime , timedelta

# IP Adresi 
def generate_ip():
    return '.'.join ([str(random.randint(0, 255)) for _ in range(4)])

# Tarih ve Zaman 
def generate_timestamp(start_date, end_date):
    start_timestamp =datetime.timestamp(start_date)
    end_timestamp  = datetime.timestamp(end_date)
    random_timestamp= random.uniform(start_timestamp, end_timestamp)
    return datetime.fromtimestamp(random_timestamp).strftime('%Y-%m-%d %H:%M:%S')

# HTTP ve URL'ler
def generate_http_method():
    return  random.choice(['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

def generate_url():
    return f"/page{random.randint(1, 1000)}"

# HTTP Durum Kodları ve Aktarım Boyutları
def generate_status_code():
    return  random.choice([200, 301, 404, 500])

def generate_content_size():
    return random.randint(100, 10000)  # bytes

# Dosyaya Yazma
def create_log_file(file_name, num_entries):
    with  open (file_name, mode='w', newline='') as file:
        writer= csv.writer(file)
        writer.writerow(['IP Address', '     Timestamp', '   HTTP Method', '     URL', '     Status Code', '    Content Size'])
        
        start_date =  datetime (2024, 1, 1)
        end_date= datetime(2024, 12, 31)
        
        for _ in range(num_entries):
            writer.writerow ([
                f"{generate_ip()}   ",  
                f"{generate_timestamp(start_date, end_date)}    ",  
                f"{generate_http_method()}  ",  
                f"{generate_url()}  ",  
                f"{generate_status_code()}  ",  
                f"{generate_content_size()} "   
            ])
   
# data yaratma
create_log_file  ('web_traffic_log.csv', 1001)
