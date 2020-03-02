import yaml
import globals.constants as glconstants
from .db import pgconn


def loadyml():
    with open("./config/config.yml", 'r') as stream:
        try:
            configs = yaml.safe_load(stream)
            print("Configuration loaded for mode:",glconstants.GLMODE)
        except yaml.YAMLError as exc:
            print(exc)
    glconstants.GLCONFIG = configs

def connections():
    loadyml()
    pgconn()