import xadmin
from .models import Category,Info,Role,HonorCategory,Honor,PiaoFang,ShangYing,GuoJia,YiMing,YanZhiYuan,ZhaiYao,PaiSheDi,ChuanBang

class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


xadmin.site.register(Category,CategoryAdmin)


class InfoAdmin(object):
    list_display = ['name','category']
    search_fields = ['name','category']
    list_filter = ['name','category']

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

class YanZhiYuanAdmin(object):
    list_display = ['name','ename','category','film','beizhu','image']
    search_fields = ['name','ename','category','film','beizhu','image']
    list_filter = ['name','ename','category','film','beizhu','image']

xadmin.site.register(YanZhiYuan,YanZhiYuanAdmin)

class ZhaiYaoAdmin(object):
    list_display = ['film','content']
    search_fields = ['film','content']
    list_filter = ['film','content']

xadmin.site.register(ZhaiYao,ZhaiYaoAdmin)


class PaiSheDiAdmin(object):
    list_display = ['film','address','changjing']
    search_fields = ['film','address','changjing']
    list_filter = ['film','address','changjing']

xadmin.site.register(PaiSheDi,PaiSheDiAdmin)

class ChuanBangAdmin(object):
    list_display = ['film','category','xiangqing']
    search_fields = ['film','category','xiangqing']
    list_filter = ['film','category','xiangqing']

xadmin.site.register(ChuanBang,ChuanBangAdmin)

