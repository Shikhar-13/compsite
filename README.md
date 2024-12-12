# Class Resources Management Website

## Overview
This project is a **Class Resources Management Website** developed using **Django**, a high-level Python web framework. It aims to streamline the management and sharing of class-related resources, such as notes, assignments, and schedules, among students and instructors.

## Features
- **User Authentication**: Secure login and registration system.
- **Resource Management**: Upload, view, and download class materials.
- **Roles**: Role-based access for students and instructors.
- **Search Functionality**: Quickly find resources by keywords or categories.
- **Responsive Design**: Optimized for various devices.

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Django 4.0+

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shikhar-13/compsite.git
   cd compsite
   ```

2. **Set up a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000`.

## Project Structure
- **static/**: Contains static files (CSS, JS, images).
- **media/**: Stores user-uploaded files.
- **templates/**: HTML templates for rendering pages.
- **apps/**: Modular applications for managing different functionalities.
- **manage.py**: Command-line utility for administrative tasks.

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a Pull Request.



## Contact
For any queries or suggestions, please reach out to the project maintainer at [Shikhar-13](https://github.com/Shikhar-13).
