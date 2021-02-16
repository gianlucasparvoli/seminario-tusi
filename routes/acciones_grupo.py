from app import *
#from models.models import *
from controllers.acciones_grupo import *

app.add_url_rule("/acciones-grupos",view_func=AccionesGruposEndPoint.as_view("acciones_grupos"))  
app.add_url_rule("/acciones-grupo/<id>",view_func=AccionesGrupoEndPoint.as_view("acciones_grupo"))  