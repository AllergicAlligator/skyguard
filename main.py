import skyguard
from pymavlink import mavutil

print("-- Program Started")
conn = mavutil.mavlink_connection("tcp:127.0.0.1:5762")

print("-- Checking Heartbeat")
conn.wait_heartbeat()
print(f"-- Heartbeat from system {conn.target_system} component {conn.target_component}")
    
waypoints = [
    (22.6172544, 120.2882078, 50), # LAUNCH POINT (HOME)
    (22.616609, 120.290679, 50),
    (22.616196, 120.288569, 50),
    (22.615178, 120.288616, 50),
    (22.616951, 120.285917, 50)
]

skyguard.upload_mission(conn, waypoints)

skyguard.set_mode(conn, 'GUIDED')

skyguard.arm(conn)

skyguard.takeoff(conn)

skyguard.set_mode(conn, 'AUTO')

skyguard.start_mission(conn)

n = len(waypoints)

for i in range(n-1):
    print("-- Message Read", conn.recv_match(type="MISSION_ITEM_REACHED", blocking=True))

skyguard.set_mode(conn, 'RTL')
