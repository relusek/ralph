from django.conf.urls.defaults import patterns, include, url
from django.views.generic import RedirectView
from tastypie.api import Api
from ralph.business.api import VentureResource, VentureLightResource,\
    RoleResource
from ralph.discovery.api import IPAddressResource, ModelGroupResource,\
    ModelResource, PhysicalServerResource, RackServerResource,\
    VirtualServerResource, BladeServerResource, DevResource

from django.conf import settings
from django.contrib import admin
from ajax_select import urls as ajax_select_urls
admin.autodiscover()

v09_api = Api(api_name='v0.9')
for r in (VentureResource, VentureLightResource, RoleResource,
    IPAddressResource, ModelGroupResource, ModelResource,
    PhysicalServerResource, RackServerResource, BladeServerResource,
    VirtualServerResource, DevResource):
    v09_api.register(r())

class VhostRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        host = self.request.META.get('HTTP_X_FORWARDED_HOST',
            self.request.META['HTTP_HOST'])
        if host == settings.DASHBOARD_SITE_DOMAIN:
            self.url = '/ventures/'
        else:
            self.url = '/ui/search/info/'
        return super(VhostRedirectView, self).get_redirect_url(**kwargs)


urlpatterns = patterns('',
    url(r'^$', VhostRedirectView.as_view(permanent=False)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    url(r'^humans\.txt$', RedirectView.as_view(url='/static/humans.txt')),
    url(r'^robots\.txt$', RedirectView.as_view(url='/static/robots.txt')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
        settings.STATIC_ROOT, 'show_indexes': True}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout'),# {'template_name': 'admin/logout.html'}),
    url(r'^ventures/(?P<venture_id>.+)/$', 'ralph.business.views.show_ventures',
        name='business-show-venture'),
    url(r'^ventures/$', 'ralph.business.views.show_ventures',
        name='business-show-ventures'),
    url(r'^browse/$', RedirectView.as_view(url='/ui/racks/')),
    url(r'^business/$', RedirectView.as_view(url='/ui/ventures/-/venture/')),
    url(r'^business/ventures/$', RedirectView.as_view(url='/ventures/')),
    url(r'^findme/$', RedirectView.as_view(url='/ui/search/info/')),
    url(r'^catalog/$', RedirectView.as_view(url='/ui/catalog/')),
    url(r'^warnings/$', RedirectView.as_view(url='/ui/catalog/')),
    url(r'^integration/', include('ralph.integration.urls')),
    url(r'^ui/', include('ralph.ui.urls')),
    url(r'^dns/', include('ralph.dnsedit.urls')),
    url(r'^cmdb/', include('ralph.cmdb.urls')),
    url(r'^api/', include(v09_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    # include the lookup urls
    (r'^admin/lookups/', include(ajax_select_urls)),
    (r'^admin/', include(admin.site.urls)),

)




