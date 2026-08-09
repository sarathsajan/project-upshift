# Project Upshift

Project Upshift is a Python-based Upstox API integration workspace for research, API prototyping, and trading workflow exploration. The repository currently contains a set of standalone examples that fetch profile and account information, read holdings, inspect brokerage charges, download exchange instrument metadata, read market LTP data, and submit a V3 order payload.

## What the project does

The repository is organized around the Upstox Python SDK and is designed to help developers understand how broker API concepts map into script-driven workflows.

The current implementation covers these practical areas:

- Reading credentials from a local configuration file.
- Retrieving account and user profile context through the SDK.
- Loading market quote examples such as last traded price retrieval.
- Pulling holdings and brokerage-related API examples.
- Downloading instrument metadata and performing simple search logic over the result data.
- Demonstrating the contract for a live order request using Upstox V3 APIs.
- Running a domain-oriented alert-bot workflow that evaluates holdings and emits buy, sell, or hold signals.

## Why the project is useful

This repository is useful for developers and researchers who want to:

- Understand how common account and market APIs are represented in the Upstox SDK.
- Experiment with a domain-driven project layout that separates examples by business concern.
- Prototype rule-based trading concepts around holdings, price thresholds, and order intent.
- Extend the current research code into a more structured strategy or automation engine.

The workspace is intentionally small and modular. Each folder acts as a functional area that can be extended independently:

- [orders/place_order.py](orders/place_order.py) demonstrates creating an Upstox V3 order request
- [market/get_ltp_quotes.py](market/get_ltp_quotes.py) fetches last-traded-price market data
- [user/get_profile.py](user/get_profile.py) and [user/get_fund_and_margin.py](user/get_fund_and_margin.py) read account context
- [portfolio/get_holdings.py](portfolio/get_holdings.py) reads broker portfolio holdings
- [charges/brokerage_details.py](charges/brokerage_details.py) demonstrates brokerage calculation access
- [instruments/get_instrument_info.py](instruments/get_instrument_info.py) downloads and searches instrument metadata

## Current status

This repository is best understood as a research implementation and planning workspace.

Current status highlights:

- Upstox integration is active and the SDK dependency is present.
- API access examples are present as scripts rather than a packaged service.
- A DCA-style trading strategy is noted in [roadmap.md](roadmap.md).
- The code is suitable for discovery and prototyping, but it is not a production-ready trading engine.
- The workspace should be treated as a proof-of-concept and not as financial advice.

## Project structure

```text
project-upshift/
├── env.json                     # runtime credentials and tokens
├── requirements.txt             # Python dependency manifest
├── roadmap.md                   # high-level execution plan
├── dev_log.txt                  # development notes and research journal
├── alert-bot/                   # alert-style bot logic and supporting credentials
├── charges/                     # brokerage examples
├── instruments/                 # complete instrument data download and search helpers
├── market/                      # market quote examples
├── orders/                      # order request examples
├── portfolio/                   # portfolio APIs and holdings examples
└── user/                        # login, profile, margin, and logout examples
```

## Getting started

### Prerequisites

Before using the repository, make sure you have:

- Python 3.11 or a compatible Python 3.x runtime.
- An Upstox developer account and access token.
- A local [env.json](env.json) file containing the required token values.
- Internet access for broker APIs and instrument data retrieval.
- A configured environment in which the API contract can be exercised safely.

### Install dependencies

The project uses the Upstox SDK and a small set of runtime packages. Install dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

The current direct dependencies are listed in [requirements.txt](requirements.txt):

```text
PyOTP==2.10.0
upstox-python-sdk==2.28.0
tzdata==2026.3
```

### Configure credentials

Create or update [env.json](env.json) with the token values expected by the credential helpers:

```json
{
  "UPSTOX_ACCESS_TOKEN": "<your-access-token>",
  "UPSTOX_ACCESS_TOKEN_SANDBOX": "<optional-sandbox-token>"
}
```

The credential helpers in each domain folder read the same shared file through a relative working-directory path. That means the scripts are expected to run from the relevant folder context and keep code and configuration aligned with that directory layout.

### Example usage

From the project root, a typical flow looks like this:

```bash
cd user
python get_profile.py
```

For market LTP reading:

```bash
cd market
python get_ltp_quotes.py
```

For order placement:

```bash
cd orders
python place_order.py
```

The scripts rely on Upstox Python SDK classes such as `OrderApiV3`, `MarketQuoteV3Api`, `UserApi`, `PortfolioApi`, and `ChargeApi`.

## Operational notes

### Account and network behavior

The APIs in this repository expect a real Upstox account context and a valid access token. In practice, login, OTP, developer dashboard generation, and static IP registration are part of the workflow described in [dev_log.txt](dev_log.txt), so the scripts should be treated as examples that require broker-side setup.

### Safety and research warning

This repository is not a machine-driven order-execution engine yet. The scripts can trigger real broker interactions if the credentials and runtime environment are configured. Do not run the order or alert logic in a production or paper-trading context without validating the contract, risk controls, and expected API responses.

## Where to get help

Useful reference points for this project are:

- [roadmap.md](roadmap.md) for milestones and trade-bot phases.
- [dev_log.txt](dev_log.txt) for historical notes and design decisions.
- The Upstox Python SDK examples that correspond to the API contract being used.
- The Upstox developer documentation for protocol, static IP, and account requirements.

For implementation questions or feature discussions, open an issue in the repository and include the script name, expected input, and API response details when possible.

## Maintainers and contributing

This repository is currently maintained as an open development workspace. Contributions are welcome in the form of:

- Bug fixes and examples that improve script correctness.
- Documentation updates that clarify setup or broker workflows.
- New API wrappers or strategy modules that fit the current project structure.

Before opening or reviewing a change, please keep the code aligned with the existing folder structure and the Python dependency manifest in [requirements.txt](requirements.txt).

> Note: This repository is a research and proof-of-concept project. It is not intended as financial advice and should not be used for production trading without security, risk, and validation review.

