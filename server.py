
# coding: utf-8

# In[ ]:


from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))


x=input("what is your name")
print(x)

