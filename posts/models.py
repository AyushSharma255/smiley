from django.db import models


# Create your models here.
class Face(models.Model):
    title = models.TextField()
    published = models.DateTimeField()

    # Face Elements
    eyeWidth = models.IntegerField(default=50)
    eyeHeight = models.IntegerField(default=50)
    happiness = models.IntegerField(default=50)
    smileWidth = models.IntegerField(default=5)
	
	@property.getter()
	def comment_count(self):
		return len(self.comments.all())

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    face = models.ForeignKey(Face, on_delete=models.CASCADE, related_name="comments")
	
    def __str__(self):
        return self.content
