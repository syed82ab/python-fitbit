from requests.auth import HTTPBasicAuth

IniFile = "/home/pi/python/python-fitbit/tokens.txt"

def GetConfig():
    print( "Reading from the config file")

    #Open the file
    FileObj = open(IniFile,'r')

    #Read first two lines - first is the access token, second is the refresh token
    AccToken = FileObj.readline()
    RefToken = FileObj.readline()
    Expires_at = float(FileObj.readline())

    #Close the file
    FileObj.close()
    #See if the strings have newline characters on the end.  If so, strip them
    if (AccToken.find("\n") > 0):
        AccToken = AccToken[:-1]
    if (RefToken.find("\n") > 0):
        RefToken = RefToken[:-1]

    #Return values
    return AccToken, RefToken, Expires_at

def WriteConfig(AccToken,RefToken, Expires_at):
    print("Writing new token to the config file")
    print("Writing this: " + AccToken + " and " + RefToken)

    #Delete the old config file
    #os.remove(IniFile)

    #Open and write to the file
    FileObj = open(IniFile,'w')
    FileObj.write(AccToken + "\n")
    FileObj.write(RefToken + "\n")
    FileObj.write(str(Expires_at) + "\n")
    FileObj.close()

#Make a HTTP POST to get a new
def GetNewAccessToken(auth2_client):
    print( "Getting a new access token")

    token = auth2_client.client.session.refresh_token(
            auth2_client.client.refresh_token_url,
            auth=HTTPBasicAuth(auth2_client.client.client_id, auth2_client.client.client_secret)
            )
    AccToken = token['access_token'];
    RefToken = token['refresh_token'];
    Expires_at = token['expires_at'];
   
    #Write the access token to the ini file
    WriteConfig(AccToken, RefToken, Expires_at)

    return AccToken, RefToken, Expires_at
