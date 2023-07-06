from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import StudentRegistration
from .models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'form': form, 'stu': stud})


# @csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        print(form, "FORM")
        if form.is_valid():
            sid = request.POST['stuid']
            name = request.POST['name']
            email = request.POST['email_id']
            password = request.POST['password']
            print(name, email, password, "AAAAAAAAAAAAAAAAAAAa")
            if sid == '':
                user = User(name=name, email_id=email, password=password)
            else:
                user = User(id=sid, name=name,
                            email_id=email, password=password)
            user.save()
            student_data = list(User.objects.values())
            return JsonResponse({"status": "Save", "student_data": student_data})
        else:
            return JsonResponse({"status": 0})
# <tr><th><label for="nameid">Name:</label></th><td><input type="text" name="name" value="var"
# class="form-control" id="nameid" maxlength="70" required></td></tr>

# <tr><th><label for="emailid">Email id:</label></th><td><ul class="errorlist"><li>This field is required.</li>
# </ul><input type="email" name="email_id" class="form-control" id="emailid" maxlength="100" required></td></tr>

# <tr><th><label for="passwordid">Password:</label></th><td><input type="password" name="password" class="form-control"
# id="passwordid" maxlength="100" required></td></tr> AAAAAAAAAAAAAAAAAAAAAaa


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        pi = User.objects.get(id=id)
        print(pi)
        pi.delete()
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 0})
# <td> <input type="button" class="btn btn-warning btn-sm btn-edit" value="Edit" data-sid="5/">
# <input type="button" class="btn btn-danger btn-sm btn-del" value="Delete" data-sid="5/"> </td>
# <td><input type="button" data-sid="5" class="btn btn-warning btn-sm btn-edit" value="Edit">
# <input type="button" data-sid="5" class="btn btn-danger btn-sm btn-del" value="Delete"> </td>


def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = User.objects.get(id=id)
        student1 = User.objects.filter(id=id)
        print(student, "student", student1)
        print(student.id, "student")
        print(student1[0].id, "student1")
        student_data = {"id": student.id, "name": student.name,
                        "email_id": student.email_id, "password": student.password}
        return JsonResponse(student_data)
