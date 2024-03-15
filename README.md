# File-Share App

The File-Share app is a secure file sharing platform that allows users to securely register, upload files, store files, download, and share them with other users.

## Description

The File-Share app provides a user-friendly interface for managing files. Users can easily register, log in, and upload files. Uploaded files are securely stored and can be downloaded by the user or shared with other registered users. The app uses Django authentication for user registration, login, and logout, ensuring secure access to files. The Python cryptography library is used for hashing passwords and encrypting files, enhancing the security of user data. Additionally, the shutil library is used for file operations such as moving and copying files.

## Screenshots

![Screenshot 3](/screenshots/home.png)
![Screenshot 1](/screenshots/register.png)
![Screenshot 2](/screenshots/login.png)
![Screenshot 4](/screenshots/upload.png)
![Screenshot 5](/screenshots/profile.png)


## Project Purpose

This project is a learning and exploration project with Django. There are many improvements to be made and many more functionalities and security features that can be added. The goal is to gain a deeper understanding of Django's capabilities and best practices for developing secure web applications.

## Features

- **User Registration**: Users can securely register accounts using Django authentication.
- **User Login and Logout**: Registered users can log in and log out of the app.
- **File Upload**: Users can upload files to the app.
- **File Storage**: Uploaded files are securely stored.
- **File Download**: Users can download files they have uploaded.
- **File Sharing**: Users can share files with other registered users.

## Technologies Used

- **Frontend**: Vanilla HTML and CSS
- **Backend**: Django
- **Database**: SQLite
- **Security**: Python cryptography library for hashing and encryption
- **File Operations**: shutil library for moving, copying, and other file-related operations

## Usage

- Register an account on the app using Django authentication.
- Log in to access the file upload, download, and sharing features.
- Log out when done using the app.

## Security

- The app uses the Python cryptography library for hashing passwords and encrypting files.
- User passwords are securely hashed before storing them in the database.

## Getting Started

1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up your Django project and configure the database.
4. Run the development server using `python manage.py runserver`.
5. Open `http://localhost:8000` in your browser to access the app.
