from django.db import models



PREFERRED_CONTACT_METHOD_CHOICES = [
  ('email', 'Email'),
  ('phone', 'Phone'),
  ('whatsapp', 'WhatsApp'),
]



INDUSTRY_CHOICES = [
  ('technology', 'Technology'),
  ('finance', 'Finance'),
  ('healthcare', 'Healthcare'),
  ('education', 'Education'),
  ('other', 'Other'),
]



CATEGORY_CHOICES = [
  ('Web Development', 'Web Development'),
  ('Mobile App', 'Mobile App'),
  ('Graphic Design', 'Graphic Design'),
  ('Writing', 'Writing'),
  ('Other', 'Other'),
]





class CheckBoxes(models.Model):
  option = models.CharField(max_length=100, blank=False, unique=True)
  def __str__(self):
    return self.option



class Project(models.Model):
  #step 1
  fullName = models.CharField(max_length=200, blank=False)
  email = models.EmailField(blank=False)
  preferred_contact_method = models.CharField(choices=PREFERRED_CONTACT_METHOD_CHOICES, blank=False, max_length=100)
  profile_picture = models.ImageField(upload_to='profile_pictures/')
  represent_a_company = models.BooleanField(blank=False)

  #step 2
  company_name = models.CharField(max_length=200, blank=True) 
  industry = models.CharField(choices=INDUSTRY_CHOICES, blank=True, max_length=100)
  industry_other = models.CharField(max_length=100, blank=True)
  company_size = models.CharField(max_length=10, blank=True)
  company_website = models.CharField(max_length=100, blank=True)

  #step 3
  project_title = models.CharField(max_length=200, blank=False)
  project_description = models.TextField(blank=False)
  category = models.CharField(choices=CATEGORY_CHOICES, blank=False, max_length=100)
  category_other = models.CharField(max_length=200, blank=True)
  budget = models.CharField(max_length=50, blank=False)
  deadline = models.DateField(blank=False)

  #step 4
  checkboxes = models.ManyToManyField(CheckBoxes, blank=True)
  #upload_files = models.ManyToManyField(UploadProjectFiles, blank=True)
  #reference_links = models.ManyToManyField(ReferenceLinks, blank=True)

  created_at = models.DateField(auto_now_add=True)


  class Meta:
    ordering = [ '-created_at' ]
    verbose_name = 'Project'
    verbose_name_plural = 'Projects'


  def __str__(self):
    return f'{self.fullName} - {self.project_title} / {self.created_at}'




class UploadProjectFiles(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='uploaded_files')
  file = models.FileField(upload_to='uploads/')
  def __str__(self):
    return self.file.name


class ReferenceLinks(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reference_links')
  url = models.CharField(max_length=100)

  def __str__(self):
    return self.url