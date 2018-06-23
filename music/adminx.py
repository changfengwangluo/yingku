import xadmin
from .models import Info

class InfoAdmin(object):
    list_display=['name']
    search_fields=['name']
    list_filter=['name']

xadmin.site.register(Info,InfoAdmin)