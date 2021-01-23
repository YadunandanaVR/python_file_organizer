import os
import shutil

image_formats = ['jpg', 'png', 'jpeg', 'gif']
video_formats = ['mp4', 'avi', 'mkv', 'webm']
audio_formats = ['mp3', 'wav']
doc_formats = ['pdf', 'docx', 'txt']
zip_formats = ['zip']
app_formats = ['exe']


while True:

    all_files = []

    for folder, sub_folders, files in os.walk('C:\\Users\\Yadunandan\\Desktop\\test'):

        for file in files:

            file_path = os.path.join(folder, file)

            if os.path.isfile(file_path):
                all_files.append(file)

    try:

        for file in all_files:

            extention = file.split('.')[-1]

            if extention in image_formats:

                if 'Images' not in os.listdir('C:\\Users\\Yadunandan\\Desktop\\test'):
                    os.mkdir('C:\\Users\\Yadunandan\\Desktop\\test\\Images')
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Images')

                else:
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Images')



            if extention in video_formats:

                if 'Videos' not in os.listdir('C:\\Users\\Yadunandan\\Desktop\\test'):
                    os.mkdir('C:\\Users\\Yadunandan\\Desktop\\test\\Videos')
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Videos')

                else:
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Videos')



            if extention in audio_formats:

                if 'Audios' not in os.listdir('C:\\Users\\Yadunandan\\Desktop\\test'):
                    os.mkdir('C:\\Users\\Yadunandan\\Desktop\\test\\Audios')
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Audios')

                else:
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Audios')



            if extention in doc_formats:

                if 'Documents' not in os.listdir('C:\\Users\\Yadunandan\\Desktop\\test'):
                    os.mkdir('C:\\Users\\Yadunandan\\Desktop\\test\\Documents')
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Documents')

                else:
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Documents')



            if extention in zip_formats:

                if 'Zips' not in os.listdir('C:\\Users\\Yadunandan\\Desktop\\test'):
                    os.mkdir('C:\\Users\\Yadunandan\\Desktop\\test\\Zips')
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Zips')

                else:
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Zips')



            if extention in app_formats:

                if 'Applications' not in os.listdir('C:\\Users\\Yadunandan\\Desktop\\test'):
                    os.mkdir('C:\\Users\\Yadunandan\\Desktop\\test\\Applications')
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Applications')

                else:
                    shutil.move('C:\\Users\\Yadunandan\\Desktop\\test\\' + file, 'C:\\Users\\Yadunandan\\Desktop\\test\\Applications')

    except:
        pass