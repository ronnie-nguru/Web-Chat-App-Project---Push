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
Install Python and pip:
sudo yum install python3
sudo yum install python3-pip
Install virtualenv: sudo pip3 install virtualenv
Create a virtual environment for your application: virtualenv venv
source venv/bin/activate.
Install the required Python libraries for your application using pip, typically stored in a requirements.txt file: pip install -r requirements.txt.
Configure Nginx as a reverse proxy: Install Nginx: sudo yum install nginx
Install Nginx: sudo yum install nginx
Install Gunicorn: pip install gunicorn

1. Clone the repository:
git clone https://github.com/ronnie-nguru/WebChat-Application-Project.git
Install the required dependencies.
Run the application.
Access the application in your web browser at http://16.170.240.125/ Deployment on AWS
## Development on AWS EC2 instance
Installing Application on AWS EC2
To install and run your application on EC2, you'll need to follow several steps including setting up the server, installing libraries, configuring Nginx as a reverse proxy, running your server with Gunicorn, and configuring various files. Here's a step-by-step guide to help you through the process:
Set up an EC2 instance:
-	- Go to the AWS Management Console and navigate to the EC2 service.
-	- Launch a new EC2 instance, choosing an appropriate Amazon Machine Image (AMI) based on your requirements.
-	- Configure the instance details, such as instance type, network settings, and storage.
-	- Create or select an existing key pair to securely connect to your EC2 instance.
-	- Launch the instance.
Connect to your EC2 instance:
Once your EC2 instance is running, you can connect to it using SSH.
Open your preferred terminal application and navigate to the directory where your key pair file is located.

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
## Credits 
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins

## Contact
-	ronnie.nguru@strathmore.edu



