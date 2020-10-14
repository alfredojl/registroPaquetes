from django.shortcuts import render

import datetime 
from home.models import Paquete

# Create your views here.
def index(request):
    return render(request, 'registroPaquetes/index.html')

"""
def sesion(request):
    if request['name']:
        return True
    else:
        return False
"""
def verificaDatos(request):
    """
    if sesion(request):
        pass
    else:
        return render(request, 'login/login.html')
    """
    if request.method == 'POST':
        try:
            noPaquete =  int(request.POST['paquete'])
        except Exception as e:
            return render(request, 'registroPaquetes/home.html', {'errorPaquete':True})

        try:
            fech = request.POST['fecha']
            y = int(("").join(fech[i] for i in range(4)))
            m = int(("").join(fech[i] for i in range(5, 7)))
            d = int(("").join(fech[i] for i in range(8, 10)))
            fecha = datetime.date(y,m,d)
        except Exception as e:
            error = True
            return render(request, 'registroPaquetes/index.html', {'errorDate':error})
        
        try:
            foInicio =  int(request.POST['foInicio'])
        except Exception as e:
            error = True
            return render(request, 'registroPaquetes/index.html', {'errorInicio':error})
        
        try:
            foFin =  int(request.POST['foFin'])
        except Exception as e:
            error = True
            return render(request, 'registroPaquetes/index.html', {'errorInicio':error})

        #paquete = Paquete.objects.cre
        p = Paquete(noPaquete = noPaquete, folioInicio = foInicio, folioFin = foFin, fechaExp = fecha)
        p.save()
        
        return render(request, 'registroPaquetes/index.html', {'status' : True})
    else:
        return render(request, 'registroPaquetes/index.html')
