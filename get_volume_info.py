#!/usr/bin/python3

import openstack
import psycopg2 as pg2
import traceback

# Initialzie and turn on debug logging
openstack.enable_logging(debug=False)

# Initialize connection
conn = openstack.connect(cloud='gcloud-a-osp')

# List Volume
try:
  volumes = conn.block_stoage.volumes(defails=True, all_project=True)

  for volume in volumes:
    volume_dict = volume.to_dict()

    try:
      volume_id=volume_dict['id].strip()
      volume_name=volume_dict['name].strip()
      volume_size=volume_dict['size].strip()
      volume_status=volume_dict['status].strip()
      volume_metadata=volume_dict['metadata']['ldev'].strip()

      # Print Volume Info
      print(volume_name,volume_id,volume_metadata,sep=',')

    except KeyError:
      continue
      
except Exception as e:
  print(traceback.print_exc())


  

      
