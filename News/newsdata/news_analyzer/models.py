from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

class Article(models.Model):
	article_id = models.AutoField(primary_key=True)
	def __unicode__(self):
		return self.article_id

	article_title = models.CharField(max_length=100)
	def __unicode__(self):
		return self.article_title

	article_date = models.CharField(max_length=50)
	def __unicode__(self):
		return self.article_date
	
	article_source = models.CharField(max_length=20)
	def __unicode__(self):
		return self.article_source
	
	article_text = models.TextField()
	def __unicode__(self):
		return self.article_text

class Author(models.Model):
	author_id = models.AutoField(primary_key=True)
	def __unicode__(self):
		return self.author_id

	author_name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.author_name

class Keyword(models.Model):
	keyword_id = models.AutoField(primary_key=True)
	def __unicode__(self):
		return self.keyword_id

	keyword_word = models.CharField(max_length=50)
	def __unicode__(self):
		return self.keyword_word
