from datetime import datetime
from py5paisa import FivePaisaClient
from env_vars import cred, fivepaidsa_client_code, fivepaisa_acc_pin, fivepaisa_totp_secret
import pyotp
import os


def get_totp(secret: str) -> str:
    """Generate a TOTP code from the shared secret.

    The generated code is used as a second-factor login value for 5paisa.
    """
    totp = pyotp.TOTP(secret)
    code = totp.now()
    print(f"totp : {code} generated at {datetime.now().strftime('%H:%M:%S')}, valid for 30 seconds")
    return code


def get_authenticated_client() -> None:
    """Create authenticated 5paisa client to communicate with 5paisa APIs"""
    os.system("clear")
    client = FivePaisaClient(cred=cred)
    client.get_totp_session(fivepaidsa_client_code, get_totp(fivepaisa_totp_secret), fivepaisa_acc_pin)
    return client


def main():
    get_authenticated_client()


if __name__ == "__main__":
    main()
