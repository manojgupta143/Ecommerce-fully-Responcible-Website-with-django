from math import ceil
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


from sweetvillaApp .models import Product,Contact
def home(request):
    cake=Product.objects.filter(cetegory='cake')
    icecream=Product.objects.filter(cetegory='ice cream')
    punjabi=Product.objects.filter(cetegory='punjabiSweet')
    bengoli=Product.objects.filter(cetegory='bengali sweet')
    sauth=Product.objects.filter(cetegory='sauthindianSweet')
    indian=Product.objects.filter(cetegory='indianSweet')
    gujrati=Product.objects.filter(cetegory='gujratisweet')
    international=Product.objects.filter(cetegory='internationalSweet')
    params={'cake':cake,'ic':icecream,'pb':punjabi,'bs':bengoli,'sauth':sauth,'ind':indian,'gj':gujrati,'inter':international }
    return render(request,'myproj/home.html',params)
@login_required
def about(request):
    return render(request,'myproj/aboutus.html')
@login_required
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact =Contact(name=name, email=email, phone=phone, detail=desc)
        contact.save()
    return render(request,'myproj/contactus.html')
@login_required
def tracker(request):
    return render(request,'myproj/tracker.html')
@login_required
def search(request):
    return render(request,'myproj/search.html')
def productView(request, id):
    product=Product.objects.filter(id=id)
    return render(request, "myproj/prodView.html",{'product':product})
def checkout(request):
    return render(request,'myproj/checkout.html')
def feedback(request):
    return render(request,'myproj/feedback.html')
@login_required
def indianSweet(request):
    products= Product.objects.filter(cetegory='indianSweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products,}
    return render(request,'myproj/indian.html',params)
@login_required
def punjabiSweet(request):
    products= Product.objects.filter(cetegory='punjabiSweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/punjabi.html',params)
@login_required
def sauthIndianSweet(request):
    products= Product.objects.filter(cetegory='sauthindiansweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/sauthindian.html',params)
@login_required
def bengaliSweet(request):
    products= Product.objects.filter(cetegory='bengali sweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/bengali.html',params)
@login_required
def internationalsweet(request):
    products= Product.objects.filter(cetegory='internationalSweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/international.html',params)
@login_required
def icecream(request):
    products= Product.objects.filter(cetegory='ice cream')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/icecream.html',params)
@login_required
def cake(request):
    products= Product.objects.filter(cetegory='cake')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/cake.html',params)
@login_required
def gujratisweet(request):
    products= Product.objects.filter(cetegory='gujratiSweet')
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'myproj/cake.html',params)
from sweetvillaApp.forms import SignupForm
from django.http import HttpResponseRedirect
def signup_form(request): 
    form=SignupForm() 
    if request.method=='POST': 
       form=SignupForm(request.POST)
       if form.is_valid(): 
          user=form.save() 
          user.set_password(user.password) 
          user.save() 
       return HttpResponseRedirect('/accounts/login/') 
    else:
        return render(request,'myproj/signup.html',{'form':form})
def logout_view(request): 
    return render(request,'myproj/logout.html') 





# Create your views here.


# Create your views here.
