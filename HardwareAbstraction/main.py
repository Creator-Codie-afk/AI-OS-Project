# main.py - Hardware Abstraction Module
import platform
import psutil

def get_hardware_info():
    """
    Function to retrieve hardware information.
    """
    hardware_info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(),
        "memory": psutil.virtual_memory().total,
        "disk": psutil.disk_usage('/').total
    }
    return hardware_info

def manage_hardware_resources():
    """
    Function to manage and monitor hardware resources.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage
    }

if __name__ == "__main__":
    # Test hardware information retrieval
    hardware_info = get_hardware_info()
    print(f"Hardware Information: {hardware_info}")
    
    # Test hardware resource management
    resource_usage = manage_hardware_resources()
    print(f"Resource Usage: {resource_usage}")
