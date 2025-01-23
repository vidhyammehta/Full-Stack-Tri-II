from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('loginprocess',views.loginprocess,name='loginprocess'),

    path('register',views.register,name='register'),
    path('registerprocess',views.registerprocess,name='registerprocess'),

    path('forgot',views.forgot,name='forgot'),
    path('add_admin',views.add_admin,name='add_admin'),
    path('add_sports',views.add_sports,name='add_sports'),
    path('add_sportsprocess',views.add_sportsprocess,name='add_sportsprocess'),
    path('deletesports/<int:id>',views.deletesports),
    
    path('add_event',views.add_event,name='add_event'),
    path('display_sports',views.display_sports,name='display_sports'),
    # path('display_sportsprocess',views.display_sportsprocess,name='display_sportsprocess'),

    path('display_event',views.display_event,name='display_event'),
    path('deleteevent/<int:id>',views.deleteevent),
    
    path('display_join',views.display_join,name='display_join'),
    path('deletejoin/<int:id>',views.deletejoin),

    path('display_feedback',views.display_feedback,name='display_feedback'),
    path('deletefeedback/<int:id>',views.deletefeedback),
    
    path('display_location',views.display_location,name='display_location'),
    path('deletelocation/<int:id>',views.deletelocation),

    path('display_notification',views.display_notification,name='display_notification'),
    path('deletenotification/<int:id>',views.deletenotification),

    path('changepassword',views.changepassword,name='changepassword'),
    path('changepasswordprocess',views.changepasswordprocess,name='changepasswordprocess'),

    path('display_user',views.display_user,name='display_user'),
    path('deleteuser/<int:id>',views.deleteuser),

    path('display_admin',views.display_admin,name='display_admin'),
    path('deleteadmin/<int:id>',views.deleteadmin),
    path('add_blog',views.add_blog,name='add_blog.html'),
    path('add_blogprocess',views.add_blogprocess,name='add_blogprocess'),
    path('page_report',views.page_report,name='page_report'),
    path('reportevent1',views.reportevent1,name='reportevent1'),
    path('page_report1',views.page_report1,name='page_report1'),
    path('reportevent2',views.reportevent2,name='reportevent2'),
    path('adminlogout',views.adminlogout),
    
    
]