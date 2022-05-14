from asyncio.windows_events import NULL
from contextlib import redirect_stderr, redirect_stdout
from csv import unregister_dialect
import email
from email import message
from ftplib import all_errors
from itertools import count
#from typing import ParamSpecArgs
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
import pkg_resources
#from platformdirs import user_log_dir

from .models import*
from random import randint
from django.http import HttpResponse

# Create your views here.
def IndexPage(request):
    return render(request,"app/index1.html")

def tablePage(request):
     all_job =   JobPostDetails.objects.all()
     return render(request,"app/company/jobpostlist.html",{'all_job':all_job})

def CompanyLogOut(request,pk):
    user = UserMaster.objects.get(pk=pk)
    #del request.session['email']
    #del request.session['password']
    del request.session['id']
    return redirect("Singup")



def CandidateLogOut(request,pk):
    
    user = UserMaster.objects.get(pk=pk)
    #del request.session['email']
    #del request.session['password']
    del request.session['id']
    return redirect("Singup")
    
def CanidatetablePage(request):
    user = request.session['id']
    if user:
     all_job =   JobPostDetails.objects.all()
     return render(request,"app/job-list.html",{'all_job':all_job})
    #return render(request,"app/index1.html",{'all_job':all_job})



def Singup(request):
    return render(request, "app/Singup.html")

def JobList(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cam = Company.objects.get(user_id = user)
    
    return render(request,"app/job-list.html",{'user': user,'cam':cam})
def ProfileComp(request,pk):
       user = UserMaster.objects.get(pk=pk)
       cam = Company.objects.get(user_id = user)
       return render(request, "app/company/jobpost.html",{'user':user,'can':cam})

def JobDetails(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cam = Company.objects.get(user_id = user)
    
    return render(request,"app/job-detail.html",{'user':user,'cam':cam})

#def UpdateProfile420(request,pk):
 #   user = UserMaster.objects.get(pk=pk)
  #  if user.role == "Candidate":
             
   #     can = Candidate.objects.get(user_id=user)
    #    can.contact = request.POST['contact'] # 2nd contact  from html, 1st one from database
     #   can.state = request.POST['state']
      #  can.city = request.POST['city']
       # can.address = request.POST['address']
        #can.dob = request.POST['DOB']
        #can.profession = request.POST['profession']
        #can.current_salary = request.POST['Current_Salary']
        #an.expected_salary = request.POST['Expected_Salary']
        #can.gender = request.POST['Gender']
        #can.shift = request.POST['Shift']
        #can.job_discription = request.POST['JobDisription']
         
       # can.profile_pic = request.FILES['profile_pic']
        
        
        
        #can.profile_pic = request.POST['profile_pic']
        #can.save()
        #url = f'/profile/{pk}' #formating url
        #return redirect(url)
    


def JobDetailsSubmit11(request,pk):
        #user_id = request.session['id']
        user = UserMaster.objects.get(id=pk)

        #if user.role == "Company":
            #UserMasterID = UserMaster.objects.get(pk=pk)
        comp = Company.objects.get(user_id=user)
            
            
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        jobsdescription = request.POST["jobsdescription"]
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        companywebsite = request.POST['companywebsite']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        salarypackage = request.POST['salarypackage']
        experience = request.POST['experience']
        logo = request.FILES['image']
        if experience == '':
                experience= 0
                                 

            

        newjob = JobPostDetails.objects.create(user_id = user, jobname=jobname,companyname=companyname,
            companyaddress=companyaddress,jobsdescription=jobsdescription,qualification=qualification,responsibilities=responsibilities,
            location=location,companywebsite=companywebsite,companyemail=companyemail,companycontact=companycontact,
            salarypackage=salarypackage,experience=experience,logo=logo)
            
            #save("")
        message = "Job post successfully"
            #url = f'/jobpost/{pk}' #formating url
           # return redirect(url)
                      

            
        
            #return HttpResponse(request,"app/company/jobpost.html",{'msg':message})
        return render(request,"app/company/jobpost.html",{'msg':message})
            
            
        

def Profile(request,pk):
       user = UserMaster.objects.get(pk=pk)
       can = Candidate.objects.get(user_id = user)
       return render(request, "app/profile.html",{'user':user,'can':can})

        
def UpdateProfile(request,pk):
    user = request.session['id']
    #user = UserMaster.objects.get(pk=pk)
    
    if user:
       user = UserMaster.objects.get(pk=pk)
       if user.role == "Candidate":
         user = UserMaster.objects.get(pk=pk)
        
         can = Candidate.objects.get(user_id=user)
         can_all_job =   Candidate.objects.all()
         can.contact = request.POST['contact'] # 2nd contact  from html, 1st one from database
         can.state = request.POST['state']
         can.city = request.POST['city']
         can.address = request.POST['address']
         can.dob = request.POST['DOB']
         can.profession = request.POST['profession']
         can.current_salary = request.POST['Current_Salary']
         can.expected_salary = request.POST['Expected_Salary']
         can.gender = request.POST['Gender']
         can.shift = request.POST['Shift']
         can.job_discription = request.POST['JobDisription']
         #if can.profile_pic:
                              
         can.profile_pic = request.FILES['img']
         #else:
          #   can.profile_pic = ''
             
        #profile_pic = request.FILES['4050can']
        
        #newpic = Candidate.objects.create(user_id=user, contact = contact,state=state,city=city,
        #address = address,dob=dob,profession=profession,current_salary=current_salary,expected_salary=expected_salary,
        #gender=gender,shift=shift,job_discription=job_discription,profile_pic=profile_pic)
        #can.profile_pic = request.POST['profile_pic']
         can.save()
         url = f'/profile/{pk}' #formating url
         return redirect(url,{'can_all_job':can_all_job})
         #return render(request,"app/company/jobpostlist.html",{'all_job':all_job})   
    
    



def OTPPage(request):
    return render(request,"app/otpverify.html") 
def detailsUpdated(request):
    return render(request,"app/otpverify.html") 

def Loginpage(request):
    return render(request,"app/login.html")


def LoginUser(request):
 
  
    if request.POST['role'] == "Candidate":
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role == "Candidate":
                can = Candidate.objects.get(user_id = user)
                #count = JobPostDetails.objects.all().count()
                
                request.session['id'] = user.id 
                request.session['role'] = user.role
                request.session['firstname']= can.firstname
                request.session['lastname']= can.lastname
                request.session['email']= user.email
                request.session['password'] = user.password
                user = request.session['id'] 
   
                count = JobPostDetails.objects.filter(jobname='Marketing').count()
                count1 = JobPostDetails.objects.filter(jobname='Customer Service').count()
                count2 = JobPostDetails.objects.filter(jobname='Human Resource').count()
                count3 = JobPostDetails.objects.filter(jobname='Project Management').count()
                count4 = JobPostDetails.objects.filter(jobname='Business Development').count()
                count5 = JobPostDetails.objects.filter(jobname='Sales & Communication').count()
                count6 = JobPostDetails.objects.filter(jobname='Teaching & Education').count()
                count7 = JobPostDetails.objects.filter(jobname='Design, Software & Creative').count()
                return render(request, "app/index1.html",{'count':count,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7})                

  
                #request.session['profile-img'] = can.Imagename
                #return redirect('index1')
                
            else:
                message = "Password does not matched"
                return render(request, "app/login.html",{'msg':message})
        else:
            message = "User doesn't exist"
            return render(request, "app/Singup.html",{'msg':message})

    elif request.POST['role'] == "Company":
        
            email = request.POST['email']
            password = request.POST['password']

            user = UserMaster.objects.get(email=email)
        
    if user:
            if user.password==password and user.role == "Company":
                cam = Company.objects.get(user_id = user)
                
                request.session['id'] = user.id 
                request.session['role'] = user.role
                request.session['firstname']= cam.firstname
                request.session['lastname']= cam.lastname
                request.session['email']= user.email
                
                request.session['password']= user.password
                
                return redirect('companyindex')
            else:
                message = "Password does not matched"
                return render(request, "app/login.html",{'msg':message})
    else:
            message = "User doesn't exist"
            return render(request, "app/Singup.html",{'msg':message})


def Otpverify(request):
    email = request.POST['email']
    OTP = int(request.POST['OTP'])
    user  = UserMaster.objects.get(email = email)

    if user:
        if user.OTP == OTP:
            message= "OTP verified done"
            return render(request,"app/login.html",{'msg':message})
        else:
            message= "OTP is incorrect"
            return render(request, "app/otpverify.html",{'msg':message})
    else:
        return render(request, "app/Singup.html")


    
def RegisterUser(request):
    
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already exist"
            return render(request,"app/Singup.html",{'msg':message})
        else:
            if password == cpassword:
                OTP = randint(10000,99999)
                newuser = UserMaster.objects.create(role=role, OTP = OTP,email =email,password=password)
                newcand = Candidate.objects.create(user_id = newuser,firstname= fname,lastname=lname)
                #newcand1 = JobPostDetails.objects.create(user_id = newuser, companyemail= email)
                return render(request,"app/otpverify.html",{'email':email})
    elif request.POST['role']=="Company":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        companyemail = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already exist"
            return render(request,"app/Singup.html",{'msg':message})
        else:
            if password == cpassword:
                OTP = randint(10000,99999)
                newuser = UserMaster.objects.create(role=role, OTP = OTP,email =email,password=password)
                #newuser1 = JobPostDetails.objects.create(user_id = newuser, companyemail=email)
                newcand = Company.objects.create(user_id = newuser,firstname= fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
       
  
        
    else: 
        message = "Wrong Selection"
        return render(request,"app/Singup.html",{'msg':message})
        
        
        ################################################### Company Side#########################
        
def CompanyIndexPage(request):
    return render(request,"app/company/index.html")

def ApplyPage(request,pk):
   user = request.session['id']
   if user:
      can = Candidate.objects.get(user_id=user)
      
      
      job  = JobPostDetails.objects.get(id=pk)
      
      return render(request,"app/Apply.html",{'user':user,'can':can,'job':job})
    

def JobCountHome(request,pk):
   user = request.session['id'] 
   if user:
    count = JobPostDetails.objects.filter(jobname='Marketing').count()
    count1 = JobPostDetails.objects.filter(jobname='Customer Service').count()
    count2 = JobPostDetails.objects.filter(jobname='Human Resource').count()
    count3 = JobPostDetails.objects.filter(jobname='Project Management').count()
    count4 = JobPostDetails.objects.filter(jobname='Business Development').count()
    count5 = JobPostDetails.objects.filter(jobname='Sales & Communication').count()
    count6 = JobPostDetails.objects.filter(jobname='Teaching & Education').count()
    count7 = JobPostDetails.objects.filter(jobname='Design, Software & Creative').count()
    return render(request, "app/index1.html",{'count':count,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7})                

                


def RegisterPage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id = user)
    #jpst = JobPostDetails.objects.get(user_id = user)

    return render(request,"app/company/profile.html", {'user':user,'comp':comp} )

def UpdateCompanyProfile(request, pk):
    user = request.session['id']
    if user:
        user = UserMaster.objects.get(pk=pk)
    
        if user.role =="Company":
            camp = Company.objects.get(user_id = user)
            camp.firstname = request.POST['firstname']
            camp.lastname = request.POST['lastname']
            camp.state = request.POST['state']
            camp.city = request.POST['city']
            camp.contact = request.POST['contact']
            camp.address = request.POST['address']
            camp.website = request.POST['website']
            camp.desciption = request.POST['desciption']
            camp.logo_pc = request.FilES['image']
            camp.save()
            url= f"/Profile1/{pk}"
            return redirect(url)


def ApplyJobold(request,pk):
    user = request.session['id']

    #user = UserMaster.objects.get(pk = user)
    if user:
        canid = request.POST['User_id']
        #can = UserMaster.objects.get(pk=canid)
        can1 = Candidate.objects.get(pk=canid)
        
        
        #job  = JobPostDetails.objects.get(id=pk)
        #all_job =  ApplyJob.objects.all()
        job1  = request.POST['job_id']
        job  = JobPostDetails.objects.get(id=job1)
        
        edu = request.POST['education']
        web = request.POST['website']
        Resume = request.FILES['Resume']
              

   
        newapply = ApplyList.objects.create(Candidate=can1,Job=job,education=edu,website=web,Resume=Resume)
        message = "Your Application successfully applied"
        return render(request,"app/index1.html",{'msg':message})


def JobApplyList(request):
    
        
     all_jobapply =   ApplyList.objects.all()
     return render(request,"app/company/applyjoblist.html",{'all_jobapply':all_jobapply})
    
############################################# ADMIN SIDE #######################


def AdminLoginPage(request):
    return render(request,"app/admin/login.html")

def AdminIndexPage(request):
    if 'UserName' in request.session and 'password' in request.session:
     return render(request,"app/admin/index.html")
    else:
        return redirect ('adminloginpage') 

def AdminLogin(request):
    UserName = request.POST['UserName']
    password = request.POST['password']
    if UserName == "admin" and password == "admin":
        request.session['UserName'] = UserName
        request.session['password'] = password
        return redirect('adminindex')
    else:
        message = "User Name and password not matched"
        return render(request,"app/admin/login.html",{'msg':message})

def AdminLogout(request):
    UserName = request.session['UserName'] 
    if UserName:
    #del request.session['email']
    #del request.session['password']
     del request.session['UserName']
     return redirect("adminindex")

def AdminUserList(request):
   
    #all_user = UserMaster.objects.filter(role="Candidate")
    #return render(request,"app/admin/Userlist.html",{'all_user':all_user})
    all_user1 =   UserMaster.objects.all().filter(role="Candidate")
    return render(request,"app/admin/Userlist.html",{'all_user1':all_user1})

def AdminCompanyList(request):
    allCom_user = UserMaster.objects.filter(role='Company')
    return render(request,"app/admin/companylist.html",{'allCom_user':allCom_user})

def Userdelete(request,pk):
     company = UserMaster.objects.get(pk=pk)
     company.delete()
     return redirect('Adminuserlist')

def VerifyCompanyPage(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        id = company.id
        return render(request,"app/admin/verify.html",{'id':id})

def VerifyCompany(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user:
        company = UserMaster.objects.get(pk=pk)
        if company:
             company.is_verified = request.POST['verifiedoption']
             company.save()
             return redirect('Admincompanylist')



def UserAdmindelete(request,pk):
   
     company = UserMaster.objects.get(pk=pk)
     company.delete()
     return redirect('Admincompanylist')
        
        





