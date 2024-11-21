import requests
import json
import os
from rich import print

def Scheduler():
    
    ReadyQueue = []
    WaitingQueue = []
    FinishedQueue = []
    Running = []
    
    