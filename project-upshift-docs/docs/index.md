# Project Upshift

This page serves as the main entry point for the end-to-end documentation for the Project Upshift trading bot.

## Objective
The project aims to build an automated trading bot that uses the 5paisa APIs to monitor markets, evaluate strategy conditions, and place orders.

## Documentation sections
- [Setup and validation](setup-and-validation.md)
- [Authentication and data retrieval](authentication-and-data.md)
- [Order management](order-management.md)
- [Operations and monitoring](operations-and-monitoring.md)
- [Strategy](strategy.md)
- [Codebase reference](codebase-reference.md)

## Project phases
### Phase 1: Setup and validation
- Verify file availability.
- Check database integrity.

### Phase 2: Authentication and data retrieval
- Authenticate and authorize with the broker API.
- Fetch the latest ticker data.

### Phase 3: Order management
- Review and cancel stale buy orders.
- Adjust trailing stop-loss levels on active sell orders.
- Place new buy and sell orders.

### Phase 4: Operations and monitoring
- Track executed operations and logs in SQLite.
- Provide a panic button or kill-switch for emergency control.

## Strategy summary
The strategy evaluates a set of stocks above a minimum price threshold, checks current holdings and active sell orders, and then decides whether to hold, sell, or buy based on price trends and profit conditions.
