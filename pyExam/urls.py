"""pyExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import users.views
import exams.views
import problems.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^login/$', users.views.login),
    url(r'^loginCheck/$', users.views.loginCheck),
    url(r'^register/$', users.views.register),
    url(r'^registerCheck/$', users.views.registerCheck),

    url(r'^showProblems/$', problems.views.showProblems),
    url(r'^addProblem/$', problems.views.addProblem),
    url(r'^addProblems/$', problems.views.addProblems),
    url(r'^editProblem/$', problems.views.editProblem),
    url(r'^deleteProblem/$', problems.views.deleteProblem),
    url(r'^editProblemCheck/$', problems.views.editProblemCheck),
    url(r'^addProblemCheck/$', problems.views.addProblemCheck),
    url(r'^addProblemsCheck/$', problems.views.addProblemsCheck),

    url(r'^showExams/$', exams.views.showExams),
    url(r'^addExam/$', exams.views.addExam),
    url(r'^addExamCheck/$', exams.views.addExamCheck)
]
