from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Program, Student
# Create your views here.
clicked = 1
def index(request) :
  global clicked
  clicked += 1
  my_dict = {'count' : clicked}
  return render(request, 'index.html', my_dict)

def help(request) :
  return render(request, 'help.html')

def year_function(request, year) :
    if year >= 2000 and year <= 2040 :
        msg = '<h2 style="color:blue"> ' + str(year) + ' is a valid year</h2>'  
    else :
        msg = '<h2 style="color:red"> '   + str(year)  + ' is NOT a valid year'
    return HttpResponse(msg)

def year_current(request ):
   msg = '<h2>this is year 2023</h2>'
   return HttpResponse(msg)

def month_function(request , year, month):
   return HttpResponse(str(year) + str(month))

def uuid_function(request , name):
   name = '075194d3-6885-417e-a8a8-6c931e272f00'
   return HttpResponse(str(name))

def process_form(request) :
    username = request.GET.get('user')
    password = request.GET.get('pwd')
    print(username, password)
    return render(request, 'form.html')

def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
 
    return HttpResponseRedirect('/student/')
  else: 
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})