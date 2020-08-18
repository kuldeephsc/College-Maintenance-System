from django.shortcuts import render, redirect
from .forms import Lab
from .models import Labrepair
from django.contrib import messages

def lab(request):
    if request.method == 'POST':
        lb = Lab(request.POST)
        if lb.is_valid():
            lbn = lb.cleaned_data['lab']
            sys = lb.cleaned_data['system']
            prb = lb.cleaned_data['problem']
            lbst = lb.cleaned_data['lab_status']
            lms = Labrepair(lab=lbn, system=sys, problem=prb, lab_status=lbst)
            lms.save();
            messages.info(request, 'Complaint Registered')
            return redirect('/LabMaintenance')
    else:
        lb = Lab()
        lbres = Labrepair.objects.all()
        return render(request, 'lab1.html', {'lab':lb, 'lbrs':lbres})
