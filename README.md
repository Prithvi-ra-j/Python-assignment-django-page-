# Django File Upload Application

## Overview
This Django-based web application allows users to upload CSV or Excel files and generates a summary report of the uploaded data. The summary is sent via email to the specified recipient along with a link to the project's GitHub repository.

## Features
- **File Upload**: Users can upload Excel or CSV files.
- **Data Summary**: The application generates a summary report using pandas, showcasing statistics like count, mean, standard deviation, min, max, and percentiles of the data.
- **Email Notifications**: The summary is sent to a specified email address along with a link to the project's GitHub repository.
- **User-Friendly Interface**: The application is designed with a modern, responsive dark theme for an engaging user experience.

## Technology Stack
- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (default)
- **Libraries**: 
  - Pandas for data manipulation
  - Django for web framework
  - Django’s email functionality for sending emails

## Setup Instructions

### Prerequisites
- Python 3.x
- Django
- Pandas
- A valid email configuration (e.g., Gmail) in Django settings

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Prithvi-ra-j/Python-assignment-django-page-

2. Navigate to the project directory:
   ```bash
   cd Python-assignment-django-page-
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Deployment
1. Push your code to a public GitHub repository.
2. Deploy the application using a free hosting platform like Heroku or Render.
3. Follow the platform-specific instructions to configure your deployment settings.

## Usage
1. Access the application in your web browser at `http://127.0.0.1:8000/upload/`.
2. Upload a CSV or Excel file using the file input.
3. Click the "Upload" button.
4. The application will process the file and generate a summary.
5. An email will be sent to the specified address with the summary and GitHub link.

