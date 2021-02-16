from app import *
#from models.models import *
from controllers.cliente import *

app.add_url_rule("/client/<id>",view_func=clientIDEndPoint.as_view("client_id"))  
app.add_url_rule("/client/all",view_func=clientAllEndPoint.as_view("client_all"))
app.add_url_rule("/client",view_func=clientEndPoint.as_view("client"))  
app.add_url_rule("/client/new",view_func=clientNewEndPoint.as_view("client-new")) 
app.add_url_rule("/client/add",view_func=clientAddEndPoint.as_view("client-add")) 
app.add_url_rule("/modificar-cliente",view_func=modifyClientEndPoint.as_view("modifyCliente"))  