import math
import time
from pymavlink import mavutil

# Arm the Drone
def arm(conn):
    print("-- Arming")

    conn.mav.command_long_send(conn.target_system, conn.target_component,
                               mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
    
    ack(conn, "COMMAND_ACK")

# Takeoff the Drone
def takeoff(conn, altitude=50):
    print("-- Takeoff Initiated")

    conn.mav.command_long_send(conn.target_system, conn.target_component,
                               mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, math.nan, 0, 0, altitude)
    
    ack(conn, "COMMAND_ACK")

# Upload teh mission items to the drone
def upload_mission(conn, waypoints):
    n = len(waypoints)
    print("-- Sending Mission Count")

    conn.mav.mission_count_send(conn.target_system, conn.target_component, n, 0)

    ack(conn, "MISSION_REQUEST")

    for seq, waypoint in enumerate(waypoints):
        print("-- Creating a waypoint")
        
        conn.mav.mission_item_send(conn.target_system,
                                   conn.target_component,
                                   seq,
                                   mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                                   mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
                                   0,
                                   1,
                                   0.0,
                                   2.0,
                                   20.0,
                                   math.nan,
                                   waypoint[0],
                                   waypoint[1],
                                   waypoint[2],
                                   0)
        
        if waypoint != waypoints[n-1]:
            ack(conn, "MISSION_REQUEST")
        # ack(conn, "MISSION_REQUEST")
    
    ack(conn, "MISSION_ACK")

        
# Send Message for the drone to return to the launch point
def set_return(conn):
    print("-- Set Return To Launch")
    conn.mav.command_long_send(conn.target_system, conn.target_component, 
                               mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0)

# Set Guided Mode
def set_mode(conn, mode='STABILIZE'):
    # mode 0: stabilize
    # mode 1: Acro
    # mode 2: AltHold
    # mode 3: Auto
    # mode 4: Guided
    # mode 5: Loiter
    # mode 6: RTL
    # https://ardupilot.org/copter/docs/parameters.html#fltmode1

    FlightMode = {
        'STABILIZE': 0,
        'ACRO': 1,
        'ALTHOLD': 2,
        'AUTO': 3,
        'GUIDED': 4,
        'LOITER': 5,
        'RTL': 6,
        'LAND': 9
    }
    print(f"-- Set Mode to {mode}")
    conn.mav.command_long_send(conn.target_system, conn.target_component, 
                               mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0, 209, FlightMode[mode], 0, 0, 0, 0, 0)
    
    while check_mode(conn) != mode:
        time.sleep(1)
        print(f"-- Set Mode to {FlightMode[mode]}")
        conn.mav.command_long_send(conn.target_system, conn.target_component, 
                                   mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0, 209, FlightMode[mode], 0, 0, 0, 0, 0)
    

def check_mode(conn):
    msg = conn.recv_match(type = 'HEARTBEAT', blocking = False)
    if msg:
        mode = mavutil.mode_string_v10(msg)
        print(f"-- Current Mode: {mode} ")
        return mode
    else:
        print(f"-- Current Mode: N/A ")
        return None
        
# Start Mission
def start_mission(conn):
    print("-- Mission Start")
    conn.mav.command_long_send(conn.target_system, conn.target_component,
                               mavutil.mavlink.MAV_CMD_MISSION_START, 0, 0, 0, 0, 0, 0, 0, 0)
    ack(conn, "COMMAND_ACK")

# Acknowledgement from the Drone
def ack(conn, keyword):
    print("-- Message Read", conn.recv_match(type=keyword, blocking=True))

# Main Function
if __name__=="__main__":
    print("-- Program Started")
    conn = mavutil.mavlink_connection("tcp:127.0.0.1:5762")

    print("-- Checking Heartbeat")
    conn.wait_heartbeat()
    print(f"-- Heartbeat from system {conn.target_system} component {conn.target_component}")
    
    waypoints = [
        (22.6162888, 120.28980, 100),
        (22.6158332, 120.28823, 100),
        (22.6165859, 120.28677, 100),
    ]

    upload_mission(conn, waypoints)

    set_mode(conn, 'GUIDED')

    arm(conn)

    takeoff(conn)

    set_mode(conn, 'AUTO')

    start_mission(conn)

    n = len(waypoints)

    for i in range(n-1):
        print("-- Message Read", conn.recv_match(type="MISSION_ITEM_REACHED", blocking=True))

    set_mode(conn, 'RTL')
