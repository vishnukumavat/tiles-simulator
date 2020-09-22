from django.urls import path, include
from wallsimulator.v1 import views as wallsimulator_views


urlpatterns = [
	path(r'login/', wallsimulator_views.PortalUserInteraction().user_login, name='WallSimulatorUserLogin'),
	path(r'logout/', wallsimulator_views.PortalUserInteraction().user_logout, name='WallSimulatorUserLogout'),
	path(r'dashboard/', wallsimulator_views.PortalUserInteraction().wall_simulator_dashboard, name='WallSimulatorDashboard'),
	path(r'new/18/12/', wallsimulator_views.PortalUserInteraction().add_new_18_12_desig, name='WallSimulatorAddNewDesign')
]

