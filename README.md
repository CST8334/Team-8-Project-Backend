# Team-8-Project-Backend

After cloning run these commands on the directory that the project is in.
These commands are only needed if the components have not been installed on your environment before.
There is no risk of harm running the command a second time, a message that it is already installed will be displayed.

"pip install django"
"pip install djangorestframework"
"pip install django-cors-headers"

Before running the server for the first time run.

"python manage.py migrate"

Finally start the server.

"python manage.py runserver"

Alternatively, start the server with a different port number.

"python manage.py runserver port#here"

To close down the server, from the terminal "ctrl + c"

Admin
--------------------------
To create a new superuser enter in the terminal

"python manage.py createsuperuser"

and follow the instructions. The new account will be of type admin and staff.

It would be a good idea to scrub the database as well to remove any current accounts that might be leftover from initial development.
