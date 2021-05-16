'''
Contains attributes and methods to assist in text processing, required nltk and re.

Variables:
    MONTHS
    STOPWORDS
    ADLIBS

Functions:
    normalise(string) --> string


Last updated 23 July 2020, 6:36 PM
'''

import nltk
import re

# VARIABLES
MONTHS = ['january', 'jan',
        'february', 'feb',
        'march', 'mar',
        'april', 'apr',
        'may',
        'june', 'jun',
        'july', 'jul',
        'august', 'aug',
        'september', 'sep',
        'october', 'oct',
        'november', 'nov',
        'december', 'dec']

# list from https://www.grammar-monster.com/lessons/apostrophes_replace_letters.htm
CONTRACTIONS = {
    "aren't":   "are not",
    "can't":    "cannot",
    "couldn't":	"could not",
    "didn't":   "did not",
    "doesn't":  "does not",
    "don't":	"do not",
    "hadn't":	"had not",
    "hasn't":	"has not",
    "haven't":	"have not",
    "he'd":	    "he had",
    "he'll":	"he will",
    "he's":	    "he is",
    "i'd":      "i had",
    "i'll":     "i will",
    "i'm":      "i am",
    "i've":	    "i have",
    "isn't":    "is not",
    "it's":	    "it is",
    "let's":	"let us",
    "mustn't":  "must not",
    "shan't":   "shall not",
    "she'd":	"she had",
    "she'll":	"she will",
    "she's":	"she is",
    "shouldn't":    "should not",
    "that's":	"that is",
    "there's":  "there is",
    "they'd":	"they had",
    "they'll":	"they will",
    "they're":	"they are",
    "they've":	"they have",
    "we'd":	    "we had",
    "we're":    "we are",
    "we've":	"we have",
    "weren't":	"were not",
    "what'll":	"what will",
    "what're":	"what are",
    "what's":	"what is",
    "what've":	"what have",
    "where's":	"where is",
    "who'd":	"who had",
    "who'll":	"who will",
    "who're":	"who are",
    "who's":	"who is",
    "who've":	"who have",
    "won't":	"will not",
    "wouldn't":	"would not",
    "you'd":	"you had",
    "you'll":	"you will",
    "you're":	"you are",
    "you've":	"you have"
}

STOPWORDS = nltk.corpus.stopwords.words('english')

# sometimes, lemma needs help (e.g.  lemmatizes 'us' to 'u')
LEMMA_EXCEPTIONS = ["us"]

# FUNCTIONS
lemmatizer = nltk.stem.WordNetLemmatizer()
stemmer = nltk.stem.PorterStemmer()

def lemmatize_word(word):
    if word not in LEMMA_EXCEPTIONS:
        return lemmatizer.lemmatize(word)
    else:
        return word 

def normalise(text, remove_punc=True, stopwords=STOPWORDS, extra_stopwords=None, lemmatize=True, expand_contractions=False, replacements=None):
    '''
    Returns normalised text according to given parameters and flags.

    Parameters:
        text (string) : string to be normalised
        remove_punc (boolean) [default = True] : to indicate whether to remove puncutation
        stopwords (list) [default = nltk.corpus.stopwords.words('english')] : 'None' to not remove stopwords or provide another list of stopwords to remove
        extra_stopwords (list) [default = None] : additional stopwords to be added to the nltk stopwords, if any
        lemmatize (boolean) [default = True]: whether to lemmatize each word, uses nltk wordnet lemmatizer
        expand_contractions (boolean) [default = False] : to indicate whether to expand contractions (can be viewed in variable CONTRACTIONS)
        replacements (dict) [default = None] : key (word), value (word's replacement), runs after contractions expanded if indicated

    Returns:
        text (string) : given text normalised according to given flags.
    '''

    # change text to lowercase and remove leading and trailing white spaces
    text = text.lower().strip()

    # remove punctuation
    if remove_punc:
        # remove punctuation
        text = re.sub(r'[\W]', ' ', text)
        # remove double spacing sometimes caused by removal of punctuation
        text = re.sub(r'\s+', ' ', text)

        # expand contractions
        if expand_contractions:
            for k, v in CONTRACTIONS.items():
                # uses a spaced version of contraction (e.g. 'don t' instead of 'don't) as punctuation removed
                contraction = k.replace("\'", " ")
                text = re.sub('\s'+contraction+'\s', ' '+v+' ', text)
    else:
        # expand contractions; might cause issues if the ' is not a stright one (aka smart quotes)
        if expand_contractions:
            expanded = [CONTRACTIONS[word] for word in txt.split() if word in CONTRACTIONS.keys()]

    # deal with replacements
    if replacements:
        replaced = [replacements[word] if word in replacements.keys() else word for word in text.split()]
        text = ' '.join(replaced)         

    # remove STOPWORDS
    if stopwords:
        # add additional stop words if any
        if extra_stopwords:
            stopwords.extend(extra_stopwords)

        no_stops = [word for word in text.split() if word not in stopwords]
        text = ' '.join(no_stops)
    
    # lemmatize
    if lemmatize:
        lemmatized = [lemmatize_word(word) for word in text.split()]
        text = ' '.join(lemmatized)

    return text


def split_n(text, n, overlap=False):
    '''
    Split the text every n words.

    Parameters:
        text (string / list) : string or list to be normalised
        n (int) : interval to split text at
        overlap (boolean) [default=False] : to indicate whether to let intervals overlap

    Returns:
        result (list) : text split every n interval.
    '''
    if isinstance(text, str):
        words = text.split()
    elif isinstance(text, list):
        words = text
    else:
        return None

    if overlap:
        result = [' '.join(words[i:(i+n)]) for i in range(len(words)-1)]
    else:
        result = [' '.join(words[i:(i+n)]) for i in range(0, len(words), n)]

    return result


if __name__ == '__main__':
    pass
