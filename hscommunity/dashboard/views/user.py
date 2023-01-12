from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import AllUser, UserRoll


def user(request):
    UserList = AllUser.objects.all()
    context = {
        'user_list': UserList
    }
    return render(request, "dashboard/user/user.html", context)


def AddUser(request):
    if request.method == 'POST':
        FirstName = request.POST.get('first_name')
        LastName = request.POST.get('last_name')
        EmailId = request.POST.get('email_id')
        ContactNo = request.POST.get('contact_no')
        UserRole = request.POST.get('user_role')
        InsertUser = AllUser(first_name=FirstName, last_name=LastName, email_id=EmailId, contact_number=ContactNo,
                             roll=UserRole)
        InsertUser.save()
        return redirect('/dashboard/user')
    UserRoles = UserRoll.objects.all()
    context = {
        'UserRole': UserRoles,
    }
    return render(request, "dashboard/user/create-user.html", context)


def UpdateUser(request, id):
    UserList = AllUser.objects.get(id=id)
    if request.method == 'POST':
        UserList.first_name = request.POST.get('first_name')
        UserList.last_name = request.POST.get('last_name')
        UserList.email_id = request.POST.get('email_id')
        UserList.contact_number = request.POST.get('contact_no')
        UserList.roll = request.POST.get('user_role')
        UserList.save()
        return redirect('/dashboard/user')
    UserRoles = UserRoll.objects.all()
    context = {
        'UserRole': UserRoles,
        'user_list': UserList,
    }
    return render(request, "dashboard/user/update-user.html", context)


def DeleteUser(request, id):
    UserList = AllUser.objects.get(id=id)
    if request.method == 'POST':
        UserList.delete()
        return redirect('/dashboard/user')
    UserRoles = UserRoll.objects.all()
    context = {
        'UserRole': UserRoles,
        'user_list': UserList,
    }
    return render(request, "dashboard/user/user-delete.html", context)
