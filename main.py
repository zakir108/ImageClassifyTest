#!/usr/bin/python

from build_dataset import  *
from cnn_training import  *
from validation_cnn import  *
from errorCalculatorN import *
import os
import shutil

def main(number_validations):
    
    # building test and validation datasets
    path_child_images = 'images/1-training/child/'
    path_non_child_images = 'images/1-training/non-child/'

    for k in range(0,2):
        if k == 0:
            dataset_type = 'validation'
        else:
            dataset_type = 'test'

        training_child_images = os.listdir(path_child_images)
        training_non_child_images = os.listdir(path_non_child_images)

        num_child_images = update_number_images(training_child_images,0.1)
        num_non_child_images = update_number_images(training_non_child_images,0.1)

        child_list = []
        non_child_list = []

        create_list(num_child_images, training_child_images, child_list)
        create_list(num_non_child_images, training_non_child_images, non_child_list)

        try:
            move_to(path_child_images, child_list, 'child', dataset_type)
            move_to(path_non_child_images, non_child_list, 'non-child', dataset_type)
        except Exception as e:                
            print('ERROR-5')
            print(e)

    # training CNN
    images_training = 'images/1-training'
    images_test = 'images/2-test'

    cnn_train(images_training,images_test)

    # cnn validation
    child_dir = 'images/3-validation-test/child/'
    non_child_dir = 'images/3-validation-test/non-child/'

    images_child = os.listdir(child_dir)
    images_non_child = os.listdir(non_child_dir)

    validation(child_dir,images_child,number_validations)
    validation(non_child_dir,images_non_child,number_validations)

    # copy result files
    #os.makedirs('models/' + str(number_validations))
    target_dir = os.path.join('models', str(number_validations))
    os.makedirs(target_dir, exist_ok=True)

    try:
        shutil.move('kids.json', 'models/' + str(number_validations))
        shutil.move('weight_kids.h5', 'models/' + str(number_validations))
    except Exception as e:            
        print('ERROR-5.1')
        print(e)                

    rebuild_dataset()

if __name__ == '__main__':
    
    # number of times to train cnn
    n = 100

    count = 1
    sum_success,sum_error = 0,0
    success_array = []
    error_array = []
    dp_suc,dp_err = 0,0

    # creating dirs

    dir_list = os.listdir("dataset")
    #dir_list = os.listdir('D:\EverythinPYTHON\AIML\child-image-detection\dataset')
    dir_create = ['1-training','2-test','3-validation-test']

    for dc in dir_create:
        if dc == '1-training':
            for dl in dir_list:
                #shutil.copytree("..dataset/" + dl, "images/" + dc + "/" + dl)
                #shutil.copytree("dataset/" + dl, "images/" + dc + "/" + dl)
                shutil.copytree("dataset/" + dl, "images/" + dc + "/" + dl, dirs_exist_ok=True)

        else:
            for dl in dir_list:
                target_dir = os.path.join('images', dc, dl)
                #os.makedirs('images/' + dc + "/" + dl)
                os.makedirs(target_dir, exist_ok=True)

                try:
                    # Attempt to create the directory
                    target_dir = os.path.join('images', dc, dl)
                    #os.makedirs('images/' + dc + "/" + dl)
                    os.makedirs(target_dir, exist_ok=True)                    
                    print(f"Directory '{target_dir}' created successfully or already exists.")
                except OSError as e:
                    # Catch and handle directory creation errors
                    print(f"Error creating directory '{target_dir}': {e}")
                

    with open('tests-results.txt','a') as file:
        file.write("Test\tSuccess\tSuccess %\tErrors\tErrors %\n")

    while count <= n:
        main(count)
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
