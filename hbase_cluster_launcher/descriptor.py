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
from argparse import ArgumentParser

nodes = "nodes"
image = "image"
flavor = "flavor"
meta = "meta"
roles = "roles"
clusterid = "clusterid"
_environment = "environment"
_puppet_master_server = "puppet_master_server"
userdata = "userdata"
files = "files"

def generate_slave_name(slave_number, cluster_id):
    return "%s-slave-%s"%(cluster_id, slave_number)

def generate_master_name(master_number, cluster_id):
    return "%s-master-%s"%(cluster_id, master_number)

def generate_slave_userdata(slave_number, args):
    pass

def generate_master_userdata(master_number, args):
    pass


def create_slave_node(slave_count, descriptor, args):
    descriptor[args.cluster_id][nodes] = {}
    for slave_number in range(slave_count):
        descriptor[args.cluster_id][nodes][generate_slave_name(slave_number, args.cluster_id)] = {
            image: args.image_id,
            flavor: args.node_flavor,
            userdata: generate_slave_userdata(slave_number, args),
            files:None,
            meta:{
                roles:"hadoop-slave",
                clusterid: args.cluster_id,
                _environment:args.environment,
                _puppet_master_server: args.puppet_master
            }
        }



def create_master_nodes(master_count, descriptor, args):
    for master_number in range(master_count):
        descriptor[args.cluster_id][nodes][generate_master_name(master_number, args.cluster_id)] = {
            image: args.image_id,
            flavor: args.node_flavor,
            userdata: generate_master_userdata(master_number, args),
            files: None,
            meta:{
                roles:"hadoop-master",
                clusterid: args.cluster_id,
                _environment:args.environment,
                _puppet_master_server: args.puppet_master
            }
        }

def calculate_slave_node_count(args):
    return args.node_count - 1


def calculate_master_node_count(args):
    return 1


def generate_descriptor(args):
    descriptor = {
        args.cluster_id:{

        }
    }
    slave_count = calculate_slave_node_count(args)
    master_count = calculate_master_node_count(args)
    create_slave_node(slave_count, descriptor, args)
    create_master_nodes(master_count, descriptor, args)
    return descriptor

def main():
    argParse = ArgumentParser(description="HBase cluster descriptor generator.")
    argParse.add_argument(metavar="<cluster_id>", dest="cluster_id", action="store", help="The cluster id to use for this cluster")
    argParse.add_argument(metavar="<node-count>", dest="node_count", action="store", type=int, help="The number of nodes to create")
    argParse.add_argument(metavar="<node-flavor>", dest="node_flavor", action="store", help="The VM flavor to use")
    argParse.add_argument(metavar="<image-id>", dest="image_id", action="store", help="The id of the VM image to use")
    argParse.add_argument(metavar="<puppet-master>", dest="puppet_master", action="store", help="The location of the puppet master server.")
    argParse.add_argument("--environment",metavar="<environment>", dest="environment", action="store", default="prod", help="The environment, default is 'prod'.")
    argParse.add_argument("--userdata",metavar="<userdata>", dest="userdata_location", action="store", help="The location of the userdata to use.")
    argParse.add_argument("--output",metavar="<output_location>", dest="output_location", action="store", help="The filename that the descriptor will be written to, defaults to ${cluster_id}.json.")
    argParse.add_argument("--config-dir",metavar="<config_dir>", dest="config_dir", default="/etc/hbase_cl_launch", action="store", help="The location of the config directory, default: /etc/hbase_cl_launch")
    args = argParse.parse_args()
    if args.output_location is None:
        args.output_location = "%s.json"%args.cluster_id
    with open(args.output_location, "wb") as data_out:
        json.dump(generate_descriptor(args), data_out, indent=4 )


if __name__ == "__main__":
    main()
