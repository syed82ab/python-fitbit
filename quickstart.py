import fitbit
#import gather_keys_oauth2 as Oauth2
import datetime
import token_access
import sys

if not (len(sys.argv) == 3):
        print("Arguments: weight and fat percentage")
        sys.exit(1)
weight = sys.argv[1]
fat = sys.argv[2]


CLIENT_ID = '239Z3V'
CLIENT_SECRET = '7ed20900e40156827fda3b90c9538baf'
#Get and write the tokens from here



#server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
#server.browser_authorize()
#ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
#REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
ACCESS_TOKEN, REFRESH_TOKEN = token_access.GetConfig()

auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

today = datetime.datetime.now()

fit_weight = auth2_client.log_weight(weight,today)
fit_fat = auth2_client.log_fat(fat,today)

#fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1min')
#prof = auth2_client.user_profile_get()

#token_access.WriteConfig(ACCESS_TOKEN,REFRESH_TOKEN)
