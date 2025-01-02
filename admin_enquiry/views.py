from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import admindatabase

def adminclick(req):
    return render(req,'adminclick.html')

def adminreg(req):
	return render(req,'areg.html')

def regtask(request):
	if request.method == "POST":
		n=request.POST.get('fname')
		cn=request.POST.get('phone')
		em=request.POST.get('email')
		p=request.POST.get('password')
		cp=request.POST.get('cpassword')
		user=admindatabase.objects.filter(email=em)
		if user:
			msg= "admin already exist"
			return render(request,'areg.html',{'msg':msg})
		else:
			if p == cp:
				newuser = admindatabase.objects.create(fname=n,phone=cn,email=em,password=p)
				msg = "Admin register Successfully"
				return render(request,'alog.html',{'msg':msg})
			else:
				msg = "Password and Confirm Password Doesnot Match"
				return render(request,"areg.html",{'msg':msg})


	
def adminlog(req):
	return render(req,'alog.html')

def alogin(req):
	if req.method=="POST":
		e=req.POST.get('email')
		p=req.POST.get('password')
		try:
			newuser=admindatabase.objects.get(email=e)
			if newuser.password==p:
				req.session['fname']=newuser.fname
				return render(req,"adashboard.html")
			else:
				msg="Invaild Password"
				return render(req,'alog.html',{'msg':msg})
		except admindatabase.DoesNotExist:
			msg="User does not exits"
			return render(req,'areg.html',{'msg':msg})









