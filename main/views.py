from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UploadProjectForm, ReviewForm
from django.contrib import messages
from .models import Project,Review
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login, logout 

# Create your views here.
def registerPage(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Account was created for " + user)
            return redirect('login')
    content={'form':form}
    return render(request,'accounts/register.html', content)
    
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password incorect")    
    content={}
    return render(request,'accounts/login.html',content)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    peters=Project.objects.all()

    context={"peters":peters}
    return render (request, 'project.html', context)

@login_required(login_url='login')
def detail(request, id):
    projects=Project.objects.get(id=id)
    context={"project":projects}
    return render(request,'projectdetail.html',context)



@login_required(login_url='login')
def  add_project(request):
    if request.method=="POST":
        form=UploadProjectForm(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect ("home")
    else:
        form=UploadProjectForm()
    return render(request, "addproject.html",{"form":form})    



def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_articles = Project.search_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"categories": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


# function to commit comments and rating
def add_review(request, id):
    if request.user.is_authenticated:
        project=Project.objects.get(id=id)
        if request.method == "POST":
            form=ReviewForm(request.POST or None)
            if form.is_valid():
                data=form.save(commit=False)
                data.comment=request.POST["comment"]
                data.rating=request.POST["rating"]
                data.user=request.user
                data.project=project
                data.save()
                return redirect("main:detail", id)
        else:
            form=ReviewForm()  
        return render(request,'main/details.html', {"form":form})
    else:
        return redirect("accounts:login")              

 #logic to delete a comment
def edit_review(request,id):
    if request.user.is_authenticated:
        project=Project.objects.get(id=id)
        review=Review.objects.get(project=project, id=id)

        # check if the review was done by looged in user
        if request.user == review.user:
            # grant user to review
            if request.method== "POST":
                form=ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data= form.save(commit=False)
                    # adding limit for rating
                    if (data.rating >10) or (data.rating <0):
                        error = "Out of range. Please select rating from  0 to 10"
                        return render(request, "main/editreview.html", {"error":error, "form":form})
                    else:    
                    # ===
                        data.save()
                        return redirect("project_details") 
            else:
                form=ReviewForm(instance=review)
            return render(request,'main/editreview.html', {"form":form})
        else:
         return redirect("accounts:login")                
# delete review
def delete_review(request,id):
    if request.user.is_authenticated:
        project=Project.objects.get(id=id)
        review=Review.objects.get(project=project, id=id)

        # check if the review was done by looged in user
        if request.user == review.user:
            # grant user to review
           review.delete()
        return redirect("project_details")
       
    else:
        return redirect("accounts:login")      
