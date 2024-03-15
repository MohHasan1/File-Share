# <span style="color:blue;">File-Share App</span>

The <span style="color:green;">File-Share app</span> is a secure file sharing platform that allows users to securely register, upload files, store files, download, and share them with other users.

## <span style="color:orange;">Description</span>

The <span style="color:purple;">File-Share app</span> provides a user-friendly interface for managing files. Users can easily register, log in, and upload files. Uploaded files are securely stored and can be downloaded by the user or shared with other registered users. The app uses Django authentication for user registration, login, and logout, ensuring secure access to files. The Python cryptography library is used for hashing passwords and encrypting files, enhancing the security of user data. Additionally, the shutil library is used for file operations such as moving and copying files.

## <span style="color:orange;">Project Purpose</span>

This project is a learning and exploration project with Django. There are many improvements to be made and many more functionalities and security features that can be added. The goal is to gain a deeper understanding of Django's capabilities and best practices for developing secure web applications.

## <span style="color:orange;">Features</span>

- **User Registration**: Users can securely register accounts using Django authentication.
- **User Login and Logout**: Registered users can log in and log out of the app.
- **File Upload**: Users can upload files to the app.
- **File Storage**: Uploaded files are securely stored.
- **File Download**: Users can download files they have uploaded.
- **File Sharing**: Users can share files with other registered users.

## <span style="color:orange;">Technologies Used</span>

- **Frontend**: Vanilla HTML and CSS
- **Backend**: Django
- **Database**: SQLite
- **Security**: Python cryptography library for hashing and encryption
- **File Operations**: shutil library for moving, copying, and other file-related operations

## <span style="color:orange;">Usage</span>

- Register an account on the app using Django authentication.
- Log in to access the file upload, download, and sharing features.
- Log out when done using the app.

## <span style="color:orange;">Security</span>

- The app uses the Python cryptography library for hashing passwords and encrypting files.
- User passwords are securely hashed before storing them in the database.

## <span style="color:orange;">Getting Started</span>

1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up your Django project and configure the database.
4. Run the development server using `python manage.py runserver`.
5. Open `http://localhost:8000` in your browser to access the app.




