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
                               database="ScalableMicroService", 
                               user="admin",
                               port="5433", 
                               password="Nevershare@123")
   except (Exception, psycopg2.DatabaseError) as error:
       print(error)
   return conn

# cur = conn.cursor()
# print("cur is working", cur)
# cur.close()
  
 
@app.route('/shareddbform') 
def shareddbform():
    return render_template('shareddbform.html') 


@app.route('/customerform') 
def customerform():
    return render_template('customerform.html') 


@app.route('/marketform') 
def marketform():
    return render_template('marketform.html') 
 
@app.route('/login', methods = ['POST', 'GET']) 
def login(db=connect()):
    if request.method == 'GET':
        return "Login via the login Form" 
    if request.method == 'POST':
        id = request.form['id']
        roll_no = request.form['roll_no'] 
        name = request.form['name'] 
        stud_class = request.form['stud_class'] 
        department = request.form['department'] 
        cur = db.cursor() 
        cur.execute(''' INSERT INTO hellodjangoapp_student VALUES(%s,%s,%s,%s,%s)''',(id, roll_no, 
        name, stud_class, department)) 
        cur.connection.commit()
        cur.close()
    return f"Done!!" 

@app.route('/gatein', methods = ['POST', 'GET']) 
def gatein(db=connect()):
    if request.method == 'GET':
        return "Login via the login Form" 
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname'] 
        country = request.form['country'] 
        subject = request.form['subject'] 
        cur = db.cursor() 
        cur.execute(''' INSERT INTO hellodjangoapp_customer VALUES(%s,%s,%s,%s,%s)''',(id, firstname, lastname, 
        country, subject)) 
        cur.connection.commit()
        cur.close()
    return f"Customer Feedback Registration Done!!" 


@app.route('/sendin', methods = ['POST', 'GET']) 
def sendin(db=connect()):
    if request.method == 'GET':
        return "Login via the login Form" 
    if request.method == 'POST':
        id = request.form['id']
        usrnm = request.form['usrnm'] 
        email = request.form['email'] 
        psw = request.form['psw'] 
        cur = db.cursor() 
        cur.execute(''' INSERT INTO hellodjangoapp_market VALUES(%s,%s,%s,%s)''',(id, usrnm, email, 
        psw)) 
        cur.connection.commit()
        cur.close()
    return f"Marketing Feedback Registration Done!!" 


@app.route('/')
@app.route('/index')
def index():
    return f"Welcome to this Microservice-1 Flask Application!, "
 


app.run(host='0.0.0.0', port=8008)

