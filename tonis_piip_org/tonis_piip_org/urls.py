from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.views.i18n import JavaScriptCatalog


admin.autodiscover()

urlpatterns = i18n_patterns(
    path("", include("accounts.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("adminpanel/", admin.site.urls),
    path("filer/", include("filer.urls")),
    # CMS urls should be handled last to avoid possible conflicts
    path("cms/", include("cms.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    handler500 = "tonis_piip_org.views.server_error"
    handler404 = "tonis_piip_org.views.page_not_found"

if settings.DEBUG:
    try:
        import debug_toolbar

        urlpatterns += [
            path("^__debug__", include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass
