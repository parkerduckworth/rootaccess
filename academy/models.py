from django.db import models


class Student(models.Model):
    user_name = models.CharField(max_length=25, unique=True, help_text='Enter student Alias')
    email = models.EmailField(unique=True, help_text='Enter student email address')
    # Need to hash this or something... probably use django form password widget
    password = models.CharField(max_length=50)

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    location = models.CharField(max_length=200, default='Somewhere', help_text='Enter student hometown')

    membership_date = models.DateTimeField(auto_now_add=True)
    current_module = models.ForeignKey('Module', on_delete=models.CASCADE)


    def __str__(self):
        return self.user_name


class Module(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the module name')
    details = models.TextField(max_length=5000, help_text='Enter a brief description of the module')

    def __str__(self):
        return self.name