#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home Directory
def hello():
    return "Hello NLP-DL track learners. Welcome to this session."

# If you want to run this app, you must call the run()
if __name__ == '__main__':
    app.run(debug=True)

