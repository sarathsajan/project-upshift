# Project Upshift

## Objective

In this project we will create a trading bot using the 5paisa APIs.

### Execution steps

- **Phase 1: Setup & Validation**
  - [Mar 2027, planned] File availability and database integrity check
- **Phase 2: Authentication & Data Retrieval**
  - [Jul 2026, in progress] Authenticate and authorise
  - [Aug 2026, planned] Fetch latest ticker data
- **Phase 3: Order Management**
  - [Sep 2026, planned] Check and cancel stale BUY orders
  - [Oct 2026, planned] Check and modify trailing stop-loss prices of active SELL orders
  - [Nov 2026, planned] Place new BUY orders
  - [Dec 2026, planned] Place new SELL orders
- **Phase 4: Operations & Monitoring**
  - [Jan 2027, planned] SQLite database for tracking all the executed operations and logs
  - [Feb 2027, planned] Panic button or kill-switch

### Strategy / Planned logic

DCA STRATEGY FLOW

```text
================= INITIALISE =================
FETCH list of stocks to consider (price greater than INR 500)
FETCH details of current stock holdings
FETCH details of active SELL orders


============= MODIFY SELL ORDER =============
FOR EACH active SELL order in list
    FETCH active SELL order details (stop loss + limit price)
    FETCH current price of stock
    IF current price GREATER THAN limit price * 0.98
        SET cancel active SELL order
        SET SELL all units at limit price at +3% of current price with stop loss at -1% of current price


=============== NEW SELL ORDER ===============
FOR EACH stock IN list
    IF stock IN holdings
        FETCH avg price of stock
        FETCH current price of stock
        IF current price GREATER THAN avg price
            LET profit percent = 5% = 1.05
            IF current price GREATER THAN (avg price * profit percent)
                SET SELL all units at limit price at +3% of current price with stop loss at -1% of current price


================= BUY ORDER =================
FOR EACH stock in list
    IF stock NOT IN holdings
        FETCH 20D avg
        FETCH 5D avg
        IF 5D avg LESS THAN 20D avg
            SET BUY 1 unit of stock at market price
    IF stock IN holdings
        FETCH avg price of stock
        FETCH current price of stock
        IF current price LESS THAN OR EQUAL TO avg price
            SET BUY 1 unit of stock at market price
```
