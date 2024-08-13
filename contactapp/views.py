from django.shortcuts import render,redirect
from .models import Contact
from django.http import HttpResponse
from django.views import View


# Create your views here.
def index(request):
    if request.method=='POST':
        contact=Contact
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.phone=phone
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1>Thanks For Contact Us</h1>")
    return render(request,'index.html')

class ListView(View):
    def get(self,request):
        contact=Contact.objects.filter(user=request.user,status=False)
        return render(request,'list.html',{'contact':contact})
    

# class DeleteView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         contact=Contact.objects.get(id=id)
#         contact.delete()
#         return redirect('cntct_list')
    

# class UpdateView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         contact=Contact.objects.get(id=id)
#         form=