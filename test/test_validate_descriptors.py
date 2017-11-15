
import os
import pytest
import subprocess

def get_json_files():
    json_files = [os.path.join('cbrain_task_descriptors',json_file) for json_file in os.listdir('cbrain_task_descriptors') if json_file.endswith('.json')]
    return json_files

def test_run():
  json_files = get_json_files()
  if json_files:
      for i in json_files:
          output = subprocess.check_output(["bosh","validate",i])
          output= output.decode('ascii').replace("\n","")
          assert output == "Boutiques validation OK"

