from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField("Название", max_length=50)
    
    def __str__(self):
        return self.title
    
class Info(models.Model):
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'

    language = models.CharField("Язык", max_length=50, default='ru')
    year = models.IntegerField("Год")
    pages = models.IntegerField("Страницы")
    country = models.CharField("Страна", max_length=50)

    def __str__(self):
        return self.country
    
class Teg(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    title = models.CharField("Возрастное категория", max_length=50)
    age = models.DecimalField("Возраст", max_digits=4, decimal_places=1)

    def __str__(self):
        return self.title

class Book(models.Model):
    RATING = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10,decimal_places=2)
    reating = models.CharField("Рейтинг", choices=RATING)
    author = models.CharField("Автор", max_length=50)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    info = models.ForeignKey(Info, verbose_name="Информация", on_delete=models.CASCADE, blank=True, null=True)
    teg = models.ManyToManyField(Teg, verbose_name="Тег")

    def __str__(self):
        return self.title
