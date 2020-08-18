from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractBaseUser
from .forms import Repair
from .models import Hostel
from django.contrib import messages


def repair(request):
    if request.method == 'POST':
        rp = Repair(request.POST)
        if rp.is_valid():
            nm = rp.cleaned_data['student_name']
            rln = rp.cleaned_data['userid']
            hs = rp.cleaned_data['hostel']
            fl = rp.cleaned_data['floor']
            rm = rp.cleaned_data['room']
            ap = rp.cleaned_data['appliances']
            st = rp.cleaned_data['status']

            rep = Hostel( student_name=nm, userid=rln, hostel=hs, floor=fl, room=rm, appliances=ap, status=st)
            rep.save();
            messages.info(request, 'Submitted Successfully')
            return redirect('/HostelMaintenance')
    else:
        rp = Repair()
        stud = Hostel.objects.all()
        return render(request, 'hostel2.html', {'repair': rp, 'stu':stud})
