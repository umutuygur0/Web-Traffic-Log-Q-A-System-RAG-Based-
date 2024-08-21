import Retrieval


def test_queries():
    queries = {#test soruları ingilizce!:
        "put results": "put results",
        "what is page40": "what is page40",
        "last GET request": "last GET request",
        "all 404 errors": "all 404 errors",
        "first request": "first request",
        "what happened on page12": "what happened on page12",
        "show post requests": "show post requests",
        "last 5 delete operations": "last 5 delete operations"
    }
    
    for query_name, query in queries.items():
        print(f"Test Soru: {query_name}")
        results = Retrieval.retrieve_logs(query, vtest=True)
        print(f"Yanıt:\n{results[['IP Address', 'Timestamp', 'HTTP Method', 'URL', 'Status Code', 'Content Size']]}\n")

if  __name__  == "__main__":
    test_queries()
