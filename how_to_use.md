## How to Use

![alt semantic search how to use](semantic-search-how-to-use.png#center)
### Prerequisites
- **Python v3.8** (preferably through Anaconda)
- This method requires a collection of social media posts in `JSON` format. Place the collection in the `corpora/` folder and update the file name in the `config.json` to point to your dataset (e.g., `tweets.20150430-223406.json`). For demonstration purposes, the method uses a sample dataset of NLTK tweets located in `corpora/tweets.20150430-223406.json`.
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
  
### Input and Output Specification (With sample)
#### **Input**
- **User Query:** The easiest way to change the query is by editing the `/data/input_queries.txt`. Currently, it contains the keywords `Social media`, `women`, `election` to find tweets relevant to these topics in the example dataset.

- **Input Dataset:** It is a collection of social media posts in `JSON` format. We use NLTK sample tweets (`corpora/tweets.20150430-223406.json`) for demonstration.

#### **Output**
- **Output:** After executing all the scripts in `lookup_socialmedia_posts.ipynb`, the output will be written in JSON format located at `/data/output.json`. Each result in the output is a JSON object that includes the post ID, post text, and the similarity score (ranging from 0 to 1). The higher the similarity score, the more relevant the post is to the query.
Below are the top-K most similar posts to the given query (with top-K set to 5 in this example):

```json
[
    {
      "Post ID": "1234567890",
      "Post Text": "Social media is transforming how we communicate globally.",
      "Similarity Score": 0.89
    },
    {
      "Post ID": "1234567891",
      "Post Text": "The impact of social media on modern society is undeniable.",
      "Similarity Score": 0.85
    },
    {
      "Post ID": "1234567892",
      "Post Text": "Many platforms now focus on promoting positive social media use.",
      "Similarity Score": 0.82
    },
    {
      "Post ID": "1234567893",
      "Post Text": "Social media helps connect people across the world.",
      "Similarity Score": 0.80
    },
    {
      "Post ID": "1234567894",
      "Post Text": "Discussions on social media often drive public opinion.",
      "Similarity Score": 0.78
    }
  ]
```


---
