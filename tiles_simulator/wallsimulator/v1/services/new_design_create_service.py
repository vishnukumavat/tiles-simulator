from wallsimulator import models as tiles_model
from django.utils.crypto import get_random_string
from django.conf import settings
import subprocess
from django.core.files.storage import FileSystemStorage

class CreateNewDesign(object):
    def __init__(self, data):
        self.data = data
        self.tile_number = self.data.get('tile_number', '')
        self.light_image = self.data.get('light')
        self.high_lighter_1_image = self.data.get('high_lighter_1')
        self.dark_image = self.data.get('dark')
        self.pwd, self.files_path = self._pwd()

    def _pwd(self):
        attachment_directory = str(self.tile_number) + '_' + str(get_random_string(length=16))
        files_path = 'wall_designs_18_12/{attachment_directory}'.format(attachment_directory=attachment_directory)
        pwd = settings.STATIC_FILES_URL + files_path
        return pwd, files_path
    
    def _create_attachment_directory(self):
        try:
            subprocess.call('mkdir {attachment_directory}'.format(
                attachment_directory=self.pwd), shell=True)
        except Exception as e:
            print('Error at new_design_create_service._create_attachment_directory due to : ', e)
    
    def _save_files_in_file_system(self, image_file, design_type):
        file_system = FileSystemStorage(location=self.pwd+'/')  
        filename = file_system.save(''.join([design_type , '_', self.tile_number, '.jpg']), image_file)
        file_url = file_system.url(filename)
        return file_url
    
    def _create_model_data(self):
        model_data = {
            'tile_number' : self.tile_number,
            'light_image_url' : settings.STATIC_HOST_URL + self.files_path + self._save_files_in_file_system(self.light_image, 'light'),
            'high_lighter_1_image_url' : settings.STATIC_HOST_URL + self.files_path +  self._save_files_in_file_system(self.high_lighter_1_image, 'high_lighter_1'),
            'dark_image_url' : settings.STATIC_HOST_URL + self.files_path + self._save_files_in_file_system(self.dark_image, 'dark')
        }
        return model_data


    def create(self):
        self._create_attachment_directory()
        model_data = self._create_model_data()
        wall_tiles_18_12_model_object = tiles_model.WallTiles_18_12_Model.objects.create(**model_data)
        return wall_tiles_18_12_model_object.id
