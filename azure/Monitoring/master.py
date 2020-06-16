#!/usr/bin/python
import argparse
import pyodbc
from azure.servicebus import *
from azure.storage.blob.baseblobservice import *

parser = argparse.ArgumentParser(description='Azure Service Monitoring Tool')
parser.add_argument("-r", "--reg", default="", help="Region Name (US or UK)")
parser.add_argument("-q", "--queue", default="", help="Queue Name")
parser.add_argument("-t", "--type", default="", help="Return Type (count, currentsize, maxsize)")
parser.add_argument("-s", "--service", default="", help="Azure Service to be Monitored (database, storage, servicebus, notificaitonhub)")
parser.add_argument("-f", "--filename", default="", help="Azure Storage Filename")

def bobc(reg,fname):
    # currently hardcoded values, add in as a parsable parameter.
    # make code cleaner, more reusable
    # no need for region check
    if reg == "":
        print "Please specify a region with --reg US or UK"
        exit
    else:
        if reg == "US":
            # bb = BaseBlobService(account_name='accountname', account_key="account_key_",
            #                     is_emulated=False, protocol='https', endpoint_suffix='core.windows.net')
            bb = BaseBlobService(account_name='accountname', account_key="account_key_",
                                 is_emulated=False, protocol='https', endpoint_suffix='core.windows.net')
        elif reg == "UK":
            # bb = BaseBlobService(account_name='accountname', account_key="account_key_",
            #                     is_emulated=False, protocol='https', endpoint_suffix='core.windows.net')
            bb = BaseBlobService(account_name='accountname', account_key="account_key_",
                                 is_emulated=False, protocol='https', endpoint_suffix='core.windows.net')

        if bb.exists(container_name='files', blob_name=fname) is True:
            # True
            print "1"
        else:
            # False
            print "0"

def db(reg):
    # currently hardcoded values, add in as a parsable parameter.
    # make code cleaner, more reusable
    # no need for region check
    if reg == "":
        print "Please specify a region with --reg US or UK"
        exit
    else:
        if reg == "US":
            # connect_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=databasename.database.windows.net;PORT=1443;DATABASE=databasename;UID=user_id;PWD=password'
            connect_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=databasename.database.windows.net;PORT=1443;DATABASE=databasename;UID=user_id;PWD=password'

            connection = pyodbc.connect(connect_string)
            try:
                connection
                print "1"
            except:
                print "0"

            connection.close()
        elif reg == "UK":
            # connect_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=databasename.database.windows.net;PORT=1443;DATABASE=databasename;UID=user_id;PWD=password'
            connect_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=databasename.database.windows.net;PORT=1443;DATABASE=databasename;UID=user_id;PWD=password'

            connection = pyodbc.connect(connect_string)
            try:
                connection
                print "1"
            except:
                print "0"

            connection.close()


def sb(reg,qn,rtrnt):
    # currently hardcoded values, add in as a parsable parameter.
    # make code cleaner, more reusable
    # no need for region check
    if reg == "US":
        # bus_service = ServiceBusService(
        #    service_namespace='servicebus-name',
        #    shared_access_key_name='AccessKey-Name',
        #    shared_access_key_value='Secret-AccessKey-Value')
        bus_service = ServiceBusService(
            service_namespace='servicebus-name',
            shared_access_key_name='AccessKey-Name',
            shared_access_key_value='Secret-AccessKey-Value')

        a = bus_service.get_queue(qn)
        if rtrnt.lower() == "maxsize":
            print a.max_size_in_megabytes * 1024 * 1024
        elif rtrnt.lower() == "currentsize":
            print a.size_in_bytes
        elif rtrnt.lower() == "count":
            print a.message_count
    elif reg == "UK":
        # bus_service = ServiceBusService(
        #    service_namespace='servicebus-name',
        #    shared_access_key_name='AccessKey-Name',
        #    shared_access_key_value='Secret-AccessKey-Value')
        bus_service = ServiceBusService(
            service_namespace='servicebus-name',
            shared_access_key_name='AccessKey-Name',
            shared_access_key_value='Secret-AccessKey-Value')

        a = bus_service.get_queue(qn)
        if rtrnt.lower() == "maxsize":
            print a.max_size_in_megabytes * 1024 * 1024
        elif rtrnt.lower() == "currentsize":
            print a.size_in_bytes
        elif rtrnt.lower() == "count":
            print a.message_count
    else:
        print "You must specify a region, without a region the script will not work"

if "__name__" == "__main()__":
    # no need for region, need to work on removing region.
    args = parser.parse_args()
    service = args.service
    region = args.reg
    queuename = args.queue
    returntype = args.type
    filenamepass = args.filename

    # print region
    if service.lower() == "":
        print "please specify a service"
    elif service.lower() == "database":
        # requirements
        # region
        # requirements
        # region
        if region == "" or (region.lower() != "us" and region.lower() != "uk"):
            print service, "Specify a valid region"
            print "Exiting"
            exit()
        else:
            db(region)
    elif service.lower() == "notificationhub":
        # requirements
        # region
        # accountname
        print "notificationhub monitoring not available currently"
    elif service.lower() == "storage":
        # requirements
        # region
        if region == "" or (region.lower() != "us" and region.lower() != "uk"):
            print service, "Specify a valid region"
            print "Exiting"
            exit()
        else:
            if filenamepass == "":
                print "Please specify a valid filename to monitor for"
            else:
                bobc(region,filenamepass)
    elif service.lower() == "servicebus":
        # requirements
        # region
        # queuename
        # returntype
        if region.lower() == "" or (region.lower() != "us" and region.lower() != "uk"):
            print service, "Specify a valid region"
            print "Exiting"
            exit()
        else:
            if queuename == "":
                print "Please specify a valid queue name to be monitored"
                print "Exiting"
                exit()
            elif returntype == "":
                print "Please specify a valid return type"
                print "Exiting"
                exit()
            else:
                sb(region,queuename,returntype)
