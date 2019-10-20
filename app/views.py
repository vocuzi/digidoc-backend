from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import *


# Create your views here.
@csrf_exempt
def login(request):
	try:
		if not request.session.get("uid"):
			if request.method == "POST":
				# if request.POST.get("phone") and request.POST.get("otp"):
				if request.method == "POST":
					# phone = int(request.POST.get("phone"))
					phone = int(9818593192)
					phone = Doctor.objects.filter(phone=phone)
					# if int(request.POST.get("otp")) == 1001 and phone.exists():
					if phone.exists():
						# return JsonResponse({"ok":False,"err":"exists"})
						# return JsonResponse({"id":phone[0].id})
						request.session["uid"]=phone[0].id
						return redirect("/welcome/")
					return JsonResponse({"ok":False,"err":"not exists"})
				return JsonResponse({"ok":False,"err":"keys not exists"})
			return JsonResponse({"ok":False,"err":"post not exists"})
		else:
			return redirect("/welcome/")
	except Exception as e:
		return JsonResponse({"ok":False,"err":str(e)})
	return JsonResponse({"ok":False})

def welcome(request):
	try:
		# return JsonResponse({"id":request.session.get("uid")})
		if request.session.get("uid"):
			doctor = Doctor.objects.get(id=request.session.get("uid"))
			return render(request,"welcome.html",{"doctor":doctor})
		else:
			return redirect("/login/")
	except Exception as e:
		return redirect("/login/")
