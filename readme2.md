# Semantic Search Over Social Media Posts (Tweets)

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic-search-over_social-media-posts/HEAD?labpath=semantic-search-over_social-media-posts.ipynb)

---

## Description
This method performs a semantic search across a collection of social media posts (e.g., tweets) and returns the most similar posts to the provided search query. It leverages a pretrained language model to compute semantic similarity between the query and posts using cosine similarity, returning the top-K matches sorted by similarity.

The method reads search queries from `data/input_queries.txt` (one query per line) and writes the results to `data/output.json`. It uses [FastText embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip) for word/token embeddings, which are averaged to compute post/document embeddings.

Social scientists can use this tool to find semantically similar posts for queries related to topics like social media, women, or elections. The method allows customization via a `config.json` file to adjust parameters such as the input dataset, the number of results (`top-K`), and preprocessing options (e.g., cleaning).

---

## How to Use

### Prerequisites
- **Python v3.8** (preferably through Anaconda)
- A collection of social media posts in JSON format placed in the `socialmedia_posts/` folder. (For demonstration, NLTK sample tweets are included in `corpora/tweets.20150430-223406.json`.)

### Steps to Execute
1. **Set up a Virtual Environment**
   - Using Anaconda:
     ```bash
     conda create -n semantic_search python=3.8
     conda activate semantic_search
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

2. **Run Jupyter Notebook**
   - Start Jupyter Lab or Notebook:
     ```bash
     jupyter lab
     ```
   - Open and execute all cells in `lookup_socialmedia_posts.ipynb`.

3. **Update Inputs**
   - Add new queries (one per line) in `data/input_queries.txt`.
   - Update the path to your JSON collection in `config.json`.

4. **View Outputs**
   - Results are saved in `data/output.json`, including post IDs, text, and similarity scores.

---

## Reproducibility

### Configuration Settings
- Update `config.json` to adjust parameters like `input_query_filepath`, `top-K`, or preprocessing options (`"ifpreprocess": true/false`).

### Random Seed Control
- The method includes predefined random seeds to ensure reproducibility of results across executions.

### Requirements and Environment
- The environment details are provided in `requirements.txt`. Running the `pip install` command ensures all necessary packages are installed.

### Sample Inputs and Outputs
- **Input queries:** Located in `data/input_queries.txt`.
- **Output format:** Saved as `data/output.json`, showing top-K similar posts with their similarity scores.

### Demo Dataset
- Uses NLTK sample tweets (`corpora/tweets.20150430-223406.json`) for demonstration.

### Hardware Details
- Average runtime: 1-2 minutes for 5000 posts on an 11th Gen Intel Core i7 processor with 16GB RAM (Windows 10).

---

## Contact Details
For questions or feedback, contact xx at **x.xx@x.x**.
