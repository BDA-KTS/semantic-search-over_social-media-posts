# Semantic Search Over Social Media Posts (Tweets)

## Description
This method allows users to perform a semantic search across a collection of social media posts (e.g., tweets) and retrieve the most relevant posts for a given query. It computes sentence embeddings for the social media posts and the input query, where the most similar posts are extracted using cosine similarity.

## Use Cases
This method is designed to identify social media posts (e.g., tweets) that are semantically similar to a given query. It is particularly useful for tasks such as:

- **Topic Exploration:** Finding posts related to specific topics like *social media*, *gender issues*, or *elections* by comparing the semantic meaning of the query with the content of the posts.
- **Content Filtering:** Extracting posts that match the intent or context of a query, even if the exact keywords are not present in the posts.
- **Trend Analysis:** Analyzing discussions around a theme by retrieving posts that are contextually relevant to a set of predefined queries.

The method uses sentence embeddings to represent both the query and the posts, and ranks the posts based on their cosine similarity to the query. This ensures that the retrieved posts are not just keyword matches but are semantically aligned with the query's meaning.

## Input Data
The input (query) text can be a word, phrase, or sentence. It can also be a social media post for semantic search over the corpus. For multiple queries, update [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt), having each query per line. A single query can be directly provided in the [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb). The input file contains the following query terms. `social media` ,`women`,`election`
 
The data dump for semantic search can be social media posts in JSON format, e.g., [Tweets](https://developer.x.com/en/docs/x-api/data-dictionary/object-model/tweet). We use NLTK sample tweets ([corpora/tweets.20150430-223406.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/corpora/tweets.20150430-223406.json)) for demonstration.

## Output Data 
After running all the scripts in [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb), the results will be saved as a JSON file in [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/output.json) as;

- `Post ID`: The unique identifier of the social media post.  
- `Post Text`: The content of the post.  
- `Similarity Score`: A numerical value (ranging from 0 to 1) indicating how closely the post matches the input query.  

Below are the K=3 most similar posts to the input query (social media, women, and election). Only a few posts similar to a query are shown as examples:

```json
  {
    "social media": [
      {
        "post ID": "13567",
        "post text": "There's something a bit \"dad dancing\" about the way the Tories try to electioneer via social media https://t.co/WH0cmv76VD",
        "sim score": "0.9372139191497816"
      },
      {
        "post ID": "9732",
        "post text": "It's extremely comforting to know that the power of mainstream media has been diluted by social media? #SNP",
        "sim score": "0.9371564729455584"
      },
      {
        "post ID": "18324",
        "post text": "@mmaher70 @RichardJMurphy So why cant they defend the position thats just total incompetence constantly allow Tories to set agenda esp media",
        "sim score": "0.918129503287474"
      }
    ],
  }
```

## Hardware Requirements
The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD).

## Environment Setup

- **Python v3.8** (preferably through Anaconda)
- Using Anaconda:
  
```bash
conda create -n semantic_search python=3.8
conda activate semantic_search
conda install -c conda-forge notebook
pip install -r requirements.txt
```

- Using Python:

```bash
python -m venv semantic_search
cd semantic_search
Scripts\activate
cd ..
pip install -r requirements.txt
```

## How to Use
Start Jupyter Lab or Notebook:

```bash
jupyter lab
```

- Open and execute all cells in [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb).
- Add new queries (one per line) in [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//data/input_queries.txt).
- Update the path to your JSON collection in [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//config.json).
- Results are saved in [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//data/output.json), including post IDs, text, and similarity scores.

## Technical Details

This method performs semantic search by computing embeddings for both queries and social media posts, and ranking posts based on their similarity to the queries. Below is a detailed breakdown of the process:

**Semantic search:**

- *Word Embeddings:* The method uses [FastText embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip) stored in [embeddings/en_embeddings.p](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/embeddings/en_embeddings.p).
- *Text-Level Embeddings:* Word embeddings are aggregated at the document or query level to produce a single embedding vector for each text unit (query or post).
- *Cosine Similarity:* The similarity between the query embeddings and the pre-computed embeddings of the corpus posts is calculated using cosine similarity.
- *Ranking:* Posts are ranked in descending order of similarity scores, and only the `K` results are included in the output.

**Workflow**

1. Load precomputed embeddings for the reference dataset
2. Load the input queries and generate their embeddings
3. Calculate cosine similarities for each query with all posts of the social media posts dataset using cosine similarity
4. Rank posts by similarity and output the `K` most similar results.

![semantic search workflow](semantic-search-design.png)

## Contact Details
For questions or feedback, contact Fakhri Momeni via [fakhri.momeni@gesis.org](mailto:fakhri.momeni@gesis.org).
