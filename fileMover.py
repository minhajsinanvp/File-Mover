import os
import shutil

def copy_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, file)
            shutil.copy(src_path, dest_path)
            print(f"Copied {src_path} to {dest_path}")

def main():
    source_directory_path = './course'
    destination_directory_path = './target'

    if not os.path.exists(destination_directory_path):
        os.makedirs(destination_directory_path)

    copy_files(source_directory_path, destination_directory_path)

if __name__ == "__main__":
    main()
