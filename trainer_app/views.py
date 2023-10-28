from django.shortcuts import render, redirect
from . models import Trainers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Home page: http://127.0.0.1:8000/home

# home view - read all trainers list with a limit of 8 trainers per page.
def home(request):
    all_trainers_list = Trainers.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_trainers_list, 8)
    
    try:
        trainers = paginator.page(page)
    except PageNotAnInteger:
        trainers = paginator.page(1)
    except EmptyPage:
        trainers = paginator.page(paginator.num_pages)

    context = {"trainers": trainers}
    return render(request, "trainer_app/home.html",context)
    
#create view - create new trainer and handling errors of user
def create(request):
    trainer = Trainers()
    context = {"trainer":trainer}
    errors = {}
    if request.method == "POST":            
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        subject = request.POST["subject"]
        
        if not first_name and not last_name and not subject:
            errors['empty_first_last_name_subject'] = 'Please enter first name, last name and subject!'
            return render(request, "trainer_app/create.html", errors)
        elif not first_name and not last_name:
            errors['empty_first_last_name'] = 'Please enter first and last name!'
            return render(request, "trainer_app/create.html", errors)
        elif not first_name and not subject:
            errors['empty_first_name_subject'] = 'Please enter first name and subject!'
            return render(request, "trainer_app/create.html", errors)
        elif not last_name and not subject:
            errors['empty_last_name_subject'] = 'Please enter last name and subject!'
            return render(request, "trainer_app/create.html", errors)
        elif not first_name:
            errors['empty_first_name'] = 'Please enter first name!'
            return render(request, "trainer_app/create.html", errors)            
        elif not last_name:
            errors['empty_last_name'] = 'Please enter last name!'
            return render(request, "trainer_app/create.html", errors)
        elif not subject:
            errors['empty_subject'] = 'Please enter subject!'
            return render(request, "trainer_app/create.html", errors)
        else:
            trainer = Trainers()
            trainer.first_name = first_name
            trainer.last_name = last_name
            trainer.subject = subject              
            trainer.save()
            context = {"first_name":trainer.first_name,
                        "last_name":trainer.last_name,
                        "subject":trainer.subject}
            return render(request, "trainer_app/create.html", context)  

    return render(request, "trainer_app/create.html", context)

# update view - update trainer's form    
def update(request, id):
    trainer_to_edit = Trainers.objects.get(id=id)
    context = {"trainer": trainer_to_edit}

    if request.method == 'POST':
        new_first_name = request.POST['first_name']
        new_last_name = request.POST['last_name']
        new_subject = request.POST['subject']
        if (new_first_name and new_last_name and new_subject):
            trainer_to_edit.first_name = new_first_name
            trainer_to_edit.last_name = new_last_name
            trainer_to_edit.subject = new_subject
            trainer_to_edit.save()
            return redirect('home')
        else:
            return redirect('home')


    return render(request, 'trainer_app/update.html', context)

# delete view - delete a trainer
def delete(request, id):
    all_trainers_list = Trainers.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_trainers_list, 8)

    try:
        trainers = paginator.page(page)
    except PageNotAnInteger:
        trainers = paginator.page(1)
    except EmptyPage:
        trainers = paginator.page(paginator.num_pages)

    trainer_to_delete = Trainers.objects.get(id=id)   
    if request.method == 'GET':
        trainer_to_delete.delete()    
        return redirect('deleted')
    
    context = {"trainers": trainers}
   
    return render(request, "trainer_app/deleted.html",context)

# deleted view - read trainers list after delete action
def deleted(request):
    all_trainers_list = Trainers.objects.all()
    paginator = Paginator(all_trainers_list, 8)
    page = request.GET.get('page', paginator.num_pages)

    try:
        trainers = paginator.page(page)
    except PageNotAnInteger:
        trainers = paginator.page(1)
    except EmptyPage:
        trainers = paginator.page(paginator.num_pages)

    context = {"trainers": trainers}
   
    return render(request, "trainer_app/deleted.html",context)

