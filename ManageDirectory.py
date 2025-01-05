
import os
import shutil
import time


def CreateDir():

    if os.path.exists('images'):        
        shutil.rmtree('images')
    if os.path.exists('models'):        
        shutil.rmtree('models')
    if os.path.exists('images'):        
        shutil.rmtree('images')
    if os.path.exists('tests-results.txt'):
        os.remove('tests-results.txt')
    print('Older Files and Directory Removed.....')    
    time.sleep(3)


    
    # creating dirs
    os.makedirs('images/1-training/child')
    os.makedirs('images/1-training/non-child')
    os.makedirs('images/2-test/child')
    os.makedirs('images/2-test/non-child')
    os.makedirs('images/3-validation-test/child')
    os.makedirs('images/3-validation-test/non-child')

    with open('tests-results.txt','a') as file:
        file.write("Test\tSuccess\tSuccess %\tErrors\tErrors %\n")