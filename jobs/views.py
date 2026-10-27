from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Job, Application, ContactMessage


# ================= HOME PAGE =================

def home(request):

    jobs = Job.objects.all()

    keyword = request.GET.get('keyword', '')
    location = request.GET.get('location', '')
    category = request.GET.get('category', '')

    # Search by job title
    if keyword:
        jobs = jobs.filter(
            title__icontains=keyword
        )

    # Search by location
    if location:
        jobs = jobs.filter(
            location__icontains=location
        )

    # Category filter
    if category:

        if category == 'IT':
            jobs = jobs.filter(
                title__icontains='developer'
            )

        elif category == 'DATA':
            jobs = jobs.filter(
                title__icontains='data'
            )

        elif category == 'DESIGN':
            jobs = jobs.filter(
                title__icontains='design'
            )

        elif category == 'MARKETING':
            jobs = jobs.filter(
                title__icontains='marketing'
            )

    return render(
        request,
        'home.html',
        {
            'jobs': jobs,
            'keyword': keyword,
            'location': location,
            'category': category
        }
    )


# ================= JOB DETAILS =================

def job_detail(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    return render(
        request,
        'job_detail.html',
        {
            'job': job
        }
    )


# ================= APPLY FOR JOB =================

@login_required
def apply_job(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    if request.method == 'POST':

        Application.objects.create(
            user=request.user,
            job=job,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            resume=request.FILES.get('resume')
        )

        return render(
            request,
            'application_success.html',
            {
                'job': job
            }
        )

    return render(
        request,
        'apply.html',
        {
            'job': job
        }
    )


# ================= USER DASHBOARD =================

@login_required
def dashboard(request):

    applications = Application.objects.filter(
        user=request.user
    ).order_by('-applied_at')

    return render(
        request,
        'dashboard.html',
        {
            'applications': applications
        }
    )


# ================= ABOUT PAGE =================

def about(request):

    return render(
        request,
        'about.html'
    )


# ================= CONTACT PAGE =================

def contact(request):

    if request.method == 'POST':

        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        return render(
            request,
            'contact.html',
            {
                'success': 'Your message has been sent successfully!'
            }
        )

    return render(
        request,
        'contact.html'
    )


# ================= REGISTER =================

def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check username already exists
        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                'register.html',
                {
                    'error': 'Username already exists'
                }
            )

        # Create new user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Go to login
        return redirect('login')

    return render(
        request,
        'register.html'
    )


# ================= LOGIN =================

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect('home')

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'login.html'
    )


# ================= LOGOUT =================

def user_logout(request):

    logout(request)

    return redirect('home')