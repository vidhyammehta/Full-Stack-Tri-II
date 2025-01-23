from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as mcdb
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
conn=mcdb.connect(host="localhost", user="root", passwd="vidhyam", database="e-sports")
print("Successfully connected to Database - Adminapp")
cur=conn.cursor()

# Create your views here.
def home(request):
    return render(request, 'admin/home.html')
 
def about(request):
    return render(request, 'admin/about.html')

def contact(request):
    return render(request, 'admin/contact.html')

def login(request):
    return render(request, 'admin/login.html')

def loginprocess(request):
    aemail = request.POST['txt1']
    apassword = request.POST['txt2']
    cur.execute("SELECT * FROM tbl_admin WHERE Admin_Email = '{}' AND Admin_Password = '{}' ".format(aemail,apassword))
    data = cur.fetchone()
    if data is not None:
        if len(data) > 0:
            admin_db_id = data[1]
            admin_db_email = data[2]
            request.session['Admin_Id'] = admin_db_id
            request.session['Admin_Email'] = admin_db_email
            response = redirect(add_admin)
            response.set_cookie('Admin_Id', admin_db_id)
            response.set_cookie('Admin_Email', admin_db_email)
            return response
        else:
            messages.success(request, "Login Failed!")
            return render(request, 'admin/login.html')
    # conn.commit()
    messages.success(request, "Login Failed!")
    return render(request, 'admin/login.html')

def register(request):
    return render(request, 'admin/register.html')

def registerprocess(request):
    # print("Http Method: " + request.method)
    a = request.POST['txt1']
    b = request.POST['txt2']
    c = request.POST['txt3']
    cur.execute("INSERT INTO tbl_admin (Admin_Name, Admin_Email, Admin_Password) VALUES ('{}', '{}', '{}')".format(a,b,c))
    conn.commit()
    messages.success(request, "Account Created Successfully!!")
    return redirect(register)

def forgot(request):
    return render(request, 'admin/forgot.html')

def add_admin(request): 
    if 'Admin_Email' in request.COOKIES and request.session.has_key('Admin_Email'):
        admin_emails = request.session['Admin_Id']
        admin_emailc = request.COOKIES['Admin_Email']
        print("Session is name is " + admin_emails) 
        print("Cookies is name is " + admin_emailc) 
        return render(request, 'admin/add_admin.html')
    else:
        return render(request, 'admin/login.html')

def add_sports(request):
    return render(request, 'admin/add_sports.html')

def add_sportsprocess(request):
    # print("Http Method: " + request.method)
    a = request.POST['txt1']
    b = request.POST['txt2']
    cur.execute("INSERT INTO tbl_sports (Sports_Name, Sports_Details) VALUES ('{}', '{}')".format(a,b))
    conn.commit()
    messages.success(request, "Successfully sport added!")
    return redirect(add_sports)

def add_event(request):
    return render(request, 'admin/add_event.html')

def add_eventprocess(request):
    a = request.POST['txt1']
    b = request.POST['txt2']
    cur.execute("INSERT INTO tbl_event (Event_Name, Event_Desctiptions) VALUES ('{}', '{}')".format(a,b))
    conn.commit()
    messages.success(request, "Successfully Event Added!")
    return redirect(add_event)

def display_sports(request):
    cur.execute("SELECT * FROM tbl_sports")
    data = cur.fetchall() 
    print(list(data))
    return render(request,'admin/display_sports.html',{'mydata':data})

def deletesports(request,id):
    print("Delete is is,",id)
    cur.execute("DELETE FROM tbl_sports WHERE Sports_Id = {}".format(id))
    conn.commit()
    return redirect(display_sports)

def display_event(request):
    return render(request, 'admin/display_event.html')

def display_event(request):
    cur.execute('''SELECT
    tbl_event.Event_Id
    , tbl_location.Location_Name
    , tbl_user.User_Firstname
    , tbl_sports.Sports_Name
    , tbl_event.Event_Name
    , tbl_event.Event_Date
    , tbl_event.Event_Time
    , tbl_event.User_Gender
    , tbl_event.Event_Desctiptions
    , tbl_event.Player_Limit
    , tbl_event.User_Email
    , tbl_event.User_Contact
    , tbl_event.Event_Img
FROM
    tbl_location
    INNER JOIN tbl_event 
        ON (tbl_location.Location_Id = tbl_event.Location_Id)
    INNER JOIN tbl_sports 
        ON (tbl_sports.Sports_Id = tbl_event.Sports_Id)
    INNER JOIN tbl_user 
        ON (tbl_user.User_Id = tbl_event.User_Id)''')
    data = cur.fetchall() 
    print(list(data))
    return render(request,'admin/display_event.html',{'mydata':data})

def deleteevent(request,id):
    print("Delete is is,",id)
    cur.execute("DELETE FROM tbl_event WHERE Event_Id = {}".format(id))
    conn.commit()
    return redirect(display_event)

def display_join(request):
    return render(request, 'admin/display_join.html')

def display_join(request):
    cur.execute("SELECT * FROM tbl_joinevent")
    data = cur.fetchall() 
    print(list(data))
    return render(request,'admin/display_join.html',{'mydata':data})

def deletejoin(request,id):
    print("Delete is is,",id)
    cur.execute("DELETE FROM tbl_joinevent WHERE Join_Id = {}".format(id))
    conn.commit()
    return redirect(display_join)

def display_feedback(request):
    return render(request, 'admin/display_feedback.html')

def display_feedback(request):
    cur.execute("SELECT * FROM tbl_feedback")
    data = cur.fetchall() 
    print(list(data))
    return render(request,'admin/display_feedback.html',{'mydata':data})

def deletefeedback(request,id):
    print("Delete is is,",id)
    cur.execute("DELETE FROM tbl_feedback WHERE Feedback_Id = {}".format(id))
    conn.commit()
    return redirect(display_feedback)

def display_location(request):
    return render(request, 'admin/display_location.html')

def display_location(request):
    cur.execute("SELECT * FROM tbl_location")
    data = cur.fetchall() 
    print(list(data))
    return render(request,'admin/display_location.html',{'mydata':data})

def deletelocation(request,id):
    print("Delete is is,",id)
    cur.execute("DELETE FROM tbl_location WHERE Location_Id = {}".format(id))
    conn.commit()
    return redirect(display_location)

def display_notification(request):
    return render(request, 'admin/display_notification.html')

def display_notification(request):
    cur.execute("SELECT * FROM tbl_notification")
    data = cur.fetchall() 
    print(list(data))
    return render(request,'admin/display_notification.html',{'mydata':data})

def deletenotification(request,id):
    print("Delete is is,",id)
    cur.execute("DELETE FROM tbl_notification WHERE Notification_Id = {}".format(id))
    conn.commit()
    return redirect(display_notification)

def display_user(request):
    return render(request, 'admin/display_user.html')

def display_user(request):
    cur.execute('''SELECT
    tbl_user.User_Id
    , tbl_user.User_Firstname
    , tbl_user.User_Lastname
    , tbl_user.User_Gender
    , tbl_user.User_DOB
    , tbl_user.User_Contact
    , tbl_user.User_Email
    , tbl_user.User_Password
    , tbl_user.User_address
    , tbl_user.User_Pin
    , tbl_location.Location_Name
    , tbl_sports.Sports_Name
    , tbl_user.Player_img
    , tbl_user.User_Details
FROM
    tbl_sports
    INNER JOIN tbl_user 
        ON (tbl_sports.Sports_Id = tbl_user.Sports_Id)
    INNER JOIN tbl_location 
        ON (tbl_location.Location_Id = tbl_user.Location_Id)''')
    data = cur.fetchall() 
    print(list(data))
    return render(request,'admin/display_user.html',{'mydata':data})

def deleteuser(request,id):
    print("Delete is is,",id)
    cur.execute("DELETE FROM tbl_user WHERE Admin_Id = {}".format(id))
    conn.commit()
    return redirect(display_user)

def display_admin(request):
    return render(request, 'admin/display_admin.html')
    
def display_admin(request):
    cur.execute("SELECT * FROM tbl_admin")
    data = cur.fetchall() 
    print(list(data))
    return render(request,'admin/display_admin.html',{'mydata':data})

def deleteadmin(request,id):
    print("Delete is is,",id)
    cur.execute("DELETE FROM tbl_admin WHERE User_Type_Id = {}".format(id))
    conn.commit()
    return redirect(display_admin)

def changepassword(request):
    return render(request, 'admin/changepassword.html')

def changepasswordprocess(request):
    if 'Admin_Id' in request.COOKIES and request.session.has_key('Admin_Id'):
        Admin_Id = request.session['Admin_Id']
        opass = request.POST['opass']
        npass = request.POST['npass']
        cpass = request.POST['cpass']
        cur.execute("SELECT * FROM tbl_admin WHERE Admin_Id = {}".format(Admin_Id))
        db_data = cur.fetchone()
        if db_data is not None:
            if len(db_data) > 0:
                oldpassword_db=db_data[3]
                if opass == oldpassword_db:
                    if npass != cpass:
                        messages.success(request,"New and confim password not matched")
                        return render(request,'admin/changepassword.html')
                    else:
                        cur.execute("UPDATE tbl_admin SET Admin_Password = '{}' WHERE Admin_Id = '{}'".format(npass, Admin_Id))
                        conn.commit()
                        messages.success(request, "Password changed successfully")
                        return render(request,'admin/changepassword.html')
                else:
                    messages.success(request,'Old Password not matched')
                    return render(request,'admin/changepassword.html')
            else:
                redirect(changepassword)
        else:
            redirect(changepassword)
    else:
        return redirect(changepassword)
    
def page_report(request):
    cur.execute("SELECT * FROM tbl_sports")
    data = cur.fetchall()
    return render(request,'admin/page_report.html',{'mydata':data})
     
def reportevent1(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['txt1']
        cur.execute("SELECT * FROM tbl_sports")
        data = cur.fetchall()
        cur.execute("SELECT * FROM tbl_event WHERE Sports_Id = {}".format(id))
        data1 = cur.fetchall()
        return render(request,'admin/page_report.html',{'mydata':data,'mydata1':data1})
    else:
        return redirect(page_report)

def page_report1(request):
    cur.execute("SELECT * FROM tbl_sports")
    data = cur.fetchall()
    return render(request,'admin/page_report1.html',{'mydata':data})

def reportevent2(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['txt1']
        cur.execute("SELECT * FROM tbl_sports")
        data = cur.fetchall()
        cur.execute("SELECT * FROM tbl_user WHERE Sports_Id = {}".format(id))
        data1 = cur.fetchall()
        return render(request,'admin/page_report1.html',{'mydata':data,'mydata1':data1})
    else:
        return redirect(page_report1)
    
def adminlogout(request):
    del request.session['Admin_Email']
    del request.session['Admin_Id']
    response = redirect(login)
    response.delete_cookie('Admin_Id')
    response.delete_cookie('Admin_Email')
    return response
    
def add_blog(request):
    return render(request, 'admin/add_blog.html')

def add_blogprocess(request):
    a = request.POST['txt1']
    b = request.POST['txt2']
    c = request.POST['txt3']
    d = request.FILES['txt4']
    cur.execute("INSERT INTO tbl_blog (Blog_Title,Blog_Date,Blog_Details,Blog_Image) VALUES ('{}', '{}', '{}', '{}')".format(a,b,c,d))
    fs = FileSystemStorage()
    myfile = request.FILES['txt4']
    myfileupload = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(myfileupload)
    print("URL: " + uploaded_file_url)
    conn.commit()
    messages.success(request, "Successfully Blog Added!")
    return redirect(add_blog)