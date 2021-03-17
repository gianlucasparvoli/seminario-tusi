from app import *
#from models.models import *
from controllers.cuenta_corriente import *

# app.add_url_rule("/prize/<id>",view_func=prizeIDEndPoint.as_view("prize_id"))  
app.add_url_rule("/current-account/cc/all",view_func=currentAccountAllEndPoint.as_view("current-account-cc_all"))
app.add_url_rule("/current-account/productos/cc/all",view_func=currentAccountProdAllEndPoint.as_view("current-account-prod-cc_all"))
app.add_url_rule("/current-account",view_func=currentAccountEndPoint.as_view("current-account"))  
app.add_url_rule("/current-account/new",view_func=currentAccountNewEndPoint.as_view("current-account-new")) 
app.add_url_rule("/current-account/add",view_func=currentAccountAddEndPoint.as_view("current-account-add")) 
# app.add_url_rule("/modificar-current-accounte",view_func=modifycurrent-accountEndPoint.as_view("modifycurrent-accounte"))  
# app.add_url_rule("/current-account/reporte",view_func=current-accountReportEndPoint.as_view("current-account-report")) 



