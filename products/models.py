from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Titlo")
    subtitle = models.CharField(max_length=200,
                                verbose_name="Subtítulo")
    content = models.TextField(
        verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen",
                              upload_to="products")
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-created']

    def __str__(self):
        return self.title
