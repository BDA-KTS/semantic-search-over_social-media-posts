# Semantic Search Over Social Media Posts (Tweets)
[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic-search-over_social-media-posts/HEAD?labpath=semantic-search-over_social-media-posts.ipynb)

## Description
This method allows users to perform a semantic search across a collection of social media posts (e.g., tweets) and retrieve the most relevant posts for a given query. For example, a social scientist studying public discourse on topics like *social media*, *gender issues*, or *elections* can use this tool to identify posts that share a similar meaning to the input query.

**Reproducibility:** The method reads search queries from [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt) (with one query per line) and writes the top-K most similar posts to [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/output.json). It uses [Fasttext embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip) loaded from [embeddings/en_embeddings.p](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/embeddings/en_embeddings.p) to get word/token embeddings that are averaged to compute post/document embeddings. Users can customize the behavior of the method by specifying their preferences and paths to resources in the [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/config.json) file. It assists in replicability by allowing to execute the method under different settings e.g., with different posts collection, different value of top-K and with/without cleaning. For reproducibility of results across executions, the working environment of the method is preserved in [requirements.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/requirements.txt) file, `random seed variables` are defined and the necessary details to reuse the method are provided in [How to Use](#How-to-Use) section. Update [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/config.json) to adjust parameters like `input_query_filepath`, `top-K`, or preprocessing options (`"ifpreprocess": true/false`). To easily run and explore the method in a pre-configured environment, you can use [Binder](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic-search-over_social-media-posts/HEAD?labpath=semantic-search-over_social-media-posts.ipynb). It allows you to execute the notebook without needing to set up the environment locally. Click the badge below to get started. The following figure explains the working of the method that computes embeddings for words in the corpora posts and the input query, aggregate them at the document level, compute cosine similarity for between each query embedding and corpora posts embeddings and finally restults tne top-K most similar posts from the corpora. 

![alt semantic search design](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-design.png)

## Keywords
*text similarity, semantic similarity search, cosine similarity, text retrieval*

## Use Case(s)
This method supports all use cases that require finding tweets (or other social media posts) for a specific topic, entity, or keyword. For example, one use case explores how users express emotions and build social connections on Twitter. By analyzing tweets for emotional sentiment, interaction patterns, and cultural references, researchers can uncover insights into individual well-being, community dynamics, and cultural identity trends.

## Repo Structure
- The folder [corpora](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/corpora) has the dataset of sample posts to use for semantic search against a user query.
- The folder [data](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data) contain [input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt) having user queries. The output file [output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/output.json) is also generated here.
- The folder [embeddings](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/embeddings) contain the Fasttext embeddings file for English [en_embeddings.p](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/embeddings/en_embeddings.p).
- The notebook [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb) is the main working notebook to execute the method.
- The utility functions used are defined in [utils.py](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/utils.py)
- The file [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/config.json) helps users directly alter the behavior of the method without interacting with the code. 

## Environment Setup
- **Python v3.8** (preferably through Anaconda)
- This method requires a collection of social media posts in `JSON` format. Place the collection in the [corpora/](/corpora) folder and update the file name in the [config.json](config.json) to point to your dataset. For demonstration purposes, the method uses a sample dataset of NLTK tweets located in [corpora/tweets.20150430-223406.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/corpora/tweets.20150430-223406.json).
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
## Hardware Requirements
Average runtime: 1-2 minutes for 5000 posts on an 11th Gen Intel Core i7 processor with 16GB RAM (Windows 10).


## Input Data
- The input (query) text can be a word, phrase or sentence or a social media post, for semantic search over the corpora. For multiple queries update [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt) having each query per line. A single query can be directly provided in the [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb).

## Sample Input and Output Data
- **User Query:** The easiest way to change the query is by editing the [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/input_queries.txt).
  - **Example Query:** The current file contains the following keywords:  
    - `Social Norms`  
    - `Cultural Identity`  
    - `Community Interaction`
 
  These keywords will be used to find tweets relevant to these topics in the dataset.

- **Input Dataset:** It can be social media posts in json format e.g., [Tweets](https://developer.x.com/en/docs/x-api/data-dictionary/object-model/tweet). We use NLTK sample tweets ([corpora/tweets.20150430-223406.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/corpora/tweets.20150430-223406.json)) for demonstration.

- **Output Format:**  
  After running all the scripts in [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb), the results will be saved as a JSON file in the following location:  
  - **File:** [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/data/output.json) 

- **Structure of Output:**  
  Each result in the JSON output file includes the following fields:  
  - `Post ID`: The unique identifier of the social media post.  
  - `Post Text`: The content of the post.  
  - `Similarity Score`: A numerical value (ranging from 0 to 1) indicating how closely the post matches the input query.  

- **Sample Output:**  
Below are the top-K most similar posts to the given query (with top-K set to 5 in this example):

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
## How to Use
![alt semantic search how to use](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-how-to-use.png#center)
- Start Jupyter Lab or Notebook:
```bash
>jupyter lab
```
- Open and execute all cells in [semantic-search-over_social-media-posts.ipynb](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main/semantic-search-over_social-media-posts.ipynb).
- Add new queries (one per line) in [data/input_queries.txt](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//data/input_queries.txt).
- Update the path to your JSON collection in [config.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//config.json).
- Results are saved in [data/output.json](https://github.com/BDA-KTS/semantic-search-over_social-media-posts/blob/main//data/output.json), including post IDs, text, and similarity scores.

## Contact Details
For questions or feedback, contact Fakhri Momeni via [fakhri.momeni@gesis.org](mailto:fakhri.momeni@gesis.org).
