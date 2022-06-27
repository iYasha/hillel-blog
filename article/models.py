from django.db import models


class Article(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=40)  # Текстовое поле
	description = models.TextField()  # Текстовое поле
	image = models.ImageField(upload_to='images/')  # Поле для загрузки изображений
	view_count = models.IntegerField(default=0)  # Целочисленное поле
	updated_at = models.DateTimeField(auto_now=True)  # Дата и время которая задается автоматически при изменении записи
	created_at = models.DateTimeField(auto_now_add=True)  # Дата и время которая задается автоматически при создании записи


class Member(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email