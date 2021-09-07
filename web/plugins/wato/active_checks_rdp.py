#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# License: GNU General Public License v2
# (c) 2014 Sixt GmbH & Co. Autovermietung KG
#          Matthias Haehnel <matthias.haehnel@sixt.com>
#

group = "activechecks"

register_rule(group,
    "active_checks:rdp",
    Tuple(
        title = _("Check RDP service"),
        help = _("Checks RDP. "),
        elements = [
            Dictionary(
                title = _("Optional parameters"),
                elements = [
                    ( "hostname",
                      TextAscii(
                            title = _("DNS Hostname or IP address"),
                            default_value = "$HOSTADDRESS$",
                            allow_empty = False,
                            help = _("You can specify a hostname or IP address different from IP address "
                                     "of the host as configured in your host properties."))),
                    ( 'port',
                      Integer(
                            title = _("RDP Port"),
                            help = _("Default is 3389."),
                            minvalue = 1,
                            maxvalue = 65535,
                            default_value = 3389)),
                   ( "response_time",
                     Tuple(
                         title = _("Expected response time"),
                         elements = [
                             Float(
                                 title = _("Warning if above"),
                                 unit = "sec",
                                 default_value = 3),
                             Float(
                                 title = _("Critical if above"),
                                 unit = "sec",
                                 default_value = 50),
                         ])
                    ),
                    ]
                )
            ]
        ),
    match = 'all')
