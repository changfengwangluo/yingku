import xadmin
from xadmin import views
from .models import LunBo

class LunBoAdmin(object):
    list_display=['title']
    search_fields=['title']
    list_filter=['title']

xadmin.site.register(LunBo,LunBoAdmin)


class GlobalSettings(object):
    site_title="长风影库后台管理系统"
    site_footer="长风网络"
    menu_style="accordion"
xadmin.site.register(views.CommAdminView,GlobalSettings)

# class BaseSetting(object):
#     enable_themes=True
#     use_bootswatch=True
#
# xadmin.site.register(views.BaseAdminView,BaseSetting)