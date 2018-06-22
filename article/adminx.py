import xadmin
from .models import YingPingInfo,YingXunInfo,KeyWords,HuaXuInfo

class YingPingInfoAdmin(object):
    list_display=['title','user','film','add_time','zan']
    search_fields=['title','user','film','add_time','zan']
    list_filter=['title','user','film','add_time','zan']

xadmin.site.register(YingPingInfo,YingPingInfoAdmin)

class YingXunInfoAdmin(object):
    list_display=['title']
    search_fields=['title']
    list_filter=['title']

xadmin.site.register(YingXunInfo,YingXunInfoAdmin)

class HuaXuInfoAdmin(object):
    list_display=['title']
    search_fields=['title']
    list_filter=['title']

xadmin.site.register(HuaXuInfo,HuaXuInfoAdmin)

class KeyWordsAdmin(object):
    list_display=['words']
    search_fields=['words']
    list_filter=['words']

xadmin.site.register(KeyWords,KeyWordsAdmin)


