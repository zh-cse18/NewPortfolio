from django.db import models

# Create your models here.


class  HeroArea(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    image = models.FileField()
    fb_link = models.CharField(max_length=100)
    tw_link = models.CharField(max_length=100)
    insta_link = models.CharField(max_length=100)
    linked_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.title

    def __str__(self):
        return self.fb_link

    def __str__(self):
        return self.tw_link

    def __str__(self):
        return self.insta_link

    def __str__(self):
        return self.linked_link


class MyDetail(models.Model):
    my_name = models.CharField(max_length=50)
    age = models.IntegerField()
    experience = models.IntegerField()
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    freelance_status = models.CharField(max_length=50)

    def __str__(self):
        return self.my_name

    def __str__(self):
        return self.age

    def __str__(self):
        return self.experience

    def __str__(self):
        return self.country

    def __str__(self):
        return self.email

    def __str__(self):
        return self.location

    def __str__(self):
        return self.phone

    def __str__(self):
        return self.freelance_status


class Education(models.Model):
    institute_name = models.CharField(max_length=50)
    passing_year = models.CharField(max_length=11)
    education_details = models.TextField()

    def __str__(self):
        return self.institute_name

    def __str__(self):
        return self.passing_year

    def __str__(self):
        return self.education_details


class Experience(models.Model):
    company_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    job_duration = models.CharField(max_length=50)
    jod_details = models.TextField()

    def __str__(self):
        return self.company_name

    def __str__(self):
        return self.position

    def __str__(self):
        return self.job_duration

    def __str__(self):
        return self.jod_details
