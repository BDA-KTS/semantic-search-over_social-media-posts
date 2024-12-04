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
