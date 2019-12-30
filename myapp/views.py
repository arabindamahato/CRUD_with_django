from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request, "index.html")

# Display all()
def display(request):
    data_topic = Topic.objects.all() # Topic is the Class name / Table name
    data_webpage = Webpage.objects.all() # Webpage is the Class name / Webpage name
    data_access_details = Access_Details.objects.all() # Access_Details is the Class name / Webpage name

    top = {'topics':data_topic, 'webpages':data_webpage, 'access_details':data_access_details}
    return render(request, "display.html", context=top)


# Display ascending order
def display_asc(request):
    access_details_asc = Access_Details.objects.order_by('date') # order_by() ordered all the data by asc order
    access_date = {'dates':access_details_asc}
    return render(request, "display_asc.html", context=access_date)


# Display a specific record # using get(key:value)
def display_specific(request):
    # specific = Webpage.objects.get('name')    
    # specific_name = {'names':specific}    
    return render(request, "display_specific.html")  



# Display the filter data
def filter_data(request):
    filterdata = Webpage.objects.filter(top_name = "Music")
    return render(request, "filter_data.html", context={'webpage':filterdata}) 

#startswith , endswith, and contains check 
def like_data(request):
    return render(request, "like_data.html")


# form demo where accepts the topic and display the topic details in webpage_details page

def topic_form(request):
    topics = Topic.objects.all()
    if request.method == "POST":
        topic = request.POST.get("top")  # getlist is for displaying multiple dropdown data
        # topic = request.POST.getlist("top")
        web_data = Webpage.objects.filter(top_name = topic)
        return render(request, "webpage_details.html", context={"webpages":web_data})
    return render(request, "form_demo.html", context={"topics":topics})

# def topic_form(request):
#     topics = Topic.objects.all()
#     if request.method == "POST":
#         # topic = request.POST.get("top")
#         topic = request.POST.getlist("top") # getlist is for displaying multiple dropdown data
#         webpages = Webpage.objects.none()
#         for i in topic:
#             webpages = webpages | Webpage.objects.filter(top_name=i)
#         return render(request, "webpage_details.html", context={"webpages":webpages})
#     return render(request, "form_demo.html", context={"topics":topics})



#it displays the webpage details by selecting from dropdown
def web_details(request):
    webpages = Webpage.objects.all()
    return render(request, "webpage_details.html", context={"webpages":webpages})


# form demo where accepts the topic and display the topic details in webpage_details page
def topic_form2(request):
    topics = Topic.objects.all()
    if request.method == "POST":
        # topic = request.POST.get("top")
        topic = request.POST.getlist("top") # getlist is for displaying multiple dropdown data
        webpages = Webpage.objects.none()
        for i in topic:
            webpages = webpages | Webpage.objects.filter(top_name=i)
        return render(request, "webpage_details2.html", context={"webpages":webpages})
    return render(request, "form_demo2.html", context={"topics":topics})



#it displays the webpage details by selecting from dropdown
def web_details2(request):
    webpages = Webpage.objects.all()
    return render(request, "webpage_details2.html", context={"webpages":webpages})


# it insert topics into the database by using form
def create_topic(request):
    if request.method == "POST":
        top_name = request.POST.get("top")  # this "top" is the name="top" from create_form
        t = Topic.objects.get_or_create(top_name = top_name)[0]
        t.save()
    return render(request, "create_topic.html")



# it will insert webpage by using form with foreign key reference , with the help of topic dropdown 
def create_webpage(request):
    if request.method == "POST":
        top_name = request.POST.get("top")
        t=Topic.objects.get_or_create(top_name = top_name)[0]
        t.save()
        name = request.POST.get("name")
        url = request.POST.get("url")
        w = Webpage.objects.get_or_create(top_name = t, name = name, url = url)[0]
        w.save()
    topics = Topic.objects.all()
    return render(request,"create_webpage.html", context={"topics":topics})

# update 
def select_webpage(request):
    webpages = Webpage.objects.all()
    return render(request, "select_webpage_for_update.html", context={"webpages":webpages})
        
def edit_webpage(request):
    if request.method=="POST":
        name=request.POST.get("name")
        webpage=Webpage.objects.get(name=name)
        return render(request,"edit_webpage.html",context={"webpage":webpage})
    return HttpResponse("No Data Found, <br> First Select the Webpage name.<br>\
     To select webpage name Click <a href='http://localhost:8000/select-webpage'>Here</a>")


def update_webpage(request):
    if request.method=="POST":
        top_name=request.POST.get("top")
        name=request.POST.get("name")
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(top_name=top_name)[0]
        web=Webpage.objects.filter(name=name).update(top_name=t,url=url)
        t.save()
        
    return HttpResponse("<h3>Record Updated successfully</h3>")

def create_access_details(request):
    if request.method == "POST":
        name = request.POST.get("name") # form element name="name"
        w = Webpage.objects.get_or_create(name = name)[0] # name = field name
        w.save()
        date = request.POST.get("date")
        a = Access_Details.objects.get_or_create(name = w, date = date)[0]
        a.save()
    access_details = Access_Details.objects.all()
    return render(request, "create_access_details.html", context={"access_details" : access_details})



# This fumction deletes only Topic 
def delete_topic(request):
    topics = Topic.objects.all()
    if request.method == "POST":
        data = request.POST.getlist("top")
        for i in data:
            t = Topic.objects.get(top_name = i)
            t.delete()
            t.save()
        
    return render(request, "delete_topic.html", context={"topics":topics})




# This function deletes Topics as well as its reference table data ..

# Write the code here for it , take help from akshay sir note book 


# def delete_topic(request):
#     topics = Topic.objects.all()
#     if request.method == "POST":
#         data = request.POST.get("top")
#         t = Webpage.objects.filter(top_name = data)
#         t.delete()
#         t.save()
        
#         # print(topics)
#     return render(request, "delete_topic.html", context={"topics":topics})





