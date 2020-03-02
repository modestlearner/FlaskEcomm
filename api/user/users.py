'''This file will have all the functions related to the user module'''

from run import app
from flask import request
import  utils.functions as funcs
import utils.db as db
import globalvars.constants as glconstants
import psycopg2.extras
import api.user.queries as queries



@app.route('/api/user/register', methods=['GET','POST'])
def registerUser():
    print(queries.EXISTINGUSERQUERY)
    # email = request.form["email"]
    # if not funcs.checkEmail(email):
    #     print("email not valid")