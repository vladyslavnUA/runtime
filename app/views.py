from django.shortcuts import render
from .forms import *
import runpy, os
import subprocess

def home(request):
    context = {}
    if request.method == 'GET':
        form = CodeForm()
        # proc = subprocess.Popen(
        #     ['python3 new.py'],             #call something with a lot of output so we can see it
        #     shell=True,
        #     stdout=subprocess.PIPE
        # )
        # print(proc, inner(), mimetype='text/html'), '::::::::::::::'
        # print(os.popen('python3 new.py').read())

    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False)
            data = form.cleaned_data.get("thecode")
            print(data)

            f = open("/Users/vladyslav/Desktop/runtime/runtime/app/new.py","w+")
            f.write(f"{data}")
            f.close()
            print('---- made it to step 1 ----')
            file = '/Users/vladyslav/Desktop/runtime/runtime/app/new.py'
            # exec(compile(open(file).read(), file, 'exec'))
            runpy.run_path(file)
            # exec(open('/Users/vladyslav/Desktop/runtime/runtime/app/new.py').read())
            # execfile('')
            print('got here')
            # obj.author = request.user
            # obj.save()
            # print(obj, request.user)
        # context = {
        #     'form': form
        # }
    else:
        form = CodeForm()
        context['form'] = form
    return render(request, 'app/index.html', context)