from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Kateg(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Введи категорію статті (н.п. Програмування, Адміністрування.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Article(models.Model):
	article_title = models.CharField("Назва статті", max_length = 200)
	article_text = models.TextField("Текст статті" )
	pub_date = models.DateTimeField('Дата публікації')
	Kateg = models.ManyToManyField(Kateg, help_text="Додати статю до категорії")
	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	def get_absolute_url(self):
		return reverse('article-detail', args=[str(self.id)])