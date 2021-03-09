from app import *
#from models.models import *
from controllers.ventas import *

app.add_url_rule("/sell/<id>",view_func=sellIDEndPoint.as_view("sell_id"))  
app.add_url_rule("/sell/all",view_func=sellAllEndPoint.as_view("sell_all"))
app.add_url_rule("/sell",view_func=sellEndPoint.as_view("sell")) 
app.add_url_rule("/sell/viewAll",view_func=sellViewEndPoint.as_view("sell_view_all")) 
app.add_url_rule("/sell/add",view_func=sellAddEndPoint.as_view("sell-add")) 
app.add_url_rule("/sell/menu",view_func=sellMenuEndPoint.as_view("sell-menu")) 
#app.add_url_rule("/modificar-selle",view_func=modifySellEndPoint.as_view("modifyselle"))  