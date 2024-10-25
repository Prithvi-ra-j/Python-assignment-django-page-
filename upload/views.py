from django.shortcuts import render
from .forms import uplooad
import pandas as pd
from django.core.mail import send_mail
from django.conf import settings

def upload_file(request):
    summary = None
    if request.method == 'POST':
        form = uplooad(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
               
                if file.name.endswith('.csv'):
                    df = pd.read_csv(file)
                elif file.name.endswith('.xlsx'):
                    df = pd.read_excel(file)
                else:
                    return render(request, 'upload/upload.html', {'form': form, 'error': 'Invalid file type'})

                github_link = "https://github.com/Prithvi-ra-j/Python-assignment-django-page-"
                summary = df.describe().to_string()
                message = f"{summary}\n\nGitHub Repository: {github_link}"
                
                send_mail(
                    subject=f'Python Assignment - Prithviraj',
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['tech@themedius.ai'],
                )

                return render(request, 'upload/upload.html', {'form': form, 'summary': summary, 'success': 'Email sent successfully!'})

            except Exception as e:
                return render(request, 'upload/upload.html', {'form': form, 'error': f'Error processing file: {e}'})
    else:
        form = uplooad()
    return render(request, 'upload/upload.html', {'form': form})
