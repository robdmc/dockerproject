import json
import os
import click
import shutil
import sys

from dockerproject.config import Config


def move_files(target_path):
    target_path = os.path.realpath(os.path.expanduser(target_path))
    if os.path.isdir(target_path):
        print(f'\nThe directory exists\n\n{target_path}\n\nYou must specify a non-existent directory.', file=sys.stderr)
        exit(1)

    file_dir = os.path.realpath(__file__)
    base_dir = os.path.dirname(file_dir)
    source_path = os.path.join(base_dir, 'default_build_files')
    shutil.copytree(source_path, target_path)

    build_script = os.path.join(target_path, 'build.sh')
    push_script = os.path.join(target_path, 'push.sh')

    blob = Config().blob

    for file_name in [build_script, push_script]:
        with open(file_name) as buff:
            contents = buff.read()
        contents = contents.format(image_name=blob['image_name'])
        with open(file_name, 'w') as buff:
            contents = buff.write(contents)




@click.command()
@click.option(
    '-d', '--directory', required=True,
    help='Prepare all files for building a project')
def main(directory):
    # move_files(directory)
    print('doin it')


if __name__ == '__main__':
    main()
