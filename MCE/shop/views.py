from django.shortcuts import render
from .models import Product,Contect
from math import ceil

def index(request):
    #products = Product.objects.all()
    #print(products)
   #  n=len(products)
    #nslides = n//4 + ceil((n/4)-(n//4))
    #params = {'no_of_slides': nslides,'range': range(1,nslides),'product': products}
    #allprods = [[products, range(1,nslides), nslides],[products, range(1,nslides), nslides]]


    allprods = []
    catprods = Product.objects.values('category','id')
    cats= { item['category'] for item in catprods}
    for cat in cats :
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(nslides), nslides])
        params = {'allprods': allprods}
    return render(request,'shop/Index.html', params)
def about(request):

    return render(request,'shop/about.html')
def contact(request):
    if request.method == 'POST':
        Name = request.POST.get('name','')
        Email =request.POST.get('email','')
        Call=request.POST.get('call','')
        City=request.POST.get('city','')
        State=request.POST.get('state','')
        Zip=request.POST.get('zip','')
        desc=request.POST.get('desc','')
        contect=Contect(Name=Name,Email=Email,Call=Call,City=City,State=State,Zip=Zip,desc=desc)
        contect.save()
    return render(request, 'shop/contact.html')
def tracker(request):
    return render(request, 'shop/tracker.html')
def prodview(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodview.html',{'product':product[0]})
def chackout(request):
    return render(request, 'shop/chackout.html')
def search(request):
    return render(request, 'shop/search.html')
