import uuid
from django.db import models


class FortuneModel(models.Model):
  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  text = models.CharField(max_length=360, null=False, unique=True)

  def __str__(self):
    return str('{text} ({uuid})'.format(uuid=self.uuid, text=self.text))


  class Meta:
    db_table = 'fortunes'
