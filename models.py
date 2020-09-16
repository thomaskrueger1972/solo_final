from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your first name must be more than 2 characters!!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your last name must be more than 2 characters!!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid format!!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!!"
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password and confirm password do not match!!"
        return errors

        
    # def login_validator(self, postData):
    #     errors = {}
    #     if len(self.filter(email = postData['email'])) < 1:
    #         errors['email'] = 'Email does not exist'
    #         return errors
    #     else:
    #         user = self.get(email = postData['email'])
    #         if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
    #             return errors
    #         else:
    #             errors['password'] = "Invalid email/password combination."
    #             return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    desc = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.desc

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     text = models.TextField(max_length=255)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



                

