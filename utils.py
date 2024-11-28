from pathlib import Path
import nltk
import re
import string
from nltk.corpus import stopwords, twitter_samples
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import json
from nltk.tokenize import TweetTokenizer
import numpy as np
parent_dir = Path.cwd()

#This function loads the query inputs and the social media posts dump into query and posts files and return it
def read_configurations(config_path = "/config.json"):
    config_path = str(parent_dir) + config_path
    with open(config_path) as file:
        configurations = json.load(file)
    file.close()
    return configurations

def load_data(queries_path, posts_path):
    #read input queries
    file = open(str(parent_dir)+queries_path)
    queries = file.read().split('\n')
    file.close()

    #read posts
    posts = twitter_samples.strings(str(parent_dir)+posts_path) #samples tweets from NLTK
    return queries, posts

def write_output(output_filepath, query_posts_similarities):
    output_filepath = str(parent_dir) + output_filepath
    with open(output_filepath, 'w') as outputfile:
        outputfile.write(query_posts_similarities)
    outputfile.close()

# clean social media posts by removing stopwords, stock market stickers, hyperlinks, hashtags and other unwanted character patterns
# then tokenize and stem (using porter stemmer) clean posts
def clean_posts(posts):
    '''
    Input:
        tweet: a string containing a tweet
    Output:
        tweets_clean: a list of words containing the processed tweet

    '''
        
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    clean_posts = []
    for post in posts:
        # remove stock market tickers like $GE
        post = re.sub(r'\$\w*', '', post)
        # remove old style retweet text "RT"
        post = re.sub(r'^RT[\s]+', '', post)
        # remove hyperlinks
        post = re.sub(r'https?:\/\/.*[\r\n]*', '', post)
        # remove hashtags
        # only removing the hash # sign from the word
        post = re.sub(r'#', '', post)
        clean_posts.append(post)
    return clean_posts
        
# tokenize and stem posts
def tokenize_posts(posts):
    # defining tokenizer using tweets tokenizer
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    all_posts_tokenized = []
    for post in posts:
        post_tokens = tokenizer.tokenize(post)
        all_posts_tokenized.append(post_tokens)
    return all_posts_tokenized

#compute cosine similarity between two posts
def cosine_similarity(query, doc):
    '''
    Input:
        query: embedded vector of the query term(s)
        doc: embedded vector of a social media post as a doc
    Output:
        cos: cosine similarity score between query and doc
    '''
    # you have to set this variable to the true label.
    cos = -10    
    dot = np.dot(query, doc)
    normb = np.linalg.norm(doc)
    
    if len(query.shape) == 1: # confirming query is a 1D vector
        norma = np.linalg.norm(query)
        cos = dot / (norma * normb)
    else: # otherwise, 
        norma = np.linalg.norm(query, axis=1)
        epsilon = 1.0e-9 # to avoid division by 0
        cos = dot / (norma * normb + epsilon)
        
    return cos


