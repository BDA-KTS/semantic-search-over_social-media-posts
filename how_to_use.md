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
  
### Sample Inputs and Outputs
- **User Query:** The easiest way to change the query is by editing the `/data/input_queries.txt`. Currently, it contains the keywords `Social media`, `women`, `election` to find tweets relevant to these topics in the example dataset.

- **Input Dataset:** 

- **Output format:** After executing all the scripts in `lookup_socialmedia_posts.ipynb`, the output will be written in JSON format located at `/data/output.json`. Each result in the output is a JSON object that includes the post ID, post text, and the similarity score (ranging from 0 to 1). The higher the similarity score, the more relevant the post is to the query.
Below are the top-K most similar posts to the given query (with top-K set to 5 in this example):

```json
{"social media": [{"post ID": "13567", "post text": "There's something a bit \"dad dancing\" about the way the Tories try to electioneer via social media https://t.co/WH0cmv76VD", "sim score": "0.9372139191497816"}, {"post ID": "9732", "post text": "It's extremely comforting to know that the power of mainstream media has been diluted by social media? #SNP", "sim score": "0.9371564729455584"}, {"post ID": "18324", "post text": "@mmaher70 @RichardJMurphy So why cant they defend the position thats just total incompetence constantly allow Tories to set agenda esp media", "sim score": "0.918129503287474"}, {"post ID": "13807", "post text": "RT @599tb: UKIP treated very differently by media #AskNigelFarage http://t.co/pLxsraTDTJ", "sim score": "0.9179315218984065"}, {"post ID": "14961", "post text": "RT @599tb: UKIP treated very differently by media #AskNigelFarage http://t.co/pLxsraTDTJ", "sim score": "0.9179315218984065"}],
"women": [{"post ID": "287", "post text": "RT @macplus4: And. Miliband stumbled. Much bigger issues to discuss - NHS, mental health, foodbanks, homelessness, usual cuts to women &amp; ch\u2026", "sim score": "0.9999048991755727"}, {"post ID": "2902", "post text": "Pigs sweat, men perspire  https://t.co/6ZIU37HYPh", "sim score": "0.7674937266310939"}, {"post ID": "4592", "post text": "@NRKesp1 \nD\u00e5 ser det m\u00f8rkt ut for han...\nVerre blir det om det blir sj\u00f8lstyre og for England ?\nTory kan tape men likevel vinne...", "sim score": "0.7657890410727743"}, {"post ID": "1972", "post text": "SNP now entrusts political polls to till girls. #snpout  https://t.co/U4EqIL7MV9", "sim score": "0.6339039759462265"}, {"post ID": "1872", "post text": "@alisonthewliss SNP now entrusts political polls to till girls. #snpout", "sim score": "0.6339039759462265"}],
"election": [{"post ID": "19237", "post text": "#ELECTION2015  https://t.co/WgCyxkkAkc", "sim score": "0.9999999995861624"}, {"post ID": "14156", "post text": "#NigelFarage #UKIP #Election2015 http://t.co/oyr8o5aJCv", "sim score": "0.99999999834465"}, {"post ID": "3134", "post text": "@MarkDiStef Haha this is hilarious &amp; brilliant. Twitter with politicians is so empty. #onmessage #tories #election http://t.co/TloIFHijCU", "sim score": "0.9999999981778775"}, {"post ID": "1399", "post text": "RT @MPH1982: #edmiliband #miliband #therock #election2015 https://t.co/3VxgBE3t4q", "sim score": "0.9999999962754627"}, {"post ID": "979", "post text": "RT @MPH1982: #edmiliband #miliband #therock #election2015 https://t.co/3VxgBE3t4q", "sim score": "0.9999999962754627"}]}
```

### Sample Dataset
- Uses NLTK sample tweets (`corpora/tweets.20150430-223406.json`) for demonstration.

---
