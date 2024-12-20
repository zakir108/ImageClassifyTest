#!/usr/bin/python

import random
import os
import shutil

def update_number_images(image_list,percent):
    total = int(len(image_list) * percent)
    # print('total: {}'.format(total))
    return total

def create_list(num,list_images,final_list):
    k = 0
    while k < num:
        n = random.choice(list_images)
        if n not in final_list:
            final_list.append(n)
            k += 1



def move_to(path,images,x,y):
    for k in images:
        if x == 'child' and y == 'test':
            #shutil.move(path + k, 'images/2-test/child/')

            src_file = os.path.join(path, k)
            dest_dir = 'images/2-test/child/'
            try:
                if os.path.exists(src_file):
                    os.makedirs(dest_dir, exist_ok=True)
                if os.path.exists(os.path.join(dest_dir, k)) == False:
                   shutil.move(src_file, dest_dir)                
                else:
                    print(f"Source file '{src_file}' 6does not exist. Skipping.")
            except Exception as e:                    
                print('HELLO8')
                print(e)



        elif x == 'non-child' and y == 'test':
            #shutil.move(path + k, 'images/2-test/non-child/')
            src_file = os.path.join(path, k)
            dest_dir = 'images/2-test/non-child/'
            
            try:
                if os.path.exists(src_file):
                    os.makedirs(dest_dir, exist_ok=True)
                if os.path.exists(os.path.join(dest_dir, k)) == False:
                    shutil.move(src_file, dest_dir)                
                else:
                    print(f"Source file '{src_file}' 5does not exist. Skipping.")
            except Exception as e:                   
                print('HELLO6')
                print(e)


            
        elif x == 'child' and y == 'validation':
            #shutil.move(path + k, 'images/3-validation-test/child/')
            src_file = os.path.join(path, k)
            dest_dir = 'images/3-validation-test/child/'

       
            try:            
                if os.path.exists(src_file):
                    os.makedirs(dest_dir, exist_ok=True)                                
                if os.path.exists(os.path.join(dest_dir, k)) == False:
                    shutil.move(src_file, dest_dir)  
                else:
                    print(f"Source file '{src_file}' 4does not exist. Skipping.")
            except Exception as e:                    
                print('HELLO2')
                print(e)

        else:

            try:
                #shutil.move(path + k, 'images/3-validation-test/non-child/')            
                src_file = os.path.join(path, k)
                dest_dir = 'images/3-validation-test/non-child/'
                if os.path.exists(src_file):
                    os.makedirs(dest_dir, exist_ok=True)
                if os.path.exists(os.path.join(dest_dir, k)) == False:
                    shutil.move(src_file, dest_dir)                
                else:
                    print(f"Source file '{src_file}' 3does not exist. Skipping.")            
            except Exception as e:    
                print()
                print('HELLO1')
                print(e)









def rebuild_dataset():
    path_test_child = 'images/2-test/child/'
    path_test_non_child = 'images/2-test/non-child/'
    path_validation_child = 'images/3-validation-test/child/'
    path_validation_non_child = 'images/3-validation-test/non-child/'

    path_list = [path_test_child, path_test_non_child, path_validation_child, path_validation_non_child]

    for k in range(len(path_list)):
        images = os.listdir(path_list[k])
        if k % 2 == 0:
            for p in images:
                #shutil.move(path_list[k] + p, 'images/1-training/child/')
                src_file = os.path.join(path_list[k], p)
                dest_dir = 'images/1-training/child/'
                try:
                    if os.path.exists(src_file):
                        os.makedirs(dest_dir, exist_ok=True)
                    if os.path.exists(os.path.join(dest_dir, p)) == False:
                        shutil.move(src_file, dest_dir)   
                    else:
                        print(f"Source file '{src_file}' 2does not exist. Skipping.")
                except Exception as e:                      
                    print('HELLO3')
                    print(e)

                
        else:
            for p in images:
                #shutil.move(path_list[k] + p, 'images/1-training/non-child/')
                src_file = os.path.join(path_list[k], p)
                dest_dir = 'images/1-training/non-child/'
                try:
                    if os.path.exists(src_file):
                        os.makedirs(dest_dir, exist_ok=True)
                    if os.path.exists(os.path.join(dest_dir, p)) == False:
                        shutil.move(src_file, dest_dir)                
                    else:
                        print(f"Source file '{src_file}' 1does not exist. Skipping.")

                except Exception as e:    
                    print('HELLO4')
                    print(e)