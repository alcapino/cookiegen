from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from fortune.serializers import FortuneSerializer
from core.models import FortuneModel

class CsrfExemptSessionAuthentication(SessionAuthentication):
  def enforce_csrf(self,request):
    return


class FortuneViewSet(ModelViewSet):
  allowed_methods = ("GET", "POST", "HEAD", "OPTIONS")
  queryset = FortuneModel.objects.all()
  pagination_class = None
  serializer_class = FortuneSerializer

  def list(self, request, *args, **kwargs):
    return super(FortuneViewSet, self).list(request, *args, **kwargs)
