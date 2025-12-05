from django.shortcuts import render ,HttpResponse,redirect
from .models import Student,User,Teacher
from django.contrib.auth import authenticate,login,logout 

# Create your views here.

def home(requset):
    return render(requset,"home.html")
    




    
def studentregister(request):
  
    if request.method=="POST":
         f=request.POST["firstname"] 
        #  l=request.POST["lastname"] 
         e=request.POST["email"]
         a=request.POST["address"] 
         p=request.POST["phone_number"]
         passw=request.POST["password"]
         u=request.POST["username"]
         g=request.POST["guardian"]
         new_user=User.objects.create_user(first_name=f,last_name=l,email=e,address=a,phone_number=p,password=passw,username=u,usertype='student',is_active=False)
         new_user.save()
         x=Student.objects.create(Student_id=new_user,guardian=g)
         x.save()
         return  HttpResponse("registration successfully")

    else:
  
     return render(request,"studentreg.html")
    





def teacherregister(request):

    if request.method=="POST":
         f=request.POST["firstname"] 
         l=request.POST["lastname"] 
         e=request.POST["email"]
         a=request.POST["address"] 
         p=request.POST["phone_number"]
         passw=request.POST["password"]
         u=request.POST["username"]
         s=request.POST["salary"]
         exp=request.POST["experience"]
         new_user=User.objects.create_user(first_name=f,last_name=l,email=e,address=a,phone_number=p,password=passw,username=u,usertype='teacher',is_staff=True,is_active=True)
         new_user.save()
         x=Teacher.objects.create(teacher_id=new_user,salary=s,experience=exp)
         x.save()
         return HttpResponse("success")
        #  return  redirect("login")

    else:
  
      return render(request,"teacherreg.html")











      

def login_view(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]
        userpass = authenticate(request, username=u, password=p)

        if userpass is not None and userpass.is_superuser == 1:
            return redirect('adminhome')

        elif userpass is not None and userpass.is_staff == 1:
            login(request, userpass)  # built-in login function
            request.session['teach_id'] = userpass.id
            return redirect("teacherhome")

        elif userpass is not None and userpass.is_active == 1:
            login(request, userpass)
            request.session['stud_id'] = userpass.id
            return redirect("studenthome")

        else:
            return HttpResponse("Invalid login")

    else:
        return render(request,'login.html')

    



def adminhome(request):
     return render(request,'adminhome.html')    
    
def teacherhome(request):
    return render(request,'teacherhome.html')

def studenthome(request):
    return render(request,'studenthome.html')

def View_student_admin(request):
     x=Student.objects.all()
     return render(request,"view_student_admin.html",{"view":x})

def view_student_teacher(request):
     x=Student.objects.all()
     return render(request,"view_student_teacher.html",{"view":x})

def view_teacher(request):
     y=Teacher.objects.all()
     return render(request,"viewteacher.html",{"data":y})


def viewteacher_student(request):
     y=Teacher.objects.all()
     return render(request,"viewteacher_student.html",{"data":y})

# def approve(request):


     
def delete(request,id):
    print(id,".......................................")
    x=Student.objects.get(id=id)
    x.delete()
    return redirect(View_student_admin)

def editstudentprofile(request):
    stud=request.session.get('stud_id')
    print(stud,"///////////////////////////////")
    student=Student.objects.get(Student_id=stud)
    user=User.objects.get(id=stud)
    return render(request,'editstudent.html',{"view":student ,"data":user})
   


def updatestudent(request,id):


   if request.method == "POST":
         stud=Student.objects.get(id=id)
         uid=stud.Student_id_id
         user=User.objects.get(id=uid)
         user.first_name=request.POST["firstname"] 
         user.last_name=request.POST["lastname"] 
         user.email=request.POST["email"]
         user.address=request.POST["address"] 
         user.phone_number=request.POST["phonenumber"] 
         stud.guardian=request.POST["guardian"] 
         user.save()
         stud.save()

         return redirect("View_student_admin")


def  approve_student(request,id):
    stud=Student.objects.select_related('Student_id').get(id=id)
    stud.Student_id.is_active=True
    stud.Student_id.save()
    return redirect("View_student_admin")
        


















def tdelete(request,id):
    print(id,".......................................")
    x=Teacher.objects.get(id=id)
    x.delete()
    return redirect(view_teacher)

def editteacher(request):
    teach=request.session.get('teach_id')
    teacher=Teacher.objects.get(teacher_id=teach)
    user=User.objects.get(id=teach)
    return render(request,'editteacher.html',{"view":teacher ,"data":user})



def updateteacher(request,id):


  if request.method == "POST":
         teach=Teacher.objects.get(id=id)
         uid=teach.teacher_id_id
         user=User.objects.get(id=uid)
         user.first_name=request.POST["firstname"] 
         user.last_name=request.POST["lastname"] 
         user.email=request.POST["email"]
         user.address=request.POST["address"] 
         user.phone_number=request.POST["phonenumber"] 
         teach.salary=request.POST["salary"] 
         teach.experience=request.POST["experience"] 

         user.save()
         teach.save()

         return redirect('view_teacher')
  






def logouts(request):
    # if "stud_id" in request.session:
        logout(request)
    #     del request.session['stud_id']
    #     print("student")
    #     return redirect('login_view')
    
    
    # else:
    #     if "teach_id" in request.session:
    #         logout(request)
    #         del request.session['teach_id']
    #         print("teacher")
    #         return redirect('login_view')
        return redirect('login_view')
  




def bootstrap(request):
    return render(request,"index.html")