#hbase_cluster-launcher is a tool for launching HBase clusters on
#Openstack clouds
#
#Copyright (C) 2013  NigelB
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

__vms = {}
__initialized = False

def register_vm_api(name, _class):
    __vms[name] = _class

def get_vm(name):
    return __vms[name]

def get_registered_vms():
    return __vms.keys()

def list_apis():
    if len(__vms) > 0:

        print "Available VM APIs:"
        for i in __vms:
            print "", i
    else:
        print "There no available VM APIs."

if not __initialized:
    import os.path, re
    for vm_mod in os.listdir(os.path.dirname(__file__)):
        m = re.match("(.*).py$", vm_mod)
        if m:
            pn = m.group(1)
            if pn not in ["__init__"]:
                try:
                    _mod = __import__(pn, globals(), locals(), fromlist=[__name__])
                    _mod.register(__vms)
                except Exception, e:
                    pass
    __initialized = True
