from django.contrib import admin
from blog.models import *
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogParagraph)
admin.site.register(BlogComment)
