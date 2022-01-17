from django.shortcuts import render
import mysql.connector as sql
fn = ''
ln = ''
s= ''
em = ''
pwd = ''



# Create your views here.
def registeraction(request):
    global fn, ln, s, em, pwd
    if request.method=="POST":
        m = sql.connect(host = "localhost", user = "root", password="Arshjain123", database = 'assignmentdjango')
        cursor = m.cursor()
        data = request.POST
        for key, value in data.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c = "insert into users Values ('{}','{}','{}','{}','{}')".format(fn, ln, s, em, pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')