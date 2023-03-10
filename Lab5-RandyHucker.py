## Lab 5: Required Questions - Dictionaries  ##

# RQ1
import doctest
_author_ = "Randy Hucker"
_credits_ = ["Me", "https://www.geeksforgeeks.org/any-all-in-python/"]
_email_ = "huckerre@mail.uc.edu"

# RQ1


def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    dict2.update(dict1)
    keyList = sorted(dict2.keys())
    dictList = {}
    for key in keyList:
        dictList[key] = dict2[key]
    return dictList


# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    list_of_words = message.split()
    counter = {}
    for word in list_of_words:
        try:
            counter[word] += 1
        except (KeyError):
            counter[word] = 1
    return counter

# RQ3


def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d,
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    for key in d:
        if d[key] == x:
            d[key] = y

# RQ4


def sumdicts(lst):
    """
    Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And
    if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned
    as the value mapped for that key
    >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
    >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
    True
    """
    return_dict = {}
    for dict in lst:
        for key in dict:
            try:
                return_dict[key] += dict[key]
            except (KeyError):
                return_dict[key] = dict[key]
    return return_dict


# RQ5


def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()


def build_successors_table(tokens):
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table


def construct_tweet(word, table):
    """Returns a string that is a random sentence starting with word, and choosing successors from table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word


def random_tweet(table):
    import random
    return construct_tweet(random.choice(table['.']), table)


def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of median length starting with word, 
    and choosing successors from table. It is difficult to write a doctest for this function, 
    since it is randomized. But my experiments showed that with 5 random samples you should usually
    get a tweet that is roughly ordinary size sentence (6-10 words).
    >>> middle_tweet(build_successors_table(shakespeare_tokens()))
    True
    """

    t1 = random_tweet(table)
    t2 = random_tweet(table)
    t3 = random_tweet(table)
    t4 = random_tweet(table)
    t5 = random_tweet(table)

    tweetArray = [t1, t2, t3, t4, t5]
    tweetArray.sort(key=len)
    return (tweetArray[2])


if __name__ == "__main__":
    doctest.testmod(verbose=True)
