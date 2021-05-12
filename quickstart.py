import fitbit
import gather_keys_oauth2 as Oauth2
import datetime

CLIENT_ID = '239Z3V'
CLIENT_SECRET = '7ed20900e40156827fda3b90c9538baf'


server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = datetime.datetime.now()

weight = 60.00
fat = 24.5
fit_weight = auth2_client.log_weight(weight,today)
fit_fat = auth2_client.log_fat(fat,today)

#fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1min')
prof = auth2_client.user_profile_get()
