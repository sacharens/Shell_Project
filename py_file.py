import os , fnmatch
import filecmp
from shutil import copyfile

#
# folder_path1 = 'T:/HertzLab/'
# folder_path2 = 'T:/HertzLab_HertzLab/'
test_folder = '/mnt/c/Users/User/PycharmProjects/Shell_Project/'

if os.path.exists(test_folder) :
    print('found path')
else:
    print('cant find path')



with open(test_folder+'diff.txt') as f:
    lines = f.readlines()

main_folder_path = '/mnt/c/Users/User/PycharmProjects/Shell_Project/Data_02_13_2020'
sub_folder_pth = '/mnt/c/Users/User/PycharmProjects/Shell_Project/Data_02_13_2020_data'

for line in lines:
    sep_line = line.split(' ')
    print(sep_line)
    if sep_line[0] == 'Files': # then the files are different but have the same name
        # file comparison
        file_main_info = os.stat(sep_line[1])
        file_sub_info = os.stat(sep_line[3])
        # st_mtime : Time of most recent content modification expressed in seconds.
        # st_size : Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is
        # the length of the pathname it contains, without a terminating null byte.
        if file_main_info.st_size < file_sub_info.st_size or file_main_info.st_mtime < file_sub_info.st_mtime:
            src = sep_line[1]
            dst = sep_line[3]
            print (src)

            copyfile(src, dst)

    if sep_line[0] == 'Only': # file is only in one of the folders
        if sep_line[2][-1] != main_folder_path:
            file_name = sep_line[3].rstrip()
            src = sub_folder_pth+'/'+file_name
            dst = main_folder_path+'/'+file_name
            print (src)

            copyfile(src, dst)
