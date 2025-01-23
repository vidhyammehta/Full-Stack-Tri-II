from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password  # For password verification
from .models import UserProfile,Contact,Event,Blog  # Import UserProfile
from datetime import datetime
import mysql.connector as mcdb

conn = mcdb.connect(host="localhost", user="root", passwd="vidhyam", database="e-sports")
print("Successfully connected to Database - Userapp")
cur=conn.cursor()

# Home View
def home(request):
    return render(request, "user/home.html")

# Login View
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            # Retrieve the user from UserProfile
            user_profile = UserProfile.objects.get(email=email)

            # Verify the password
            if check_password(password, user_profile.password):  # Password should be hashed in DB
                # Simulate session management
                request.session['user_id'] = user_profile.id
                request.session['user_name'] = user_profile.firstname
                messages.success(request, "Login successful!")
                return redirect("home")
            else:
                messages.error(request, "Invalid email or password.")
                return redirect("login")
        except UserProfile.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
            return redirect("login")
    
    return render(request, "user/login.html")

# Register View
def register(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        gender = request.POST.get("gender")
        password = request.POST.get("password")

        # Check if the email already exists
        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        # Save user in UserProfile
        hashed_password = password  # Add hashing before saving in production
        user_profile = UserProfile.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            contact=contact,
            gender=gender,
            password=hashed_password
        )
        user_profile.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect("login")
    
    return render(request, "user/register.html")

# Logout View
def logout_user(request):
    # Clear the session
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect("home")

# Contact View
def contact_view(request):
    if request.method == "POST":
        # Collect form data
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate required fields
        if not (first_name and last_name and email and phone and subject and message):
            messages.error(request, "All fields are required.")
            return redirect('contact')

        # Save to the database
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        # Show success message
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, "user/contact.html")

def about(request):
    return render(request, 'user/about.html')


def create_event(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        sports_name = request.POST.get('sports_name')
        start_date = request.POST.get('start_date')
        start_time = request.POST.get('start_time')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        event_description = request.POST.get('event_description')
        player_limit = request.POST.get('player_limit')
        price = request.POST.get('price')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        upload_image = request.FILES.get('upload_image')

        # Validate data (you can add more validation rules as needed)
        if not event_name or not sports_name or not start_date or not start_time:
            messages.error(request, "Please fill out all required fields.")
        else:
            # Save event to the database
            event = Event(
                event_name=event_name,
                sports_name=sports_name,
                start_date=start_date,
                start_time=start_time,
                gender=gender,
                address=address,
                event_description=event_description,
                player_limit=player_limit,
                price=price,
                email=email,
                contact_number=contact_number,
                upload_image=upload_image,
            )
            event.save()
            messages.success(request, "Event created successfully!")
            return redirect('event_list')  # Redirect to an event list page (implement it as needed)

    return render(request, 'user/create_event.html')


def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        #date = request.POST.get('blog_date')
        blog_content = request.POST.get('blog_content')
        blog_image = request.FILES.get('blog_image')

        # Validate required fields
        if not title or not author or not blog_content:
            messages.error(request, "Please fill out all required fields.")
        else:
            # Save blog to the database
            blog = Blog(
                title=title,
                author=author,
                blog_content=blog_content,
                blog_image=blog_image,
                #date=datetime.strptime(date, '%Y-%m-%d')
            )
            blog.save()
            messages.success(request, "Blog created successfully!")
            return redirect('user/blog.html')  # Redirect to a blog list page (implement as needed)

    return render(request, 'user/create_blog.html')

def blog(request):
    cur.execute("SELECT * FROM tbl_blog")   
    data = cur.fetchall() 
    print(list(data))
    return render(request,'user/blog.html',{'mydata':data})

def single_blog(request,id):
    id = id
    cur.execute("SELECT * FROM tbl_blog WHERE Blog_Id ='{}'".format(id))
    data = cur.fetchall() 
    print(list(data))
    return render(request, 'user/single_blog.html',{'mydata':data})

def events(request):
    # cur.execute("SELECT * FROM tbl_event")
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
    tbl_event
    INNER JOIN tbl_location 
        ON (tbl_event.Location_Id = tbl_location.Location_Id)
    INNER JOIN tbl_sports 
        ON (tbl_sports.Sports_Id = tbl_event.Sports_Id)
    INNER JOIN tbl_user 
        ON (tbl_user.User_Id = tbl_event.User_Id)''')

    data = cur.fetchall() 
    # print(list(data))
    return render(request, 'user/events.html',{'mydata':data})

def single_event(request,id):
    id = id
    cur.execute('''SELECT
    tbl_event.Event_Id
    , tbl_location.Location_Name
    , tbl_user.User_Firstname
    , tbl_sports.Sports_Name
    , tbl_event.Event_Name
    , tbl_event.Event_Date
    , tbl_event.User_Gender
    , tbl_event.Event_Time
    , tbl_event.Event_Desctiptions
    , tbl_event.Player_Limit
    , tbl_event.User_Email
    , tbl_event.User_Contact
    , tbl_event.Event_Img
FROM
    tbl_sports
    INNER JOIN tbl_event 
        ON (tbl_sports.Sports_Id = tbl_event.Sports_Id)
    INNER JOIN tbl_location 
        ON (tbl_location.Location_Id = tbl_event.Location_Id)
    INNER JOIN tbl_user 
        ON (tbl_user.User_Id = tbl_event.User_Id) WHERE  tbl_event.Event_Id = '{}' '''.format(id))
    data = cur.fetchall() 
    print(list(data))
    return render(request, 'user/single_event.html',{'mydata':data})

def joinevent_form(request):
    return render(request, 'user/joinevent_form.html')

def joineventprocess(request):
    if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
        a = request.POST['name']
        b = request.POST['message'] 
        id = request.session['user_id']
        estatus = "Pending"
        cur.execute("INSERT INTO tbl_joinevent (User_Name,Message,User_Id,Join_Status) VALUES ('{}', '{}','{}', '{}')".format(a,b,id,estatus))
        conn.commit()
        messages.success(request, "Event Join Successfully!!")
        return redirect(joinevent_form)
    return redirect(login_user)
