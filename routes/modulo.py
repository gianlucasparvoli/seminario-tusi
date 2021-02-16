from app import *
#from models.models import *
from controllers.modulo import *

app.add_url_rule("/modulo/<id>",view_func=ModuloEndPoint.as_view("modulo_id"))  

app.add_url_rule("/modulos",view_func=ModulosEndPoint.as_view("modulos"))  