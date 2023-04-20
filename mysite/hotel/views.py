from django.shortcuts import render

def index():
    return render(template_name='welcome.html')
