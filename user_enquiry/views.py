from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDataBase,UserEnquiry

def userclick(req):
    return render(req,'userclick.html')

def userreg(req):
	return render(req,'ureg.html')

def usertask(req):
	if req.method=="POST":
		n=req.POST.get('fname')
		cn=req.POST.get('phone')
		em=req.POST.get('email')
		p=req.POST.get('password')
		cp=req.POST.get('cpassword')
		user=UserDataBase.objects.filter(email=em)
		if user:
			msg="user already exist"
			return render(req,'ureg.html',{'msg':msg})
		else:
			if p == cp:
				newuser=UserDataBase.objects.create(fname=n,phone=cn,email=em,password=p)
				msg="user register successfuly"
				return render(req,'ulog.html',{'msgg':msg})
			else:
				msg="passowrd and confirm password does not match"
				return render(req,'ureg.html',{'msg':msg})

def userlog(req):
	return render(req,'ulog.html')


def ulogin(req):
	if req.method=="POST":
		e=req.POST.get('email')
		p=req.POST.get('password')
		try:
			newuser=UserDataBase.objects.get(email=e)
			if newuser.password==p:
				req.session['fname']=newuser.fname
				return render(req,'udashboard.html')
			else:
				msg="Invaild password"
				return render(req,'ulog.html',{'msg':msg})
		except UserDataBase.DoesNotExist:
			msg="User does not exits"
			return render(req,'ureg.html',{'msg':msg})
		
def eqfm(req):
	return render(req,'enquiry.html')

def eqtask(request):
	if request.method == "POST":
		n=request.POST.get('fname')
		em=request.POST.get('email')
		cn=request.POST.get('phone')
		q=request.POST.get('query')
		dum=UserEnquiry(fname=n,email=em,phone=cn,query=q)
		dum.save()
	return render(request,"udashboard.html")

def ShowPage(request):
    all_data=UserEnquiry.objects.all()
    return render(request,'showpage.html',{'key1':all_data})

def delete(req,id):
	fm=UserEnquiry.objects.get(pk=id)
	fm.delete()
	return redirect('/logindata/showpage')

def updaterec(request,id):
	if request.method=="POST":
		n=request.POST.get('fname')
		em=request.POST.get('email')
		cn=request.POST.get('phone')
		q=request.POST.get('query')
		d1=UserEnquiry(id=id,fname=n,email=em,phone=cn,query=q)
		d1.save()
		return redirect('/logindata/showpage')
	d1=UserEnquiry.objects.get(pk=id)
	return render(request,'editupdate.html',{'data':d1})