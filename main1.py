
from build_dataset import  *
import os
import shutil

from train_cnn import cnn_train
import validation


def myMain(number_validations):
    
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
