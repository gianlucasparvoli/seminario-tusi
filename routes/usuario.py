from app import *
#from models.models import *
from controllers.usuario import *

app.add_url_rule("/sigin",view_func=UsersSigInEndPoint.as_view("users_sigin"))  
app.add_url_rule("/login",view_func=UsersLogInEndPoint.as_view("users_login"))  
app.add_url_rule("/gestion-usuarios/<id>",view_func=UsersGestionEndPoint.as_view("users_gestion"))  


app.add_url_rule("/usuarios",view_func=UsersEndPoint.as_view("users"))  
app.add_url_rule("/usuario/<id>",view_func=UserEndPoint.as_view("user")) 

app.add_url_rule("/menu/<id>",view_func=UsersMenuEndPoint.as_view("users_menu"))  

app.add_url_rule("/modificar-usuario/<id>",view_func=UsersModifEndPoint.as_view("modificar_usuario")) 

app.add_url_rule("/cambiar-clave/<id>",view_func=UsersCambiarClaveEndPoint.as_view("cambiar_clave")) 
# app.add_url_rule("/cambiar-clave",view_func=UsersCambiarClave2EndPoint.as_view("cambiar_clave_2")) 

app.add_url_rule("/resetear-clave/<id>/<idAdmin>",view_func=UsersResetearClaveEndPoint.as_view("resetear_clave")) 