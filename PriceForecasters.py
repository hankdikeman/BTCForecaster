"""
Contains objects to forecast future trends by predicting the suitability of a buy/sell order. Core methods and structure contained in abstract class 'GenericForecaster'
Creation Date:      10/19/21
Modify Date:        10/19/21

TO-DO:
    1. abstract inference methods, returns favorability of a buy/sell
    2. basic sample forecaster, simple trend following (SheepTracker 🐑)
    3. decide on modelling framework (sklearn, pytorch, general?)
"""
from abc import ABC, abstractmethod
import numpy as np

# abstract tracker class, with abstract methods for DB writes and update functions
class GenericForecaster(ABC):
    """
    Class:      GenericForecaster    
    --------------------------------
    Abstract baseclass for making real-time trading decisions using trained models and recent price trends
    """
    def __init__() -> None:
        pass
