from django.urls import path
from sampleapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("studentregister",views.studentregister,name="studentregister"),
    path("teacherregister",views.teacherregister,name="teacherregister"),
    path("adminhome",views.adminhome,name="adminhome"),
     path("studenthome",views.studenthome,name="studenthome"),
    path("teacherhome",views.teacherhome,name="teacherhome"),
    path("teacherhome",views.teacherhome,name="teacherhome"),
    path("View_student_admin",views.View_student_admin,name="View_student_admin"),


    path("view_teacher",views.view_teacher,name="view_teacher"),
    path("delete/<int:id>",views.delete,name="delete"),
    path('tdelete/<int:id>', views.tdelete, name='tdelete'),
    path("updateteacher/<int:id>",views.updateteacher,name="updateteacher"),
    path("editteacher",views.editteacher,name="editteacher"),
     path("updatestudent/<int:id>",views.updatestudent,name="updatestudent"),
    path('editstudentprofile', views.editstudentprofile,name='editstudentprofile'),
    path("view_student_teacher",views.view_student_teacher,name="view_student_teacher"),


    path("approve_student/<int:id>",views.approve_student,name="approve_student"),

    path("viewteacher_student",views.viewteacher_student,name="viewteacher_student"),

    path("logout",views.logouts,name="logout"),

    path("bootstrap",views.bootstrap,name="bootstrap"),



  ]