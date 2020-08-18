from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MEoutpass
from .models import ME


def me(request):
    if request.method == 'POST':
        st = MEoutpass(request.POST)
        if st.is_valid():
            nm = st.cleaned_data['me_name']
            rl = st.cleaned_data['me_rollnumber']
            yr = st.cleaned_data['me_year']
            br = st.cleaned_data['me_branch']
            rs = st.cleaned_data['me_reason']
            std = st.cleaned_data['me_start_date']
            end = st.cleaned_data['me_end_date']
            per = st.cleaned_data['me_permission']
            itst = ME(me_name=nm, me_rollnumber=rl, me_year=yr, me_branch=br, me_reason=rs, me_start_date=std,
                      me_end_date=end, me_permission=per)
            itst.save();
            messages.info(request, 'Successfully applied for leave')
            return redirect('/StudentOutpass/ME')


    else:
        st = MEoutpass()
        itstud = ME.objects.all()
        return render(request, 'OutpassME.html', {'ITstudent': st, 'itians': itstud})




# Create your views here.
