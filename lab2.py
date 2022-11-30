""" Follow the lab project and answer-

3. The source object has 30 lines. For every copied object there has to be item*10 no. lines. 												20

Example: 
some_1.txt will have 10 lines,
some_2.txt will have 20 lines, 
some_3.txt will have 30 lines,


4. Package all the converted files before sending to the destination directory. Send the .zip file to the destination folder. Unzip after sending.					20

5. Your event should trigger copying for .txt files only. If you find .py files, it should run them automatically.										20

6. Capture the output and errors of running python files. 				20
 """

import glob
import shutil
import zipfile
import os
import time
 
source_path = '../source/*'
destination_path = '../destination/'
index = 0
allworkingfile = []
while True:
    source_object = glob.glob(source_path)
    if len(source_object) > 0 and index < len(source_object):
        fullpath = source_object[index]
        if fullpath not in allworkingfile:
            source_object_path = fullpath.split('\\')
            file_name =  source_object_path[1].split('.')[0]
            extension_name = source_object_path[1].split('.')[1]
            print(f'\n\nWorking ...:{fullpath}')
            if extension_name == 'txt':
                all_lines  = []
                with open(fullpath,'r') as sourcefile:
                        for lines in sourcefile.readlines():
                                all_lines.append(lines)
                   
                allfiles = []
                print('Copy to server.')
                time.sleep(1)
                for item in range(3):
                    full_file_name = f'{file_name}_{item+1}.txt'
                    with open(full_file_name,'w') as des_file:
                        des_file.write(''.join(all_lines[:(item+1)*10]))
                    des_file.close()
                    allfiles.append(full_file_name)
               
                print('Zipping.')
                time.sleep(1)
                zip_file_name = f'{file_name}.zip'
                zip_file_path = f'./{zip_file_name}'
                with zipfile.ZipFile(zip_file_path,'w') as zip_file:      
                    for item in allfiles:
                        zip_file.write(item)
                        os.remove(item)
                zip_file.close()
                print('Copying to destination.')
                time.sleep(1)
                shutil.copy(zip_file_path,destination_path)
                os.remove(zip_file_path)
                print('Extracting.')
                time.sleep(1)
                with zipfile.ZipFile(f'{destination_path}{zip_file_name}') as zf:
                    zf.extractall(f'{destination_path}')
                os.remove(f'{destination_path}{zip_file_name}')
                os.remove(fullpath)
                print(f'Done:{fullpath}')
            elif extension_name == 'py':
                allworkingfile.append(fullpath)
                index += 1
                print('Running script:',end="")
                for i in range(5):
                    time.sleep(1)
                    print('.',end='')
                print("\n")
                try :
                    os.system(f'python {fullpath}')
                    os.remove(fullpath)
                except os.error :
                    print(os.error)
                print('\n--End--')
        else:
             index += 1
    else:
         index = 0