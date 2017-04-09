
# coding: utf-8

# # Preprocessing

# 1. Words retrieval and glove vectorization

# In[8]:

from nltk import sent_tokenize, word_tokenize
import os
from collections import Counter

character_counter=0;
word_counter=0;
sentence_counter=0;
word_counter_dict = Counter()
lower_word_counter_dict = Counter()
char_counter_dict = Counter()
home = os.path.expanduser("~")
data_set_files = os.path.join(home,"Holmes_Training_Data1")
files = list(os.listdir(data_set_files))
for one_file in files:
    with open(os.path.join(data_set_files, one_file), 'r') as opened_one:
        text=opened_one.read()          
        sentences = sent_tokenize(text)
        sentence_counter+= len(sentences)
        for sentence in sentences:
            words = word_tokenize(sentence)
            word_counter += len(words)
            for word in words:
                word_counter_dict[word] += 1
                character_counter += len(word)
                characters = list(word)
                for character in characters:
                    char_counter_dict[character] += 1

glove_path = os.path.join(home,'data','glove', "glove.6B.100d.txt")
glove_dict = {}
with open(glove_path, 'r') as fh:
    for line in fh:
        array = line.lstrip().rstrip().split(" ")
        word = array[0]
        vector = list(map(float, array[1:]))
        if word in word_counter_dict:
            glove_dict[word] = vector
print glove_dict
                    


# # Preprocessing V2

# In[ ]:

import nltk

folder = nltk.data.find(dirpath)


print "The number of sentences =", len(corpusReader.sents())
print "The number of patagraphs =", len(corpusReader.paras())
print "The number of words =", len([word for sentence in corpusReader.sents() for word in sentence])
print "The number of characters =", len([char for sentence in corpusReader.sents() for word in sentence for char in word])

