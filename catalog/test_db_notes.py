# *********** READ ME ***********
# don't run this. only use the commands in the shell
# python manage.py shell

from catalog.models import User_Profile

u = User_Profile(user_name='panda', name='gladys chan', email='123@gmail.com')
u.save()
# below command to check if user was inserted to table
u.get_user_name() # gives back panda
User_Profile.set_name(u.id, 'griz')

# https://docs.djangoproject.com/en/2.1/topics/db/queries/
# https://docs.djangoproject.com/en/2.1/topics/db/managers/#django.db.models.Manager
