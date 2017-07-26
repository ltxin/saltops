from http.client import HTTPResponse
import better_exceptions
from django.http import HttpResponse
from django.template.defaultfilters import register
from django.contrib.auth.decorators import login_required
from django.db.models import Model
from django.forms import ModelForm
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import RequestContext
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_http_methods

from cmdb.models import Cabinet, HostIP
from cmdb.models import Host
from cmdb.models import IDC
from cmdb.models import ISP
from cmdb.models import Rack
from cmdb.models.Host import MINION_STATUS
from common.pageutil import preparePage
from django.forms import *

from saltjob.tasks import scanServerJob


@require_http_methods(["GET"])
@gzip_page
@login_required
def scan_server(kwargs):
    scanServerJob()
    return HttpResponse("")