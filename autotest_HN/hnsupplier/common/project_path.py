import time
import os

#项目目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


good_image=r"outputs\pic\shark.png"
good_image_dir=os.path.join(BASE_DIR,good_image)

picture_path='outputs'+os.sep+'screenshots'
picture_path_file=os.path.join(BASE_DIR,picture_path)
picture_name=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))+'.png'
picture_file_name=os.path.join(BASE_DIR,picture_name)









annoucement_name='testdatas'+os.sep+'orderDatas'+os.sep+'announcement_name.json'
anouncement_name_file_name=os.path.join(BASE_DIR,annoucement_name)



















