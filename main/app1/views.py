from django.shortcuts import render,redirect
from app1.models import form 
from django.core.paginator import Paginator



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']


        data=form(
            username=username,
            password=password,
            email=email,
        )

        data.save()
        
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
       

        data=form.objects.filter(email=email,password=password)
        if data.count() > 0:
            mydata = data.values()[0]
         
            request.session['user'] = mydata.get('username')
            return redirect('/home/')
        else:
            return render(request,'error.html')
        
        
    
    return render(request,'login.html')


def homepage(request):
    # if 'user' not in request.session:
    #     return render(request,'login.html')

     
    
    name = request.session['user']
    return render(request, 'welcome.html',{'name':name})
    
  
def logout(request):

    
    del request.session['user']
    return redirect('/login/')  


def viewdata(request):
    my_objects =form.objects.all()
    paginator = Paginator(my_objects, 5) # Display 25 objects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'viewdata.html',{'page_obj':page_obj})
 