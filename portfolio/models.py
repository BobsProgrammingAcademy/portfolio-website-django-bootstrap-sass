from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image


class Hero(models.Model):
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=300)
  description = models.CharField(max_length=500)
  image = models.ImageField()

  class Meta:
    verbose_name = 'Hero'
    verbose_name_plural = 'Hero'

  def __str__(self):
    return '{0} {1}'.format(self.title, self.subtitle)


class About(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  icon = models.CharField(max_length=30)  # Material Icon name

  class Meta:
    verbose_name = 'About'
    verbose_name_plural = 'About'

  def __str__(self):
    return self.title


class Tag(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


class Project(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  link = models.CharField(max_length=250)
  image = models.ImageField()
  tags = models.ManyToManyField(Tag)

  # override the save method and
  # use the Image class of the PIL package
  # to convert it to JPEG
  def save(self, *args, **kwargs):
    if self.image:
      filename = "%s.jpg" % self.image.name.split('.')[0]

      image = Image.open(self.image)
      # for PNG images discard the alpha channel and fill it with some color
      if image.mode in ('RGBA', 'LA'):
        background = Image.new(image.mode[:-1], image.size, '#fff')
        background.paste(image, image.split()[-1])
        image = background
        image_io = BytesIO()
        image.save(image_io, format='JPEG', quality=100)

        # change the image field value to be the newly modified image value
        self.image.save(filename, ContentFile(image_io.getvalue()), save=False)
    super(Project, self).save(*args, **kwargs)

  def __str__(self):
    return self.name


class Contact(models.Model):
  address = models.CharField(max_length=250)
  email = models.CharField(max_length=150)
  phone = models.CharField(max_length=20)

  class Meta:
    verbose_name = 'Contact'
    verbose_name_plural = 'Contact'

  def __str__(self):
    return self.email


class Footer(models.Model):
  copyright = models.CharField(max_length=200)

  class Meta:
    verbose_name = 'Footer'
    verbose_name_plural = 'Footer'

  def __str__(self):
    return self.copyright
