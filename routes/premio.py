from app import *
#from models.models import *
from controllers.premio import *

# app.add_url_rule("/prize/<id>",view_func=prizeIDEndPoint.as_view("prize_id"))  
app.add_url_rule("/prize/all",view_func=prizeAllEndPoint.as_view("prize_all"))
app.add_url_rule("/prize",view_func=prizeEndPoint.as_view("prize"))  
app.add_url_rule("/prize/new",view_func=prizeNewEndPoint.as_view("prize-new")) 
app.add_url_rule("/prize/add",view_func=prizeAddEndPoint.as_view("prize-add")) 
# app.add_url_rule("/modificar-prizee",view_func=modifyprizeEndPoint.as_view("modifyprizee"))  
app.add_url_rule("/prize/reporte",view_func=prizeReportEndPoint.as_view("prize-report")) 