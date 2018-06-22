import xadmin
from .models import Category,Info,Role,HonorCategory,Honor,Show,PiaoFang

class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


xadmin.site.register(Category,CategoryAdmin)


class InfoAdmin(object):
    list_display = ['name','daoyan','category']
    search_fields = ['name','daoyan','category']
    list_filter = ['name','daoyan','category']

xadmin.site.register(Info,InfoAdmin)


class RoleAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

xadmin.site.register(Role,RoleAdmin)


class HonorCategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

xadmin.site.register(HonorCategory,HonorCategoryAdmin)


class HonorAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

xadmin.site.register(Honor,HonorAdmin)

class ShowAdmin(object):
    list_display = ['time']
    search_fields = ['time']
    list_filter = ['time']

xadmin.site.register(Show,ShowAdmin)

class PiaoFangAdmin(object):
    list_display = ['num']
    search_fields = ['num']
    list_filter = ['num']

xadmin.site.register(PiaoFang,PiaoFangAdmin)


