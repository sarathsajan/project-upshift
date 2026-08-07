# Project Upshift

A research-oriented Upstox API automation workspace for building a trading workflow around market data, holdings, user profile information, brokerage checks, and order placement.

## What the project does

Project Upshift is an exploratory Python project that connects to the Upstox SDK and uses broker API examples to test and prototype a trading system. The current workspace is organized around a collection of broker integration scripts rather than a finished trading engine.

The repository currently covers these practical areas:

- reading credentials from a local JSON configuration file
- retrieving user and account context through the Upstox SDK
- fetching market information such as current LTP and instrument reference data
- loading portfolio and brokerage-related API examples
- placing a V3 order request against the Upstox API contract

## Why the project is useful

This project is useful for developers and researchers who are:

- learning how Upstox Python SDK examples map to REST-style broker workflows
- prototyping rule-based trading logic around buy, sell, and stop-loss ideas
- exploring a directory-driven layout that separates API access by domain
- turning a proof-of-concept trading strategy into a more maintainable codebase

The repository is intentionally small and modular. Each directory is a functional area that can be extended independently:

- [orders/place_order.py](orders/place_order.py) demonstrates creating an Upstox V3 order request
- [market/get_ltp_quotes.py](market/get_ltp_quotes.py) fetches last-traded-price market data
- [user/get_profile.py](user/get_profile.py) and [user/get_fund_and_margin.py](user/get_fund_and_margin.py) read account context
- [portfolio/get_holdings.py](portfolio/get_holdings.py) reads broker portfolio holdings
- [charges/brokerage_details.py](charges/brokerage_details.py) demonstrates brokerage calculation access
- [instruments/get_instrument_info.py](instruments/get_instrument_info.py) downloads and searches instrument metadata

## Current status

This repository is best understood as an implementation sandbox and planning workspace:

- Upstox integration is active and the SDK dependency is present
- Data access and order examples are present as scripts
- A DCA-style trading strategy is described in [roadmap.md](roadmap.md)
- The project is not a production-ready trading engine and should not be treated as financial advice

## Getting started

### Prerequisites

Before using the repository, make sure you have:

- Python 3.11 or a compatible Python 3.x runtime
- an Upstox developer account and access token
- a local [env.json](env.json) file containing the required token values
- internet access for broker API and instrument data calls

### Install dependencies

Install the Python requirements from the repository root:

```bash
python -m pip install -r requirements.txt
```

The current direct dependencies are listed in [requirements.txt](requirements.txt):

```text
PyOTP==2.10.0
upstox-python-sdk==2.28.0
```

### Configure credentials

Create or update [env.json](env.json) with the token values expected by the credential loaders:

```json
{
  "UPSTOX_ACCESS_TOKEN": "<your-access-token>",
  "UPSTOX_ACCESS_TOKEN_SANDBOX": "<optional-sandbox-token>"
}
```

Each read helper reads the same file using a path relative to the current working directory. Because the scripts are standalone examples, they are usually run from within their own folder.

### Example usage

To try the order example from the project root:

```bash
cd orders
python place_order.py
```

If you want to inspect market quotes:

```bash
cd market
python get_ltp_quotes.py
```

The scripts rely on the Upstox Python SDK classes, such as `OrderApiV3`, `MarketQuoteV3Api`, `UserApi`, and `PortfolioApi`.

## Project layout

```text
project-upshift/
├── env.json                   # runtime credentials and tokens
├── requirements.txt           # Python dependency manifest
├── roadmap.md                 # high-level execution plan
├── dev_log.txt                # development notes and research journal
├── charges/                   # brokerage examples
├── instruments/               # complete instrument data download and search helpers
├── market/                    # market quote examples
├── orders/                    # order request examples
├── portfolio/                 # portfolio APIs and holdings examples
└── user/                      # login, profile, margin, and logout examples
```

## Where to get help

Useful reference points for this project are:

- [roadmap.md](roadmap.md) for milestones and trade-bot phases
- [dev_log.txt](dev_log.txt) for historical notes and design decisions
- the Upstox Python SDK examples that correspond to the API contract being used
- the Upstox developer documentation for protocol and account requirements

For implementation questions or feature discussions, open an issue in the repository and include the script name, expected input, and API response details when possible.

## Maintainers and contributing

This repository is currently maintained as an open development workspace. Contributions are welcome in the form of:

- bug fixes and examples that improve script correctness
- documentation updates that clarify setup or broker workflows
- new API wrappers or strategy modules that fit the current project structure

Before opening or reviewing a change, please keep the code aligned with the existing folder structure and the Python dependency manifest in [requirements.txt](requirements.txt).

> Note: This repository is a research and proof-of-concept project. It is not intended as financial advice and should not be used for production trading without security, risk, and validation review.

