from django.db import models

class NameDescriptionModel(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Category(NameDescriptionModel):
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

class Complexity(NameDescriptionModel):
    
    class Meta:
        verbose_name = 'Complexity'
        verbose_name_plural = 'Complexities'
        ordering = ['name']

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=256, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['uploaded_at']

class Game(NameDescriptionModel):
    rating = models.FloatField(default=0.0)
    
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='games')
    complexity = models.ForeignKey(Complexity, on_delete=models.DO_NOTHING, related_name='games')
    logo = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='game_logo')
    screenshots = models.ManyToManyField(Image, blank=True, related_name='game_screenshots')
    
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['name']