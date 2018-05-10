import re
def checkio(data):
    if(data.islower() == False and data.isupper() == False and len(data) >= 10 and data.isdecimal() == False and re.search("[0-9]",data) != None):
        return True
    else:
        return False

print(checkio('A1213pokl'))
print(checkio('bAse730onE4'))
print(checkio('asasasasasasasaas'))
print(checkio('QWERTYqwerty')) 
print(checkio('123456123456')) 
print(checkio('QwErTy911poqqqq'))  
