import os
import shutil

source = input("Enter the source: ")
destination = input("Enter the destination: ")

source = source + '/'
destination = destination + '/'

listOfFiles = os.listdir(source) 

for file in listOfFiles :
    shutil.copy((source + file), destination) 