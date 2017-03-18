from django.db import models

# Create your models here.

class BlogPost(models.Model):
	#post_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	#text = models.TextField()

	def __str__(self):
		return '%s %s' % (self.id, self.title)

	class Meta:
		unique_together = (("title"),)

class BlogParagraph(models.Model):
	paragraph = models.TextField()
	blog_post = models.ForeignKey(BlogPost)

	def __str__(self):
		return '%s %s' % (self.id, self.paragraph)

class BlogComment(models.Model):
	#comment_id = models.AutoField(primary_key=True)
	text = models.CharField(max_length=255)
	paragraph = models.ForeignKey(BlogParagraph, related_name='+')

	def __str__(self):
		return self.text
