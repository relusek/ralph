# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from bob.menu import MenuItem

from ralph.discovery.models_network import Network, IPAddress
from ralph.ui.views.common import (Info, Prices, Addresses, Costs,
    Purchase, Components, History, Discover)
from ralph.discovery.models import ReadOnlyDevice
from ralph.account.models import Perm
from ralph.ui.views.common import BaseMixin,DeviceDetailView, CMDB
from ralph.ui.views.devices import BaseDeviceList
from ralph.util import presentation


class SidebarNetworks(object):
    def __init__(self, *args, **kwargs):
        super(SidebarNetworks, self).__init__(*args, **kwargs)
        self.network = None

    def set_network(self):
        network_symbol = self.kwargs.get('network')
        if network_symbol:
            self.network = get_object_or_404(Network, name__iexact=network_symbol)
        else:
            self.network = None

    def get_context_data(self, **kwargs):
        ret = super(SidebarNetworks, self).get_context_data(**kwargs)
        self.set_network()
        self.networks = list(Network.objects.all().order_by('min_ip', 'max_ip'))
        stack = []
        for network in self.networks:
            network.parent = None
            while stack:
                if network in stack[-1]:
                    network.parent = stack[-1]
                    break
                else:
                    stack.pop()
            if network.parent:
                network.depth = network.parent.depth + 1
            else:
                network.depth = 0
            network.indent = ' ' * network.depth
            stack.append(network)
        icon = presentation.get_network_icon
        sidebar_items = [('fugue-prohibition', "Unknown", '')]
        for n in self.networks:
            sidebar_items.append(
                MenuItem(n.name, fugue_icon=icon(n), view_name='networks',
                         indent = n.indent,
                         view_args=[n.name, ret['details'], '']))
        ret.update({
            'sidebar_items': sidebar_items,
            'sidebar_selected': self.network.name if self.network else self.network,
            'section': 'networks',
            'subsection': self.network.name if self.network else self.network,
        })
        return ret


class Networks(SidebarNetworks, BaseMixin):
    pass


class NetworksDeviceList(SidebarNetworks, BaseMixin, BaseDeviceList):
    section = 'networks'

    def user_allowed(self):
        has_perm = self.request.user.get_profile().has_perm
        return has_perm(Perm.read_network_structure)

    def get_queryset(self):
        self.set_network()
        if self.network is None:
            return ReadOnlyDevice.objects.none()
        if self.network == '':
            return ReadOnlyDevice.objects.filter(
                ipaddress=None
            ).order_by(
                'dc', 'rack', 'model__type', 'position'
            )
        addresses = IPAddress.objects.filter(
                number__gte=self.network.min_ip,
                number__lte=self.network.max_ip,
            )
        queryset = ReadOnlyDevice.objects.filter(
                ipaddress__in=addresses
            ).order_by(
                'dc', 'rack', 'model__type', 'position'
            )
        return super(NetworksDeviceList, self).get_queryset(queryset)

    def get_context_data(self, **kwargs):
        ret = super(NetworksDeviceList, self).get_context_data(**kwargs)
        ret.update({
            'subsection': self.network.name if self.network else self.network,
        })
        return ret

class NetworksInfo(Networks, Info):
    pass

class NetworksComponents(Networks, Components):
    pass

class NetworksPrices(Networks, Prices):
    pass

class NetworksAddresses(Networks, Addresses):
    pass

class NetworksCosts(Networks, Costs):
    pass

class NetworksHistory(Networks, History):
    pass

class NetworksPurchase(Networks, Purchase):
    pass

class NetworksDiscover(Networks, Discover):
    pass


class NetworksCMDB(Networks, CMDB,DeviceDetailView ):
    pass


