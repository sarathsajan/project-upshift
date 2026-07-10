# docs_user_authentication.md

## Overview
This script handles authentication for the 5Paisa trading API. It generates a time-based one-time password (TOTP) from a shared secret and uses it to create an authenticated client session that other modules can reuse.

In the broader solution, this module is the gateway to the broker API. Without a valid authenticated client, the portfolio, order-book, and order-placement scripts cannot communicate with 5Paisa.

## Purpose in the Solution
- Securely authenticate the application with 5Paisa.
- Generate a fresh TOTP code every time authentication is requested.
- Return a ready-to-use client object for downstream trading operations.

## User-Defined Functions

### `get_totp(secret: str) -> str`
- Generates a TOTP using the provided secret.
- Uses the `pyotp` library to create a current code value.
- Prints the generated code and the current timestamp for debugging and operational visibility.
- Returns the TOTP string that is used during login.

### `get_authenticated_client() -> None`
- Clears the terminal screen before authentication.
- Creates a `FivePaisaClient` instance using credentials from the environment configuration module.
- Calls the `get_totp_session` method with the client code, a generated TOTP, and the account PIN.
- Returns the authenticated client instance for use by other scripts.

### `main()`
- Serves as the entry point for the script.
- Calls `get_authenticated_client()` when the file is executed directly.

## Operational Flow
1. The script imports the required credentials and authentication helpers.
2. When executed, `main()` calls `get_authenticated_client()`.
3. `get_authenticated_client()` requests a fresh TOTP from `get_totp()`.
4. The generated TOTP is sent to the 5Paisa authentication flow.
5. Once authentication is successful, the authenticated client object is available for other modules to use.

## Notes
- The script depends on the credential values stored in the environment configuration module.
- The TOTP is time-sensitive and must be generated close to the authentication request time.
