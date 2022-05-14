from email.policy import default
from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models
from distutils.command.upload import upload
import email
from pyexpat import model
from statistics import mode
from tkinter import CASCADE

#from platformdirs import user_log_dir
#from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    OTP = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    
    


class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    profession = models.CharField(max_length=100,default='')
    current_salary = models.BigIntegerField(default=1)
    expected_salary = models.BigIntegerField(default=1)
    gender = models.CharField(max_length=50)
    shift = models.CharField(max_length=20,default='')
    job_discription = models.CharField(max_length=100,default='')
    #Imagename = models.CharField(max_length=100, default='')
    profile_pic = models.ImageField(upload_to="CandidateImage/")
    #Resume = models.FileField(upload_to="Resume/", null = True,blank=True)
    
    #resume = models.FileField(upload_to="app/resume/candidate", default ='')

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    website = models.CharField(max_length=250,default='')
    desciption = models.CharField(max_length=500,default='')
    logo_pc = models.ImageField(upload_to="CompanyImage/")
    

class JobPostDetails(models.Model):
    #candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    #company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=250,default='')
    companyname = models.CharField(max_length=250,default='')
    companyaddress = models.CharField(max_length=250,default='')
    jobsdescription = models.TextField(max_length=500,default='')
    qualification = models.CharField(max_length=250,default='')
    responsibilities = models.CharField(max_length=250,default='')
    location = models.CharField(max_length=250,default='')
    companywebsite = models.CharField(max_length=250,default='')
    companyemail = models.CharField(max_length=250,default='')
    companycontact = models.CharField(max_length=20,default='')
    salarypackage = models.CharField(max_length=250,default='')
    experience = models.IntegerField()
    logo = models.ImageField(upload_to="JobPostImage/")
    Resume = models.FileField(upload_to="Resume/")
  

class ApplyList(models.Model):
    #company_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    #User = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    Job = models.ForeignKey(JobPostDetails,on_delete=models.CASCADE)
    education = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    Resume = models.FileField(upload_to="app/Resume/")


