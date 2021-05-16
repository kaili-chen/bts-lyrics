'''
Contains attributes and methods to assist in processing lyrics.
'''

import re

# variables
CONTRACTIONS = {
    "i\'mma" : "imma",
    "i mma": "imma",
    "gotta": "got to",
    "gonna": "going to",
    "kinda": "kind of",
    "boutta": "about to",
    "hella": "hella",
    "lotta": "lot of",
    "betta": "better",
    "playa": "player",
    "tryna": "trying to",
    "sucka": "sucker",
    "fella": "fellow",
    "killa": "killer",
    "finna": "fixing to",
    "wanna": "want to",
    "lovin": "love",
    "makin": "make",
    "dreamin": "dream",
    "gal": "girl",
    "goin": "going",
    "vibin": "vibing",
    "jigglin": "jiggling",
    "grippin": "gripping",
    "steppin": "stepping",
    "c\'mon": "come on",
    "cmon": "come on",
    "cryin": "crying",
    "cheatin": "cheating",
    "feelin": "feeling",
    "blockin": "blocking",
    "shinin": "shining",
    "firin": "firing",
    "somethin": "somthing",
    "sayin": "saying",
    "gigglin": "giggling",
    "gon": "going to",
    "freakin": "freaking",
    "everythin": "everything",
    "rockin": "rocking",
    "doublin": "doubling",
    "sippin": "sipping",
    "nothin": "nothing",
    "dreamin": "dreaming",
    "ridin": "riding",
    "livin": "living",
    "eatin": "eating",
    "dyin": "dying",
    "kiddin": "kidding",
    "stoppin": "stopping",
    "fallin": "falling",
    "doin": "doing",
    "ballin": "balling",
    "singin": "singing",
    "poppin": "popping",
    "jumpin": "jumping",
    "goin": "going",
    "flashin": "flashing",
    "askin": "asking",
    "cruisin": "cruising",
    "swaggin": "swagging",
    "lookin": "looking",
    "swimmin": "swimming",
    "missin": "missing",
    "takin": "taking",
    "tippin": "tipping",
    "lyin": "lying",
    "walkin": "walking",
    "rollin": "rolling",
    "trippin": "tripping",
    "runnin": "running",
    "kissin": "kissing",
    "spittin": "spitting",
    "yall": "you all",
    "y\'all": "you all",
    "y all": "you all",
    "luv": "love",
    "wassup": "what is up",
    "wussup": "what is up",
    "whatchu": "what you",
    "em": "them",
    "\'em'": "them",
    "ya": "you",
    "leggo": "lets go",
    "gurl": "girl",
    "errday": "everyday",
    "err day": "everyday",
    "lemme": "let me",
    "hol": "hold",
    "thang": "thing",
    "killin": "killing",
    "dunno": "don know",
    "dis": "this",
    "becuz": 'because',
    "cuz": "because",
    "dat": "that",
    "errbody": "everybody",
    "errthing": "everything",
    "pourin": "pouring"
}

# non-lexical vocables
NON_LEX_VOCABLES_PATTERNS = {
    "^(aa*hh*)$": "ah",
    "ahem": "ahem",
    "^(aa*yy*)$": "ay",
    "^(ll*aa*)$": "la",
    "^(heyy*)$": "hey",
    "^(nn*aa*)$": "na",
    "^(oo*hh*)$": "oh",
    "^(uu*hh*)$": "uh",
    "^(yy*aa*)$": "ya",
    "yeah": "yeah",
    "^(yoo*)$": "yo",
    "^(hh*aa*)$": "ha",
    "haha": "ha",
    "heh": "heh",
    "^(ee*hh*)$": "eh",
    "wow": "wow",
    "^(w+o+)$": "wo",
    "^(hh*oo*)$": "ho",
    "^(whoo*)$": "wo",
    "owoah": "woah",
    "woah": "woah",
    "ayo": "ayo"    
}

NON_LEX_VOCABLES = list(NON_LEX_VOCABLES_PATTERNS.values())

# methods
def expand_contractions(lyrics):
    '''
    Returns a list of the given lyrics (string) with adlib reduced to plain form.

    Parameters:
        lyrics (string) : lyrics to reduce contractions from

    Returns:
        clean (string) : string with contractions expanded
    '''
    lyrics = lyrics.lower().strip()
    lyrics = lyrics.split()
    clean = []

    for word in lyrics:
        match = False
        for pattern, value in CONTRACTIONS.items():
            if re.match(pattern, word):
                match = True
                clean.append(value)

        if not match:
            clean.append(word)

    return " ".join(clean)


def reduce_non_lex_vocables(lyrics):
    '''
    Returns a list of the given lyrics (string) with adlib reduced to plain form.

    Parameters:
        lyrics (string) : lyrics to reduce adlibs from

    Returns:
        clean (string) : string with adlibs reduced
    '''
    lyrics = lyrics.lower().strip()
    lyrics = lyrics.split()
    clean = []

    for word in lyrics:
        match = False
        for pattern, value in NON_LEX_VOCABLES_PATTERNS.items():
            if re.match(pattern, word):
                match = True
                clean.append(value)

        if not match:
            clean.append(word)

    return " ".join(clean)


def count_non_lex_vocables(lyrics):
    '''
    Returns a dictionary of the counts of each adlib in the lyrics.

    Parameters:
        lyrics (string) : lyrics to extract adlib counts from

    Returns:
        counts (dictionary) : contains each adlib and their counts in the lyrics
    '''
    lyrics = lyrics.lower().strip()
    lyrics = lyrics.split()
    counts = {}

    for word in lyrics:
        for pattern, value in NON_LEX_VOCABLES_PATTERNS.items():
            found = re.findall(pattern, word)
            if len(found) > 0:
                if value in counts:
                    counts[value] += len(found)
                else:
                    counts[value] = len(found)

    return counts

def remove_non_lex_vocables(lyrics):
    '''
    Returns a list of the given lyrics (string) with adlibs removed.

    Parameters:
        lyrics (string) : lyrics to remove adlib from

    Returns:
        lyrics_no_ab (string) : string with adlibs removed
    '''
    lyrics = lyrics.lower().strip()
    lyrics = lyrics.split()
    clean = []

    for word in lyrics:
        match = False
        for pattern, value in NON_LEX_VOCABLES_PATTERNS.items():
            if re.match(pattern, word):
                match = True

        if not match:
            clean.append(word)

    return " ".join(clean)

if __name__ == '__main__':
    pass
