from app import *
#from models.models import *
from controllers.grupos_usuario import *

app.add_url_rule("/grupos-usuarios",view_func=GruposUsuariosEndPoint.as_view("grupos_usuarios"))  
app.add_url_rule("/grupos-usuario/<id>",view_func=GruposUsuarioEndPoint.as_view("grupos_usuario"))  
