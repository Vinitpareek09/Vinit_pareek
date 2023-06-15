import sys 
import logging 
import importlib 
from pathlib import Path 
 
 
def load_plug(plug_name): 
    path = Path(f"CVPYTHON/plugins/{plug_name}.py") 
    name = "CVPYTHON.plugins.{}".format(plug_name) 
    spec = importlib.util.spec_from_file_location(name,path) 
    load = importlib.util.module_from_spec(spec) 
    load.logger = logging.getLogger(plug_name) 
    spec.loader.exec_module(load) 
    sys.modules["CVPYTHON.plugins." + plug_name] = load 
    print("rjbot has Imported" + plug_name)