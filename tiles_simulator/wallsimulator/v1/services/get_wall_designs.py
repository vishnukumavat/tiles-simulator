from wallsimulator import models

class GetWallDesign(object):
    def get_all_designs(self):
        wall_design_data = models.WallTiles_18_12_Model.objects.all().values()
        return wall_design_data
    
    def get_design_by_id(self, id):
        filtered_design_data = models.WallTiles_18_12_Model.objects.filter(id=id).values()[0]
        return filtered_design_data