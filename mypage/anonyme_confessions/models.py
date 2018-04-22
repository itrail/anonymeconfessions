from django.db import models
from datetime import datetime
import pytz

class User(models.Model):
    username = models.CharField(max_length=150, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.username)


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    keywords = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Data opublikowania', default=datetime.now(pytz.timezone('Europe/Warsaw')))

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    commentator_nick = models.CharField(max_length=150, null=True)
    comment = models.CharField(max_length=600, null=True)
    com_date = models.DateTimeField('Data opublikowania', default=datetime.now(pytz.timezone('Europe/Warsaw')))

class Reported_article(models.Model):
    id = models.AutoField(primary_key=True)
    reported_article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    reason = models.CharField(max_length=500)