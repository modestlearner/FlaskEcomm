'''This is a utility file where all the utility functions will be made'''

import re 

def checkEmail(email):  
  
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if(re.search(regex,email)):  
       return True
          
    else:  
       return False