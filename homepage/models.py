from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from notifications.signals import notify
from django.utils.text import Truncator
from django.db import models
from tinymce.models import HTMLField

# models from my understanding are the location of all the info about your data. you use it to make databases

class Subject(models.Model):
    subject= models.CharField(max_length=64)

    def __str__(self):
        return self.subject

class Chapter(models.Model):
    chapter= models.CharField(max_length=64)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.chapter

class Tag(models.Model):
    tag= models.CharField(max_length=64)
    def __str__(self):
        return self.tag

class Post(models.Model):
    chapter= models.ForeignKey(Chapter, on_delete= models.SET_NULL, blank=True, null=True)
    tag= models.ForeignKey(Tag, on_delete= models.SET_NULL, blank=True, null=True)
    caption = models.TextField(max_length=500, blank=True)  # caption is a field in this Post model. it specifies a class attribute Charfield and represents a database column. blank=True lets the field be optional left empty
    date_posted = models.DateTimeField(default=timezone.now)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = HTMLField(blank=True,null=True)
    def __str__(self):
        return f"{self.caption}+1"

class Introduction(models.Model):
    chapter= models.ForeignKey(Chapter,on_delete= models.SET_NULL, blank=True, null=True )
    intro= models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.intro}"


class Video(models.Model):
    chapter= models.ForeignKey(Chapter,on_delete= models.SET_NULL, blank=True, null=True )
    description= models.TextField(blank=True, null=True)
    video_id= models.CharField(max_length=300)
    v_type= models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.video_id}+ {self.v_type}"


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    modelimage = models.ImageField(upload_to='post_images')



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=500, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})  # returns a string to the post detail that uses the pk of the comment instance. post. pk to link to the correct detail page ie. /post/

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        n = 4
        truncatewords = Truncator(self.content).words(n)
        notify.send(self.author, recipient=self.post.author, verb='commented "' + truncatewords + '" on your post!', action_object=self.post, description='comment', target=self)


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
        notify.send(self.liker, recipient=self.post.author, verb='liked your post!', action_object=self.post, description='like', target=self)

# this model is many to one (many images for one user) related to the Post model. the equilavalcy to match users is:
# PostImage.objects.get(pk=1).post =  Post.objects.get(pk=4)
