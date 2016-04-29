from django.contrib import admin

from born_user.models import user, MusicFile

class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdate', 'updatedate', 'account', 'password', \
                    'name', 'nickname', 'birthday', 'email', 'sex')

admin.site.register(user, userAdmin)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'musicfile',)

admin.site.register(MusicFile, MusicAdmin)
