from .models import Project, UploadProjectFiles, ReferenceLinks, CheckBoxes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializer import ProjectSerializer


class ProjectCreate(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request):
        # Make data mutable
        data = request.data.copy()
        
        # Handle checkboxes
        if 'checkboxes' in data:
            checkboxes_value = data.getlist('checkboxes')
            checkbox_ids = []
            for value in checkboxes_value:
                checkbox, created = CheckBoxes.objects.get_or_create(option=value)
                checkbox_ids.append(checkbox.id) # type: ignore
            data.setlist('checkboxes', checkbox_ids)

        # Handle uploaded files 
        uploaded_files = []
        reference_links = []
        
        if 'uploaded_files' in data:
            files = data.getlist('uploaded_files')
            uploaded_files = files
            # Remove from data - we'll handle manually
            del data['uploaded_files']

        # Handle reference links
        if 'reference_links' in data:
            links = data.getlist('reference_links')
            reference_links = links
            # Remove from data - we'll handle manually
            del data['reference_links']

        serializer = ProjectSerializer(data=data)

        if serializer.is_valid():
            project = serializer.save()
            
            # Manually create files and links
            files_created = 0
            for file in uploaded_files:
                try:
                    UploadProjectFiles.objects.create(project=project, file=file)
                    files_created += 1

                except Exception as e:
                    print(f"Error creating file {file.name}: {e}")
            
            links_created = 0
            for link in reference_links:
                try:
                    ReferenceLinks.objects.create(project=project, url=link)
                    links_created += 1
                except Exception as e:
                    print(f"Error creating link {link}: {e}")
            
            
            return Response({
                'message': 'Project created successfully',
                'project_id': project.id, # type: ignore
                'files_created': files_created,
                'links_created': links_created,
            }, status=status.HTTP_201_CREATED)
        else:
            print(f"=== DEBUG: Serializer errors ===")
            print(serializer.errors)
            return Response({
                'message': 'Project creation failed',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)