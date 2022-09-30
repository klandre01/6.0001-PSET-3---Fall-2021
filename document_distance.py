# 6.0001 Fall 2019
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Karen Andre
# Collaborators: https://docs.python.org/3/howto/sorting.html
# Time Spent: 4:00
# Late Days Used: 0 

import string
import math

# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other 


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()

### Problem 0: Prep Data ###
def prep_data(input_text):
    """
    Args:
        input_text: string representation of text from file,
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text
    """
    input_list = input_text.split()
    return input_list

### Problem 1: Find Bigrams ###
def find_bigrams(single_words):
    """
    Args:
        single_words: list of words in the text, in the order they appear in the text
            all words are made of lowercase characters
    Returns:
        list of bigrams from input text list
    """
    bigrams = []
    for i in range(len(single_words) - 1):
        new_phrase = single_words[i] + " " + single_words[i + 1]
        bigrams.append(new_phrase)
    return bigrams

### Problem 2: Word Frequency ###
def get_frequencies(words):
    """
    Args:
        words: list of words (or bigrams), all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string 
        is a word (or bigram) in words and the corresponding int 
        is the frequency of the word (or bigram) in words
    """
    freq_dict = {}
    for word in words:
        try: 
            freq_dict[word] += 1
        except:
            freq_dict[word] = 1
    return freq_dict

### Problem 3: Similarity ###
def calculate_similarity_score(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.
    
    Args:
        dict1: frequency dictionary of words or bigrams for one text
        dict2: frequency dictionary of words or bigrams for another text
    Returns:
        float, a number between 0 and 1, inclusive 
        representing how similar the texts are to each other
        
        The difference in text frequencies = DIFF sums words 
        from these three scenarios: 
        * If a word or bigram occurs in dict1 and dict2 then 
          get the difference in frequencies
        * If a word or bigram occurs only in dict1 then take the 
          frequency from dict1
        * If a word or bigram occurs only in dict2 then take the 
          frequency from dict2
         The total frequencies = ALL is calculated by summing 
         all frequencies in both dict1 and dict2. 
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    # calculating diff & all
    diff = 0
    all = 0
    for word in dict1.keys():
        if word in dict2.keys():
            diff += abs(dict2[word]-dict1[word])
        else:
            diff += dict1[word]
        all += dict1[word]
    for word in dict2.keys():
        if word not in dict1.keys():
            diff += dict2[word]
        all += dict2[word]
    similarity = round((1.0-diff/all), 2)
    return similarity

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.
    
    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries
    
    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency. 
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2. 
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    combined_freq = {}
    # populating combined_freq
    for word in dict1.keys():
        if word in dict2.keys():
            if word not in combined_freq.keys():
                combined_freq[word] = dict1[word] + dict2[word]
            else:
                combined_freq[word] += dict1[word] + dict2[word]
        else:
            if word not in combined_freq.keys():
                combined_freq[word] = dict1[word]
            else:
                combined_freq[word] += dict1[word]
    for word in dict2.keys():
        if word not in dict1.keys():
            if word not in combined_freq.keys():
                combined_freq[word] = dict2[word]
            else:
                combined_freq[word] += dict2[word]
    # finding max value
    max_word_count = combined_freq[max(combined_freq)]  # max(combined_freq) returns key with max value
    most_frequent = []  # list of most frequently occurring word(s)
    # populating most_frequent
    for word in combined_freq.keys():
        if combined_freq[word] == max_word_count:
            most_frequent.append(word)
    return sorted(most_frequent)

    

### Problem 5: Finding TF-IDF ###
def get_tf(text_file):
    """
    Args:
        text_file: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_word_frequencies from earlier
    """
    file_words = prep_data(load_file(text_file))
    word_count = len(file_words)
    word_freq = get_frequencies(file_words)
    tf_dict = {}
    for word in word_freq.keys():
        tf_dict[word] = word_freq[word] / word_count
    return tf_dict


def get_idf(text_files):
    """
    Args:
        text_files: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculatd as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    doc_count = len(text_files)
    idf_dict = {}
    for doc in text_files:  # iterate through each document
        word_list = prep_data(load_file(doc))
        for word in word_list:  # go through each word in the current document
            if word not in idf_dict:
                # check if the word is in each of the documents
                for file in text_files:
                    if word in prep_data(load_file(file)):
                        try:
                            idf_dict[word] += 1
                        except:
                            idf_dict[word] = 1
    # convert document frequency to idf
    for key in idf_dict.keys():
        val = idf_dict[key]
        idf_dict[key] = math.log10(doc_count / val)
    return idf_dict



def get_tfidf(text_file, text_files):
    """
        Args:
            text_file: name of file in the form of a string (used to calculate TF)
            text_files: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)

        """
    tf_dict = get_tf(text_file)
    idf_dict = get_idf(text_files)
    tfidf_list = []
    for i in tf_dict.keys():
        tfidf_list.append((i, tf_dict[i]*idf_dict[i]))
    return sorted(tfidf_list, key=lambda word: word[0])
    
    
if __name__ == "__main__":
    pass
    #Uncomment the following lines to test your implementation
    # Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/" 
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt') 
    world, friend = prep_data(hello_world), prep_data(hello_friend)
    print(world) ## should print ['hello', 'world', 'hello']
    print(friend) ## should print ['hello', 'friends']

    ## Tests Problem 1: Find Bigrams
    world_bigrams, friend_bigrams = find_bigrams(world), find_bigrams(friend)
    print(world_bigrams) ## should print ['hello world', 'world hello']
    print(friend_bigrams) ## should print ['hello friends']

    # Tests Problem 2: Get frequency
    world_word_freq, world_bigram_freq = get_frequencies(world), get_frequencies(world_bigrams)
    friend_word_freq, friend_bigram_freq = get_frequencies(friend), get_frequencies(friend_bigrams)
    print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    print(world_bigram_freq) ## should print {'hello world': 1, 'world hello': 1}
    print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}
    print(friend_bigram_freq) ## should print {'hello friends': 1}

    # Tests Problem 3: Similarity
    word_similarity = calculate_similarity_score(world_word_freq, friend_word_freq)
    bigram_similarity = calculate_similarity_score(world_bigram_freq, friend_bigram_freq)
    print(word_similarity) ## should print 0.4
    print(bigram_similarity) ## should print 0.0

    # Tests Problem 4: Most Frequent Word(s)
    freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    most_frequent = get_most_frequent_words(freq1, freq2)
    print(most_frequent) ## should print ["hello", "world"]

    # Tests Problem 5: Find TF-IDF
    text_file = 'tests/student_tests/hello_world.txt'
    text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(text_file)
    idf = get_idf(text_files)
    tf_idf = get_tfidf(text_file, text_files)
    print(tf) ## should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf) ## should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) ## should print [('hello', 0.0), ('world', 0.10034333188799373)]
