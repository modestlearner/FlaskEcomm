from flask import Flask

app = Flask(__name__)

import utils.loadconf as loadconfig
import globalvars.constants as glconstants
from api.user.users import *

if __name__ == '__main__':
    loadconfig.connections()
    app.run()

    

  
