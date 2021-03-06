from django.db import models
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from tinymce import models as tinymce_models

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __unicode__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField('Company', max_length=200)
    slug = models.SlugField(unique=True)
    year = models.CharField(max_length=4)
    design = models.CharField(max_length=50, blank=True)
    #description = models.TextField()
    description = tinymce_models.HTMLField()
    description_en = tinymce_models.HTMLField()
    url = models.URLField(blank=True)
    pub_date = models.DateTimeField('Date published');
    category = models.ForeignKey(Category)
    order = models.IntegerField(blank=True)
    
    class Meta:
        verbose_name_plural = "companies"
    
    def __unicode__(self):
        return self.company_name
    
    def get_absolute_url(self):
        #import pdb; pdb.set_trace()
        return reverse('portfolios.views.detail', args=[str(self.slug)])

class Image(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    thumb = ImageSpecField([ResizeToFill(220, 147)], image_field='image', format='JPEG', options={'quality': 90})

    def __unicode__(self):
        return self.name