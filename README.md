# Lifestyle Cost Calculator

This is a Streamlit application that helps you determine the income needed for your dream life in different countries. The app calculates the required monthly and annual income based on various expenses and financial goals.

## Features

- Calculate required income for different countries: USA, Netherlands, South Africa, and South Korea.
- Input sections for housing costs, vehicle expenses, daily expenses, financial goals, and other expenses.
- Real-time updates of required income and expense breakdown.
- Visual representation of monthly expenses using pie charts.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/repl-nix-dreamlifecalculator.git
    cd repl-nix-dreamlifecalculator
    ```

2. Install Poetry if you haven't already:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

4. Activate the virtual environment:
    ```sh
    poetry shell
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run main.py
    ```

2. Open your web browser and go to the URL provided in the terminal output (usually `http://localhost:5000`).

## Configuration

The app is configured to run in headless mode on `0.0.0.0` and port `5000`. You can change these settings in the [config.toml](http://_vscodecontentref_/0) file.

```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000
