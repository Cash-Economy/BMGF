from main.models import PoolMembership, UserContribution, UserPointMovement
import datetime

contrib = UserContribution(175,0,datetime.datetime(2016, 10, 1), user_id=1, group_id=1)


INSERT INTO main_usercontribution
VALUES (1, 1,value3,...);