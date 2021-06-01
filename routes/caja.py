from app import *
from controllers.caja import *

app.add_url_rule("/caja",view_func=cajaEndPoint.as_view("caja"))  
