[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic_search/HEAD?labpath=lookup_socialmedia_posts.ipynb)

# Semantic search over social media posts (tweets)

## Description
This method performs a semantic search across a collection of social media posts (e.g., tweets) and returns the most similar posts to the provided search query. The method uses a pretrained language model (embeddings) to compute the semantic similarity between the query and posts using cosine similarity, identifying the closest matches. For each query, the method returns the top-K posts, sorted in descending order of similarity.

The method reads search queries from `data/input_queries.txt` (with one query per line) and writes the top-K most similar posts to `data/output.json`. The method loads [Fasttext embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip) from `embeddings/en_embeddings.p` file and computes document embeddings by averaging the embeddings of the tokens in each post.
Users can customize the behavior of the method by specifying their preferences and paths to resources in the `config.json` file. It assists in replicability by allowing to execute the method under different settings e.g., with different posts collection, different value of top-K and with/without cleaning. Furthermore, working environment of the method is preserved in `requirements.txt` file, `random seed variables` are defined and the necessary details to reuse the method are provided in `How to Use`, in this document. *The method takes 1-2mins for 5000 posts on 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz (with 16GB RAM) PC (Windows 10 OS).* 

## Prerequisite
The prerequisites for running this method are `Python v3.8.*` (or ideally, Anaconda to create a virtual environment with the required Python version). Following the `How To Use` section will lead to installing other required packages.

This method requires a collection of social media posts in `JSON` format. Place this collection in the `socialmedia_posts/` folder and update the file path in the config.json.
For the sake of demo, it operates on the NLTK sample tweets placed in `corpora/tweets.20150430-223406.json`.

## Keywords
*Text similarity, Semantic similarity search, text retrieval* 

## Science Usecase(s)
- A social scientist interested in finding relevant tweets about `social media`, `women` and `election`

## Applicability to DBD Datasets
The method is applicable to query social media posts in json format e.g., [Tweets](https://developer.x.com/en/docs/x-api/data-dictionary/object-model/tweet). 

## How to Use
- **Setting up virtual environment**
    - with Anaconda prompt
      -  `conda create -n semantic_search python=3.8`
      -  `conda activate semantic_search`
      -  `pip install -r requirements.txt` 
    - with python v3.8
      - `python -m venv semantic_search`
      - `cd semantic_search`
      - `Scripts\activate`
      - `cd ..`
   - `jupyter lab` 
   - *execute all notebook cells* 
- **Replicability**
   - set path to your social media posts in JSON format through `input_query_filepath`` in `/config.json`
   - Update `/data/input_queries.txt` with new input queries, one per line
   - Toggle `"ifpreprocess": true/false` in `/config.json` to compare results with/without special characters
   - Change the value of `"top-k": 5` for desired number of top similar posts for each query 


### Sample input (Search queries):
The easiest way to change the query is by editing the `/data/input_queries.txt`. Currently, it contains the keywords `Social media`, `women`, `election` to find tweets relevant to these topics in the example dataset.

### Sample output:
After executing all the scripts in `lookup_socialmedia_posts.ipynb`, the output will be written in JSON format located at `/data/output.json`. Each result in the output is a JSON object that includes the post ID, post text, and the similarity score (ranging from 0 to 1). The higher the similarity score, the more relevant the post is to the query.
Below are the top-K most similar posts to the given query (with top-K set to 5 in this example):

```ruby
{"social media": [{"post ID": "13567", "post text": "There's something a bit \"dad dancing\" about the way the Tories try to electioneer via social media https://t.co/WH0cmv76VD", "sim score": "0.9372139191497816"}, {"post ID": "9732", "post text": "It's extremely comforting to know that the power of mainstream media has been diluted by social media? #SNP", "sim score": "0.9371564729455584"}, {"post ID": "18324", "post text": "@mmaher70 @RichardJMurphy So why cant they defend the position thats just total incompetence constantly allow Tories to set agenda esp media", "sim score": "0.918129503287474"}, {"post ID": "13807", "post text": "RT @599tb: UKIP treated very differently by media #AskNigelFarage http://t.co/pLxsraTDTJ", "sim score": "0.9179315218984065"}, {"post ID": "14961", "post text": "RT @599tb: UKIP treated very differently by media #AskNigelFarage http://t.co/pLxsraTDTJ", "sim score": "0.9179315218984065"}],
"women": [{"post ID": "287", "post text": "RT @macplus4: And. Miliband stumbled. Much bigger issues to discuss - NHS, mental health, foodbanks, homelessness, usual cuts to women &amp; ch\u2026", "sim score": "0.9999048991755727"}, {"post ID": "2902", "post text": "Pigs sweat, men perspire  https://t.co/6ZIU37HYPh", "sim score": "0.7674937266310939"}, {"post ID": "4592", "post text": "@NRKesp1 \nD\u00e5 ser det m\u00f8rkt ut for han...\nVerre blir det om det blir sj\u00f8lstyre og for England ?\nTory kan tape men likevel vinne...", "sim score": "0.7657890410727743"}, {"post ID": "1972", "post text": "SNP now entrusts political polls to till girls. #snpout  https://t.co/U4EqIL7MV9", "sim score": "0.6339039759462265"}, {"post ID": "1872", "post text": "@alisonthewliss SNP now entrusts political polls to till girls. #snpout", "sim score": "0.6339039759462265"}],
"election": [{"post ID": "19237", "post text": "#ELECTION2015  https://t.co/WgCyxkkAkc", "sim score": "0.9999999995861624"}, {"post ID": "14156", "post text": "#NigelFarage #UKIP #Election2015 http://t.co/oyr8o5aJCv", "sim score": "0.99999999834465"}, {"post ID": "3134", "post text": "@MarkDiStef Haha this is hilarious &amp; brilliant. Twitter with politicians is so empty. #onmessage #tories #election http://t.co/TloIFHijCU", "sim score": "0.9999999981778775"}, {"post ID": "1399", "post text": "RT @MPH1982: #edmiliband #miliband #therock #election2015 https://t.co/3VxgBE3t4q", "sim score": "0.9999999962754627"}, {"post ID": "979", "post text": "RT @MPH1982: #edmiliband #miliband #therock #election2015 https://t.co/3VxgBE3t4q", "sim score": "0.9999999962754627"}]}
```
## Repo Structure
The repository structure is as follows:
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


## Contact Details
For questions or feedback, contact Fakhri Momeni via Email: fakhri.momeni@gesis.org.






