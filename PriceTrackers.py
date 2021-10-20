"""
Contains objects to track prices and write to price databases. Core methods and structure contained in abstract class 'GenericTracker'
Creation Date:      10/19/21
Modify Date:        10/19/21

TO-DO:
    1. database R/W methods, either more substantial SQL-like query params or simple high-level protocol
    2. non-abstract continuous write methods
    3. instantiation using BTC to USD metrics

TO-CONSIDER:
    1. should 'DatabaseReader' and 'DatabaseWriter' be low-level objects? Or too much to keep track of?
"""
from abc import ABC, abstractmethod
from threading import Thread
import numpy as np

# abstract tracker class, with abstract methods for DB writes and update functions
class GenericTracker(ABC):
    """
    Class:      GenericTracker    
    --------------------------------
    Abstract baseclass for tracking pricing and finance metrics of given currency. Operates in active write or full online mode (only most recent metric kept)
    """
    def __init__(self, db_name: str, active_write: bool) -> None:
        # store internal database name
        self.db_name = db_name
        # if tracker is initialized to active write, dispatch threads using generator
        if active_write:
            self.init_dbwrite()

    def init_dbwrite(self) -> None:
        """
        Function:   init_dbwrite    
        --------------------------------
        Dispatches threads to perform continuous DB writes using abstract method 'continuous_write'
        Returns:    None
        """
        self.writethread = Thread(target=self.continuous_write)
        self.writethread.start()

    # should probably be rewritten in some non-abstract way calling subfunctions, most of this code will be reusable
    @abstractmethod
    def continuous_write(self) -> None:
        """
        Function:   continuous_write
        --------------------------------
        Performs continuous database writes at some user-defined interval
        Returns:    None
        """
        pass

    @abstractmethod
    def get_current_metrics(self) -> np.ndarray:
        """
        Function:   get_current_metrics
        --------------------------------
        Returns current price metrics
        Returns:    current_stats
        """
        pass
