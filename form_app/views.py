from django.shortcuts import render, HttpResponse, redirect
# import your forms 
from .forms import CustomerForm

def index(request):
    # Bring your form into the context 
    form = CustomerForm()
    # if it is a post then save the request post as form 
    if request.method == 'POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        # if everything is valid then save it 
        if form.is_valid():
            form.save()
            
    context = {'form' : form}
    
    return render(request, "index.html", context)  
