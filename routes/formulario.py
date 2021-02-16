from app import *
#from models.models import *
from controllers.formulario import *

app.add_url_rule("/formulario/<id>",view_func=FormularioEndPoint.as_view("formulario_id"))  
app.add_url_rule("/formulario-mod/<id>",view_func=FormularioModEndPoint.as_view("formulario_mod_id")) 