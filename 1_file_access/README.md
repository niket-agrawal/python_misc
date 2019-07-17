### To access all files inside any particular directory 
**(Dependencies - os)**
This code is mainly written for access of specific extension file type/s (.jpg in this case) inside any specific folder. The folder path must be supplied in `sub_path` variable, and list of folders to be accessed is to be supplied manually in `folders` variable.

Alternatively, you can also access all folders by un-commenting the `folders` variable access below.

## How to Run -
- for specific folders (inside any main_folder), just supply its list by manually entering the list.
- for all folders, inside it, (comment line3 & uncomment line5). It will use Python's function `os.listdir('path_to_be_supplied' )` to make list of all folders automatically inside the main folder. 

**Example of output**
Input folder is `main_folder`

Directory tree<br> 
![image](https://user-images.githubusercontent.com/10254081/61349139-94475c00-a852-11e9-80b4-0222344c1e6a.png)

Output is :
```
Image img1.jpg is in folder Patient1
Image img2.jpg is in folder Patient1
Image img1.jpg is in folder Patient2
Image img1.jpg is in folder Patient3
Image img2.jpg is in folder Patient3
Image img3.jpg is in folder Patient3

Total images : 6
```
