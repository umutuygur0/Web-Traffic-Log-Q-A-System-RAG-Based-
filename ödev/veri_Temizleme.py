import pandas as pd
df = pd.read_csv('web_traffic_log.csv')

# düzenleme işlemi
df.columns = df.columns.str.strip()

# kontrol
print(df.columns)

# Geçerli durum kodları
valid_status_codes = [200, 301, 404, 500]

# Veri temizleme işlemleri
df = df[df['Status Code'].isin(valid_status_codes)]

# Temizlenmiş veriyi kaydetme
df.to_csv('cleaned_web_traffic_log.csv', index=False)
