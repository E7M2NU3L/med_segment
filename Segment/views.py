from django.shortcuts import render

# Create your views here.
# 1. Home page
def home(request):
    return render(request, 'index.html', name = "Homepage")

# 2. Login Page
def login(request):
    return render(request, 'login.html', name = "Login")

# 3. Register Page
def register(request):
    return render(request,'signup.html', name = "Register")

# 4. Classify Page
def classify(request):
    return render(request, 'classify.html', name = "Classify")

# 5. Segment Page
def segment(request):
    return render(request,'segment.html', name = "Segment")

# 6. Project Page
def project(request):
    return render(request, 'project.html', name = "Project")

# 7. Classified output page
def Classified_output(request):
    return render(request, 'class_output.html', name = "Classified_output")

# 8. Segmented Output Page
def Segmented_output(request):
    return render(request,'seg_output.html', name = "Segmented_output")