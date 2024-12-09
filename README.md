# Semantic Search Over Social Media Posts (Tweets)

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic-search-over_social-media-posts/HEAD?labpath=semantic-search-over_social-media-posts.ipynb)

---
## Description
This method allows users to perform a semantic search across a collection of social media posts (e.g., tweets) and retrieve the most relevant posts for a given query. For example, a social scientist studying public discourse on topics like *social media*, *gender issues*, or *elections* can use this tool to identify posts that share a similar meaning to the input query.

The method reads search queries from `data/input_queries.txt` (with one query per line) and writes the top-K most similar posts to `data/output.json`. It uses [Fasttext embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip) loaded from `embeddings/en_embeddings.p` to get word/token embeddings that are averaged to compute post/document embeddings.

- **[How to Use](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/how_to_use.md):** Detailed instructions for setting up the environment, configuring the method, and running the script.
- **[Reproducibility](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/reproducibility.md):** Information about the actual implementation and reproduction of the method.

### Usecase(s)
The method supports applications like trend analysis and content categorization in user-generated content. It is particularly useful for understanding how a specific topic is discussed across various contexts in social media.


### Keywords
*Text similarity, Semantic similarity search, text retrieval*

## Applicability to DBD Datasets
The method is applicable to query social media posts in json format e.g., [Tweets](https://developer.x.com/en/docs/x-api/data-dictionary/object-model/tweet). 

---



## Contact Details
For questions or feedback, contact Fakhri Momeni via Email: fakhri.momeni@gesis.org.
