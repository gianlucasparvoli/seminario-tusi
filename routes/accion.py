from app import *
#from models.models import *
from controllers.accion import *

app.add_url_rule("/accion/<id>",view_func=AccionEndPoint.as_view("accion_id"))  
app.add_url_rule("/accion-formulario/<id>",view_func=AccionFormularioEndPoint.as_view("accion_formulario_id")) 