# docs_order_tracking_order_book.md

## Overview
This script retrieves the current order book from the authenticated 5Paisa client. It helps track the orders that are currently active, pending, or recently processed.

In the broader trading solution, this module is important for monitoring order state and supporting later actions such as cancellation, modification, or risk management.

## Purpose in the Solution
- Fetch the current order book from the broker account.
- Display order-related data in a structured format.
- Support monitoring of active trading activity.

## User-Defined Functions

### `fetch_order_book()`
- Creates an authenticated client using the shared authentication logic.
- Calls the `order_book()` method on the client.
- Prints the returned order book data in a readable and structured way.

## Operational Flow
1. The script imports the authentication helper.
2. `fetch_order_book()` obtains an authenticated broker client.
3. The client requests the order book from 5Paisa.
4. The returned order-book data is printed for review.

## Notes
- This script is focused on observation and monitoring.
- It does not currently perform actions such as canceling or modifying orders.
