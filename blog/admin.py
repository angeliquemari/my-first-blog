from django.contrib import admin
from .models import Post, Comment
# from .models import CommentTest

admin.site.register(Post)
# admin.site.register(CommentTest)
admin.site.register(Comment)
