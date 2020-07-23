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

STOPWORDS = nltk.corpus.stopwords.words('english')

def normalise(text, remove_punc=True, stopwords=STOPWORDS):
    '''
    Returns normalised text according to given parameters and flags.

    Parameters:
        text (string) : string to be normalised
        remove_punc (boolean) [default=True] : to indicate whether to remove puncutation
        words (list) [default=nltk.corpus.stopwords.words('english')] : 'None' to not remove stopwords or provide another list of stopwords to remove

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

    # remove STOPWORDS
    if stopwords:
        no_stops = [word for word in text.split() if word not in stopwords]

        text = ' '.join(no_stops)

    return text


if __name__ == '__main__':
    pass
