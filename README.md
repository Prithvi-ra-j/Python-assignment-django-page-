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
