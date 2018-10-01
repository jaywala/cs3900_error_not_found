

import django
django.setup()

import catalog.models as c

a = c.Advertisement.objects.filter(poster="gladyschanmail@gmail.com")
print(a)
