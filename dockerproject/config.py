import json
import os
import click


class Config:
    BLOB_DIR = os.path.realpath(os.path.expanduser('~/.dockerproject'))
    DEFAULT_IMAGE_NAME = 'robdmc/dockerproject'

    @property
    def default_blob(self):
        return {
            'image_name': self.DEFAULT_IMAGE_NAME
        }

    @property
    def config_file_name(self):
        return os.path.join(self.BLOB_DIR, 'config.json')

    @property
    def blob(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file_name) as buff:
                blob = json.load(buff)
        else:
            blob = self.default_blob
            self.save_blob(blob)

        return blob.copy()

    def save_blob(self, blob):
        with open(self.config_file_name, 'w') as buff:
            json.dump(blob, buff)

    def set_image_name(self, image_name):
        blob = self.blob
        blob.update({'image_name': image_name})
        self.save_blob(blob)


@click.command()
@click.option('--image-name', help='The name of the docker image to use for creating containers')
def main(image_name):
    print(f'image is {image_name}')


if __name__ == '__main__':
    main()
