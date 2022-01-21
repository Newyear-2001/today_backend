from django.db import models

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    socore = models.IntegerField()
    content = models.CharField(max_length=100)
    nickname = models.CharField(max_length=10)
    pub_date = models.DateTimeField(auto_now_add=True)

class Dress(models.Model):
    temputure = models.FloatField()
    dress_1 = models.CharField(max_length=10, null=False)
    dress_2 = models.CharField(max_length=10, null=True)
    dress_3 = models.CharField(max_length=10, null=True)
    dress_4 = models.CharField(max_length=10, null=True)
    dress_5 = models.CharField(max_length=10, null=True)
    dress_6 = models.CharField(max_length=10, null=True)