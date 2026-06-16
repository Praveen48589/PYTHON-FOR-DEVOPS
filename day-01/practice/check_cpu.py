import psutil
# install pstil using pip install psutil on terminal
# Find current CPU usage of your system using Python
# send email if CPU usage is greater than 75%

def check_cpu_threshold():
    threshold_cpu = int(input("Enter the current cpu threshold :"))
    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU % is : ", current_cpu)
    if current_cpu > threshold_cpu:
        print("CPU ALERT Email sent to admin")
    else:
        print("CPU usage is normal")
    


check_cpu_threshold()