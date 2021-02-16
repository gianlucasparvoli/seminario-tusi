from app import *
#from models.models import *
from controllers.grupo import *

app.add_url_rule("/grupos",view_func=GruposEndPoint.as_view("grupos"))  

app.add_url_rule("/gestion-grupos/<id>",view_func=GruposGestionEndPoint.as_view("group_gestion")) 

app.add_url_rule("/add-grupo",view_func=AddGrupoEndPoint.as_view("addgrupo"))  