from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from cmdb.models.HostGroup import HostGroup
from cmdb.models.Cabinet import Cabinet
from cmdb.models.IDC import IDC
from cmdb.models.Rack import Rack
from common.models import BaseModel
from cmdb.models.Host import Host
class Nginx(BaseModel):
    host_group = models.ForeignKey(HostGroup, verbose_name='主机组', blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True, verbose_name="域名")
    real_server = models.CharField(max_length=255, blank=True, null=True, verbose_name="后端机器")
    mem_total = models.CharField(max_length=255, blank=True, null=True, verbose_name="内存总数")
    num_cpus = models.IntegerField(blank=True, null=True, verbose_name="CPU数量")
    idc = models.ForeignKey(IDC, verbose_name='IDC', blank=True, null=True)


    def __str__(self):
        return self.host

    class Meta:
        verbose_name = "nginx"
        verbose_name_plural = verbose_name
