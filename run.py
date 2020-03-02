from flask import Flask

app = Flask(__name__)

import utils.loadconf as loadconfig
import globals.constants as glconstants


if __name__ == '__main__':
    loadconfig.connections()
    app.run()

    

  
