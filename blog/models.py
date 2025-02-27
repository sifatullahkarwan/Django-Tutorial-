from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse# revers return the full URL to the route as string

# Create your models here.
# the class name is going to represent the database tables like our table name is Post

class Post(models.Model):
    title = models.CharField(max_length=100)# this chracter field
    content = models.TextField()# it line and line of text or unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)# auto_now = True: which means update the date posted 
    #to the current 
    author = models.ForeignKey(User,on_delete=models.CASCADE)# ondelete tell django what shuld do when a auther field is deleted
    # user is seprated table and foreignkey shows the one_money relationship on user can have multiple post
    # CASCADE means when we delete the post it will not delate the user

    def __str__(self):# it descriptive our table while >>> Post.objects.all()
        return self.title


    def get_absolute_url(self):# after creating this method if we create a post it redirect as to post.html
        return reverse('post-detail',kwargs={'pk': self.pk})





# migaration allow us to change our database even after it created

    # now save migaration to terminal
    # python manag.py makemigrations # it will make these table on migrations/0001
    # python manage.py migrate # it run the 0001 fields


# now how to see the sql code
# got terminal
# python manage.py sqlmigrate blog 0001

# to run the sql shell
# python manage.py shell
#>>from blog.models import post
# >>form django.contrib.auth.models import USer
#>>User.objects.all() it print all users
# >> User.objects.first() # it give the first user
# >> User.objects.filter(username = 'khan') # it filter User tabel
#>>> user = User.objects.filter(username = 'khan').first()# add the query to user varaible
# # >> user.id 
# >> user.pk primarykey
#Post.objects.all()
# Now create new post
#>>> post_1 = Post(title = 'Blog 1' , content ='First Post Content! ' , author=user)
# post_1.save()# it save this new post to database
# >>> post_4 = Post(title = 'Blog 4 ', content = 'Fourth content', author_id = user2.id) : with auhor_id we can define the author

# post = Post.objects.first()
# post.content
# post.author
# >>> user1.post_set.all() ; it allow us to easily list all the post by user1


