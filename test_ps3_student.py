import os
import document_distance as ds
import unittest
import string

#Constants
a1 = ['from', 'time', 'to', 'time', 'this',
      'submerged', 'or', 'latent', 'theater',
      'in', 'becomes', 'almost', 'overt', 'it', 
      'is', 'close', 'to', 'the', 'surface', 'in', 
      'hamlets', 'pretense', 'of', 'madness', 'the', 
      'antic', 'disposition', 'he', 'puts', 'on', 
      'to', 'protect', 'himself', 'and', 'prevent', 
      'his', 'antagonists', 'from', 'plucking', 'out', 
      'the', 'heart', 'of', 'his', 'mystery', 'it', 
      'is', 'even', 'closer', 'to', 'the', 'surface', 
      'when', 'hamlet', 'enters', 'his', 'mothers', 
      'room', 'and', 'holds', 'up', 'side', 'by', 
      'side', 'the', 'pictures', 'of', 'the', 'two', 
      'kings', 'old', 'hamlet', 'and', 'claudius', 
      'and', 'proceeds', 'to', 'describe', 'for', 'her', 
      'the', 'true', 'nature', 'of', 'the', 'choice', 
      'she', 'has', 'made', 'presenting', 'truth', 'by', 
      'means', 'of', 'a', 'show', 'similarly', 'when', 
      'he', 'leaps', 'into', 'the', 'open', 'grave', 'at', 
      'ophelias', 'funeral', 'ranting', 'in', 'high', 'heroic', 
      'terms', 'he', 'is', 'acting', 'out', 'for', 'laertes', 
      'and', 'perhaps', 'for', 'himself', 'as', 'well', 'the', 
      'folly', 'of', 'excessive', 'melodramatic', 'expressions', 
      'of', 'grief']
a1_freq = {'from': 2, 'time': 2, 'to': 5, 'this': 1, 'submerged': 1,
        'or': 1, 'latent': 1, 'theater': 1, 'in': 3, 'becomes': 1, 
        'almost': 1, 'overt': 1, 'it': 2, 'is': 3, 'close': 1, 
        'the': 10, 'surface': 2, 'hamlets': 1, 'pretense': 1, 'of': 7, 
        'madness': 1, 'antic': 1, 'disposition': 1, 'he': 3, 'puts': 1, 
        'on': 1, 'protect': 1, 'himself': 2, 'and': 5, 'prevent': 1, 
        'his': 3, 'antagonists': 1, 'plucking': 1, 'out': 2, 'heart': 1, 
        'mystery': 1, 'even': 1, 'closer': 1, 'when': 2, 'hamlet': 2, 
        'enters': 1, 'mothers': 1, 'room': 1, 'holds': 1, 'up': 1, 
        'side': 2, 'by': 2, 'pictures': 1, 'two': 1, 'kings': 1, 'old': 1, 
        'claudius': 1, 'proceeds': 1, 'describe': 1, 'for': 3, 'her': 1, 
        'true': 1, 'nature': 1, 'choice': 1, 'she': 1, 'has': 1, 'made': 1, 
        'presenting': 1, 'truth': 1, 'means': 1, 'a': 1, 'show': 1, 
        'similarly': 1, 'leaps': 1, 'into': 1, 'open': 1, 'grave': 1, 
        'at': 1, 'ophelias': 1, 'funeral': 1, 'ranting': 1, 'high': 1, 
        'heroic': 1, 'terms': 1, 'acting': 1, 'laertes': 1, 'perhaps': 1, 
        'as': 1, 'well': 1, 'folly': 1, 'excessive': 1, 'melodramatic': 1, 
        'expressions': 1, 'grief': 1}

b1 = ['almost', 'all', 'of', 'shakespeares', 'hamlet', 'can', 'be', 
        'understood', 'as', 'a', 'play', 'about', 'acting', 'and', 'the', 
        'theater', 'for', 'example', 'there', 'is', 'hamlets', 'pretense', 
        'of', 'madness', 'the', 'antic', 'disposition', 'that', 'he', 
        'puts', 'on', 'to', 'protect', 'himself', 'and', 'prevent', 'his', 
        'antagonists', 'from', 'plucking', 'out', 'the', 'heart', 'of', 
        'his', 'mystery', 'when', 'hamlet', 'enters', 'his', 'mothers', 
        'room', 'he', 'holds', 'up', 'side', 'by', 'side', 'the', 'pictures', 
        'of', 'the', 'two', 'kings', 'old', 'hamlet', 'and', 'claudius', 
        'and', 'proceeds', 'to', 'describe', 'for', 'her', 'the', 'true', 
        'nature', 'of', 'the', 'choice', 'she', 'has', 'made', 'presenting', 
        'truth', 'by', 'means', 'of', 'a', 'show', 'similarly', 'when', 'he', 
        'leaps', 'into', 'the', 'open', 'grave', 'at', 'ophelias', 'funeral', 
        'ranting', 'in', 'high', 'heroic', 'terms', 'he', 'is', 'acting', 
        'out', 'for', 'laertes', 'and', 'perhaps', 'for', 'himself', 'as', 
        'well', 'the', 'folly', 'of', 'excessive', 'melodramatic', 
        'expressions', 'of', 'grief']
b1_freq = {'almost': 1, 'all': 1, 'of': 8, 'shakespeares': 1, 'hamlet': 3, 
        'can': 1, 'be': 1, 'understood': 1, 'as': 2, 'a': 2, 'play': 1, 
        'about': 1, 'acting': 2, 'and': 5, 'the': 9, 'theater': 1, 'for': 4, 
        'example': 1, 'there': 1, 'is': 2, 'hamlets': 1, 'pretense': 1, 
        'madness': 1, 'antic': 1, 'disposition': 1, 'that': 1, 'he': 4, 
        'puts': 1, 'on': 1, 'to': 2, 'protect': 1, 'himself': 2, 'prevent': 1, 
        'his': 3, 'antagonists': 1, 'from': 1, 'plucking': 1, 'out': 2, 
        'heart': 1, 'mystery': 1, 'when': 2, 'enters': 1, 'mothers': 1, 
        'room': 1, 'holds': 1, 'up': 1, 'side': 2, 'by': 2, 'pictures': 1, 
        'two': 1, 'kings': 1, 'old': 1, 'claudius': 1, 'proceeds': 1, 
        'describe': 1, 'her': 1, 'true': 1, 'nature': 1, 'choice': 1, 
        'she': 1, 'has': 1, 'made': 1, 'presenting': 1, 'truth': 1, 
        'means': 1, 'show': 1, 'similarly': 1, 'leaps': 1, 'into': 1, 
        'open': 1, 'grave': 1, 'at': 1, 'ophelias': 1, 'funeral': 1, 
        'ranting': 1, 'in': 1, 'high': 1, 'heroic': 1, 'terms': 1, 
        'laertes': 1, 'perhaps': 1, 'well': 1, 'folly': 1, 'excessive': 1, 
        'melodramatic': 1, 'expressions': 1, 'grief': 1}

tf2_dict = {'from': 0.015151515151515152, 'time': 0.015151515151515152, 'to': 0.03787878787878788,
            'this': 0.007575757575757576, 'submerged': 0.007575757575757576, 'or': 0.007575757575757576,
            'latent': 0.007575757575757576, 'theater': 0.007575757575757576, 'in': 0.022727272727272728,
            'becomes': 0.007575757575757576, 'almost': 0.007575757575757576, 'overt': 0.007575757575757576,
            'it': 0.015151515151515152, 'is': 0.022727272727272728, 'close': 0.007575757575757576,
            'the': 0.07575757575757576, 'surface': 0.015151515151515152, 'hamlets': 0.007575757575757576,
            'pretense': 0.007575757575757576, 'of': 0.05303030303030303, 'madness': 0.007575757575757576,
            'antic': 0.007575757575757576, 'disposition': 0.007575757575757576, 'he': 0.022727272727272728,
            'puts': 0.007575757575757576, 'on': 0.007575757575757576, 'protect': 0.007575757575757576,
            'himself': 0.015151515151515152, 'and': 0.03787878787878788, 'prevent': 0.007575757575757576,
            'his': 0.022727272727272728, 'antagonists': 0.007575757575757576, 'plucking': 0.007575757575757576,
            'out': 0.015151515151515152, 'heart': 0.007575757575757576, 'mystery': 0.007575757575757576,
            'even': 0.007575757575757576, 'closer': 0.007575757575757576, 'when': 0.015151515151515152,
            'hamlet': 0.015151515151515152, 'enters': 0.007575757575757576, 'mothers': 0.007575757575757576,
            'room': 0.007575757575757576, 'holds': 0.007575757575757576, 'up': 0.007575757575757576,
            'side': 0.015151515151515152, 'by': 0.015151515151515152, 'pictures': 0.007575757575757576,
            'two': 0.007575757575757576, 'kings': 0.007575757575757576, 'old': 0.007575757575757576,
            'claudius': 0.007575757575757576, 'proceeds': 0.007575757575757576, 'describe': 0.007575757575757576,
            'for': 0.022727272727272728, 'her': 0.007575757575757576, 'true': 0.007575757575757576,
            'nature': 0.007575757575757576, 'choice': 0.007575757575757576, 'she': 0.007575757575757576,
            'has': 0.007575757575757576, 'made': 0.007575757575757576, 'presenting': 0.007575757575757576,
            'truth': 0.007575757575757576, 'means': 0.007575757575757576, 'a': 0.007575757575757576,
            'show': 0.007575757575757576, 'similarly': 0.007575757575757576, 'leaps': 0.007575757575757576,
            'into': 0.007575757575757576, 'open': 0.007575757575757576, 'grave': 0.007575757575757576,
            'at': 0.007575757575757576, 'ophelias': 0.007575757575757576, 'funeral': 0.007575757575757576,
            'ranting': 0.007575757575757576, 'high': 0.007575757575757576, 'heroic': 0.007575757575757576,
            'terms': 0.007575757575757576, 'acting': 0.007575757575757576, 'laertes': 0.007575757575757576,
            'perhaps': 0.007575757575757576, 'as': 0.007575757575757576, 'well': 0.007575757575757576,
            'folly': 0.007575757575757576, 'excessive': 0.007575757575757576, 'melodramatic': 0.007575757575757576,
            'expressions': 0.007575757575757576, 'grief': 0.007575757575757576}


idf2_dict = {'from': 0.0, 'time': 0.3010299956639812, 'to': 0.0, 'this': 0.3010299956639812,
             'submerged': 0.3010299956639812, 'or': 0.3010299956639812,
             'latent': 0.3010299956639812, 'theater': 0.0, 'in': 0.0, 'becomes': 0.3010299956639812,
             'almost': 0.0, 'overt': 0.3010299956639812, 'it': 0.3010299956639812, 'is': 0.0,
             'close': 0.3010299956639812, 'the': 0.0, 'surface': 0.3010299956639812, 'hamlets': 0.0,
             'pretense': 0.0, 'of': 0.0, 'madness': 0.0, 'antic': 0.0, 'disposition': 0.0, 'he': 0.0,
             'puts': 0.0, 'on': 0.0, 'protect': 0.0, 'himself': 0.0, 'and': 0.0, 'prevent': 0.0,
             'his': 0.0, 'antagonists': 0.0, 'plucking': 0.0, 'out': 0.0, 'heart': 0.0, 'mystery': 0.0,
             'even': 0.3010299956639812, 'closer': 0.3010299956639812, 'when': 0.0, 'hamlet': 0.0,
             'enters': 0.0, 'mothers': 0.0, 'room': 0.0, 'holds': 0.0, 'up': 0.0, 'side': 0.0, 'by': 0.0,
             'pictures': 0.0, 'two': 0.0, 'kings': 0.0, 'old': 0.0, 'claudius': 0.0, 'proceeds': 0.0,
             'describe': 0.0, 'for': 0.0, 'her': 0.0, 'true': 0.0, 'nature': 0.0, 'choice': 0.0, 'she': 0.0,
             'has': 0.0, 'made': 0.0, 'presenting': 0.0, 'truth': 0.0, 'means': 0.0, 'a': 0.0, 'show': 0.0,
             'similarly': 0.0, 'leaps': 0.0, 'into': 0.0, 'open': 0.0, 'grave': 0.0, 'at': 0.0,
             'ophelias': 0.0, 'funeral': 0.0, 'ranting': 0.0, 'high': 0.0, 'heroic': 0.0, 'terms': 0.0,
             'acting': 0.0, 'laertes': 0.0, 'perhaps': 0.0, 'as': 0.0, 'well': 0.0, 'folly': 0.0,
             'excessive': 0.0, 'melodramatic': 0.0, 'expressions': 0.0, 'grief': 0.0, 'all': 0.3010299956639812,
             'shakespeares': 0.3010299956639812, 'can': 0.3010299956639812, 'be': 0.3010299956639812,
             'understood': 0.3010299956639812, 'play': 0.3010299956639812, 'about': 0.3010299956639812,
             'example': 0.3010299956639812, 'there': 0.3010299956639812, 'that': 0.3010299956639812}


tfidf_list = [('and', 0.0), ('as', 0.0), ('the', 0.0), ('to', 0.0), ('a', 0.0007341667652125487),
              ('acting', 0.0007341667652125487), ('almost', 0.0007341667652125487),
              ('choice', 0.0007341667652125487), ('expressions', 0.0007341667652125487),
              ('grave', 0.0007341667652125487), ('has', 0.0007341667652125487),
              ('her', 0.0007341667652125487), ('into', 0.0007341667652125487),
              ('laertes', 0.0007341667652125487), ('made', 0.0007341667652125487),
              ('mothers', 0.0007341667652125487), ('ophelias', 0.0007341667652125487),
              ('pictures', 0.0007341667652125487), ('she', 0.0007341667652125487),
              ('show', 0.0007341667652125487), ('theater', 0.0007341667652125487),
              ('true', 0.0007341667652125487), ('truth', 0.0007341667652125487),
              ('two', 0.0007341667652125487), ('hamlet', 0.0014683335304250973),
              ('when', 0.0014683335304250973), ('antagonists', 0.0016806723455784576),
              ('antic', 0.0016806723455784576), ('at', 0.0016806723455784576),
              ('claudius', 0.0016806723455784576), ('describe', 0.0016806723455784576),
              ('disposition', 0.0016806723455784576), ('enters', 0.0016806723455784576),
              ('even', 0.0016806723455784576), ('excessive', 0.0016806723455784576),
              ('folly', 0.0016806723455784576), ('funeral', 0.0016806723455784576),
              ('grief', 0.0016806723455784576), ('hamlets', 0.0016806723455784576),
              ('heart', 0.0016806723455784576), ('heroic', 0.0016806723455784576),
              ('high', 0.0016806723455784576), ('holds', 0.0016806723455784576),
              ('kings', 0.0016806723455784576), ('leaps', 0.0016806723455784576),
              ('madness', 0.0016806723455784576), ('means', 0.0016806723455784576),
              ('melodramatic', 0.0016806723455784576), ('mystery', 0.0016806723455784576),
              ('nature', 0.0016806723455784576), ('old', 0.0016806723455784576),
              ('on', 0.0016806723455784576), ('open', 0.0016806723455784576),
              ('perhaps', 0.0016806723455784576), ('plucking', 0.0016806723455784576),
              ('presenting', 0.0016806723455784576), ('pretense', 0.0016806723455784576),
              ('prevent', 0.0016806723455784576), ('proceeds', 0.0016806723455784576),
              ('protect', 0.0016806723455784576), ('puts', 0.0016806723455784576),
              ('ranting', 0.0016806723455784576), ('room', 0.0016806723455784576),
              ('similarly', 0.0016806723455784576), ('terms', 0.0016806723455784576),
              ('up', 0.0016806723455784576), ('well', 0.0016806723455784576),
              ('for', 0.002202500295637646), ('he', 0.002202500295637646), ('his', 0.002202500295637646),
              ('in', 0.002202500295637646), ('is', 0.002202500295637646), ('becomes', 0.0030146970353942242),
              ('close', 0.0030146970353942242), ('closer', 0.0030146970353942242),
              ('latent', 0.0030146970353942242), ('or', 0.0030146970353942242),
              ('overt', 0.0030146970353942242), ('submerged', 0.0030146970353942242),
              ('this', 0.0030146970353942242), ('by', 0.003361344691156915),
              ('from', 0.003361344691156915), ('himself', 0.003361344691156915),
              ('it', 0.003361344691156915), ('out', 0.003361344691156915), ('side', 0.003361344691156915),
              ('of', 0.00513916735648784), ('surface', 0.0060293940707884484), ('time', 0.0060293940707884484)]




# Helper function to retrieve filepaths; ripped from https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory
def absolute_file_paths(directory):
    filepaths=[]
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            filepaths.append(os.path.abspath(os.path.join(dirpath, f)))

    return filepaths


# Test shell
class TestPrepData(unittest.TestCase):
    def load_file(self, filename):
        """
        Args:
             filename: string, name of file to read
        Returns:
             string, contains file contents
        """
        inFile = open(filename, 'r', encoding='ascii', errors='ignore')
        line = inFile.read()
        for char in string.punctuation:
             line = line.replace(char, "")
        inFile.close()
        return line.lower()

    def test_prep_hello_world(self):
        expected = ["hello", "world", "hello"]
        result = ds.prep_data(self.load_file("tests/student_tests/hello_world.txt"))
        self.assertEqual(result, expected)

    def test_prep_1a(self):
        expected = a1
        result = ds.prep_data(self.load_file("tests/student_tests/test1a.txt"))
        self.assertEqual(result, expected)

    def test_prep_all_whitespace(self):
        test_input = "hello  it is\nme\rmario"
        expected = ["hello", "it", "is", "me", "mario"]
        result = ds.prep_data(test_input)
        self.assertEqual(result, expected)

class TestWordFrequency(unittest.TestCase):
    def load_text(self, filename):
        """
        Args:
             filename: string, name of file to read
        Returns:
             string, contains file contents
        """
        inFile = open(filename, 'r', encoding='ascii', errors='ignore')
        line = inFile.read()
        for char in string.punctuation:
             line = line.replace(char, "")
        inFile.close()
        return line.lower()
    
    def test_frequency_hello_world(self):
         text = self.load_text("tests/student_tests/hello_world.txt")
         data = ["hello", "world", "hello"]
         result = ds.get_frequencies(data)
         expected = {"hello":2, "world":1}
         self.assertDictEqual(result, expected)
    
    def test_frequency_1a(self):
         text = self.load_text("tests/student_tests/test1a.txt")
         data = a1
         result = ds.get_frequencies(data)
         expected = a1_freq
         self.assertDictEqual(result, expected)
    
    def test_frequency_1b(self):
         text = self.load_text("tests/student_tests/test1b.txt")
         data = b1
         result = ds.get_frequencies(data)
         expected = b1_freq
         self.assertDictEqual(result, expected)
    
class TestBigrams(unittest.TestCase):
     def test_bigrams_empty(self):
         result = ds.find_bigrams([""])
         expected = []
         self.assertListEqual(result, expected)
    
     def test_bigrams_hello(self):
         result = ds.find_bigrams(["hello", "world", "hello", 
                                  "friends", "hello"])
         expected = ['hello world', 'world hello', 'hello friends', 'friends hello']
         self.assertListEqual(result, expected)
    
class TestSimilarity(unittest.TestCase):
     def test_similarity1(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":2, "world":1}
         result = ds.calculate_similarity_score(f1, f2)
         expected = 1
         self.assertEqual(result, expected)
    
     def test_similarity2(self):
         f1 = {}
         f2 = {"hello":1}
         result = ds.calculate_similarity_score(f1, f2)
         expected = 0
         self.assertEqual(result, expected)
    
     def test_similarity3(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":2, "friends":1}
         result = ds.calculate_similarity_score(f1, f2)
         expected = .67
         self.assertEqual(round(result, 2), expected)
    
     def test_similarity4(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":1, "friends":1}
         result = ds.calculate_similarity_score(f1, f2)
         expected = 0.4
         self.assertEqual(result, expected)
    
class TestGetFrequentWords(unittest.TestCase):
    def load_text(self, filename):
         """
         Args:
             filename: string, name of file to read
         Returns:
             string, contains file contents
        """     
         inFile = open(filename, 'r', encoding='ascii', errors='ignore')
         line = inFile.read()
         for char in string.punctuation:
             line = line.replace(char, "")
         inFile.close()
         return line.lower()
    
    def test_words1(self):
        f1 = {"hello":1, "world":2}
        f2 = {"hello":1, "world":5}
        result = ds.get_most_frequent_words(f1, f2)
        expected = ['world']
        self.assertListEqual(result, expected)
    
    def test_words2(self):
        f1 = {"hello":5, "world":1}
        f2 = {"hello":1, "world":5}
        result = ds.get_most_frequent_words(f1, f2)
        expected = ['hello', 'world']
        self.assertListEqual(result, expected)
    
class TestTFIDF(unittest.TestCase):
    # Helper function to check if two dictionaries are equal within a range; ripped from https://stackoverflow.com/questions/50935269/assertalmostequal-for-a-value-in-a-dict
    def assertDictAlmostEqual(self, d1, d2, msg=None, places=7):
        # check if both inputs are dicts
        self.assertIsInstance(d1, dict, 'First argument is not a dictionary')
        self.assertIsInstance(d2, dict, 'Second argument is not a dictionary')

        # check if both inputs have the same keys
        self.assertEqual(d1.keys(), d2.keys())

        # check each key
        for key, value in d1.items():
            if isinstance(value, dict):
                self.assertDictAlmostEqual(d1[key], d2[key], msg=msg)
            else:
                self.assertAlmostEqual(d1[key], d2[key], places=places, msg=msg)

    # Helper function to check if two lists are equal within a range; ripped from https://stackoverflow.com/questions/8311202/python-assert-for-lists-of-floats
    def assertListAlmostEqual(self, list1, list2, places=7):
        self.assertEqual(len(list1), len(list2))
        for a, b in zip(list1, list2):
            self.assertAlmostEqual(a[1], b[1], places=places)

    def test_tf1(self):
        text_file = "tests/student_tests/hello_world.txt"
        result = ds.get_tf(text_file)
        expected = {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
        self.assertDictAlmostEqual(result, expected)

    def test_tf2(self):
        text_file = "tests/student_tests/test1a.txt"
        result = ds.get_tf(text_file)
        expected = tf2_dict
        self.assertDictAlmostEqual(result, expected)
    
    def test_idf1(self):
        text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
        result = ds.get_idf(text_files)
        expected = {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
        self.assertDictAlmostEqual(result, expected)

    def test_idf2(self):
        text_files = ['tests/student_tests/test1a.txt', 'tests/student_tests/test1b.txt']
        result = ds.get_idf(text_files)
        expected = idf2_dict
        self.assertDictAlmostEqual(result, expected)
    
    def test_tfidf_small(self):
        text_file = 'tests/student_tests/hello_world.txt'
        text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
        result = ds.get_tfidf(text_file, text_files)
        expected = [('hello', 0.0), ('world', 0.10034333188799373)]
        self.assertListAlmostEqual(result, expected)

    def test_tfidf_big(self):
        text_file = 'tests/student_tests/test1a.txt'
        text_files = ['tests/student_tests/test1a.txt', 'tests/student_tests/test1b.txt', 'tests/student_tests/test2a.txt', 'tests/student_tests/test2b.txt', 'tests/student_tests/test3a.txt']
        result = ds.get_tfidf(text_file, text_files)
        expected = tfidf_list
        self.assertListAlmostEqual(result, expected)


#Dictionary mapping function names from the above TestCase class to 
# the point value each test is worth. Make sure these add up to 5! 
point_values = {
        'test_prep_hello_world': .05,
        'test_prep_all_whitespace': .05,
        'test_prep_1a': .10,
        'test_frequency_hello_world' : .40,
        'test_frequency_1a' : .40,
        'test_frequency_1b': .40,
        'test_bigrams_empty': .10,
        'test_bigrams_hello': .10,
        'test_similarity1': .20,
        'test_similarity2': .20,
        'test_similarity3': .20,
        'test_similarity4': .20,
        'test_words1': .30,
        'test_words2': .30,
        'test_tf1': .25,
        'test_tf2': .25,
        'test_idf1': .5,
        'test_idf2': .5,
        'test_tfidf_small': .25,
        'test_tfidf_big': .25
    }

failure_messages = {
    'test_prep_hello_world': 'Your function generated an incorrect list to represent hello_world.txt',
    'test_prep_all_whitespace': 'Your function generated an incorrect list that strips all whitespace.',
    'test_prep_1a': 'Your function generated an incorrect list to represent test1a.txt',
    'test_frequency_hello_world' : 'Your function generated the incorrect frequency dictionary for hello_world.txt',
    'test_frequency_1a' : 'Your function generated the incorrect frequency dictionary for test1a',
    'test_frequency_1b':  'Your function generated the incorrect frequency dictionary for test1b',
    'test_bigrams_empty': 'Your function fails to generate an empty bigram list for the empty string',
    'test_bigrams_hello': 'Your function generates the incorrect bigrams for a sentence with repeated words',
    'test_similarity1': 'Your function generated an incorrect similarity for identical frequency dictionaries',
    'test_similarity2': 'Your function generated an incorrect similarity for an empty frequency dictionary',
    'test_similarity3': 'Your function generated an incorrect similarity for similar word frequency dictionaries',
    'test_similarity4': 'Your function generated an incorrect similarity for dissimilar word frequency dictionaries',
    'test_words1': 'You did not find the most frequent word from a frequency dictionary',
    'test_words2': 'You did not find the most frequent words in the case of a tie',
    'test_tf1': 'Your function get_tf returned an incorrect answer for tf1.',
    'test_tf2': 'Your function get_tf returned an incorrect answer for tf2.',
    'test_idf1': 'Your function get_idf returned an incorrect answer for idf1.',
    'test_idf2': 'Your function get_idf returned an incorrect answer for idf2.',
    'test_tfidf_small': 'Your function get_tfidf returned an incorrect answer for the small test case.',
    'test_tfidf_big': 'Your function get_tfidf returned an incorrect answer for the big test case.'
}

error_messages = {
    'test_prep_hello_world': 'Your function generated an error while preparing hello_world.txt',
    'test_prep_all_whitespace': 'Your function generated an error while preparing a string with multiple types of whitespace.',
    'test_prep_1a': 'Your function generated an error while preparing test1a.txt',
    'test_frequency_hello_world' : 'Your function produced an error while generating a frequency dictionary for hello_world.txt',
    'test_frequency_1a' : 'Your function produced an error while generating a frequency dictionary for 1a',
    'test_frequency_1b':  'Your function produced an error while generating a frequency dictionary for 1b',
    'test_bigrams_empty': 'Your bigram function produces an error for the empty string',
    'test_bigrams_hello': 'Your bigram function produces an error for a sentence with repeated words',
    'test_similarity1': 'Your similarity function produces an error for identical frequency dictionaries',
    'test_similarity2': 'Your similarity function produces an error for an empty frequency dictionary.',
    'test_similarity3': 'Your similarity function produces an error for similar word frequency dictionaries',
    'test_similarity4': 'Your similarity function produces an error for dissimilar word frequency dictionaries',
    'test_words1': 'Your function produced an error when finding the most frequent word from a frequency dictionary',
    'test_words2': 'Your function produced an error in the case of a tie',
    'test_words3': 'Your function produced an error when finding the most frequent word in a loaded text',
    'test_tf1': 'Your function get_tf produced an error for tf1.',
    'test_tf2': 'Your function get_tf produced an error for tf2.',
    'test_idf1': 'Your function get_idf produced an error for idf1.',
    'test_idf2': 'Your function get_idf produced an error for idf2.',
    'test_tfidf_small': 'Your function get_tfidf produced an error for the small test case.',
    'test_tfidf_big': 'Your function get_tfidf produced an error for the big test case.'
}

# Subclass to track a point score and appropriate
# grade comment for a suit of unit tests
class Results_600(unittest.TextTestResult):
    # We override the init method so that the Result object
    # can store the score and appropriate test output. 
    def __init__(self, *args, **kwargs):
        super(Results_600, self).__init__(*args, **kwargs)
        self.output = []
        self.points = 5

    def addFailure(self, test, err):
        test_name = test._testMethodName
        self.handleDeduction(test_name, failure_messages[test_name])
        super(Results_600, self).addFailure(test, err)

    def addError(self, test, err):
        test_name = test._testMethodName
        self.handleDeduction(test_name, error_messages[test_name])
        super(Results_600, self).addError(test, err)

    def handleDeduction(self, test_name, messages):
        point_value = point_values[test_name]
        self.output.append('[-%s]: %s' % (point_value, messages))
        self.points -= point_value
    def getOutput(self):
        if len(self.output) == 0:
            return "All correct!"
        return '\n'.join(self.output)

    def getPoints(self):
        return round(self.points, 3)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPrepData))
    suite.addTest(unittest.makeSuite(TestWordFrequency))
    suite.addTest(unittest.makeSuite(TestBigrams))
    suite.addTest(unittest.makeSuite(TestGetFrequentWords))
    suite.addTest(unittest.makeSuite(TestSimilarity))
    suite.addTest(unittest.makeSuite(TestTFIDF))
    result = unittest.TextTestRunner(verbosity=4, resultclass=Results_600).run(suite)

    output = result.getOutput()
    points = result.getPoints()
    #sys.stdout=store
    print("\n\nProblem Set 3 Unit Test Results:")
    print(output)
    print("Points: %s/5\n" % points)
