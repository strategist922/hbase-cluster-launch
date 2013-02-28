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

from argparse import ArgumentParser
from hbase_cluster_launcher.api import get_vm, get_registered_vms

def main():
    argParse = ArgumentParser(description="HBase cluster launcher.")
    subparsers = argParse.add_subparsers(description="Available VM APIs")
    for vms in get_registered_vms():
        p = get_vm(vms)()
        parser_a = subparsers.add_parser(vms, help=p.description())
        p.initialize_parser(parser_a)

    args = argParse.parse_args()
    launcher = args.vm
    launcher.parse(args)
    machine_data = launcher.launch_vm(args)



if __name__ == "__main__":
    main()