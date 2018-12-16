
# coding: utf-8

# In[15]:


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
import spacy
from nltk.tokenize import PunktSentenceTokenizer


# In[51]:


sentence="On Thursday, there was a massive U.S. aerial bombardment in which more than 300 Tomahawk cruise missiles rained down on Baghdad. Earlier Saturday, Baghdad was again targeted.."


# In[63]:


words = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(words)


# In[54]:


chunkGram = r"""Chunk: {<JJ>+<NN>?}"""
chunkParser = nltk.RegexpParser(chunkGram)
chunked = chunkParser.parse(tagged)


# In[55]:


nltk_chunked=[]
for i in chunked:
    if hasattr(i,'label'):
        nltk_chunked.append(' '.join(c[0] for c in i))


# In[56]:


nltk_chunked


# In[57]:


wiki = TextBlob(sentence)


# In[58]:


textblob_list=wiki.tags
textblob_chunked=[]


# In[59]:


for i in range(len(textblob_list)):
    if (textblob_list[i][1])=='JJ':
        textblob_chunked.append(textblob_list[i][0])


# In[60]:


textblob_chunked


# In[61]:


nlp = spacy.load('en')
ex2 = nlp(sentence)
spacy_chunked = []
for word in ex2:
#     print(word.text,word.pos_,word.tag_)
    if word.tag_ == 'JJ' :
            spacy_chunked.append(word)


# In[62]:


spacy_chunked


# In[72]:


#Using majority vote to determine final list
vote=0
final_list=[]
for word in nltk_chunked:
    vote=0
    if word in textblob_chunked :
        vote+=1
    if word in str(spacy_chunked):
        vote+=1
    
    if vote >0:
        final_list.append(word)
        
    print(vote,word)


# In[71]:




