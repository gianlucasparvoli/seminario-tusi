from app import *
#from models.models import *
from controllers.producto import *

app.add_url_rule("/product/<id>",view_func=productIDEndPoint.as_view("product_id"))  
app.add_url_rule("/product/all",view_func=productAllEndPoint.as_view("product_all"))  
app.add_url_rule("/product",view_func=productEndPoint.as_view("product"))  
app.add_url_rule("/product/new",view_func=productNewEndPoint.as_view("product-new")) 
app.add_url_rule("/productos/add",view_func=productAddEndPoint.as_view("product-add")) 
app.add_url_rule("/modificar-producto",view_func=modifyProductEndPoint.as_view("modifyProduct"))  
app.add_url_rule("/producto/reporte",view_func=reportProductEndPoint.as_view("reportProduct"))  

app.add_url_rule("/products/history",view_func=historyProductEndPoint.as_view("historyProduct"))  
app.add_url_rule("/products/history/all",view_func=historyAllProductEndPoint.as_view("historyProductAll"))