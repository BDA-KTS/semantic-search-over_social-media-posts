# Semantic search over social media posts (tweets)

## Description
The method implements semantic search over a collection of social media posts e.g., tweets, and returns the most similar posts to the search query. It uses a pretrained language model (embeddings) to determine the posts closest to the query text using cosine similarity. Top-K posts arranged in descending order of similarity are produced for each query.

The method reads search queries from `data/input_queries.txt` having each query per line as input and writes output in `data/output.json` file having top-K posts. The method loads [Fasttext embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip) from `embeddings/en_embeddings.p` file and computes doc-embeddings as the average of its token embeddings.
The users can easily customize the behavior of the method by providing their preferences and paths to resources in the `config.json`. It assists in replicability by allowing to execute the method under different settings e.g., with different posts collection, different value of top-K and with/without cleaning. Furthermore, working environment of the method is preserved in `requirements.txt` file, `random seed variables` are defined and the necessary details to reuse the method are provided in this document. *The method takes 1-2mins for 5000 posts on 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz (with 16GB RAM) PC (Windows 10 OS).* 

## Prerequisite
The pre-requisites for this method are `Python v3.8.*` or ideally Anaconda (to create virtual environments with required python version) installed on the system. Following the `How To Use` section will lead to installing other required packages.

This method requires social media posts collection in `JSON` format to be placed in the `socialmedia_posts/` folder and its path updated in the `config.json` file. For the sake of demo, it operates on the NLTK sample tweets placed in `corpora/tweets.20150430-223406.json`.

## Keywords
*Text similarity, Semantic similarity search, text retrieval* 

## Science Usecase(s)
- A social scientist interested in finding relevant tweets about `social media`, `women` and `election`

## Applicability to DBD Datasets
The method is applicable to query social media posts in json format e.g., tweets. 

## 1. How to Use (For the use case example)
- **Setting up virtual environment**
    - Create isolated virtual environment to execute the method
    - Using Conda `conda create -n <venv-name> python=3.8` *or*
    - Using python `python -m venv <venv-name>`
    - Install all required packages freezed into the requirements.txt file using command `pip install -r requirements.txt` 
- **Executing method**
    - Provide specific configurations and file paths in the `config.json` file
    - Open jupyter lab to execute the method notebook i.e., `lookup_socialmedia_posts.ipynb` with command `jupyter lab`
    - Execute the notebook cells (some internal utility functions are called from `utils.py`)


### 2. Sample input (Search queries):
You can enter the queries you want to search within the posts, with one query per line, in the file located at `/data/input_queries.txt`, such as:
`social media` \
`women` \
`election`


### 3. Sample output:
After executing all the scripts in `lookup_socialmedia_posts.ipynb`, the output will be written in JSON format located at `/data/output.json`. Below are the top-K most similar posts to the given query (with top-K set to 5 in this example):

```ruby
{
'social media': [
        {
            'post ID': "13567",
            'post text': "There's something a bit \"dad dancing\" about the way the Tories try to electioneer via social media https://t.co/WH0cmv76VD",
            'sim score': "0.9372139191497816" 
        }
        {
            'post ID': "9732",
            'post text': "It's extremely comforting to know that the power of mainstream media has been diluted by social media? #SNP",
            'sim score': "0.9371564729455584" 
        }
        {
            'post ID': "18324",
            'post text': "@mmaher70 @RichardJMurphy So why cant they defend the position thats just total incompetence constantly allow Tories to set agenda esp media",
            'sim score': "0.918129503287474" 
        }
        {
            'post ID': "13807",
            'post text': "RT @599tb: UKIP treated very differently by media #AskNigelFarage http://t.co/pLxsraTDTJ",
            'sim score': "0.9179315218984065" 
        }
        {
            'post ID': "14961",
            'post text': "RT @599tb: UKIP treated very differently by media #AskNigelFarage http://t.co/pLxsraTDTJ",
            'sim score': "0.9179315218984065" 
        }
    ]
...
}
```
## Repo Structure
The repository is organized as follows:
- **Folders**:
  - `data`: Contains the input file `input_queries.txt`. The output file `output.json` is also created here
  - `embeddings`: Contains the English embeddings file from Fasttext `en_embeddings.p`
  - `corpora` Contains the collection of social media posts in `JSON` format

- **Code files**:
  - `lookup_socialmedia_posts.ipynb`: The main code implemented as a Jupyter Notebook. It contains four sections covering document embeddings, tweet lookup, similarity computation, and hash table creation..
  - `utils.py`: Contains essential functions needed for the method's functionality.
    
- **Open science/Reproducibility files**
  - `LICENSE.txt` Apache 2.0 license allowing commercial/non-commercial reuse of the resources developed and their modified versions
  - `config.json` The files helps executing the method under different settings to help replication by altering the behavior of the method with ease i.e., without directly interacting with the code
  - `requirements.txt` The working environment including the software packages used with their specific versions are preserved in this file and can recreate the experimental setup with a single command (more details in `How to Use` section)
  -  `postBuild` file supports competibility with the execution environment to interactively execute and/or modify the method
  -  `CITATION.cff` file provides information on how this resource can be cited

methods_hub/
│
├── data/
│   ├── input_queries.txt
│   ├── output.json
│
├── embeddings/
│   ├── en_embeddings.p
│
├── corpora/
│   ├── tweets.20150430-223406.json
│
├── utils.py
├── lookup_socialmedia_posts.ipynb
├── config.json
├── requirements.txt
├── LICENSE.txt
├── CITATION.cff
└── postBuild


## Contact Details
For questions or feedback, contact Fakhri Momeni via Email: fakhri.momeni@gesis.org.






