import enumerate_file
import pprint

pp = pprint.PrettyPrinter(indent=4)

basepath = "/Users/JohnLiu/CodeProject/test/"
result = enumerate_file.enumerate_file(basepath,["php"],["erb","py"])
pp.pprint(result['file_list'])
pp.pprint(result['path_list'])
