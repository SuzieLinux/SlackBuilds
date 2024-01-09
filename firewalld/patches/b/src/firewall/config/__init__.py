# SPDX-License-Identifier: GPL-2.0-or-later
#
# Copyright (C) 2007-2016 Red Hat, Inc.
#
# Authors:
# Thomas Woerner <twoerner@redhat.com>

# translation
import locale

try:
    locale.setlocale(locale.LC_ALL, "")
except locale.Error:
    import os

    os.environ["LC_ALL"] = "C"
    locale.setlocale(locale.LC_ALL, "")

DOMAIN = "firewalld"
import gettext

gettext.install(domain=DOMAIN)

from . import dbus  # noqa: F401

# configuration
DAEMON_NAME = "firewalld"
CONFIG_NAME = "firewall-config"
APPLET_NAME = "firewall-applet"
DATADIR = "/usr/share/" + DAEMON_NAME
CONFIG_GLADE_NAME = CONFIG_NAME + ".glade"
COPYRIGHT = "(C) 2010-2017 Red Hat, Inc."
VERSION = "2.1.0"
AUTHORS = [
    "Thomas Woerner <twoerner@redhat.com>",
    "Jiri Popelka <jpopelka@redhat.com>",
    "Eric Garver <e@erig.me>",
]
LICENSE = gettext.gettext(
    "This program is free software; you can redistribute it and/or modify "
    "it under the terms of the GNU General Public License as published by "
    "the Free Software Foundation; either version 2 of the License, or "
    "(at your option) any later version.\n"
    "\n"
    "This program is distributed in the hope that it will be useful, "
    "but WITHOUT ANY WARRANTY; without even the implied warranty of "
    "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the "
    "GNU General Public License for more details.\n"
    "\n"
    "You should have received a copy of the GNU General Public License "
    "along with this program.  If not, see <http://www.gnu.org/licenses/>."
)
WEBSITE = "http://www.firewalld.org"


def set_system_config_paths(path):
    global ETC_FIREWALLD, FIREWALLD_CONF, ETC_FIREWALLD_ZONES, ETC_FIREWALLD_SERVICES, ETC_FIREWALLD_ICMPTYPES, ETC_FIREWALLD_IPSETS, ETC_FIREWALLD_HELPERS, FIREWALLD_DIRECT, LOCKDOWN_WHITELIST, ETC_FIREWALLD_POLICIES
    ETC_FIREWALLD = path
    FIREWALLD_CONF = path + "/firewalld.conf"
    ETC_FIREWALLD_ZONES = path + "/zones"
    ETC_FIREWALLD_SERVICES = path + "/services"
    ETC_FIREWALLD_ICMPTYPES = path + "/icmptypes"
    ETC_FIREWALLD_IPSETS = path + "/ipsets"
    ETC_FIREWALLD_HELPERS = path + "/helpers"
    ETC_FIREWALLD_POLICIES = path + "/policies"
    FIREWALLD_DIRECT = path + "/direct.xml"
    LOCKDOWN_WHITELIST = path + "/lockdown-whitelist.xml"


set_system_config_paths("/etc/firewalld")


def set_default_config_paths(path):
    global USR_LIB_FIREWALLD, FIREWALLD_ZONES, FIREWALLD_SERVICES, FIREWALLD_ICMPTYPES, FIREWALLD_IPSETS, FIREWALLD_HELPERS, FIREWALLD_POLICIES
    USR_LIB_FIREWALLD = path
    FIREWALLD_ZONES = path + "/zones"
    FIREWALLD_SERVICES = path + "/services"
    FIREWALLD_ICMPTYPES = path + "/icmptypes"
    FIREWALLD_IPSETS = path + "/ipsets"
    FIREWALLD_HELPERS = path + "/helpers"
    FIREWALLD_POLICIES = path + "/policies"


set_default_config_paths("/usr/lib/firewalld")

FIREWALLD_LOGFILE = "/var/log/firewalld"

FIREWALLD_LOGTARGET = "mixed"

FIREWALLD_PIDFILE = "/var/run/firewalld.pid"

FIREWALLD_TEMPDIR = "/run/firewalld"

SYSCONFIGDIR = "/etc/sysconfig"
IFCFGDIR = "/etc/sysconfig/network-scripts"

SYSCTL_CONFIG = "/etc/sysctl.conf"

# commands used by backends
COMMANDS = {
    "ipv4": "/usr/sbin/iptables",
    "ipv4-restore": "/usr/sbin/iptables-restore",
    "ipv6": "/usr/sbin/ip6tables",
    "ipv6-restore": "/usr/sbin/ip6tables-restore",
    "eb": "/usr/sbin/ebtables",
    "eb-restore": "/usr/sbin/ebtables-restore",
    "ipset": "/usr/sbin/ipset",
    "modprobe": "/usr/sbin/modprobe",
    "rmmod": "/usr/sbin/rmmod",
}

LOG_DENIED_VALUES = ["all", "unicast", "broadcast", "multicast", "off"]
AUTOMATIC_HELPERS_VALUES = ["yes", "no", "system"]
FIREWALL_BACKEND_VALUES = ["nftables", "iptables"]

# fallbacks: will be overloaded by firewalld.conf
FALLBACK_ZONE = "public"
FALLBACK_MINIMAL_MARK = 100
FALLBACK_CLEANUP_ON_EXIT = True
FALLBACK_CLEANUP_MODULES_ON_EXIT = False
FALLBACK_LOCKDOWN = False
FALLBACK_IPV6_RPFILTER = True
FALLBACK_INDIVIDUAL_CALLS = False
FALLBACK_LOG_DENIED = "off"
FALLBACK_AUTOMATIC_HELPERS = "no"
FALLBACK_FIREWALL_BACKEND = "nftables"
FALLBACK_FLUSH_ALL_ON_RELOAD = True
FALLBACK_RELOAD_POLICY = "INPUT:DROP,FORWARD:DROP,OUTPUT:DROP"
FALLBACK_RFC3964_IPV4 = True
FALLBACK_ALLOW_ZONE_DRIFTING = False
FALLBACK_NFTABLES_FLOWTABLE = "off"
FALLBACK_NFTABLES_COUNTERS = False
