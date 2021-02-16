from app import *
#from models.models import *
from controllers.index import *

app.add_url_rule("/",view_func=IndexEndPoint.as_view("index"))  