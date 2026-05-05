from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Paragraph
from django.contrib import messages
import json
from django.http import JsonResponse

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Employee.objects.filter(email=email).first()

        if user:
            if user.password == password:
                request.session['empid'] = user.empid
                request.session['name'] = user.name
                request.session['phno'] = user.phno
                messages.success(request, "Login successful")
                return redirect("dashboard")
            else:
                messages.error(request, "Wrong password")
        else:
            messages.error(request, "Employee does not exist")

    return render(request, "login.html")
def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    empid = request.session.get('empid')

    if not empid:
        return redirect('login')  # user not logged in

    user = Employee.objects.filter(empid=empid).first()

    if not user:
        return redirect('login')  # invalid session

    return render(request, 'profile.html', {'user': user})



def change_password(request):
    user_id = request.session.get('empid')

    if not user_id:
        return redirect('login')

    user = Employee.objects.filter(empid=user_id).first()

    if request.method == "POST":
        old = request.POST.get("old_password")
        new = request.POST.get("new_password")
        confirm = request.POST.get("confirm_password")

        # 🔴 Step 1: check old password
        if user.password != old:
            messages.error(request, "Old password is incorrect")
            return redirect('change_password')

        # 🔴 Step 2: new == confirm
        if new != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('change_password')

        # 🔴 Step 3: prevent weak logic
        if old == new:
            messages.error(request, "New password cannot be same as old")
            return redirect('change_password')

        # ✅ Update password
        user.password = new
        user.save()

        messages.success(request, "Password updated successfully")
        return redirect('dashboard')

    return render(request, 'change_password.html')
def start_work(request):
    para = Paragraph.objects.order_by('?').first()
    return render(request, 'start_work.html', {'paragraph': para})

def submit_work(request):
    if request.method == "POST":
        data = json.loads(request.body)
        typed_text = data.get("text")

        # 👉 Save typed text (optional)
        # Work.objects.create(user=..., text=typed_text)

        # 👉 Get new paragraph
        new_para = Paragraph.objects.order_by('?').first()

        return JsonResponse({
            "new_paragraph": new_para.text
        })

def logout(request):
    request.session.flush()   # clears ALL session data
    return redirect('login')