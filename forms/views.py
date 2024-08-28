from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm

# def user_profile_view(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = UserProfileForm()

#     return render(request, 'userprofileform.html', {'form': form})

# def success_view(request):
#     return render(request, 'submit.html')


from django.shortcuts import render
from .forms import UserProfileForm

def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
        else:
            success = False
    else:
        form = UserProfileForm()
        success = False

    return render(request, 'submit.html', {'form': form, 'success': success})


def submit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = UserProfileForm()

    return render(request, 'submit.html', {'form': form})


