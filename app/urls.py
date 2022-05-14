import posixpath
from django.urls import path, include
from . import views
#from django.views import *

#from app import views


urlpatterns = [
    path("", views.Loginpage, name="loginpage"),
    path("index1/",views.IndexPage, name="index1"),
    path("Singup/",views.Singup, name="Singup"),
    #path("login/",views.login, name="login"),
    path("register/", views.RegisterUser, name="register"),
    #path("register/", views.RegisterUser1, name="register"),
    path("otppage/", views.OTPPage,name="otppage" ),
    path("OTP/",views.Otpverify, name ="OTP"),
    
    path("Canlogin/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.Profile,name="profile"),
    path("Canprofileupdate/<int:pk>",views.UpdateProfile,name="Canpcrofileupdate"),
    
    path("canjoblist/",views.CanidatetablePage, name="canjoblist"),
    path("CandidateLogOut/<int:pk>",views.CandidateLogOut, name="CandidateLogOut"),
    path("AppyJob/<int:pk>",views.ApplyPage, name="applyjob"),
    path("appliedjob/<int:pk>",views.ApplyJobold, name="appliedjob"),
    #path("canidateHome/<int:pk>",views.JobCountHome, name="canhome"),
    path("canidateHome/<int:pk>",views.JobCountHome, name="canhome"),
    path("jobaaplications/",views.JobApplyList,name="jobaaplications"),
    
    
    

    ##############################company side #########################

    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("Profile1/<int:pk>",views.RegisterPage,name="Profile1"),
    path("updatecompanyprofile/<int:pk>",views.UpdateCompanyProfile,name="updatecompanyprofile"),
    path("job-list/<int:pk>",views.JobList,name="JobList"),
    path("job-detail/<int:pk>",views.JobDetails,name="JobDetails"),
    path("PostJob1/<int:pk>",views.ProfileComp,name="PostJob1"),
    path("jobpost/<int:pk>", views.JobDetailsSubmit11,name="jobpost"),
    path("tables/",views.tablePage, name="tables"),
    path("companylogout/<int:pk>",views.CompanyLogOut, name="companylogout"),
    
 
 ############## admin side ###

 path("adminloginpage/", views.AdminLoginPage, name="adminloginpage"),
 path("adminstraition/", views.AdminIndexPage, name= "adminindex"),
 path("adminlogin/", views.AdminLogin, name ="adminlogin"),
 path("Adminout/", views.AdminLogout, name="Adminout"),
 path("Adminuserlist/",views.AdminUserList, name="Adminuserlist"),
 path("Admincompanylist/",views.AdminCompanyList, name="Admincompanylist"),
 path("deleteuser/<int:pk>",views.Userdelete, name="userdelted"),
 path("deleteuser/<int:pk>",views.UserAdmindelete, name="useradmindelted"),
 path("Verifycompanypage/<int:pk>", views.VerifyCompanyPage, name="verifypage"),
 path("verifymethod/<int:pk>", views.VerifyCompany, name="verifymethod"),

     
  ]
  