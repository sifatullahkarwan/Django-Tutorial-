from django.db import models
from django.contrib.auth.models import User
from PIL import Image# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities. 
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)# create onto one relationship between User field
    # CASCADE means when we delete the user it should delete the profile

    image = models.ImageField(default = 'default.jpg',upload_to=' profile_pics')# it is image field and it accept th default.jpg by defalut if no imaeg uploaded to user and uploadt_to directory that images uploded to tath
    def __str__(self):
        return f'{self.user.username} Profile'#Save the current instance

    def save(self): # This save(self) method  gets run after our model is saved
        super().save()#records the instance in the database
        img = Image.open(self.image.path)# Opens and identifies the given image file.
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)#A thumbnail is a small image representation of a larger image
            img.save(self.image.path)#Saves this image under the given filename

# pillow is the labrary that we work with images
# pip install pillow

# to save the images and this models make migrations
#then go to shell
# >>> user = User.objects.filter(username = 'admin').first()
# user.profile # it access the admin user  profile
#>>> user.profile.image.width # print the width of the image
# >>> user.profile.image.url : print the url of image uploaded


