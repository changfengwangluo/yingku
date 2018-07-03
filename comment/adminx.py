import xadmin
from .models import FilmComments

class FilmCommentsAdmin(object):
    list_display=['content','film','add_time']
    search_fields=['content','film','add_time']
    list_filter=['content','film','add_time']

xadmin.site.register(FilmComments,FilmCommentsAdmin)