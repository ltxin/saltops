from django.db import models
#from smart_selects.db_fields import ChainedForeignKey

#from cmdb.models.Host import Host
from common.models import BaseModel


class ServiceName(BaseModel):
    ip = models.CharField(max_length=255, blank=True, null=True, verbose_name="IP地址")
    host_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="主机DNS名称")
    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "servicename"
        verbose_name_plural = verbose_name
