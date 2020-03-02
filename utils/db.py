'''This file is used to create connections and execute PG quries'''

import psycopg2
import globalvars.constants as glconstants

def pgconn():
    if glconstants.GLPGCONN:
        print("Postgres already made")
        return 
    try:
        params = glconstants.GLCONFIG[glconstants.GLMODE]["db"]["postgres"]
        glconstants.GLPGCONN = psycopg2.connect(**params)
        print("Postgres connection made")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def executePGQuery(query):
    crsr = glconstants.GLPGCONN.cursor(cursor_factory=psycopg2.extras.DictCursor)
    crsr.execute(query)
    result=crsr.fetchall()
    data={}
    for r in range(len(result)):
        data[r]=dict(result[r])
    return data
