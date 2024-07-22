"""
URL configuration for classroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CoursesUpload.views import InformationsPDF, UploadPDFform, SuccessPage, InformationsPDFList, download_pdf
from auth_app.views import main, sign_up, loginType, student_home, teacher_home
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('download/<int:course_id>/', download_pdf, name='download_pdf'),
    path('register-pdf/upload-pdf/success/courses-list/', InformationsPDFList, name='courses_list2'),
    path('courses-list/', InformationsPDFList, name='courses_list'),
    path('register-pdf/upload-pdf/success/', SuccessPage, name='success'),
    path('register-pdf/upload-pdf/', UploadPDFform, name='upload_pdf'),
    path('register-pdf/', InformationsPDF, name='info_pdf'),
    path('login/accounts/profile/student_home', student_home, name='student_home'),
    path('login/accounts/profile/teacher_home', teacher_home, name='teacher_home'),
    path('sign-up/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('sign-up/', sign_up, name='signup'),
    path('login/', loginType, name='login'),
    path('', main, name='accueil'),
    path('admin/', admin.site.urls),
]
