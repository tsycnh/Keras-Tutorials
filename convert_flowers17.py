import numpy as np
import os
from shutil import copyfile,rmtree
# 数据预处理，将原始花朵数据集转换成keras要求的格式,如下.每一个子文件夹代表一类
'''
data/
    train/
        class1/
            img1
            img2
            ...
        class2/
            img1
            ...
    validation/
        class1/
            img1
            img2
            ...
        class2/
            img1
            ...
    test/
        class1/
            img1
            img2
            ...
        class2/
            img1
            ...
'''

data_folder = '/Users/shidanlifuhetian/All/data/flowers17/'#原始图像目录
new_data_folder = './flowers17/'#新的文件夹

# add label first
np.random.seed(0)# 统一seed，保证每次随机结果都一样

file_a = open(data_folder+'files.txt',mode='r')
text = file_a.readlines()
file_a.close()
labels = []
file_b = open('./newtext.txt',mode='a')
for i,item in enumerate(text):
    if i%80 ==0:
        class_num = i//80
    t = item.split('\n')
    newtext = t[0]+' flower_'+chr(65+class_num)+'\n'
    print(newtext)
    file_b.write(newtext)
file_b.close()
# split dataset
if os.path.exists(new_data_folder):
    rmtree(new_data_folder)
train_size = 800
val_size = int((1360-train_size)/2)
test_size = int(val_size)

label_file = open('newtext.txt')

labels = label_file.readlines()
np.random.shuffle(labels)

def save_images(current_i,phase,d_size):

    if phase == 'train':
        dst_folder = new_data_folder+'train/'
    elif phase == 'test':
        dst_folder = new_data_folder+'test/'
    elif phase == 'validation':
        dst_folder = new_data_folder+'validation/'
    else:
        print('phase error')
        exit()

    for i in range(current_i,current_i+d_size):
        item = labels[i]
        r = item.split(' ')
        img_full_path = data_folder+r[0]
        img_class = r[1].split('\n')[0]
        img_new_path = dst_folder+img_class+'/'+r[0]

        if not os.path.exists(dst_folder+img_class):
            os.makedirs(dst_folder+img_class)
        copyfile(img_full_path,img_new_path)
        print(img_new_path,' copied')
    current_i = i

    return current_i

new_i = save_images(current_i=0,phase='train',d_size=train_size)
new_i = save_images(current_i=new_i,phase='test',d_size=test_size)
new_i = save_images(current_i=new_i,phase='validation',d_size=val_size)
