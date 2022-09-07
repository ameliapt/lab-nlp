import re
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


def clean_up(s):
    """
    Cleans up numbers, URLs, and special characters from a string.

    Args:
        s: The string to be cleaned up.

    Returns:
        A string that has been cleaned up.
    """
    remove_url = re.sub(r"http\S+", "", s)
    replaced_string = re.sub('\W', ' ', remove_url).lower()
    cleaned_str = (" ".join(replaced_string.split())) 
    return cleaned_str


def tokenize(s):
    """
    Tokenize a string.

    Args:
        s: String to be tokenized.

    Returns:
        A list of words as the result of tokenization.
    """
    wrds_lst = word_tokenize(s)
    return wrds_lst


def stem_and_lemmatize(l):
    """
    Perform stemming and lemmatization on a list of words.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after being stemmed and lemmatized.
    """
    ps = PorterStemmer()
    lem = WordNetLemmatizer()
    lst_converted_strings = []
    
    for word in l:
        stem = ps.stem(word)
        lemm = lem.lemmatize(stem)
        lst_converted_strings.append(lemm)
        
    return lst_converted_strings
        
    
def remove_stopwords(l):
    """
    Remove English stopwords from a list of strings.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after stop words are removed.
    """
    stop_words = list(stopwords.words('english'))
    list_without_stopwords = [l.remove(w) for w in l if w in stop_words]
        
    return l