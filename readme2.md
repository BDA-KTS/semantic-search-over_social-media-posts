# Semantic Search Over Social Media Posts (Tweets)

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic-search-over_social-media-posts/HEAD?labpath=semantic-search-over_social-media-posts.ipynb)

## Table of Contents
- [Description](#description)
- [How to Use](#how-to-use)
- [Reproducibility](#reproducibility)

---
## Description
This method allows users to perform a semantic search across a collection of social media posts (e.g., tweets) and retrieve the most relevant posts for a given query. For example, a social scientist studying public discourse on topics like *social media*, *gender issues*, or *elections* can use this tool to identify posts that share a similar meaning to the input query.
### Usecase(s)
The method supports applications like trend analysis and content categorization in user-generated content. It is particularly useful for understanding how a specific topic is discussed across various contexts in social media.

### Keywords
*Text similarity, Semantic similarity search, text retrieval*

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

### Applicable Dataset
- Uses NLTK sample tweets (`corpora/tweets.20150430-223406.json`) for demonstration.

### Interactive Environment:  
-To make it easier to reproduce the results, you can run this method in an interactive pre-configured environment using Binder. Click the badge below to get started:  

   [![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/BDA-KTS/semantic-search-over_social-media-posts/HEAD?labpath=semantic-search-over_social-media-posts.ipynb)

   ![alt semantic search design](semantic-search-design.png)

### Hardware Details
- Average runtime: 1-2 minutes for 5000 posts on an 11th Gen Intel Core i7 processor with 16GB RAM (Windows 10).

---

## Contact Details
For questions or feedback, contact Fakhri Momeni via Email: fakhri.momeni@gesis.org.
