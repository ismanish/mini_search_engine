Building a Mini Search Engine: From Retrieval to Evaluation
Introduction
In this repository, we build a miniature text retrieval system using the classic Cranfield collection. We walk through the entire process, from loading and preprocessing data to evaluating our search engine's performance. Key concepts include inverted indexing, document ranking, and various evaluation metrics.

Key Components
Data Loading and Preprocessing
We load and preprocess the Cranfield collection, which contains 1,000 short documents from the aerodynamics field and 225 queries with corresponding relevance judgments.

Inverted Index
An inverted index is a fundamental data structure in information retrieval systems. It maps terms to the documents that contain them, allowing efficient full-text searches.

Document Ranking
We rank documents based on term frequencies and other metrics to determine their relevance to a given query.

Evaluation Metrics
We use several metrics to evaluate the performance of our retrieval system, including:

Precision and Recall
Average Precision (AP) and Mean Average Precision (MAP)
Normalized Discounted Cumulative Gain (NDCG)


#### Please use download.py file to download Cranfield data from a public GitHub repository:
