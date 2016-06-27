from django.shortcuts import render, render_to_response
from django.template.response import TemplateResponse
from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm

# Create your views here.
def home(request):
    home_data = {'title' : 'My title', 'body': 'This is the home page'}
    # return TemplateResponse(request, 'firstapp/home.html', {'data': home_data})

    #val = request.POST.get('name')
    #print val
    return render(request, 'app/firstapp/home.html', {})
    #return render_to_response('firstapp/home.html', RequestContext(request), {})

def login(request):
    return render(request, 'registration/login.html', {})

def login1(request):
    return render(request, 'firstapp/login1.html', {})

def python_course(request):
    return render(request, 'firstapp/course.html', {})

def overview(request):
    return render(request, 'firstapp/overview.html', {})

def setup(request):
    return render(request, 'firstapp/setup.html', {})

def interview_questions(request):
    return render(request, 'firstapp/interview_questions.html', {})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            print request.POST.get('subject')
            return HttpResponse('Thank you, form has been submitted successfully')
    return render(request, 'firstapp/contact_form.html',
        {'errors': errors})

def login2(request):
    username = "not logged in"
    if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
    else:
      MyLoginForm = Loginform()
    return render(request, 'firstapp/loggedin.html', {"username" : username})

def intro(request):
   return render(request, 'firstapp/day1/intro.html', {})

def objects(request):
   return render(request, 'firstapp/day1/objects.html', {})

def basic_operators(request):
   return render(request, 'firstapp/day1/basic_operators.html', {})

def decision_making(request):
   return render(request, 'firstapp/day1/decision_making.html', {})

def loops(request):
   return render(request, 'firstapp/day1/loops.html', {})

def strings(request):
   return render(request, 'firstapp/day1/strings.html', {})

def lists(request):
   return render(request, 'firstapp/day1/lists.html', {})

def dict_tuples(request):
   return render(request, 'firstapp/day1/dict_tuples.html', {})

def datetime(request):
   return render(request, 'firstapp/day1/datetime.html', {})

def list_comprehension(request):
   return render(request, 'firstapp/day1/list_comprehension.html', {})

def map_reduce_filter_lambda(request):
   return render(request, 'firstapp/day1/map_reduce_filter_lambda.html', {})

def functions(request):
   return render(request, 'firstapp/day2/functions.html', {})

def file_handling(request):
   return render(request, 'firstapp/day2/file_handling.html', {})

def exceptions(request):
   return render(request, 'firstapp/day2/exceptions.html', {})

def classes_and_objects(request):
   return render(request, 'firstapp/day2/classes_and_objects.html', {})

def data_scraping(request):
   return render(request, 'firstapp/day4/data_scraping.html', {})

def reg_expressions(request):
   return render(request, 'firstapp/day4/reg_expressions.html', {})

