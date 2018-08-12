import sys
import os

def filename_filter(ignore_file_list, file):
    for ignore_file in ignore_file_list:
        if file.endswith(ignore_file)>0:
            return True
    return False

def foldername_filter(ignore_folder_list, sub_path):
    for ignore_folder in ignore_folder_list:
        if sub_path.find(ignore_folder)>0:
            return True
    return False

def enumerate_file(basepath,ignore_folder_list=[],ignore_file_list=[]):
    path_lists = [basepath]
    file_lists = []
    for path in path_lists:
        for file in os.listdir(path):
            sub_path = os.path.join(path, file)
            if filename_filter(ignore_file_list, file) or foldername_filter(ignore_folder_list, sub_path):              
                continue
            elif os.path.isdir(sub_path):
                path_lists.append(sub_path)
            else:
                file_lists.append(sub_path)
                continue

    result ={"path_list":path_lists, "file_list":file_lists}
    return result
                


