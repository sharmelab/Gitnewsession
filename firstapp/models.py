from django.db import models

class Library(models.Model):
	BookName = models.CharField(max_length=30)
	PublisherName = models.CharField(max_length=30)
	AuthorName = models.CharField(max_length=30)
	EditionName = models.CharField(max_length=30)

	def __str__(self):
		return self.BookName
		
