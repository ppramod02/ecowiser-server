from api.models import Brand
from api.serializers import BrandSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Brand(name='ecowiser', description='an org', logo='base64 image')
snippet.save()