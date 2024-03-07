import os
import random
import string
import time


class File:
    GEN_FOLDER = "GEN_FOLDER"
    FILE_NAME = "text_file"

    def __init__(self, filename, content, created_time, full_path, size):
        self.filename = filename
        self.content = content
        self.created_time = created_time
        self.full_path = full_path
        self.size = size

    @staticmethod
    def generate_files():
        try:
            os.makedirs(File.GEN_FOLDER)
        except FileExistsError:
            pass

        text_samples = [
            "Привіт шо ти.",
            "Хелоу.",
            "тарараараарар.",
            "ку.",
            "пока."
        ]

        for i in range(random.randint(5, 10)):
            filename = f"{File.FILE_NAME}_{i}.txt"
            content = random.choice(text_samples)
            created_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            full_path = os.path.join(File.GEN_FOLDER, filename)
            size = len(content.encode('utf-8'))
            with open(full_path, 'w') as file:
                file.write(content)

    @staticmethod
    def list_files():
        files = []
        for filename in os.listdir(File.GEN_FOLDER):
            print(filename)
            files.append(filename)
        print(f"Number of files: {len(files)}")
        return files

    @classmethod
    def initialize_files(cls):
        files = []
        for filename in os.listdir(cls.GEN_FOLDER):
            full_path = os.path.join(cls.GEN_FOLDER, filename)
            with open(full_path, 'r') as file:
                content = file.read()
                created_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(full_path)))
                size = os.path.getsize(full_path)
                files.append(cls(filename, content, created_time, full_path, size))
        return files


def main():
    File.generate_files()
    File.list_files()
    files = File.initialize_files()
    for file in files:
        print(f"Filename: {file.filename}")
        print(f"Content: {file.content}")
        print(f"Created Time: {file.created_time}")
        print(f"Full Path: {file.full_path}")
        print(f"Size: {file.size} bytes")
        print()


if __name__ == "__main__":
    main()
