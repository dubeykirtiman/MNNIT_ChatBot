# This is a file to connect our chatbot project with mysql database
# prequisite software for this is mysql and mysql- python connector

import mysql.connector
import openai
openai.api_key='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'

def insertquery(query,username,usermail):
	mydb=mysql.connector.connect(host="localhost",user="root",passwd="1009",database="chatbot") 
	#here implement your passwd and create a chatbot database befor running
	mycursor=mydb.cursor()
	#create table first
	#tableCreate="CREATE TABLE queries (Query varchar(1000),Username varchar(25),Usermail varchar(50),Answer varchar(500));"
	#mycursor.execute(tableCreate);
	completions=openai.Completion.create(engine='text-davinci-002',prompt=query,max_tokens=1024)
    message=completions.choices[0].text
	ins='INSERT TABLE queries (Query,Username,Usermail,Answer) VALUES("{}","{}","{}","{}");'.format(query,username,usermail,message)
	mycursor.execute(ins)
	mydb.commmit()
	print("query registered")
