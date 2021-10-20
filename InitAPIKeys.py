"""
Import this file to initialize your API keys for the Binance API and define functions to use later

To export environment variables on your local machine, use this syntax:
    VAR_NAME="value"

Creation Date:      10/19/21
Modify Date:        10/19/21
"""
import os

# imports environment variables from local machine
MY_API_USERNAME = os.environ.get("BINANCE_USER")
MY_API_KEY = os.environ.get("BINANCE_KEY")

def binance_api_user() -> str:
    """
    Function:   binance_api_user
    --------------------------------
    Provides stored environment variable with Binance API username
    Returns:    username (str)
    """
    return MY_API_USERNAME

def binance_api_key() -> str:
    """
    Function:   continuous_write
    --------------------------------
    Provides stored environment variable with Binance API key
    Returns:    key (str)
    """
    return MY_API_KEY
