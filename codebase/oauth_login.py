'''
5paisa API documentation
    https://xstream.5paisa.com
    https://xstream.5paisa.com/dev-docs/user-authentication-system/oauth-login



OAuth Login [POST] [JSON]
The OAuth mechanism enables a secure and seamless customer login flow on the
partner's platform using 5paisa's Open APIs. When a customer initiates login
from the partner's web or mobile app, they are redirected to the official
5paisa login page to authenticate using their demat account credentials.

After successful login, the customer is redirected back to the partner's
platform via a predefined callback URL. This flow ensures that authentication 
is handled securely by 5paisa while allowing the partner platform authorized 
access to the customer's data as per the granted permissions.

The login flow starts from navigating to public Xstream login endpoint.
A successful login comes with a RequestToken as a URL query parameter to 
redirect the URL registered for that API key.

After successful login, user will be redirected to the callback URL provided by 
the partner/user.


Request Token URL
https://dev-openapi.5paisa.com/WebVendorLogin/VLogin/Index?VendorKey=<Your Vendor Key>&ResponseURL=<Redirect URL>&State=<Pass reference value if needed>


PARAMETERS      DESCRIPTION
ResponseURL     The callback URL where partner wants to redirect customer after 
                successful login through OAuth.
VendorKey       The API key of the partner provided by 5pasia along with other 
                API credentials. Partner can use the key provided to them or 
                User can use his own User Key.
State           This is the redirection params, which is passed to the response 
                URL on successful login.
                
Note:
Partner has to redirect customer to the URL mentioned above and along with it 
pass parameters listed below through POST method. This login has been updated 
as per the SEBI regulations of 2-factor authentication. It is based on client 
code, PIN and a real-time OTP/TOTP.


After successful login, user will be redirected to the callback URL provided by 
the user and user will receive following parameters as URL Params. The Request 
Token returned on successful login is valid for 60 min only. This token is to be
used to call fetch Access token which can be used for sending request through 
all other Open APIs.

PARAMETERS      DESCRIPTION
State Params    State Variables to be send on response URL as URI params.
RequestToken    Request Token which can be used to obtain access token.
'''

import requests

# this section handles the construction of login url

VENDOR_KEY = ""
CALLBACK_URL = ""
STATE_OPTIONAL = "" # a random value for security
OAUTH_LOGIN_URL = f"https://dev-openapi.5paisa.com/WebVendorLogin/VLogin/Index?VendorKey={VENDOR_KEY}&ResponseURL={CALLBACK_URL}&State={STATE_OPTIONAL}"

# this section handles the login process (sending request + callback handler)