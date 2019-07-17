import os
#used for accessing the particular folders
folders = ['Patient1', 'Patient2','Patient3']
#uncomment the following line to access all folders present in the directory
#folders = os.listdir("C:\\Users\\niket\\Desktop\\Download Dustbin\\main_folder")
def load_from_folder(folder):
	images = []
	sub_path = "C:\\Users\\niket\\Desktop\\Download Dustbin\\main_folder\\" + folder
	for filename in os.listdir(sub_path):
		if any([filename.endswith(x) for x in ['.jpg', '.jpeg']]):
			tple = (folder, os.path.splitext(filename)[0])
			images.append(tple)
	return images

all_images = []
for folder in folders:
	images = load_from_folder(folder)
	for single_img in images:
		all_images.append(single_img)
		
		
for file_img in all_images:
		print(file_img)
		print("Image",file_img[1]+'.jpg is in folder',file_img[0])
		
print("\nTotal images :",len(all_images))
