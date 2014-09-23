from django.contrib import admin
from django.contrib.comments.admin import CommentsAdmin
from django.contrib.comments.models import Comment

from comments.models import MPTTComment

admin.site.register(MPTTComment, CommentsAdmin)