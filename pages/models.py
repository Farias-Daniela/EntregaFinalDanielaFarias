from django.db import models

from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    subtitle = models.CharField(max_length=150, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='pages/', verbose_name="Imagen")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        return self.title
    

class PageImage(models.Model):
    product = models.ForeignKey(Page, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

