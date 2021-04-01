from app import *
#from models.models import *
from controllers.miloteria import *

app.add_url_rule("/lottery/<id>",view_func=MyLotteryFindOneEndPoint.as_view("MyLottery_id"))  
app.add_url_rule("/lottery",view_func=MyLotteryEndPoint.as_view("my_lottery"))  

app.add_url_rule("/lottery/movement",view_func=MyLotteryMovementEndPoint.as_view("my_lottery_movement"))