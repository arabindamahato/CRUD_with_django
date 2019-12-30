from django.urls import path
from myapp import views
app_name = 'myapp'

urlpatterns = [
    
    path('',views.index, name='index'),
    path('display/',views.display, name='display'), # display all data 
    path('display-asc/',views.display_asc, name='display_asc'), # display all data in asc order
    path('display-specific/',views.display_specific, name='display_specific'),
    path('filter-data/',views.filter_data, name='filter_data'),
    path('like-data/',views.like_data, name='like_data'),

    # display topic details by submitting single topic by select option
    path('form/',views.topic_form, name='topic_form'),
    path('web-details/',views.web_details, name='web_details'),

    # display topic details by submitting multiple topic by checkbox
    path('form2/',views.topic_form2, name='topic_form2'),
    path('web-details2/',views.web_details2, name='web_details2'),

    # insert topic by form 
    path('create-topic/',views.create_topic, name='create_topic'),
    

    # insert webpage by form with foreign key 
    path('create-webpage/',views.create_webpage, name='create_webpage'),

    # select webpage for update by dropdown  
    path('select-webpage/',views.select_webpage, name='select_webpage'),

    # edit webpage details for update in form  
    path('edit-webpage/',views.edit_webpage, name='edit_webpage'),

    # edit webpage details for update in form  
    path('update-webpage/',views.update_webpage, name='update_webpage'),

    # insert access details by form with foreign key 
    path('create-access-details/',views.create_access_details, name='create_access_details'),

    # delete topic by form 
    path('delete-topic/',views.delete_topic, name='delete_topic'),






    
]


