import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import hnswlib
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import  WordNetLemmatizer



# data yükle
df =  pd.read_csv('cleaned_web_traffic_log.csv')
df['Text'] = df['IP Address'] + ' ' + df['Timestamp'] + ' ' + df['HTTP Method'] + ' ' + df['URL'] + ' ' + df['Status Code'].astype(str) + ' ' + df['Content Size'].astype(str)

lemmatizer= WordNetLemmatizer()       # Initialization
stop_words= list(stopwords.words('english'))

def expand_query(query):
    expanded_terms = set ()
    for word in query.split():
        word= word.lower ()
        if word not in stop_words:
            expanded_terms.add (word)
            for syn  in wn.synsets(word):
                for lemma in syn.lemmas():
                    expanded_word= lemmatizer.lemmatize(lemma.name())
                    if expanded_word  not in stop_words:
                        expanded_terms.add (expanded_word)
    return ' '.join(expanded_terms)

vectorizer= TfidfVectorizer(stop_words=stop_words)     # TF-IDF 
log_vectors= vectorizer.fit_transform(df['Text']).toarray()

num_elements , dim = log_vectors.shape       # HNSW , k-NN için
p = hnswlib.Index (space='cosine', dim=dim)
p.init_index(max_elements=num_elements, ef_construction=200, M=16)
p.add_items(log_vectors)
p.set_ef(500)

def retrieve_logs (query, top_n=5, vtest=False):
    expanded_query= expand_query(query)
    query_vector  = vectorizer.transform([expanded_query]).toarray()
    
    # tümünü arama
    labels , distances = p.knn_query(query_vector, k=num_elements)
    relevant_logs  = df.iloc[labels[0]]
    
    # gerksizleri eleme
    threshold =0.9
    relevant_logs  = relevant_logs[distances[0] < threshold]
    
    #sadece testler için aç
    #if vtest:
    #    print(f"Expanded Query: {expanded_query}")
    #    print(f"Query Vector: {query_vector}")
    #    print(f"Distances: {distances}")
    
    result_count =len(relevant_logs)
    print(f"I found {result_count} relevant logs. Displaying {min(result_count, top_n)} sample outputs:")
    
    # zaman adımı
    if  "first"  in   query.lower():
        relevant_logs=  relevant_logs.sort_values (by="Timestamp", ascending=True)
    elif "last" in query.lower():
        relevant_logs  = relevant_logs.sort_values(by="Timestamp", ascending=False)
    
    
    return relevant_logs.head ( top_n)

# interaktif soru
if __name__==  "__main__":
    while True:
        query =  input ("Sorunuzu girin(çıkmak için 'q' tuşuna basın): ")
        if  query.lower()==  'q':
            break
        results=  retrieve_logs(query)
        print ("Yanıt:\n", results[ ['IP Address', 'Timestamp', 'HTTP Method', 'URL', 'Status Code', 'Content Size']], "\n")
