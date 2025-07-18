# Semantic Search Over Social Media Posts (Tweets)

## Description
This method allows users to perform a semantic search across a collection of social media posts (e.g., tweets) and retrieve the most relevant posts for a given query. It computes sentence embeddings for the social media posts and the input query, where the most similar posts are extracted using cosine similarity.

## Use Cases
Searching a discourse for topics of interest like *social media*, *gender issues*, or *elections* using this method to identify posts with semantic similarity to the input query.

## Input Data
The input (query) text can be a word, phrase, or sentence. It can also be a social media post for semantic search over the corpus. For multiple queries, update [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt), having each query per line. A single query can be directly provided in the [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb). The input file contains the following query terms.

- `social media`  
- `women`
- `election`
 
The data dump for semantic search can be social media posts in JSON format, e.g., [Tweets](https://developer.x.com/en/docs/x-api/data-dictionary/object-model/tweet). We use NLTK sample tweets ([corpora/tweets.20150430-223406.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/corpora/tweets.20150430-223406.json)) for demonstration.

## Output Data 
After running all the scripts in [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb), the results will be saved as a JSON file in [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/output.json) as;

- `Post ID`: The unique identifier of the social media post.  
- `Post Text`: The content of the post.  
- `Similarity Score`: A numerical value (ranging from 0 to 1) indicating how closely the post matches the input query.  

Below are the top-K (with K=5) most similar posts to the input query (social media, women, and election). Only a few posts similar to a query are shown as examples:

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
    "women": [
      {
        "post ID": "287",
        "post text": "RT @macplus4: And. Miliband stumbled. Much bigger issues to discuss - NHS, mental health, foodbanks, homelessness, usual cuts to women &amp; ch…",
        "sim score": "0.9999048991755727"
      },
      {
        "post ID": "2902",
        "post text": "Pigs sweat, men perspire https://t.co/6ZIU37HYPh",
        "sim score": "0.7674937266310939"
      }
    ],
    "election": [
      {
        "post ID": "19237",
        "post text": "#ELECTION2015 https://t.co/WgCyxkkAkc",
        "sim score": "0.9999999995861624"
      },
      {
        "post ID": "14156",
        "post text": "#NigelFarage #UKIP #Election2015 http://t.co/oyr8o5aJCv",
        "sim score": "0.99999999834465"
      }
    ]
  }
```

## Hardware Requirements
The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD).

## Environment Setup

- **Python v3.8** (preferably through Anaconda)
- Using Anaconda:
  
```bash
>conda create -n semantic_search python=3.8
>conda activate semantic_search
>conda install -c conda-forge notebook
>pip install -r requirements.txt
```
- Using Python:
```bash
>python -m venv semantic_search
>cd semantic_search
>Scripts\activate
>cd ..
>pip install -r requirements.txt
```

## How to Use
- Start Jupyter Lab or Notebook:
```bash
>jupyter lab
```

- Open and execute all cells in [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb).
- Add new queries (one per line) in [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//data/input_queries.txt).
- Update the path to your JSON collection in [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//config.json).
- Results are saved in [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//data/output.json), including post IDs, text, and similarity scores.

## Technical Details
The method reads search queries from [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt) (with one query per line) and searches the top-K most similar posts to to each query, written in output file [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/output.json). The method computes word embeddings using [Fasttext embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip) from [embeddings/en_embeddings.p](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/embeddings/en_embeddings.p) for each word, aggregated at the document or query level to get a single embeddings vector per text unit. The most similar posts are determined by computing cosine similarity between the embeddings of the query and corpus posts.

The method loads configuration settings from the file [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/config.json), which can be used to alter the behavior of the method under different settings. Its workflow is explained in the following figure, where the embeddings of the corpus are pre-computed. The query embeddings and their cosine similarity are computed at the time of execution. The posts are arranged in decreasing order of their similarity scores to the query, and only the  top-K are presented as output.

![semantic search workflow](semantic-search-design.png)

## Contact Details
For questions or feedback, contact Fakhri Momeni via [fakhri.momeni@gesis.org](mailto:fakhri.momeni@gesis.org).
