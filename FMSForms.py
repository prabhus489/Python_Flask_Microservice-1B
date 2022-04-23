from flask import Flask,render_template, request 
import psycopg2
 
app = Flask(__name__) 
 

'''
def connect():
    conn = None
    try:
        Key1 = 'snjdnajindiu@1234'
        Key2 = 'jksndfjoasnf@chat'
        File_Name = 'filepath/config.properties'
        Pg_Conn_Dict = get_pg_conn_details(Key2, File_Name, Key1)
        conn = psycopg2.connect(host=Pg_Conn_Dict["HostName"], database=Pg_Conn_Dict["DBName"],
                                user=Pg_Conn_Dict["UserName"], port=Pg_Conn_Dict["Port"],
                                password=Pg_Conn_Dict["Password"])
        # conn = psycopg2.connect(host='', database='',
        #                         user='', port='',
        #                         password='')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn
'''

def connect():
   conn = None
   try:
       conn = psycopg2.connect(host="us-west-2.fa6fca4b-3c0f-45e2-8e9d-029747d86672.aws.ybdb.io", 
                               database="ScalableFlaskService", 
                               user="admin",
                               port="5433", 
                               password="Nevershare@123")
   except (Exception, psycopg2.DatabaseError) as error:
       print(error)
   return conn

# cur = conn.cursor()
# print("cur is working", cur)
# cur.close()
 
@app.route('/form') 
def form():
    return render_template('form.html') 
 
@app.route('/login', methods = ['POST', 'GET']) 
def login(db=connect()):
    if request.method == 'GET':
        return "Login via the login Form"
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cur = db.cursor() 
        print(cur)
        cur.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age)) 
        cur.connection.commit() 
        cur.close()
    return f"Done!!" 
 

app.run(host='0.0.0.0', port=5000)