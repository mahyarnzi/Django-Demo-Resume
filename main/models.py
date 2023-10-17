from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill  # or try ResizeToFill


class Profile(models.Model):
    image = ProcessedImageField(upload_to='profile/', format='JPEG', processors=[ResizeToFill(170, 170)],
                                options={'quality': 100}, default='default/no-avatar.jpg')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    summary = models.TextField()
    resume = models.FileField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class TechnicalSkill(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(max_length=30)
    degree = models.CharField(max_length=20)
    field = models.CharField(max_length=30)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.degree + ' ' + self.field


class Experience(models.Model):
    logo = ProcessedImageField(upload_to='experience/', format='JPEG', processors=[ResizeToFill(20, 20)],
                               options={'quality': 100}, default='default/no-avatar.jpg')
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    task = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title + ' at ' + self.company


class Certificate(models.Model):
    logo = ProcessedImageField(upload_to='certificate/', format='JPEG', processors=[ResizeToFill(20, 20)],
                               options={'quality': 100}, default='default/no-avatar.jpg')
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    issue_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name + ' at ' + self.organization


class SoftSkill(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Honor(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publish_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Language(models.Model):
    name = models.CharField(max_length=50)
    ORDER_CHOICES = [(i, i) for i in range(1, 6)]
    level = models.IntegerField(choices=ORDER_CHOICES, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Background(models.Model):
    name = models.CharField(max_length=10, default='main')
    background = ProcessedImageField(upload_to='background/', format='JPEG', processors=[ResizeToFill(1600, 825)],
                                     options={'quality': 100}, default='default/no-avatar.jpg')
    icon = ProcessedImageField(upload_to='background/', format='png', processors=[ResizeToFill(30, 30)],
                               options={'quality': 100}, default='default/no-avatar.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
