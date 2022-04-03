## Import the zipfile library to open zipfiles in python

import zipfile


## log each attempt at open sequentially

count = 1

## Open the dictionary text file that contains all possible 6 digit combinations and read as bytes, for each entry thats in the dictionary file step through the passwords listed

with open('dict.txt','rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            
## open the zip file needs to be cracked 

            with zipfile.ZipFile('secret.zip','r') as zf:
                zf.extractall(pwd=password)

## Decode the password to print back to text using UTF8

                print('''PASSWORD FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!\nPassword cracked and is %s''' 
                    % (password.decode('utf8')))
                break

## To provide the continuation try of any failed password attempt
        
        except:
            number = count
            print('Attempt number %s Incorrect! - password attempted was %s' % (number,password.decode('utf8')))
            count += 1
            pass

