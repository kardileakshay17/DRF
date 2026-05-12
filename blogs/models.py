from django.db import models

# Create your models here.

class BlogsModel(models.Model):
    blog_title=models.CharField(max_length=32)
    blog_body=models.CharField(max_length=32)

    def __str__(self):
        return self.blog_title
    
class CommentModel(models.Model):
    blog = models.ForeignKey(BlogsModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment