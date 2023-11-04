#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost', user='attendence', passwd='attendence',database='attendence')
t=con.cursor()
try:
    f=cgi.FieldStorage()
    cond=f.getvalue('cond')
    if(cond=='entry'):
        t.execute('select * from signup where email="'+str(f.getvalue('t2'))+'"')
        if(t.fetchall()==[]):
            if(f.getvalue('t3')=='Student'):
                t.execute("insert into signup(name,email,user_type,class,roll,phone,sec_q,ans,pass) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(f.getvalue('t1'),f.getvalue('t2'),f.getvalue('t3'),f.getvalue('t4'),f.getvalue('t5'),f.getvalue('t7'),f.getvalue('t9'),f.getvalue('t10'),f.getvalue('t11')))
            else:
                t.execute("insert into signup(name,email,user_type,faculty,phone,sec_q,ans,pass) values(%s,%s,%s,%s,%s,%s,%s,%s)",(f.getvalue('t1'),f.getvalue('t2'),f.getvalue('t3'),f.getvalue('t6'),f.getvalue('t8'),f.getvalue('t9'),f.getvalue('t10'),f.getvalue('t11')))
            con.commit()
            print("Successfully Created!!&&0")
        else:
            print('Already Email Exists!!')
    elif(cond=='login'):
        t.execute('select * from signup where email="'+str(f.getvalue('t1'))+'" and pass="'+str(f.getvalue('t2'))+'"')
        rs=t.fetchall()
        if(rs!=[]):
            print(rs[0][1],rs[0][2],rs[0][3],sep="&&")
        else:
            print(0)
    elif(cond=='forgot'):
        t.execute('select * from signup where email="'+str(f.getvalue('t1'))+'" and sec_q="'+str(f.getvalue('t4'))+'" and ans="'+str(f.getvalue('t3'))+'"')
        if(t.fetchall()!=[]):
            t.execute('update signup set pass="'+str(f.getvalue('t2'))+'" where email="'+str(f.getvalue('t1'))+'"')
            con.commit()
            print('Password Updated Succesfully!!&&0')
        else:
            print('Please Enter Correct Cerenditals!!')
    elif(cond=='report_run'):
        t.execute('select * from attendence where user_type="'+str(f.getvalue('t1'))+'" and email="'+str(f.getvalue('t2'))+'" order by sn desc')
        count=t.fetchall()
        if(count!=[]):
            num=0
            print('<table class="show"><caption>Report</caption><tr><th>Sn</th><th>Date</th><th>Reporting Time</th><th>Status</th></tr>')
            for i in count:
                num=num+1
                print('<tr><td>'+str(num)+'</td><td>'+str(i[3])+'</td><td>'+str(i[4])+'</td><td>'+str(i[5])+'</td></tr>')
            print('</table>')
        else:
            print('<table class="show"><caption>Report</caption><tr><td colspan="3" style="border-radius:1rem;background:pink;color:white;font-size:3rem;">No Attendence Record Available Till Now!!</td></tr>')
    elif(cond=='report_sub'):
        from datetime import datetime, timedelta
        given_date = datetime.strptime(f.getvalue('t3'), "%Y-%m-%d")
        one_day_before = given_date - timedelta(days=1)
        one_day_before_str = one_day_before.strftime("%Y-%m-%d")
        t.execute('select * from attendence where user_type="'+str(f.getvalue('t1'))+'" and email="'+str(f.getvalue('t2'))+'" and da="'+one_day_before_str+'"')
        if(t.fetchall()==[]):
            t.execute("insert into attendence(user_type,email,da,stat) values(%s,%s,%s,%s)",(f.getvalue('t1'),f.getvalue('t2'),str(one_day_before_str),'Absent'))
            con.commit()
        t.execute('select * from attendence where user_type="'+str(f.getvalue('t1'))+'" and email="'+str(f.getvalue('t2'))+'" and da="'+str(f.getvalue('t3'))+'"')
        if(t.fetchall()==[]):
            t.execute("insert into attendence(user_type,email,da,dat,stat) values(%s,%s,%s,%s,%s)",(f.getvalue('t1'),f.getvalue('t2'),f.getvalue('t3'),f.getvalue('t4'),'Present'))
            con.commit()
            print('Successfully Attendence Done!!')
        else:
            print('Already Submitted!!')
    elif(cond=='profile_run'):
        t.execute('select phone from signup where email="'+str(f.getvalue('t1'))+'"')
        rs=t.fetchall()
        print(rs[0][0]+'&&')
        t.execute('select * from profile where email="'+str(f.getvalue('t1'))+'"')
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                for i in a:
                    print(str(i)+'&&')
    elif(cond=='update'):
        t.execute('select * from profile where email="'+str(f.getvalue('t2'))+'"')
        if(t.fetchall()==[]):
            t.execute("insert into profile(name,email,cont,dob,gender,stat,dist,pin,loaction,about) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(f.getvalue('t1'),f.getvalue('t2'),f.getvalue('t3'),f.getvalue('t4'),f.getvalue('t5'),f.getvalue('t6'),f.getvalue('t7'),f.getvalue('t8'),f.getvalue('t9'),f.getvalue('t10')))
        else:
            t.execute('update profile set name="'+str(f.getvalue('t1'))+'",cont="'+str(f.getvalue('t3'))+'",dob="'+str(f.getvalue('t4'))+'",gender="'+str(f.getvalue('t5'))+'",stat="'+str(f.getvalue('t6'))+'",dist="'+str(f.getvalue('t7'))+'",pin="'+str(f.getvalue('t8'))+'",loaction="'+str(f.getvalue('t9'))+'",about="'+str(f.getvalue('t10'))+'" where email="'+f.getvalue('t2')+'"')
        con.commit()
        print('Profile Updated Succesfully!!&&0')
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        t.close()