from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta


# Create your models here.
class Topic(models.Model):
    MAX_CHAR_LEN = 128
    author_user_id = models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=now() + timedelta(hours=1))
    # TYPES = (
    #     ('S', 'Single'),
    #     ('M', 'Multiple'),
    # )
    type = models.CharField(max_length=1, default='S')  # 0 单选  1 多选
    title = models.CharField(max_length=MAX_CHAR_LEN)
    context = models.CharField(max_length=MAX_CHAR_LEN)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    option1 = models.CharField(max_length=MAX_CHAR_LEN)
    option2 = models.CharField(max_length=MAX_CHAR_LEN)
    option3 = models.CharField(max_length=MAX_CHAR_LEN)
    option4 = models.CharField(max_length=MAX_CHAR_LEN)
    option5 = models.CharField(max_length=MAX_CHAR_LEN)
    cnt1 = models.IntegerField(default=0)
    cnt2 = models.IntegerField(default=0)
    cnt3 = models.IntegerField(default=0)
    cnt4 = models.IntegerField(default=0)
    cnt5 = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return super().user.username


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    author_id = models.CharField(max_length=128)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    context = models.CharField(max_length=128)


class PollRecord(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)


class LikeRecord(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    situation = models.IntegerField(default=0)
