# Web-Traffic-Log-Q-A-System-RAG-Based-
Question-answer (Q&amp;A) system using traffic logs generated for a website. The system is designed to accept natural language questions from users, analyze the relevant log data, and provide the most appropriate responses. The core of this system is based on the Retrieval-Augmented Generation (RAG) model.

Project Description
The Web Traffic Log Q&A System analyzes web traffic logs to answer user questions accurately. The system searches preprocessed and vectorized log data based on the questions asked by users, retrieves relevant log entries, and uses them to generate meaningful answers.

Features:
Data Processing: Cleaning, processing, and preparing log files for analysis.
Vectorization: Converting log data into vectors using TF-IDF.
Query Expansion: Expanding the query meaning using WordNet.
Similarity Search: Fast search in the vector database using HNSW (Hierarchical Navigable Small World).
Sorting: Sorting based on the first (oldest) and last (newest) log entries.
Interactive Querying: Command-line interface for direct interaction with the system.
