# docs_portfolio_management_holdings.md

## Overview
This script retrieves the current portfolio holdings from the authenticated 5Paisa client. It is used to inspect the assets currently held by the user.

In the broader solution, this module provides portfolio visibility, which is important for monitoring account status and deciding whether to place or modify orders.

## Purpose in the Solution
- Fetch the current holdings from the broker account.
- Display the number of assets in the portfolio.
- Print each holding in a readable format for manual review or further automation.

## User-Defined Functions

### `fetch_holdings()`
- Calls `get_authenticated_client()` to obtain a valid broker session.
- Sends a request to the broker API to fetch holdings using `client.holdings()`.
- If no holdings are found, it prints a message indicating that the portfolio is empty.
- If holdings exist, it prints the count and then prints each item with formatted output.

## Operational Flow
1. The script imports the authentication helper.
2. `fetch_holdings()` creates an authenticated client.
3. The client requests the user's holdings from 5Paisa.
4. The returned holdings list is checked for emptiness.
5. If holdings exist, they are printed one by one for inspection.

## Notes
- This script is read-only and does not place or modify orders.
- It is intended as a portfolio inspection utility for the trading workflow.
