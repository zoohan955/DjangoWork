from django.db import models

# Create your models here.


class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('datePublished')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choise(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choise_text=models.CharField(max_length=200)
    votes=models.ImageField(default=0)
    def __str__(self):
        return self.choise_text
    