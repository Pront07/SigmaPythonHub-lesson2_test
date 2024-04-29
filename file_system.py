import time
from random import randint
import os
import shutil
from texts import texts


class File:
    GEN_FOLDER = "variable_name"
    FILE_NAME = "text_file"

    def __init__(self, file_name, file_content):
        self.file_name = file_name
        self.file_content = file_content
        self.created_at = time.time()
        self.full_path = os.path.abspath(file_name)
        self.size = os.stat(f"{File.GEN_FOLDER}/{file_name}").st_size

    @staticmethod
    def generation(f_amount):
        if os.path.exists(File.GEN_FOLDER):
            shutil.rmtree(File.GEN_FOLDER)
        os.mkdir(File.GEN_FOLDER)

        for i in range(f_amount):
            filename = f"{File.FILE_NAME}{i + 1}.txt"
            selected_text = texts[f"text{randint(1, 5)}"]
            print(selected_text)
            with open(os.path.join(File.GEN_FOLDER, filename), 'w', encoding='utf-8') as filter:
                filter.write(selected_text)

    @staticmethod
    def list_files():
        files_list = os.listdir(File.GEN_FOLDER)
        for file in files_list:
            print(file)
        print(f"amount of files: {len(files_list)}")
        return files_list

    @classmethod
    def initialize_objects(cls):
        objects = []
        for item in os.listdir(cls.GEN_FOLDER):
            full_path = os.path.join(cls.GEN_FOLDER, item)
            with open(full_path, 'r', encoding='utf-8') as filter:
                content = filter.read()
                file_obj = cls(item, content)
                objects.append(file_obj)
        return objects


File.generation(5)
File.list_files()
files_objects = File.initialize_objects()

for data in files_objects:
    print("\n")
    print(f"name: {data.file_name}\n")
    print(f"f_content: {data.file_content}\n")
    print(f"created_at: {data.created_at}\n")
    print(f"full_path: {data.full_path}\n")
    print(f"size: {data.size}\n")
