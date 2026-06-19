import psutil

def get_system_metrics():
    """
       Monitor the current system resource utilization.
       This function collects CPU, memory, and disk usage statistics
       using the psutil library.


       Metrics Collected:
       - CPU usage percentage
       - Memory usage percentage
       - Disk usage percentage
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent
    cpu_threshold = 15

    status = "High CPU" if cpu_percent > cpu_threshold else "Healthy" 

    return {
        "cpu_percentage":cpu_percent,
        "memory_percentage":memory_percent,
        "disk_percentage":disk_percent,
        "cpu_threshold":cpu_threshold,
        "system_status":status
    }

