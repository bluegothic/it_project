from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=128, unique=True)
  views = models.IntegerField(default=0)
  likes = models.IntegerField(default=0)
  slug = models.SlugField(unique=True)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Category, self).save(*args, **kwargs)

  class Meta:
    verbose_name_plural = 'Categories'

  def __str__(self):
      return self.name

class Page(models.Model):
  category=models.ForeignKey(Category, on_delete=models.CASCADE)
  title=models.CharField(max_length=128)
  url=models.URLField()
  views=models.IntegerField(default=0)

  def __str__(self):
      return self.title

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  website = models.URLField(blank=True)
  picture = models.ImageField(upload_to='profile_images',blank=True)

  def __str__(self):
      return super().user.username


class Comment(models.Model):
  comment_id = models.IntegerField(primary_key=True)
  author_id = models.CharField(max_length=128)
  topic_id = models.ForeignKey(Category, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  context = models.CharField(max_length=128)
