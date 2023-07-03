from django.contrib.auth.models import User

from io import BytesIO # handles images and resizing
from PIL import Image # importing image from PIL library

from django.core.files import File # easy to create thumbnails using this 
from django.db import models

# Create your models here.
class Matches(models.Model): # field 'name' which is Charfield (name of the Game) # creating a new model Matches 
    name = models.CharField(max_length=255) # field 'name' which is Charfield (name of the Match)
    slug = models.SlugField() # address version of the name

    class Meta:
        ordering = ('name',) # ordering matches by name

    def __str__(self):
        return self.name # string representation of the match to make it clear on the backend

    def get_absolute_url(self):
        return f'/{self.slug}/' # get url to handle with the frontend

class Game(models.Model): 
    matches = models.ForeignKey(Matches, related_name='games', on_delete=models.CASCADE) # reference to the match using ForeignKey (index in the database or a relational key), if we delete matches then we also delete the games due to on_delete=models.CASCADE
    name = models.CharField(max_length=255) # name of the game 
    slug = models.SlugField() # address version of the game
    description = models.TextField(blank=True, null=True) # description of the game, set to blank=True, null=True if we don't want description
    price = models.DecimalField(max_digits=6, decimal_places=2) # price of the game, decimal_places=2 as Great British Pounds is set to two decimal places 
    image = models.ImageField(upload_to='uploads/', blank=True, null=True) # image of the game, uploaded to an image folder 'uploads' set to blank=True, null=True if we don't want image of the game 
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True) # thumbnail of the game, uploaded to an image folder 'uploads' set to blank=True, null=True if we don't want thumbnail of the game and generated from the image field 
    date_added = models.DateTimeField(auto_now_add=True) # when creating a new game on the backend it will automatically fill a date time to know when it has been added to the database 

    class Meta:
        ordering = ('-date_added',) # ordered by newest game added in descending order    

    def __str__(self):
        return self.name # string representation of the game to make it clear on the backend

    def get_absolute_url(self):
        return f'/{self.matches.slug}/{self.slug}/' # get slug based on the matches field 

    def get_image(self):
        if self.image: # checking if we have image in the field 
            return "http://127.0.0.1:8000" + self.image.url # returns whole address to make it easy to use on frontend 
        return ''

    def get_thumbnail(self):
        if self.thumbnail: # checking if we have thumbnail in the field 
            return "http://127.0.0.1:8000" + self.thumbnail.url
        else:
            if self.image: # check if we have image first as thumbnail is based on the image 
                self.thumbnail = self.make_thumbnail(self.image) # generates thumbnail 
                self.save() # saved in backend/database  

                return "http://127.0.0.1:8000" + self.thumbnail.url
            else:
                return '' # if game has no image 

    def make_thumbnail(self, image, size=(300, 200)): # default size 300 by 200 pixels wide 
        img = Image.open(image) # importing from image library to create an image 
        img.convert('RGB') # converted into RGB to make sure image is clear 
        img.thumbnail(size) # thumbnail size 300 by 200 pixels wide 

        thumb_io = BytesIO() 
        img.save(thumb_io, 'JPEG', quality=85) # saved as JPEG and quality size of 85 to make it a thumbnail

        thumbnail = File(thumb_io, name=image.name) # creating thumbnail imported from 'django.core.files import File'

        return thumbnail

# Leaderboard implementation
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return self.user.username



