def get_uptime_seconds():
    """Returns the system uptime in seconds."""
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

# Example usage:
print(f"Uptime: {get_uptime_seconds()} seconds")
