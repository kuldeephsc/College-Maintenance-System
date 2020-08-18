from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EEoutpass
from .models import EE


def ee(request):
    if request.method == 'POST':
        st = EEoutpass(request.POST)
        if st.is_valid():
            nm = st.cleaned_data['ee_name']
            rl = st.cleaned_data['ee_rollnumber']
            yr = st.cleaned_data['ee_year']
            br = st.cleaned_data['ee_branch']
            rs = st.cleaned_data['ee_reason']
            std = st.cleaned_data['ee_start_date']
            end = st.cleaned_data['ee_end_date']
            per = st.cleaned_data['ee_permission']
            itst = EE(ee_name=nm, ee_rollnumber=rl, ee_year=yr, ee_branch=br, ee_reason=rs, ee_start_date=std,
                      ee_end_date=end, ee_permission=per)
            itst.save();
            messages.info(request, 'Successfully applied for leave')
            return redirect('/StudentOutpass/EE')


    else:
        st = EEoutpass()
        itstud = EE.objects.all()
        return render(request, 'OutpassEE.html', {'EEform': st, 'itians': itstud})




# Create your views here.
