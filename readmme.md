# Semantic Search Over Social Media Posts (Tweets)
[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic-search-over_social-media-posts/HEAD?labpath=semantic-search-over_social-media-posts.ipynb)

## Description
This method allows users to perform a semantic search across a collection of social media posts (e.g., tweets) and retrieve the most relevant posts for a given query. For example, a social scientist studying public discourse on topics like *social media*, *gender issues*, or *elections* can use this tool to identify posts that share a similar meaning to the input query.

**Reproducibility:** The method reads search queries from [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt) (with one query per line) and writes the top-K most similar posts to [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/output.json). It uses [Fasttext embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip) loaded from [embeddings/en_embeddings.p](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/embeddings/en_embeddings.p) to get word/token embeddings that are averaged to compute post/document embeddings. Users can customize the behavior of the method by specifying their preferences and paths to resources in the [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/config.json) file. It assists in replicability by allowing to execute the method under different settings e.g., with different posts collection, different value of top-K and with/without cleaning. For reproducibility of results across executions, the working environment of the method is preserved in [requirements.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/requirements.txt) file, `random seed variables` are defined and the necessary details to reuse the method are provided in [How to Use](#How-to-Use) section. Update [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/config.json) to adjust parameters like `input_query_filepath`, `top-K`, or preprocessing options (`"ifpreprocess": true/false`). To easily run and explore the method in a pre-configured environment, you can use [Binder](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic-search-over_social-media-posts/HEAD?labpath=semantic-search-over_social-media-posts.ipynb). It allows you to execute the notebook without needing to set up the environment locally. Click the badge below to get started. The following figure explains the working of the method that computes embeddings for words in the corpora posts and the input query, aggregate them at the document level, compute cosine similarity for between each query embedding and corpora posts embeddings and finally restults tne top-K most similar posts from the corpora. 

![alt semantic search design](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-design.png)

## Keywords
*text similarity, semantic similarity search, cosine similarity, text retrieval*

## Science Usecase(s)
This method supports all use cases that require finding tweets (or other social media posts) for a specific topic, entity, or keyword. For example, one use case explores how users express emotions and build social connections on Twitter. By analyzing tweets for emotional sentiment, interaction patterns, and cultural references, researchers can uncover insights into individual well-being, community dynamics, and cultural identity trends.

## Repo Structure
- [corpora](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/corpora) has the dataset of sample posts to use for semantic search against a user query.
- [data](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data) contain [input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt) having user queries. The output file [output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/output.json) is also generated here.
- [embeddings](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/embeddings) contain the Fasttext embeddings file for English [en_embeddings.p](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/embeddings/en_embeddings.p).
- The notebook [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb) is the main working notebook to execute the method.
- The utility functions used are defined in [utils.py](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/utils.py)
- [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/config.json) file helps users directly alter the behavior of the method without interacting with the code. 

...

## Contact Details
For questions or feedback, contact Fakhri Momeni via [fakhri.momeni@gesis.org](mailto:fakhri.momeni@gesis.org).
