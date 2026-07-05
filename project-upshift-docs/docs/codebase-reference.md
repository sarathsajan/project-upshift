# Codebase reference

This page provides a central place to document the Python modules and supporting files used by the trading bot.

## Current modules
- login.py: handles authentication, TOTP generation, and portfolio holdings retrieval.
- env_vars.py: stores runtime configuration values such as client identifiers and broker credentials.

## Secret and environment files
- Environment and secret files should be documented by purpose, scope, and expected usage.
- Their actual values must remain hidden from the documentation.
- When new configuration files are introduced, add a short entry here describing what they contain and how the bot uses them.

## Configuration guidance
- Keep sensitive values in local environment variables or secure secret storage instead of committing them to the repository.
- Document the purpose of each configuration setting here, but do not include the actual secret values in the documentation.
- When new modules are added, add a short summary here with their role, input/output expectations, and any associated configuration.

## Planned additions
As the project grows, the following areas should be documented here:
- order execution logic
- database storage and logging
- monitoring and alerting
- risk controls and emergency shutdown logic
