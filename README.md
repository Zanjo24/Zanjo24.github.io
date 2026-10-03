# Django Personal Portfolio Project

## Project Overview

This repository contains a full-stack Django personal portfolio featuring dynamic project listings, tech stack management, secure superuser-only admin authentication, and a custom admin dashboard.

## Prerequisites & Setup Instructions

Follow these step-by-step instructions to clone and run the project locally for grading and testing:

### 1. Clone the Repository
git clone https://github.com/Zanjo24/Zanjo24.github.io.git
cd Zanjo24.github.io

### 2. Create and Activate a Virtual Environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables
Duplicate the .env.example file to create your own .env file in the root directory:
cp .env.example .env

### 5. Run Database Migrations
python manage.py migrate

### 6. Create a Superuser (Required for Admin Dashboard Access)
python manage.py createsuperuser

### 7. Run the Development Server
python manage.py runserver

Open http://127.0.0.1:8000/ in your browser to test the project locally.