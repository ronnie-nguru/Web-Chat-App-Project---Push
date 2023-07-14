# Web Chat Application using AES
The Flask Web Chat Application is a real-time chat platform that allows users to communicate with each other in a web-based environment. This application is built using Flask framework and is hosted on AWS (Amazon Web Services) for accessibility  and reliability. It is secured using AES encryption.
## Features
- Real-time Messaging: Users can exchange messages instantly, ensuring seamless communication. 
- User Authentication: Users can create accounts, log in, and maintain their own profiles. 
- Message Integrity: Message integrity is ensured through the use of cryptographic hash functions.
## Technologies Used
- Python
- Flask (web framework)
-  AES Encryption: Utilizing the PyCryptodome library for AES encryption and decryption.
- AWS EC2 instance
- SQLite (database)
- HTML/CSS/JavaScript
## Installation
1. Clone the repository:
git clone https://github.com/ronnie-nguru/WebChat-Application-Project.git
Install the required dependencies.
Run the application.
Access the application in your web browser at http://16.170.240.125/ Deployment on AW
## Usage
Open your web browser and navigate to the public Ip address of your EC2 instance.
Create an account or log in with your existing credentials. 
Start messaging and enjoy secure and private conversations with other users.
## File Structure
├── app
│   ├── _init_.py
│   ├── auth
│   │   ├── _init_.py
│   │   ├── email.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── errors
│   │   ├── _init_.py
│   │   └── handlers.py
│   ├── main
│   │   ├── _init_.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── profile.css
│   │   │   └── styles.css
│   │   ├── images
│   │   └── loading.gif
│   └── templates
│       ├── _post.html
│       ├── auth
│       │   ├── login.html
│       │   ├── register.html
│       │   ├── reset_password.html
│       │   └── reset_password_request.html
│       ├── base.html
│       ├── edit_profile.html
│       ├── errors
│       │   ├── 404.html
│       │   └── 500.html
│       ├── index.html
│       ├── styles.css
│       └── user.html
├── app.db
├── config.py
├── microblog.py
├── static
│   └── images
│       └── avatar-3d6aa7ff8ba1ed6b83a9554fcac6ed4f.jpeg
├── tests.py
└── uploads
    ├── avatar-2c3ebcea2f24031351de56ef400a47bd.jpeg
    ├── avatar-3f43bd18c332bc59cf4c1624028329e5.jpeg
    └── avatar-7afb0547e6301b9a37455021a2bf979b.jpeg

13 directories, 34 files
## License

## Contact
-	ronnie.nguru@strathmore.edu



