'''
Contains attributes and methods to assist in processing lyrics.

Variables:
    CONTRACTIONS
    ADLIB_PATTERNS
    ADLIBS

Functions:
    count_adlibs(string) --> dictionary object


Last updated 23 July 2020, 9:43 PM
'''

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
    "rollin": "rollin",
    "trippin": "tripping",
    "runnin": "running",
    "kissin": "kissing",
    "spittin": "spitting",
    "yall": "you all",
    "y\'all": "you all",
    "y all": "you all",
    "luv": "love",
    "wassup": "what is up",
    "em": "them",
    "\'em'": "them",
    "ya": "you",
    "leggo": "lets go",
    "gurl": "girl",
    "errday": "everyday",
    "err day": "everyday"
}

ADLIB_PATTERNS = {
    "^(aa*hh*)$": "ah",
    "^(aa*yy*)$": "ay",
    "^(ll*aa*)$": "la",
    "^(heyy*)$": "hey",
    "^(nn*aa*)$": "na",
    "^(oo*hh*)$": "oh",
    "^(uu*hh*)$": "uh",
    "^(yy*aa*)$": "ya",
    "yeah": "yeah",
    "^(yoo*)$": "yo",
    "heh": "heh",
    "^(ee*hh*)$": "eh",
    "wow": "wow",
    "^(hh*oo*)$": "ho"
}

ADLIBS = ADLIB_PATTERNS.values()

# methods
def count_adlibs(lyrics):
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
        for pattern, value in ADLIB_PATTERNS.items():
            found = re.findall(pattern, word)
            if len(found) > 0:
                if value in counts:
                    counts[value] += len(found)
                else:
                    counts[value] = len(found)

    return counts

if __name__ == '__main__':
    pass
