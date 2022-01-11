from django.shortcuts import render
from django.contrib import messages
import re
import smtplib
import os

# Create your views here.
def HomePageView(request):
    if request.method == 'POST':
        To = request.POST.get('To').replace(" ", "")
        content = request.POST.get('content')
        if To=="" or content=="":
            return render(request, 'main.html', context={'message':True, 'text':'To or Message or both are empty'})
        else:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            def check(email):
                if(re.fullmatch(regex, email)):
                    sender_email = 'saigo8112@gmail.com'
                    rec_email = To
                    message = content
                    password = os.environ.get('Email Password')

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, rec_email, message)
                    return "Mail sent"
                else:
                    return "InValid Email ID"     
            return render(request, 'main.html', context={'message':True, 'text':check(To)})            
    else:
        return render(request, 'main.html')