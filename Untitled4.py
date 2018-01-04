
# coding: utf-8

# In[1]:


get_ipython().system('pip install --user flask')


# In[21]:


from flask import Flask,request,make_response,jsonify
from ptt_crawler import Pttcrawler

app=Flask('flask-api')

@app.route('/')
def hello_world():
    message={'message':'hello world!'}
    return jsonify(message)
@app.route('/ptt_crawler',methods=['GET','POST'])
def run_crawler():
    if request.method=='GET':
        crawler=Pttcrawler('/Gossiping/',1)
    elif request.method=='POST':
        board=request.get_json().get('board','Gossiping')
        page=request.get_json().get('page',1)
        crawler=Pttcrawler(board,page)
    result=crawler.run()
    return jsonify(result)


# In[22]:


import json

resp=app.test_client().get('/')
print(resp.data)
print(json.loads(resp.data.decode()))


# In[23]:


import json

resp=app.test_client().get('/')
print(resp.data)
print(json.loads(resp.data.decode()))
print('============')
resp=app.test_client().get('/ptt_crawler')
print(json.loads(resp.data.decode())[0:3])


# In[27]:


resp=app.test_client().post('/ptt_crawler',
                           data=json.dumps({'board':'/cat/','page':1}),
                            content_type='application/json')
print(json.loads(resp.data.decode())[0:3])

