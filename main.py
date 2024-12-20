#!/usr/bin/python
from asyncio import sleep
import time
from build_dataset import  *
import os
import shutil
from errorCalculator import error_calculate
from main1 import myMain

if __name__ == '__main__':

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

    # number of times to train cnn
    n = 100
    count = 1
    sum_success,sum_error = 0,0
    success_array = []
    error_array = []
    dp_suc,dp_err = 0,0
    
    # creating dirs
    os.makedirs('images/1-training/child')
    os.makedirs('images/1-training/non-child')
    os.makedirs('images/2-test/child')
    os.makedirs('images/2-test/non-child')
    os.makedirs('images/3-validation-test/child')
    os.makedirs('images/3-validation-test/non-child')

    with open('tests-results.txt','a') as file:
        file.write("Test\tSuccess\tSuccess %\tErrors\tErrors %\n")

    while count <= n:
        myMain(count)
        total = error_calculate(count)
        success_array.append(total[0])
        error_array.append(total[1])
        count += 1

    for k in range(n):
        sum_success += success_array[k]
        sum_error += error_array[k]

    average_success = sum_success / n
    average_error = sum_error / n

    for k in range(n):
        dp_suc += (success_array[k] - average_success)**2
        dp_err += (error_array[k] - average_error)**2

    dp1 = (dp_suc / n)**(0.5)
    dp2 = (dp_err / n)**(0.5)

    with open('tests-results.txt','a') as file:
        file.write("\nAverage suc:\t{}\nAverage err:\t{}\nStd deviation suc:\t{:.2f}\nStd deviation err:\t{:.2f}\n"
        .format(average_success,average_error,dp1,dp2))


