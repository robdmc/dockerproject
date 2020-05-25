import json
import os
import click
import shutil


# class Build:
#     BLOB_DIR = os.path.realpath(os.path.expanduser('~/.dockerproject'))
#     DEFAULT_IMAGE_NAME = 'robdmc/dockerproject'

#     @property
#     def default_blob(self):
#         return {
#             'image_name': self.DEFAULT_IMAGE_NAME
#         }

#     @property
#     def config_file_name(self):
#         return os.path.join(self.BLOB_DIR, 'config.json')

#     @property
#     def blob(self):
#         if os.path.isfile(self.config_file):
#             with open(self.config_file_name) as buff:
#                 blob = json.load(buff)
#         else:
#             blob = self.default_blob
#             self.save_blob(blob)

#         return blob.copy()

#     def save_blob(self, blob):
#         with open(self.config_file_name, 'w') as buff:
#             json.dump(blob, buff)

#     def set_image_name(self, image_name):
#         blob = self.blob
#         blob.update({'image_name': image_name})
#         self.save_blob(blob)


def move_files(target_path):
    target_path = os.path.realpath(os.path.expanduser(target_path))
    if not os.path.isdir(target_path):
        prompt = f'\nThe directory does not exists\n\n{target_path}\n\nCreate it?  y/n: '
        answer = input(prompt).lower()
        if answer != 'y':
            print('Nothing done.')
            exit()

    file_dir = os.path.realpath(__file__)
    base_dir = os.path.dirname(file_dir)
    source_path = os.path.join(base_dir, 'default_build_files')
    shutil.copytree(source_path, target_path)




@click.command()
@click.option(
    '-d', '--directory', required=True,
    help='Put default build files in this directory')
def main(directory):
    move_files(directory)


if __name__ == '__main__':
    main()
