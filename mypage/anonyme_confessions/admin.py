from django.contrib import admin
from .models import User, Article, Reported_article, Comment

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Reported_article)