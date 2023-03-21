from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, EceStudents, CseStudents
from myapp.forms import StudentForm
import pandas as pd

# Create your views here.

# Create Employee

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail, EmpDesignation= EmpDesignation)
        data.save()
  
        return redirect('show/')
    else:
        return render(request, 'insert.html')

# Retrive Employee
        
def show_emp(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees} )


# Update Employee

def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employees.EmpId = request.POST['EmpId']
        employees.EmpName = request.POST['EmpName']
        employees.EmpGender = request.POST['EmpGender']
        employees.EmpEmail = request.POST['EmpEmail']
        employees.EmpDesignation = request.POST['EmpDesignation']
        employees.save()
        return redirect('/show')

    context = {
        'employees': employees,
    }

    return render(request,'edit.html',context)

# Delete Employee

def remove_emp(request, pk):
    employees = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employees.delete()
        return redirect('/show')

    context = {
        'employees': employees,
    }

    return render(request, 'delete.html', context)



def upload_files(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"upload_file.html",{'form':student})


def handle_uploaded_file(f):  
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)


def read_csv_file(request):
    import pandas as pd 
    df=pd.read_csv("myapp/static/upload/data.csv")

    print(df)

    print(len(df.Name)) # count number of rows

    name_list = list(df.Name)
    age_list = list(df.Age)
    email_list = list(df.Email)
    password_list = list(df.Password)

    for index in range(0, len(name_list)):

        print(name_list[index])
        print(age_list[index])
        print(email_list[index])
        print(password_list[index])

        cs_stds = CseStudents(name=name_list[index], age=age_list[index], email=email_list[index], pass_word=password_list[index])
        cs_stds.save()

    return render(request,"csv_data.html")

def write_into_csv_file(request):
    # We need to fetch db details as columns wise first
    db_details =  CseStudents.objects.all().order_by('name').values()
    print(type(db_details))
    dict_of_csv_data = {
        'name':None,
        'age':None,
        'email':None,
        'pass_word':None
    }
    id_list = []
    name_list = []
    age_list = []
    email_list = []
    pass_word_list = []

    for index in range(0, len(db_details)): # for number of rows
        # Store in a list to add in dictionary to change it into csv file
        name_list.append(db_details[index].get('name'))
        age_list.append(db_details[index].get('age'))
        email_list.append(db_details[index].get('email'))
        pass_word_list.append(db_details[index].get('pass_word'))
    
    # Update columns details in dict
    dict_of_csv_data['name'] = name_list
    dict_of_csv_data['age'] = age_list
    dict_of_csv_data['email'] = email_list
    dict_of_csv_data['pass_word'] = pass_word_list
    print(dict_of_csv_data)

    # Convert into Dataframe object
    df = pd.DataFrame(dict_of_csv_data)
    print(df)
    # saving in csv file
    df.to_csv('myapp/static/upload/file1.csv')

    return HttpResponse("Success")
    
