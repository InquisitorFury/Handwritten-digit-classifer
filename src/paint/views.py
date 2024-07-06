from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import base64
from django.core.files.base import ContentFile
from .models import Digit

@method_decorator(csrf_exempt, name='dispatch')
class PaintView(View):

    def get(self, request):
        return render(request, 'base.html')

    def post(self, request):
        data_url = request.POST.get('image')
        format, imgstr = data_url.split(';base64,')
        ext = format.split('/')[-1]
        file_name = 'drawing.' + ext
        file_content = ContentFile(base64.b64decode(imgstr), name=file_name)
        
        drawing = Digit(image=file_content)
        drawing.save()

        return JsonResponse({'status': 'success', 'file_name': drawing.image.url})