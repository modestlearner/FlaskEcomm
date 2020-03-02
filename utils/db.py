import psycopg2
import globals.constants as glconstants

def pgconn():
    if glconstants.GLPGCONN is not None:
        print("Postgres already made")
        return 
    try:
        params = glconstants.GLCONFIG[glconstants.GLMODE]["db"]["postgres"]
        glconstants.GLPGCONN = psycopg2.connect(**params)
        print("Postgres connection made")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def executeQuery():
    pass
