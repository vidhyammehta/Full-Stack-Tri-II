from django.urls import path
from .views import home,register,login_user,logout_user,contact_view,about,create_event,create_blog,blog,single_blog,events,single_event,joinevent_form,joineventprocess

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),   
    path('contact/', contact_view, name='contact'),
    path('about/', about, name='about'),
    path('create_event/',create_event, name='create_event'),
    path('create_blog/', create_blog, name='create_blog'),
    path('blog/', blog, name='blog'),
    path('single_blog/<int:id>',single_blog,name='single_blog.html'),
    path('events/', events, name='events'),
    path('single_event/<int:id>',single_event,name='single_event'),
    path('joinevent_form/',joinevent_form,name="joinevent_form"),
    path('joineventprocess/',joineventprocess,name='joineventprocess'),
]