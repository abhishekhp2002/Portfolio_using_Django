from django.views import View
from django.shortcuts import render
from django.contrib import messages
from .models import Project, Contact

class IndexView(View):
    def get(self, request):
        # Handle GET requests (e.g., fetching projects)
        projects = Project.objects.all()
        return render(request, 'home.html', {'projects': projects})

    def post(self, request):
        # Handle POST requests (e.g., contact form submission)
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')

        if not (2 <= len(name) <= 30):
            messages.error(request, 'Name must be between 2 and 30 characters.')
        elif not (2 <= len(email) <= 40):
            messages.error(request, 'Invalid email address.')
        elif not (len(number) == 10 and number.isdigit()):
            messages.error(request, 'Invalid phone number. It must be 10 digits.')
        elif len(content.strip()) == 0:
            messages.error(request, 'Message content cannot be empty.')
        else:
            Contact.objects.create(name=name, email=email, content=content, number=number)
            messages.success(request, "Thank you for contacting me! Your message has been saved.")
        
        projects = Project.objects.all()
        return render(request, 'home.html', {'projects': projects})
