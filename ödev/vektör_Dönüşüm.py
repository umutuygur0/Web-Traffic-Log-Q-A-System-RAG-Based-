import tensorflow as tf
from keras_preprocessing.text import  Tokenizer
from keras_preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as  np


df =  pd.read_csv ('cleaned_web_traffic_log.csv')# Temizleme
df['Text'] = df ['IP Address']  + ' ' + df  ['Timestamp'] + ' ' + df  ['HTTP Method'] + ' ' + df['URL'] + ' ' + df['Status Code'].astype(str) + ' ' + df['Content Size'].astype(str)

# Tokenizer - tokenize etme 
tokenizer  =   Tokenizer (num_words   =5000 ,oov_token="<OOV>")
tokenizer.fit_on_texts(df['Text'].tolist())

sequences=  tokenizer.texts_to_sequences(df['Text'].tolist())

# aynı uzunluk - padding uygulama
padded_sequences= pad_sequences(sequences , padding='post')


embeddings =np.array(padded_sequences)# numpy 


np.save ('tensorflow_embeddings.npy' , embeddings)

print(" Metin  verileri başarıyla vektörlere dönüştürüldü ve kaydedildi.")
