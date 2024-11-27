# Semantic search over social media posts (tweets)

## Description
The method implements semantic search over a collection of social media posts e.g., tweets, and returns the most similar posts to the search query. It uses a pretrained language model (embeddings) to determine the posts closest to the query text using cosine similarity and returns the most relevant posts to the search query.  

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


## Applicable Datasets
The method is designed to work with textual datasets from various sources. Examples include social media platforms, such as:

Tweets Dataset: Collections of Twitter posts in formats like JSON or CSV, containing text.
Telegram Messages Dataset: Text data extracted from public or private Telegram channels and groups, typically available in JSON format or other exportable structures.
These datasets must contain structured text fields to facilitate processing and analysis by the method.

## How to Use
Follow these steps to install Jupyter Notebook, download the tutorial materials, navigate to the directory, open the notebook, and execute the provided code in the Jupyter Notebook environment:

1. **Install Python and Necessary Packages**:
   - Ensure that Python is installed on your system. You can download and install Python from the official website (https://www.python.org/).
   - Install the necessary packages:
     ```
     pip install -r requirements.txt 
     ```
     

2. **Download the Folder**:
   - Download the provided folder containing the tutorial materials to your local machine. Ensure that you have extracted the contents of the folder if it is in a compressed format (e.g., .zip).

3. **Navigate to the Directory**:
   - Open a command prompt or terminal window and navigate to the directory where you have saved the downloaded folder using the `cd` command. For example:
     ```
     cd path/to/downloaded/folder
     ```

4. **Launch Jupyter Notebook**:
   - Once you are in the directory, start Jupyter Notebook.
   This will open Jupyter Notebook in your default web browser.


5. **Run the Codes**:
   - In the Jupyter Notebook interface, navigate to the "Looking up the Tweets.ipynb" file and click on it to open the notebook.
     Run each code cell in the notebook sequentially by selecting the cell and pressing Shift + Enter or using the "Run" button in the Jupyter Notebook interface.


## Sample Input and Output Data
### Input:
Here is a keyword to search in all tweets:
![image](https://github.com/user-attachments/assets/20f30a39-6522-406f-b3d2-a9eb3fe9e040)

### Output:
Here are three most similar tweets to the given tweet:

![image](https://github.com/user-attachments/assets/79c608f4-ab49-4215-b5fe-b68205e424aa)




## Contact Details
For questions or feedback, contact Fakhri Momeni via Email: "fakhri.momeni@gesis.org".






