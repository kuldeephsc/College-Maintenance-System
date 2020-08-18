from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IToutpass
from .models import IT

def it(request):
    if request.method=='POST':
        st = IToutpass(request.POST)
        if st.is_valid():
            nm = st.cleaned_data['it_name']
            rl = st.cleaned_data['it_rollnumber']
            yr = st.cleaned_data['it_year']
            br = st.cleaned_data['it_branch']
            rs = st.cleaned_data['it_reason']
            std = st.cleaned_data['it_start_date']
            end = st.cleaned_data['it_end_date']
            per = st.cleaned_data['it_permission']
            itst = IT(it_name=nm, it_rollnumber=rl, it_year=yr, it_branch=br, it_reason=rs, it_start_date=std,
                      it_end_date=end, it_permission=per)
            itst.save();
            messages.info(request, 'Successfully applied for leave')
            return redirect('/StudentOutpass/IT')


    else:
        st = IToutpass()
        itstud = IT.objects.all()
        return render(request, 'OutpassIT.html', {'ITstudent':st, 'itians':itstud})

