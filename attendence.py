#! C:\Users\ASUS\AppData\Local\Programs\Python\Python312\python.exe

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
        if(f.getvalue('t3').strip()=='Complete'):
            t.execute('select * from attendence where user_type="'+str(f.getvalue('t1'))+'" and email="'+str(f.getvalue('t2'))+'" order by sn desc')
        elif(f.getvalue('t3').strip()=='some'):
            t.execute('select * from attendence where user_type="'+str(f.getvalue('t1'))+'" and email="'+str(f.getvalue('t2'))+'" order by sn desc limit 7')
        count=t.fetchall()
        if(count!=[]):
            num=absent=present=0
            print('<table class="show"><caption>Attendence Report</caption><tr><th>Sn</th><th>Date</th><th>Reporting Time</th><th>Status</th></tr>')
            for i in count:
                num=num+1
                if(i[5].strip()=='Absent'):
                    absent=absent+1
                else:
                    present=present+1
                print('<tr><td>'+str(num)+'</td><td>'+str(i[3])+'</td><td>'+str(i[4])+'</td><td>'+str(i[5])+'</td></tr>')
            print('</table>')
            print('     '+str(absent)+'&&'+str(present))
        else:
            print('<table class="show"><caption>Attendence Report</caption><tr><td colspan="3" style="border-radius:1rem;background:pink;color:white;font-size:3rem;">No Attendence Record Available Till Now!!</td></tr>')
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
    elif(cond=='leave_sub'):
        t.execute('select * from leave_details where from_date="'+str(f.getvalue('t4'))+'" and to_date="'+str(f.getvalue('t5'))+'" and email="'+str(f.getvalue('t2'))+'"')
        if(t.fetchall()==[]):
            t.execute("insert into leave_details(user_type,email,leave_type,from_date,to_date,reason,stat) values(%s,%s,%s,%s,%s,%s,%s)",(f.getvalue('t1'),f.getvalue('t2'),f.getvalue('t3'),f.getvalue('t4'),f.getvalue('t5'),f.getvalue('t6'),'Not Approved'))
            con.commit()
            print("Successfully Created!!&&0")
        else:
            print('Already Record Exists!!')
    elif(cond=='leave_report'):
        t.execute('select * from leave_details where user_type="'+str(f.getvalue('t1'))+'" and email="'+str(f.getvalue('t2'))+'" order by sn desc')
        rs=t.fetchall()
        print('<table class="t3"><caption style="font-weight: 600;text-decoration: underline;">Leave Report</caption>')
        if(rs==[]):
            print('<tr><th colspan="4">No Leaves Taken!!</th></tr></table>')
        else:
            num=0
            print('<tr><th>SNO.</th><th>Leave Type</th><th>Date</th><th>Status</th></tr>')
            for r in rs:
                num=num+1
                print('<tr><td>'+str(num)+'</td><td>'+str(r[3])+'</td><td>'+str(r[4])+' to '+str(r[5])+'</td><td>'+str(r[7])+'</td></tr>')
            print('</table')
    elif(cond=='leave_request'):
        t.execute('select * from leave_details where stat="Not Approved" order by sn desc')
        rs=t.fetchall()
        print('<div class="leavepop"><input type="button" value="&#10006;&nbsp;Close" class="cut"><h1 align="center" style="font-size: 3rem; line-height: 4rem;" class="t5h">Leave Request</h1><table class="t5">')
        if(rs==[]):
            print('<tr><td colspan="7" style="background:pink;color:white;font-size:3rem;"><center>No Requests Yet!!</center></td></tr></table></div>')
        else:
            num=0
            print('<tr style="background-color: #427D9D; color: white;"><th>SNO.</th><th style="display:none;">SNO.</th><th>Name</th><th>Email</th><th>From-To Date</th><th style="width: 40%;">Reason</th><th colspan="2">Status</th></tr><tbody>')
            for a in rs:
                num=num+1
                t.execute('select name from signup where email="'+str(a[2])+'"')
                print('<tr><td>'+str(num)+'   </td><td style="display:none;" id="sn">'+str(a[0])+'   </td><td>'+str(t.fetchall()[0][0])+'   </td><td>'+str(a[2])+'   </td><td>'+str(a[4])+' to '+str(a[5])+'   </td><td>'+str(a[6])+'   </td><td><label class="unicode" title="Approve">&#10004;</label></td><td><label class="unicode2" title="Reject">&#10006;</label></td></tr>')
            print('</tbody></table></div>')
    elif(cond=='update_leave'):
        t.execute('update leave_details set stat="'+str(f.getvalue('t2').strip())+'" where sn='+str(f.getvalue('t1')))
        con.commit()
        print('Successfully Request Done!!&&0')
    elif(cond=='view_report_combo'):
        t.execute('select distinct name,email from signup where name!="Administrator"')
        rs=t.fetchall()
        if(rs!=[]):
            name=email=set()
            print('<option selected disabled>--Select Any Name--</option>')
            for a in rs:
                print('<option value="'+str(a[1])+'">'+str(a[0])+'</option>')
                email.add(a[1])
            print('&&<option selected disabled>--Select Any Email--</option>')
            for a in email:
                print('<option>'+str(a)+'</option>')
    elif(cond=='leave_search'):
        url='select * from leave_details where '
        name=f.getvalue('t1')
        email=f.getvalue('t2')
        fro=f.getvalue('t3')
        to=f.getvalue('t4')
        mail=''
        if(name==None and email!=None):
            mail=email
        elif(name!=None and email==None):
            mail=name
        elif(name!=None and email!=None):
            mail=name
        if(f.getvalue('t5')=='all'):
            url='select * from leave_details'
        else:
            if(fro!=None and to!=None and name==None and email==None):
                url='select * from leave_details where from_date between "'+fro+'" and "'+to+'"'
            else:
                if((name!=None or email!=None or (name!=None and email!=None)) and fro==None and to==None):
                    url=url+'email="'+mail+'"'
                elif((name!=None or email!=None or (name!=None and email!=None)) and fro!=None and to!=None):
                    url=url+'email="'+mail+'" and from_date between "'+fro+'" and "'+to+'"'
        url=url+' order by sn desc'
        t.execute(url)
        rs=t.fetchall()
        print('<table class="runtable">')
        if(rs==[]):
            print('<tr><td colspan="6" style="background:pink;color:white;font-size:2rem;"><center>No Requests Yet or Record Not Available for this record!!</center></td></tr></table></div>')
        else:
            num=0
            print('<tr style="background-color: #427D9D; color: white;"><th>SNO.</th><th>Name</th><th>Email</th><th>From-To Date</th><th>Reason</th><th>Status</th></tr><tbody>')
            for a in rs:
                num=num+1
                t.execute('select name from signup where email="'+str(a[2])+'"')
                print('<tr><td>'+str(num)+'</td><td>'+str(t.fetchall()[0][0])+'</td><td>'+str(a[2])+'</td><td>'+str(a[4])+' to '+str(a[5])+'</td><td>'+str(a[6])+'</td><td>'+str(a[7])+'</td></tr>')
            print('</tbody></table>')
    else:
        t.execute('select * from attendence order by sn desc')
        count=t.fetchall()
        if(count!=[]):
            num=0
            student=0
            employee=0
            print('<table class="show"><caption>Attendence Report</caption><tr><th>Sn</th><th>Name</th><th>User_Type</th><th>Email</th><th>Date</th><th>Reporting Time</th><th>Status</th></tr>')
            for i in count:
                num=num+1
                if(i[1].strip()=='Student'):
                    student=student+1
                else:
                    employee=employee+1
                t.execute('select name from signup where email="'+i[2]+'"')
                print('<tr><td>'+str(num)+'</td><td>'+str(t.fetchall()[0][0])+'</td><td>'+str(i[1])+'</td><td>'+str(i[2])+'</td><td>'+str(i[3])+'</td><td>'+str(i[4])+'</td><td>'+str(i[5])+'</td></tr>')
            print('</table>')
            print('     '+str(student)+'&&'+str(employee))
        else:
            print('<table class="show"><caption>Attendence Report</caption><tr><td colspan="3" style="border-radius:1rem;background:pink;color:white;font-size:3rem;">No Attendence Record Available Till Now!!</td></tr>')
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        t.close()