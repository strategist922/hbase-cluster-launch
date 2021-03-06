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

import json
from hbase_cluster_launcher.api.base import VMLaunch

#socket.gethostbyname()
class QemuKVMLaunch(VMLaunch):

    def description(self):
        return "Launch a local QEMU KVM Cluster"

    def parse(self, args):
        descriptor = json.load(args.descriptor)
        args.descriptor.close()
        args.descriptor = descriptor


    def launch_vm(self, config):
        pass



def register(vms):
    vms["qemu_kvm"] = QemuKVMLaunch

