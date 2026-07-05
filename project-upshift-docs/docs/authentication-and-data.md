# Authentication and data retrieval

This section captures the login and data collection flow for the bot.

## Relevant code
The authentication workflow is documented here and summarized in [Codebase reference](codebase-reference.md).

## Configuration notes
- The authentication flow depends on values stored in the project codebase, especially the environment configuration module used by the bot.
- These values include identifiers and credentials required for the broker session.
- The documentation should describe their purpose and usage, but the actual secret values should never be exposed.

## Function explanations
### get_totp(secret)
This function generates a time-based one-time password (TOTP) from the shared secret. It is called before authentication so the broker can verify the login attempt.

### print_holdings_summary(holdings_list)
This function formats and prints the portfolio data returned by the broker. It shows each stock's average purchase price, current price, quantity, and total value. It also decides whether the position should be treated as a buy or sell signal based on the current price versus the average price.

### main()
This is the entry point of the script. It creates the 5paisa client, logs in with the TOTP and PIN, fetches the holdings, and then prints the holdings summary.

## Code explanation
1. The script imports the 5paisa client library, the TOTP helper, and the credentials stored in the environment configuration file.
2. The get_totp function creates a fresh TOTP code that is valid for a short window, which is required for secure broker authentication.
3. The main function initializes the client and calls get_totp_session with the client code, the generated TOTP, and the PIN.
4. Once the session is established, the script fetches the portfolio holdings and passes them to the summary function.
5. The summary function prints a structured view of each holding so the bot can inspect the portfolio before making trading decisions.

## Planned work
- Authenticate and authorize with the 5paisa APIs.
- Retrieve the latest ticker data for the instruments being monitored.
- Prepare the market data needed for decision-making.
