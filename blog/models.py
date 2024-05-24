from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст Новостей')
    image = models.ImageField("Картинуа поста", upload_to='post_img/')
    feature = models.BooleanField(' в слайдере', default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    slug = models.SlugField('сылка', unique=True)
    created_at = models.DateTimeField('дата создания поста', default=timezone.now)

    class Meta:
        verbose_name = 'Novost'
        verbose_name_plural = "Novosti"
    def __str__(self):
        return self.title
    

    def get_link(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

class Category(models.Model):
    title = models.CharField('Nazvanie kategorii',max_length=255)
    image = models.ImageField('kartinka kategorii', upload_to='cat_img/')
    slug = models.SlugField('Ссылка', unique=True)


    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Katigorii'
    
    def __str__(self):
       return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()


    class Meta:
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.author.login + ' ' + self.post.title