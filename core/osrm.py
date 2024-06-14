__docformat__ = "google"
"""
Package: core/osrm.py - this package contains the functionality related to working with the OSRM server.
An OSRM server should be running on the host specified at core/config/OSRM_HOST and port specified in
core/config/OSRM_PORT. To get an OSRM server up and running for this project see the osrmserver/ directory.
"""
import requests
from copy import deepcopy
import math
import traceback
import pandas as pd
import datetime as dt
from shapely.geometry import LineString
import config as config

def request_travel_time_matrix(all_pts, return_response=False, source_index=None):
    """
    This function will take a list of points, where each point is of the form {'lon': float, 'lat': float}
    and will generate a travel time matrix. If return_response is True then also returns the json of the response
    from the OSRM get call.

    Args:
        all_pts: (list[dict]) list of points, where each point is of the form {'lon': float, 'lat': float}
        return_response: (bool) if return_response is True then also returns the json of the response
            from the OSRM get call
    Returns:
        list[list[int]]
    Raises:
        (ValueError) there is a null value in all_pts.
        (KeyError) if 'durations' is not in the JSON response from the API call to OSRM.
    """
    for x in all_pts:
        if pd.isna(x['lon']) or pd.isna(x['lat']):
            raise ValueError(f"error in core.optimizer.request_travel_time_matrix: there is a null lon or lat in input. all_pts={all_pts}")
    source_pts_str = ";".join([f"{x['lon']},{x['lat']}" for x in all_pts])
    if source_index is None:
        url = f"http://{config.OSRM_HOST}:{config.OSRM_PORT}/table/v1/driving/{source_pts_str}?fallback_speed=5"
    else:
        url = f"http://{config.OSRM_HOST}:{config.OSRM_PORT}/table/v1/driving/{source_pts_str}?sources={source_index}&fallback_speed=5"
    res = requests.get(url)
    r = res.json()
    try:
        time_matrix_float = r['durations']
    except:
        raise KeyError(f"error in core.optimizer.request_travel_time_matrix: durations is not in response, the code for the response is {r['code']}")
    time_matrix = []
    for row in time_matrix_float:
        temp = [math.ceil(x) for x in row]
        time_matrix.append(temp)
    if return_response:
        return time_matrix, r
    else:
        return time_matrix


def request_distance_matrix(all_pts, return_response=False):
    """
    This function will take a list of points, where each point is of the form {'lon': float, 'lat': float}
    and will generate a distance matrix. If return_response is True then also returns the json of the response
    from the OSRM get call.

    Args:
        all_pts: (list[dict]) list of points, where each point is of the form {'lon': float, 'lat': float}
        return_response: (bool) if return_response is True then also returns the json of the response
            from the OSRM get call
    Returns:
        list[list[int]]
    Raises:
        (ValueError) there is a null value in all_pts.
        (KeyError) if 'durations' is not in the JSON response from the API call to OSRM.
    """
    for x in all_pts:
        if pd.isna(x['lon']) or pd.isna(x['lat']):
            raise ValueError(f"error in core.optimizer.request_travel_time_matrix: there is a null lon or lat in input. all_pts={all_pts}")
    source_pts_str = ";".join([f"{x['lon']},{x['lat']}" for x in all_pts])
    url = f"http://{config.OSRM_HOST}:{config.OSRM_PORT}/table/v1/driving/{source_pts_str}?fallback_speed=5"
    payload = {'annotations': "distance"}
    res = requests.get(url, params=payload)
    r = res.json()
    try:
        time_matrix_float = r['distances']
    except:
        raise KeyError(f"error in core.optimizer.request_travel_time_matrix: durations is not in response, the code for the response is {r['code']}")
    time_matrix = []
    for row in time_matrix_float:
        temp = [math.ceil(x) for x in row]
        time_matrix.append(temp)
    if return_response:
        return time_matrix, r
    else:
        return time_matrix
    
    
def request_travel_time_row(all_pts, return_response=False):
    r = [0]
    for i in range(len(all_pts)-1):
        temp = deepcopy(r[-1]) + request_travel_time(all_pts[i], all_pts[i+1])
        r.append(deepcopy(temp))
    return r


def request_travel_time(source_pt, target_pt):
    """
    This function will get the travel time between source_pt and target_pt where source_pt and target_pt are of the
    form {'lat': float, 'lon': float}.

    Examples:
        r = request_travel_time({'lat': 35.121, 'lon': -85.6329}, {'lat': 36.134, 'lon': -86.926})

    Args:
        source_pt: (dict) of the form {'lat': float, 'lon': float}
        target_pt: (dict) of the form {'lat': float, 'lon': float}
    Returns:
        float
    Raises:
        TODO
    """
    if source_pt == target_pt:
        return 0
    url = f"http://{config.OSRM_HOST}:{config.OSRM_PORT}/route/v1/driving/{source_pt['lon']},{source_pt['lat']};{target_pt['lon']},{target_pt['lat']}"
    try:
        res = requests.get(url)
        r = res.json()
    except Exception as e:
        return config.OSRM_FALLBACK_TIME
    if r['code'] == "Ok":
        durations = [int(math.ceil(x['duration'])) for x in r['routes']]
        return min(durations)
    else:
        return config.OSRM_FALLBACK_TIME


def request_travel_distance(source_pt, target_pt):
    """
    This function will get the travel time between source_pt and target_pt where source_pt and target_pt are of the
    form {'lat': float, 'lon': float}.

    Examples:
        r = request_travel_time({'lat': 35.121, 'lon': -85.6329}, {'lat': 36.134, 'lon': -86.926})

    Args:
        source_pt: (dict) of the form {'lat': float, 'lon': float}
        target_pt: (dict) of the form {'lat': float, 'lon': float}
    Returns:
        float
    Raises:
        TODO
    """
    if source_pt == target_pt:
        return 0
    url = f"http://{config.OSRM_HOST}:{config.OSRM_PORT}/route/v1/driving/{source_pt['lon']},{source_pt['lat']};{target_pt['lon']},{target_pt['lat']}"
    try:
        res = requests.get(url)
        r = res.json()
    except Exception as e:
        return config.OSRM_FALLBACK_TIME
    if r['code'] == "Ok":
        durations = [int(x['distance']) for x in r['routes']]
        return min(durations)
    else:
        return config.OSRM_FALLBACK_TIME


def reverse_geocode(pt):
    url = f"http://{config.OSRM_HOST}:{config.OSRM_PORT}/nearest/v1/driving/{pt['lon']},{pt['lat']}?number=1"
    try:
        res = requests.get(url)
        r = res.json()
        result = r['waypoints'][0]['name'] + ", Chattanooga, TN"
    except:
        result = "no address found"
    return result


def interperolate_location_between_points(source_pt, target_pt, time_to_target):
    url = f"http://{config.OSRM_HOST}:{config.OSRM_PORT}/route/v1/driving/{source_pt['lon']},{source_pt['lat']};{target_pt['lon']},{target_pt['lat']}?geometries=geojson&overview=full"
    try:
        res = requests.post(url)
        r = res.json()
        line = LineString(r['routes'][0]['geometry']['coordinates'])
        total_duration = r['routes'][0]['duration']
    except:
        return target_pt
    if time_to_target >= total_duration:
        return source_pt

    else:
        # TODO - account for new if/else for end of trip
        if total_duration == 0:
                percent_of_trip_completed = 1
        else:
            percent_of_trip_completed = 1 - (time_to_target / total_duration)
        point = line.interpolate(percent_of_trip_completed, normalized=True)
        return {'lat': point.y, 'lon': point.x}


def get_route_details(source_pt, target_pt):
    """
    Gets List of route points along with distance and duration based on two points
    Args:
        source_pt:
        target_pt:

    Returns:

    """
    url = f"http://{config.OSRM_HOST}:{config.OSRM_PORT}/route/v1/driving/{source_pt['lon']},{source_pt['lat']};{target_pt['lon']},{target_pt['lat']}?geometries=geojson&overview=full"
    try:
        res = requests.get(url)
        r = res.json()
        line = r['routes'][0]['geometry']['coordinates']
        total_duration = r['routes'][0]['duration']
        total_distance = r['routes'][0]['distance']
        return line, total_distance, total_duration
    except:
        return target_pt, 0, 0

