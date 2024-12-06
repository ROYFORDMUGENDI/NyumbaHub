from django.shortcuts import render,redirect


from nyumbaapp.forms import ImageUploadForm
from nyumbaapp.models import Seller, House1
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def agents(request):
    return render(request,'agents.html')

def contact(request):
    return render(request,'contact.html')

def properties(request):
    property=House1.objects.all()
    return render(request,'properties.html',{'property':property})

def services(request):
    return render(request,'services.html')

def property_single(request,id):
    houses=House1.objects.get(id=id)
    return render(request,'property-single.html',{'houses':houses})

def service_details(request):
    return render(request,'service-details.html')

def starterpage(request):
    return render(request,'starter-page.html')

def register(request):
    if request.method == 'POST':
        theseller=Seller(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        theseller.save()
        return redirect('login')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')


@login_required
def addhouse(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/properties')
        else:
            return render(request,'addhouse.html',{'form':form})
    else:
        form = ImageUploadForm()

        return render(request, 'addhouse.html', {'form': form})



# Create your views here.
