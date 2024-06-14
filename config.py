__docformat__ = 'google'
from os import environ, path, getenv, getcwd
import pytz
from dotenv import load_dotenv
import datetime as dt
from ortools.constraint_solver import routing_enums_pb2
import diskcache
import sys

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, '.env'))

cache = diskcache.Cache('./cache')

OSRM_HOST = getenv('OSRM_HOST')
OSRM_PORT = getenv('OSRM_PORT')


OSRM_TAG = "tennessee-extended-prod-amd64"
EARLYARRIVAL_WINDOW = 4
LATEARRIVAL_WINDOW = 2

"""
VRP solver: time window for carta in seconds.
"""
DEPOT = "MetMin"
DEPOT_ADDRESS = "1617 Wilcox Blvd, Chattanooga, Tennessee, 37406, United States"
DEPOT_LON = -85.269
"""
VRP solver: longitude of depot location
"""
DEPOT_LAT = 35.057
"""
VRP solver: latitude of depot location
"""
DWELL_TIME = 300 
"""
VRP solver: vehicle dwell time, how long we plan for a vehicle staying at a location to pickup/dropoff passenger
in seconds.
"""
MAX_VEHICLE_SLACK = 90000
"""
VRP solver: maximum amount of time a vehicle can wait at a location before it can service the location in seconds.
"""
OBJECTIVE_IS_DISTANCE = True
#FIRST_SOLUTION_STRATEGY = routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION
#FIRST_SOLUTION_STRATEGY = routing_enums_pb2.FirstSolutionStrategy.BEST_INSERTION
FIRST_SOLUTION_STRATEGY = routing_enums_pb2.FirstSolutionStrategy.AUTOMATIC
"""
VRP solver: VRP first solution strategy.
"""
#LOCAL_SEARCH_METAHEURISTIC = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
LOCAL_SEARCH_METAHEURISTIC = routing_enums_pb2.LocalSearchMetaheuristic.AUTOMATIC
"""
VRP solver: VRP search heuristic.
"""
VRP_TIME_LIMIT = 300
#VRP_TIME_LIMIT = 180
"""
VRP solver: cutoff time for VRP solver.
"""
LOG_SEARCH = False
DAY_END_TIME = 90000

# OSRM
OSRM_NCORES = 4
OSRM_FALLBACK_TIME = 90000
OSRM_PARALLEL = True
