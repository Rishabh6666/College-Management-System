from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import AddModel
from .forms import AddForm
from .models import UploadModel
from .forms import UploadForm
from .models import PollModel
from .forms import PollForm
from .models import AnotesModel
from .forms import AnotesForm

def pnf(request,exception):
	return redirect("feed")

def feed(request):
	data = PollModel.objects.all()
	return render(request,"feed.html",{"data":data})
def vfeed(request):
	data = PollModel.objects.all()
	return render(request,"vfeed.html",{"data":data})
	

def create(request):
	if request.method=="POST":
		data = PollForm(request.POST)
		if data.is_valid():
			data.save()
			msg = "poll created"
			fm = PollForm()
			return render(request,"create.html",{"fm":fm,"msg":msg})
		else:
			msg = "check errors"
			fm = PollForm()
			return render(request,"create.html",{"fm":data,"msg":msg})
	else:
		fm = PollForm()
		return render(request,"create.html",{"fm":fm})
def vote(request,id):
	data = PollModel.objects.get(id=id)
	if request.method == "POST":
		op = request.POST.get("op")
		if op == "op1":
			data.op1c += 1
		elif op == "op2":
			data.op2c += 1
		else:
			data.op3c += 1
		data.save()
		return redirect("home")
	else:
		return render(request,"vote.html",{"data":data})

def result(request,id):
	data = PollModel.objects.get(id=id)
	return render(request,"result.html",{"data":data})

def remove(request,id):
	up = UploadModel.objects.get(sid=id)
	up.delete()
	return redirect("view")

def nremove(request,id):
	up = AnotesModel.objects.get(sid=id)
	up.delete()
	return redirect("vnotes")


def main(request):
	return render(request,"main.html")

def tlogin(request):
	if request.user.is_authenticated:
		return redirect("thome")
	elif request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
		if usr is None:
			return render(request,"login.html", {"msg":"invalid login"})
		else:
			login(request,usr)
			return redirect("thome")
	else:
		return render(request,"tlogin.html")

def tsignup(request):
	if request.user.is_authenticated:
		return redirect("thome")
	elif request.method == "POST":
		un = request.POST.get("un")
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		if pw1 == pw2:
			try:
				usr = User.objects.get(username=un)
				return render(request,"tsignup.html",{"msg":"user already exists"})
			except User.DoesNotExist:
				usr = User.objects.create_user(username=un,password=pw1)
				usr.save()
				return redirect("tlogin")
		else:
			return render(request,"tsignup.html",{"msg":"password did not match"})
	else:
		return render(request,"tsignup.html")

def home(request):
	if request.user.is_authenticated:
		return render(request,"home.html")
	else:
		return redirect("ulogin")
def thome(request):
	if request.user.is_authenticated:
		return render(request,"thome.html")
	else:
		return redirect("tlogin")

def ulogin(request):
	if request.user.is_authenticated:
		return redirect("home")
	elif request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
		if usr is None:
			return render(request,"login.html", {"msg":"invalid login"})
		else:
			login(request,usr)
			return redirect("home")
	else:
		return render(request,"login.html")

def usignup(request):
	if request.user.is_authenticated:
		return redirect("home")
	elif request.method == "POST":
		un = request.POST.get("un")
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		if pw1 == pw2:
			try:
				usr = User.objects.get(username=un)
				return render(request,"signup.html",{"msg":"user already exists"})
			except User.DoesNotExist:
				usr = User.objects.create_user(username=un,password=pw1)
				usr.save()
				return redirect("ulogin")
		else:
			return render(request,"signup.html",{"msg":"password did not match"})
	else:
		return render(request,"signup.html")

def ulogout(request):
	logout(request)
	return redirect("main")
def tlogout(request):
	logout(request)
	return redirect("main")

def addmin(request):
	return render(request,"addmin.html")


def student(request):
	data = AddModel.objects.all()
	return render(request,"student.html",{"data":data})

def snotes(request):
	data = AnotesModel.objects.all()
	return render(request,"snotes.html",{"data":data})

	
def upload(request):	
	if request.method == "POST":
		data = UploadForm(request.POST, request.FILES)
		if data.is_valid():
			data.save()
			msg = "Assignment Submitted"
			um = UploadForm()
			return render(request,"upload.html",{"um":um,"msg":msg})
		else:
			msg="check error"
			return render(request,"upload.html",{"um":data,"msg":msg})
	
	else:
		um = UploadForm()
		return render(request,"upload.html",{"um":um})


	

def add(request):
	if request.method == "POST":
		data = AddForm(request.POST, request.FILES)
		if data.is_valid():
			data.save()
			msg = "Assignment Added"
			fm = AddForm()
			return render(request,"add.html",{"fm":fm,"msg":msg})
		else:
			msg="check error"
			return render(request,"add.html",{"fm":data,"msg":msg})
	
	else:
		fm = AddForm()
		return render(request,"add.html",{"fm":fm})

def anotes(request):
	if request.method == "POST":
		data = AnotesForm(request.POST, request.FILES)
		if data.is_valid():
			data.save()
			msg = "Notes Added"
			fm = AnotesForm()
			return render(request,"anotes.html",{"fm":fm,"msg":msg})
		else:
			msg="check error"
			return render(request,"anotes.html",{"fm":data,"msg":msg})
	
	else:
		fm = AnotesForm()
		return render(request,"anotes.html",{"fm":fm})
def vnotes(request):
	data = AnotesModel.objects.all()
	return render(request,"vnotes.html",{"data":data})



		

def view(request):
	data = UploadModel.objects.all()
	return render(request,"view.html",{"data":data})



