from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20)
    # lastName = models.CharField(max_length=20)
    # address = models.TextField()
    # phoneNumber = models.IntegerField()

    def __str__(self):
        return self.name


# ---------------------------------------------------------------------------------------------------------------


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title + " | " + self.author.name


# ---------------------------------------------------------------------------------------------------------------
