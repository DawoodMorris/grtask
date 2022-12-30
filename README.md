This is the Test Task - Python Django Engineer/Remote GR 122 by Dawood Morris Kaundama

Make sure to install the mysqlclient library, as this app uses the mysql backend

The admin username is: gradmin
The password for the admin is: 12345%Qwerty
Email can be any email

If login does not work, please create the admin user with the `manage.py` command utils

The `DEBUG = True` in the Django settings file

Here is how to run the app:

After clonning the repo, cd into it then run the server locally.

Then head to http://127.0.0.1:8000/admin and use the given credentials.
Add or remove reservations or rentals as required

Head to http://127.0.0.1:8000/grapp/reservations/ to display/view the rervations

grtask stands for Guest Ready Task

Run the tests with the command

`$ python manage.py test grapp`

More tests could be added, such as:
Make sure we do not add a duplicate reservation to the same rental (e.g same checkin, checkout dates)
