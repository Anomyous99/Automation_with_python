import logging
import os
import shutil
import time
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "/home/reborn666/Downloads/"           # You can add your directory location here
dest_img_dir = "/home/reborn666//"                  # Same here
dest_music_dir = "/home/reborn666/Music/"           # here
dest_videos_dir = "/home/reborn666/Videos/"         # here 
dest_docs_dir = "/home/reborn666/Documents/"        # and here

#This is where you add your extension, if you want you can stick with the given extension or 
#add some more to your liking

image_ext = [".png", ".jpg", ".jpeg"]
music_ext = [".mp3", ".wav", ".m4a", ".flac"]
video_ext = [".mp4", ".mkv", ".webm", ".avi"]
docs_ext = [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt",
             ".odt", ".ods", ".odp", ".odg", ".odf", ".odm", ".7z", ".rar",
             ".zip", ".gz", ".bz2", ".xz", ".pdf", ".html", ".xml"]

#This is the place where the fun starts
#it will copy the files based on their extension

def separate_files(source_dir, dest_dir, ext): 
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(ext):
                src_file = os.path.join(root, file)
                shutil.move(src_file, dest_dir)
def copy_files(source_dir, dest_dir, ext):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(tuple(ext)):
                src_file = os.path.join(root, file)
                shutil.copy(src_file, dest_dir)

copy_files(source_dir, dest_img_dir, image_ext)
copy_files(source_dir, dest_music_dir, music_ext)
copy_files(source_dir, dest_videos_dir, video_ext)
copy_files(source_dir, dest_docs_dir, docs_ext)

def move_files(source_dir, dest_dir, ext):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(tuple(ext)):
                src_file = os.path.join(root, file)
                shutil.move(src_file, dest_dir)

move_files(source_dir, dest_img_dir, image_ext)
move_files(source_dir, dest_music_dir, music_ext)
move_files(source_dir, dest_videos_dir, video_ext)
move_files(source_dir, dest_docs_dir, docs_ext) 
class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(f"event type: {event.event_type}, filename: {event.src_path}")

        if event.event_type == 'created':
            # Take any action here when a file is first created.
            print(f"Event type: {event.event_type}, filename: {event.src_path}")

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print(f"Event type: {event.event_type}, filename: {event.src_path}")
            move_files(source_dir, dest_img_dir, image_ext)
            move_files(source_dir, dest_music_dir, music_ext)
            move_files(source_dir, dest_videos_dir, video_ext)
            move_files(source_dir, dest_docs_dir, docs_ext)
Observers = Observer()
Observers.schedule(MyHandler(), source_dir, recursive=True)
Observers.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    Observers.stop()
    Observers.join()

event_handler = MyHandler()
Observers = Observer()
Observers.schedule(event_handler, source_dir, recursive=True)
Observers.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    Observers.stop()
    Observers.join()
def check_files(source_dir, dest_dir, ext):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(ext):
                src_file = os.path.join(root, file)
                shutil.move(src_file, dest_dir)

check_files(source_dir, dest_img_dir, image_ext)
check_files(source_dir, dest_music_dir, music_ext)
check_files(source_dir, dest_videos_dir, video_ext)
check_files(source_dir, dest_docs_dir, docs_ext)    

#WARNING!!
#You should not change the code below 
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    logging.info("Starting Auto-File-Organizer...")

    while True:
        time.sleep(10)

    logging.info("Auto-File-Organizer stopped.")
    path = "/home/reborn666/Downloads/"
    observers = watchdog.observers.observers()
    observers.schedule(event_handler, path, recursive=True)
    observers.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observers.stop()
    observers.join()

