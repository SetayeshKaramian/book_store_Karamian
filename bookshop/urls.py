from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('', include('book.urls')),
                  path('', include('cart.urls')),
                  path('', include('users.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

"""Admin site customization"""
admin.site.site_header = "ادمین کتاب فروشی ستا"
admin.site.site_title = "سایت ادمین کتاب فروشی ستا"
admin.site.index_title = "ادمین کتاب فروشی"
