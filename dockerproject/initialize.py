import os
import click
import shutil

from dockerproject.config import Config


def move_files(target_path, env_name):
    hook_path = os.path.join(target_path, 'bash_hooks')
    activation_script = os.path.join(hook_path, 'activate_env.sh')
    os.makedirs(hook_path, exist_ok=True)
    with open(activation_script, 'w') as buff:
        buff.write(f'conda activate {env_name} 2>/dev/null || true')

    file_dir = os.path.realpath(__file__)
    base_dir = os.path.dirname(file_dir)
    source_path = os.path.join(base_dir, 'default_project_files', 'default')
    base_file_names = [
        'environment.yml',
        'docker-compose.yml'
    ]

    blob = Config().blob
    for base_file_name in base_file_names:
        source = os.path.join(source_path, base_file_name)
        target = os.path.join(target_path, base_file_name)
        shutil.copy(source, target)

        with open(target) as buff:
            contents = buff.read()
        contents = contents.format(image_name=blob['image_name'], env_name=env_name)
        with open(target, 'w') as buff:
            buff.write(contents)


@click.command()
@click.option('-d', '--directory', required=True, help='Prepare all files for building a project')
@click.option('-n', '--name', help='The env name (defaults to directory name')
def main(directory, name):
    directory = os.path.realpath(os.path.expanduser(directory))
    if name is None:
        name = os.path.basename(directory)
    move_files(directory, name)


if __name__ == '__main__':
    main()
