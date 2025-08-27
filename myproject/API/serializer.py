from rest_framework import serializers
from .models import Project, UploadProjectFiles, ReferenceLinks, CheckBoxes

class UploadProjectFilesSerializer(serializers.ModelSerializer):
  class Meta:
    model = UploadProjectFiles
    fields = ['file']

  
class ReferenceLinksSerializer(serializers.ModelSerializer):
  class Meta:
    model = ReferenceLinks
    fields = ['url']




class ProjectSerializer(serializers.ModelSerializer):
  uploaded_files = UploadProjectFilesSerializer(many=True, required=False)
  reference_links = ReferenceLinksSerializer(many=True, required=False)

  checkboxes = serializers.PrimaryKeyRelatedField(
    many=True,
    queryset=CheckBoxes.objects.all(),
    required=False
  )


  class Meta:
    model = Project
    fields = [
      'fullName', 'email', 'preferred_contact_method', 'profile_picture',
      'represent_a_company', 'company_name', 'industry', 'industry_other',
      'company_size', 'company_website', 'project_title', 'project_description',
      'category', 'category_other', 'budget', 'deadline', 'checkboxes',
      'uploaded_files', 'reference_links'
    ]

  def validate(self, data):

    if data.get('represent_a_company') and not data.get('company_name'):
      raise serializers.ValidationError({
          'company_name': 'Company name is required when representing a company.'
      })

    if data.get('category') == 'Other' and not data.get('category_other'):
      raise serializers.ValidationError({
          'category_other': 'Please specify the other category.'
      })
    
    if data.get('industry') == 'Other' and not data.get('industry_other'):
      raise serializers.ValidationError({
        'industry_other': 'Please specify the other industry.'
      })
    
    return data
    
  
  def create(self, validated_data):
    # extract nested data
    uploaded_files_data = validated_data.pop('uploaded_files', [])
    reference_links_data = validated_data.pop('reference_links', [])
    checkboxes_data = validated_data.pop('checkboxes', [])



    #create project
    project = Project.objects.create(**validated_data)


    #create related object
    for file_data in uploaded_files_data:
      if isinstance(file_data, dict):
        #if it's a dict extarct the file
        UploadProjectFiles.objects.create(project=project, file=file_data['file'])
      else:
        #if it's alredy a file object
        UploadProjectFiles.objects.create(project=project, file=file_data)

    for link_data in reference_links_data:
      if isinstance(link_data, dict):
        # if it's a dict extract the url
        ReferenceLinks.objects.create(project=project, url=link_data['url'])
      else:
        ReferenceLinks.objects.create(project=project, url=link_data)

    project.checkboxes.set(checkboxes_data)

    return project

