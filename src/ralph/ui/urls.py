# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

from ralph.ui.views import typeahead_roles, unlock_field, logout, discover
from ralph.ui.views.common import Home, BulkEdit
from ralph.ui.views.ventures import (VenturesRoles, VenturesVenture,
        VenturesInfo, VenturesComponents, VenturesAddresses,
        VenturesPrices, VenturesCosts, VenturesHistory, VenturesPurchase,
        VenturesDiscover)
from ralph.ui.views.racks import (
        RacksInfo, RacksComponents, RacksAddresses, RacksPrices,
        RacksCosts, RacksHistory, RacksPurchase, RacksDiscover, RacksCMDB,
        )
from ralph.ui.views.search import (SearchDeviceList,
        SearchInfo, SearchComponents, SearchAddresses, SearchPrices,
        SearchCosts, SearchHistory, SearchPurchase, SearchDiscover)
from ralph.ui.views.networks import (
        NetworksDeviceList, NetworksInfo, NetworksComponents, NetworksAddresses,
        NetworksPrices,NetworksCMDB,
        NetworksCosts, NetworksHistory, NetworksPurchase, NetworksDiscover)
from ralph.ui.views.catalog import (Catalog, CatalogDevice, CatalogComponent)
from ralph.ui.views.ventures import VenturesDeviceList,VenturesCMDB
from ralph.ui.views.racks import RacksDeviceList


urlpatterns = patterns('',
    url(r'^logout/$', login_required(logout), {}, 'logout'),
    url(r'^discover/$', login_required(discover), {}, 'discover'),
    url(r'^typeahead/roles/$', login_required(typeahead_roles), {}, 'typeahead-roles'),
    url(r'^unlock-field/$', login_required(unlock_field), {}, 'unlock-field'),
    url(r'^$', login_required(Home.as_view()), {}, 'home'),

    url(r'^(?P<section>\w+)/(?P<details>bulkedit)/$',
            login_required(BulkEdit.as_view()), {}, 'bulkedit'),
    url(r'^(?P<section>\w+)/.*/(?P<details>bulkedit)/$',
            login_required(BulkEdit.as_view()), {}, 'bulkedit'),

    url(r'^search/$',
            login_required(SearchDeviceList.as_view()), {}, 'search'),
    url(r'^search/(?P<details>\w*)/(?P<device>)$',
            login_required(SearchDeviceList.as_view()), {}, 'search'),
    url(r'^search/(?P<details>info)/(?P<device>\d+)$',
            login_required(SearchInfo.as_view()), {}, 'search'),
    url(r'^search/(?P<details>components)/(?P<device>\d+)$',
            login_required(SearchComponents.as_view()), {}, 'search'),
    url(r'^search/(?P<details>addresses)/(?P<device>\d+)$',
            login_required(SearchAddresses.as_view()), {}, 'search'),
    url(r'^search/(?P<details>prices)/(?P<device>\d+)$',
            login_required(SearchPrices.as_view()), {}, 'search'),
    url(r'^search/(?P<details>costs)/(?P<device>\d+)$',
            login_required(SearchCosts.as_view()), {}, 'search'),
    url(r'^search/(?P<details>history)/(?P<device>\d+)$',
            login_required(SearchHistory.as_view()), {}, 'search'),
    url(r'^search/(?P<details>purchase)/(?P<device>\d+)$',
            login_required(SearchPurchase.as_view()), {}, 'search'),
    url(r'^search/(?P<details>discover)/(?P<device>\d+)$',
            login_required(SearchDiscover.as_view()), {}, 'search'),

    url(r'^ventures/$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>info|components|addresses|prices|costs|history|purchase|discover|cmdb)/(?P<device>)$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>)(?P<details>info|components|addresses|prices|costs|history|purchase|discover|cmdb)/(?P<device>)$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>info)/(?P<device>\d+)$',
        login_required(VenturesInfo.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(VenturesComponents.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(VenturesAddresses.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>prices)/(?P<device>\d+)$',
        login_required(VenturesPrices.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>costs)/(?P<device>\d+)$',
        login_required(VenturesCosts.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(VenturesHistory.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>purchase)/(?P<device>\d+)$',
        login_required(VenturesPurchase.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>discover)/(?P<device>\d+)$',
        login_required(VenturesDiscover.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>roles)/(?P<role>[-\w]*)$',
        login_required(VenturesRoles.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>venture)/(?P<device>)$',
        login_required(VenturesVenture.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>cmdb)/(?P<device>\w+)$',
        login_required(VenturesCMDB.as_view()), {}, 'ventures'),

    url(r'^racks/$',
        login_required(RacksDeviceList.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>\w+)/(?P<device>)$',
        login_required(RacksDeviceList.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>info)/(?P<device>\d+)$',
        login_required(RacksInfo.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(RacksComponents.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(RacksAddresses.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>prices)/(?P<device>\d+)$',
        login_required(RacksPrices.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>costs)/(?P<device>\d+)$',
        login_required(RacksCosts.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(RacksHistory.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>purchase)/(?P<device>\d+)$',
        login_required(RacksPurchase.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>discover)/(?P<device>\d+)$',
        login_required(RacksDiscover.as_view()), {}, 'racks'),
    url(r'^(?P<section>racks)/(?P<rack>[-\w]*)/(?P<details>bulkedit)/$',
        login_required(BulkEdit.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>cmdb)/(?P<device>\d+)$',
        login_required(RacksCMDB.as_view()), {}, 'racks'),
    url(r'^networks/$',
        login_required(NetworksDeviceList.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>\w+)/(?P<device>)$',
        login_required(NetworksDeviceList.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>info)/(?P<device>\d+)$',
        login_required(NetworksInfo.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(NetworksComponents.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(NetworksAddresses.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>prices)/(?P<device>\d+)$',
        login_required(NetworksPrices.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>costs)/(?P<device>\d+)$',
        login_required(NetworksCosts.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(NetworksHistory.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>purchase)/(?P<device>\d+)$',
        login_required(NetworksPurchase.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>discover)/(?P<device>\d+)$',
        login_required(NetworksDiscover.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>cmdb)/(?P<device>\d+)$',
        login_required(NetworksCMDB.as_view()), {}, 'networks'),


    url(r'^catalog/$', login_required(Catalog.as_view()), {}, 'catalog'),
    url(r'^catalog/(?P<kind>device)/(?P<type>\d*)/$', login_required(CatalogDevice.as_view()), {}, 'catalog'),
    url(r'^catalog/(?P<kind>component)/(?P<type>\d*)/$', login_required(CatalogComponent.as_view()), {}, 'catalog'),
    url(r'^catalog/(?P<kind>device)/(?P<type>\d*)/(?P<group>\d*)/$', login_required(CatalogDevice.as_view()), {}, 'catalog'),
    url(r'^catalog/(?P<kind>component)/(?P<type>\d*)/(?P<group>\d*)/$', login_required(CatalogComponent.as_view()), {}, 'catalog'),
)
