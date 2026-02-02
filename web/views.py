from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, Education, ContactMessage

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')

    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by('-proficiency')
    projects = Project.objects.all().order_by('-created_at')
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'web/index.html', context)
