import xadmin
from .models import Category,Info,Role,HonorCategory,Honor,PiaoFang,ShangYing,GuoJia,YiMing

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

class PiaoFangAdmin(object):
    list_display = ['num']
    search_fields = ['num']
    list_filter = ['num']

xadmin.site.register(PiaoFang,PiaoFangAdmin)

class ShangYingAdmin(object):
    list_display = ['film','guojia','chengshi','shijian']
    search_fields = ['film','guojia','chengshi','shijian']
    list_filter = ['film','guojia','chengshi','shijian']

xadmin.site.register(ShangYing,ShangYingAdmin)


class GuoJiaAdmin(object):
    list_display = ['film','name']
    search_fields = ['film','name']
    list_filter = ['film','name']

xadmin.site.register(GuoJia,GuoJiaAdmin)

class YiMingAdmin(object):
    list_display = ['film','guojia','name']
    search_fields = ['film','guojia','name']
    list_filter = ['film','guojia','name']

xadmin.site.register(YiMing,YiMingAdmin)

