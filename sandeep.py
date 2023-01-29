from flask import Flask, render_template
import mysql.connector
import json

app=Flask(__name__)
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='reddy@1620',
    database='being_engineer'
)

def insert():
    cursor=mydb.cursor()
    with open('data.json') as f:
        data=json.load(f)
        
    for i in data['links']:
        stmt='insert into data_links(courseName,platform,category,courseLink) values(%s,%s,%s,%s)'
        val=(i['Course Name'],i['Platform'],i['Category'],i['CourseLink'],)
        cursor.execute(stmt,val)    
        mydb.commit()
        cursor.close()
@app.route('/')
def display():
    cursor=mydb.cursor()
    stmt='select courseName,platform,category,courseLink from data_links'
    cursor.execute(stmt)
    result=cursor.fetchall()
    return render_template('home.html',result=result)


app.run()