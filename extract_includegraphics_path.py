import os
import re


def extract_path_list(texfile,exclude_commented=True):
    '''
    from a texfile, extract a list of the relative path to the files used in "\includegraphics[...]{path}" '''
    with open(texfile) as file:
        lines=file.readlines()
    if exclude_commented: 
        all_lines = "".join([(line.strip()).split("%")[0] for line in lines])
    else:
        all_lines = "".join([line.strip() for line in lines])
    path_list = re.findall(r'\\includegraphics(?:\[.*?\])?\{(.+?)\}', all_lines)
        
    return "\n".join(path_list)


print ( extract_path_list("Hindenlang_Plunk_Maj_varenna2024_frenet.tex") )



