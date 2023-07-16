from ckeditor_uploader import fields
from django.contrib.auth.models import User
from django.db import models


class Ads(models.Model):
    content = fields.RichTextUploadingField()
    title = models.CharField(max_length=128)
    category = models.ManyToManyField('Category', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    dateTime_publ = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    content = models.TextField()
    status = models.BooleanField(default=False)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)


class Category(models.Model):
    tanks = 'TK'
    healers = 'HL'
    DD = 'DD'
    merchants = 'MT'
    guildmaster = 'GM'
    kvestgiver = 'KG'
    kuznets = 'KZ'
    kozhevn = 'KZH'
    zel_yevar = 'ZV'
    master_zaklinaniy = 'MZ'

    CATEGORIES = (
        (tanks, 'Танки'),
        (healers, 'Хилы'),
        (DD, 'ДД'),
        (merchants, 'Торговец'),
        (guildmaster, 'Гилдмастер'),
        (kvestgiver, 'Квестгивер'),
        (kuznets, 'Кузнец'),
        (kozhevn, 'Кожевник'),
        (zel_yevar, 'Зельевар'),
        (master_zaklinaniy, 'Мастер заклинаний')
    )

    name = models.CharField(max_length=3, choices=CATEGORIES)
