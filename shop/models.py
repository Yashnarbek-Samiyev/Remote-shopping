from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translation = TranslatedFields(
        title=models.CharField(max_length=200),
        slug=models.SlugField(max_length=250, unique=True),
    )
    is_sub = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering=['title']
        # indexes=[models.Index(fields=['title'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Product(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=250),
        slug=models.SlugField(max_length=250, unique=True),
        description=models.TextField(blank=True),
    )
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ('-date_created',)
        indexes=[
            
            # models.Index(fields=['id', 'slug']),
            # models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class SlideShow(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=250),
        description = models.TextField(blank=True),   
    )
    
    image = models.ImageField(upload_to='slideshow')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
