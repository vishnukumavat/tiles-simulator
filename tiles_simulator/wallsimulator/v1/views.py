import ossaudiodev
from wallsimulator.v1 import forms as wallsimulator_forms 
from wallsimulator.v1.services import get_wall_designs
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.response import Response
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


class PortalUserInteraction(object):
    @xframe_options_exempt
    def user_login(self, request):
        if request.session.has_key('username') and request.session.has_key('password'):
            return redirect('../dashboard/')
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            auth_secret = settings.AUTHENTICATION_SECRETS.get('tiles_simulator', {})
            if username == auth_secret.get('username') and password == auth_secret.get('password'):
                request.session['username'] = username
                request.session['password'] = password
                request.session.get_expire_at_browser_close()
                return redirect('../dashboard/')
            messages.info(request, 'Incorrect Password/Username')
            return redirect('../login/')
        return render(request, 'v1/login_form.html')

    @xframe_options_exempt
    def user_logout(self, request):
        if request.session.has_key('username') and request.session.has_key('password'):
            request.session.flush()
        return redirect('../login/')
    
    @xframe_options_exempt
    def wall_simulator_dashboard(self, request):
        if request.session.has_key('username') and request.session.has_key('password'):

            wall_design_data_list = get_wall_designs.GetWallDesign().get_all_designs()
            image_url_data_list = list()
            if wall_design_data_list:
                for item in wall_design_data_list:
                    image_url_data = {
                        'id' : item.get('id', ''),
                        'tile_number' : item.get('tile_number', ''),
                        'high_lighter' : item.get('high_lighter_1_image_url', ''),
                    }
                    image_url_data_list.append(image_url_data)
            
            if request.method == 'POST':
                wall_design_data = get_wall_designs.GetWallDesign().get_design_by_id(int(request.POST['design_id']))
                template_data = {
                    'image_url_data_list' : image_url_data_list, 
                    'show_designs' : True,
                    'light_image_url' : wall_design_data.get('light_image_url', ''),
                    'high_lighter_1_image_url' : wall_design_data.get('high_lighter_1_image_url', ''),
                    'dark_image_url' : wall_design_data.get('dark_image_url', ''),
                    'tile_number' : wall_design_data.get('tile_number', '')
                }
                return render(request, 'v1/dashboard.html', template_data)
            return render(request, 'v1/dashboard.html', {'image_url_data_list' : image_url_data_list, 'show_designs' : False})
        return redirect('../login/')
    
    @xframe_options_exempt
    def add_new_18_12_desig(self, request):
        if request.session.has_key('username') and request.session.has_key('password'):
            if request.method == 'POST':
                form = wallsimulator_forms.NewDesignCreateForm(request.POST, request.FILES)
                if form.is_valid():
                    form.perform_task_and_get_data()
            return render(request, 'v1/new_18_12_design.html')
        return redirect('../login/')