from py5paisa import FivePaisaClient
from env_vars import *
import pprint

Client = FivePaisaClient(cred=cred)
Client.get_totp_session(client_code, totp, pin)
pprint.pprint(vars(Client))