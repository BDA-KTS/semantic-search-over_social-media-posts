# Semantic search over social media posts (tweets)

## Description
The method implements semantic search over a collection of social media posts e.g., tweets, and returns the most similar posts to the search query. It uses a pretrained language model (embeddings) to determine the posts closest to the query text using cosine similarity and returns the ranked results.  

## Keywords
Text similarity, Semantic similarity search, text retrieval 

## Science Usecase(s)
- To a social media post in query, find the most relevant posts i.e., with highest semantic similarity in a dump of posts.   

## Repo Structure
The repository is organized as follows:
- **Folders**:
  - `__pycache__`: Contains cached Python bytecode files.
  - `data`: Stores data used by the method.
  - `tmp2`: Contains additional files and data, including stopwords and the `twitter_samples` dataset.

- **Files**:
  - `Looking up the tweets.ipynb`: The main code implemented as a Jupyter Notebook. It contains four sections covering document embeddings, tweet lookup, similarity computation, and hash table creation..
  - `readme.md`: Guideline document providing instructions for using the method.
  - `utils.py`: Contains essential functions needed for the method's functionality.
  

## Environment Setup
Requires Python and the NLTK library. Install NLTK using:

```
pip install nltk
```


## Input Data
Social media posts e.g., tweets in (https://data.gesis.org/tweetskb/)  

## Sample Input and Output Data
### Input:
Here is a keyword to search in all tweets:
![image](https://github.com/user-attachments/assets/20f30a39-6522-406f-b3d2-a9eb3fe9e040)

### Output:
Here are three most similar tweets to the given tweet:

![image](https://github.com/user-attachments/assets/f2576dd0-f10c-4e2a-9550-36358ceb6c54)


## How to UseTo utilize this tutorial effectively, follow these steps:

1. **Install Python and Necessary Packages**:
   - Ensure that Python is installed on your system. You can download and install Python from the official website (https://www.python.org/).
   - Install Jupyter Notebook, which is a web-based interactive computing environment that allows you to create and share documents containing live code, equations, visualizations, and narrative text. Install it using pip:
     ```
     pip install notebook
     ```

2. **Download the Folder**:
   - Download the provided folder containing the tutorial materials to your local machine. Ensure that you have extracted the contents of the folder if it is in a compressed format (e.g., .zip).

3. **Navigate to the Directory**:
   - Open a command prompt or terminal window and navigate to the directory where you have saved the downloaded folder using the `cd` command. For example:
     ```
     cd path/to/downloaded/folder
     ```

4. **Launch Jupyter Notebook**:
   - Once you are in the directory containing the tutorial materials, start Jupyter Notebook by entering the following command in the command prompt or terminal:
     ```
     jupyter notebook
     ```
   This will open Jupyter Notebook in your default web browser.

5. **Open the Notebook**:
   - In the Jupyter Notebook interface, navigate to the "Looking up the Tweets.ipynb" file and click on it to open the notebook.

6. **Run the Codes**:
   - Run each code cell in the notebook sequentially by selecting the cell and pressing Shift + Enter or using the "Run" button in the Jupyter Notebook interface.

Follow these steps to install Jupyter Notebook, download the tutorial materials, navigate to the directory, open the notebook, and execute the provided code in the Jupyter Notebook environment.


## Contact Details
For questions or feedback, contact Fakhri Momeni via Email: "fakhri.momeni@gesis.org".






