from django.db import models

### PORTFOLIO INFORMATION ###
class Information(models.Model):
  sessionKey = models.CharField(max_length=50, blank=True, null=True)
  country = models.CharField(max_length=50, blank=True, null=True)
  Ip_address = models.GenericIPAddressField(blank=True, null=True)
  device_type = models.CharField(max_length=150, blank=True, null=True)
  

### HOME PAGE ###
class Home(models.Model):
  ### INFORMATION ###
  no_of_visted = models.IntegerField(default=0, blank=True, null=True)
  no_of_views = models.IntegerField(default=0, blank=True, null=True)

  ### first section ###
  showcase_image = models.ImageField(upload_to="img/", blank=True, null=True)
  header_content = models.CharField(max_length=200, blank=True, null=True)
  specialize_content = models.CharField(max_length=250, blank=True, null=True)

  ### second section ###
  specialist_title = models.CharField(max_length = 200, blank=True, null=True)
  specialist_summary = models.CharField(max_length=800, blank=True, null=True)

  ###    THIRD SECTION   ###
  client = models.IntegerField(blank=True, null=True)
  award = models.IntegerField(blank=True, null=True)
  hours_worked = models.IntegerField(blank=True, null=True)
  project_completed = models.IntegerField(blank=True, null=True)

  ### fourth section ###
  section_title = models.CharField(max_length = 100, blank=True, null=True)
  section_content = models.CharField(max_length=800, blank=True, null=True)

class Specialize_data(models.Model):
  section = models.ForeignKey(Home, on_delete = models.CASCADE, related_name = "section", blank=True, null=True)
  data_words = models.CharField(max_length = 500, blank=True, null=True)

    
class Specialize_section(models.Model):
  section_1 = models.ForeignKey(Home, on_delete = models.CASCADE, related_name = "section_1", blank=True, null=True)
  title = models.CharField(max_length = 50, blank=True, null=True)
  content = models.TextField(blank=True, null=True) 

class Process_section(models.Model):
  section_3 = models.ForeignKey(Home, on_delete = models.CASCADE, related_name = "section_3", blank=True, null=True)
  title = models.CharField(max_length = 50, blank=True, null=True)
  content = models.TextField(blank=True, null=True)

### ABOUT PAGE ###
class About(models.Model):
  ### INFORMATION ###
  no_of_visted = models.IntegerField(default=0, blank=True, null=True)
  no_of_views = models.IntegerField(default=0, blank=True, null=True)

  ### BODY CONTENT ###
  image = models.ImageField(upload_to='self/', blank=True, null=True)
  heading = models.CharField(max_length=100, blank=True, null=True)
  title = models.CharField(max_length=50, blank=True, null=True)
  details = models.TextField(blank=True, null=True)

class Award_section(models.Model):
  section_1 = models.ForeignKey(About, on_delete = models.CASCADE, related_name = "section_1", blank=True, null=True)
  title=models.CharField(max_length=100, default="AWARD ONE", blank=True, null=True)
  details = models.CharField(max_length=250, blank=True, null=True)
  link = models.URLField(blank=True, null=True)

class Skills_section(models.Model):
  section_2 = models.ForeignKey(About, on_delete = models.CASCADE, related_name = "section_2", blank=True, null=True)
  skills = models.CharField(max_length=30, blank=True, null=True)
  level = models.IntegerField(blank=True, null=True)

class Logo_section(models.Model):
  section_3 = models.ForeignKey(About, on_delete = models.CASCADE, related_name = "section_3", blank=True, null=True)
  logo = models.ImageField(upload_to="logo/", blank=True, null=True)

class Testimonials_section(models.Model):
  section_4 = models.ForeignKey(About, on_delete = models.CASCADE, related_name = "section_4", blank=True, null=True)
  name = models.CharField(max_length=100, blank=True, null=True)
  image = models.ImageField(upload_to = "testimonials/", blank=True, null=True)
  comment = models.TextField(blank=True, null=True)

### work ###
class Work(models.Model):
  ### INFORMATION ###
  no_of_visted = models.IntegerField(default=0)
  no_of_views = models.IntegerField(default=0)

  ### BODY CONTENT ###
  image = models.ImageField(upload_to='items/',blank=True, null=True)
  video = models.FileField(upload_to='video/', blank=True, null=True)
  github_link = models.URLField(blank=True, null=True)
  title = models.CharField(max_length=100, blank=True, null=True)
  description = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.title



### CONTACT PAGE ###
class Contact(models.Model):
  ### INFORMATION ###
  no_of_visted = models.IntegerField(default=0)
  no_of_views = models.IntegerField(default=0)

  ### BODY CONTENT ###
  name = models.CharField(max_length=250, blank=True, null=True)
  email = models.EmailField(max_length=250, blank=True, null=True)
  subject = models.CharField(max_length = 250, blank=True, null=True)
  phone = models.IntegerField(blank=True, null=True)
  message = models.TextField(blank=True, null=True)

  sent_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
