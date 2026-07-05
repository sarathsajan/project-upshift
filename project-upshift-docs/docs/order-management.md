# Order management

This section describes the logic for creating and adjusting trading orders.

## Code and configuration notes
- Future order execution logic should be added as new Python modules in the codebase directory.
- Any new configuration required for order management should be documented in [Codebase reference](codebase-reference.md).
- Secrets and environment values must be described conceptually, without exposing the actual values.

## Planned work
- Review and cancel stale buy orders when needed.
- Update the trailing stop-loss details on active sell orders.
- Place new buy orders and sell orders based on the strategy rules.
