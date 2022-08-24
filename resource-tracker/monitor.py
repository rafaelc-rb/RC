import psutil

# Method set_size() performs the formatting of sizes, in KB, MB, GB, TB and PB.
# @param bytes receives the value to be transformed.
# @param suffix saves the letter "B" which will complete the unit abbreviation
# return returns the value already transformed
def set_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f}{unit}{suffix}"
        bytes /= factor

# Method that returns memory resources, via the psutil library, 
# and uses the set_size() method to format the data.
# Receives the information for total, free, in-use memory, 
# and percentage of use, and then compress the information into a variable.
# return returns the variable with the information.
def mem():
    mem = psutil.virtual_memory()

    total = "Total: " + str(set_size(mem.total))
    free = "Free: " + str(set_size(mem.free))
    used = "In Use: " + str(set_size(mem.used))
    percent = "Percentage of Use: " + str(mem.percent) + "%"

    mem_data = "Memory" + ";" + total + ";" + free + ";" + used + ";" + percent
    return mem_data


# Method that returns cpu resources, via the psutil library.
# Receives information for logical, non-logical cores, and percentage of use,
# and then compress the information into a variable.
# return returns the variable with the information.
def cpu():
    logical = "Logical Cores: " + str(psutil.cpu_count())
    nonlogical = "Non-Logical Cores:" + str(psutil.cpu_count(logical=False))
    percent = "Percentage of Use: " + str(psutil.cpu_percent(interval=1)) + "%"

    cpu_data = "CPU" + ";" + logical + ";" + nonlogical + ";" + percent
    return cpu_data

# Method that returns disk usage resources, via the psutil library, 
# and uses the set_size() method to format the data.
# Receives the information for total, free, in-use disk, 
# and percentage of use, and then compress the information into a variable.
# return returns the variable with the information.
def disk():
    disk = psutil.disk_usage('C:\\')

    total = "Total: " + str(set_size(disk.total))
    free = "Free: " + str(set_size(disk.free))
    used = "In Use: " + str(set_size(disk.used))
    percentage = "Percentage of Use: " + str(disk.percent) + '%'

    disk_data = "Disk" + ";" + total + ";" + free + ";" + used + ";" + percentage
    return disk_data