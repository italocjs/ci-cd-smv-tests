import os
import subprocess

# ANSI escape codes for colored text
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Settings
DEBUG = True  # Debug flag, set to True to enable debug prints
MAKEFILE_DIR = "."  # Directory where the Makefile is located
COMPILER_TIMEOUT = 10  # Time in seconds before the compiler is killed
RUN_TIMEOUT = 10  # Time in seconds before the program is killed

# Create absolute paths (python is relative path)
app_path = os.path.join(MAKEFILE_DIR, "app.elf")  # Updated to point to app.elf


# Debug print function
def debug_print(message, msg_type="INFO"):
    if DEBUG:
        color = RESET  # Default color
        
        if "ERROR" in msg_type:
                color = RED
        elif "SUCCESS" in msg_type:
                color = GREEN
        elif "INFO" in msg_type:
                color = BLUE
        
        print(f"{color}{message}{RESET}")


# Function to check if 'make' is in PATH
def check_make_in_path():
    for path in os.environ['PATH'].split(os.pathsep):
        make_path = os.path.join(path, 'make')
        if os.path.exists(make_path) and os.access(make_path, os.X_OK):
            return True
    return False



# Pre-build checks
debug_print(f"- Pre-build checks", "INFO")
if check_make_in_path():
    debug_print(f"\t'make' found in PATH", "INFO")
else:   
    debug_print("\t'make' not found in PATH. Please install it or add it to PATH.", "ERROR")
    exit(1) # exit with error
debug_print(f"\tCurrent working directory: {os.getcwd()}", "INFO")
debug_print(f"\tApp path: {app_path}", "INFO")
debug_print(f"- Starting build process", "INFO")


# Compile the code using Makefile
debug_print("- Building code using Makefile...", "INFO")
try:
    ret = subprocess.run(["make"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         timeout=COMPILER_TIMEOUT)
    
    # Parse the output
    output = ret.stdout.decode("utf-8")
    output = output.replace("\r", "")
    output = output.replace("\n", "")
    debug_print(f"\tCompiler STDOUT: {output}", "INFO")
    output = ret.stderr.decode("utf-8")
    if (output):
        debug_print(f"\tCompiler STDERR: {output}", "ERROR")
    debug_print(f"\tMake success: ret={ret.returncode}", "INFO")

        # Delete all .o files
    debug_print("\tCleaning all .o files...", "INFO")
    subprocess.run(["make", "clean"],
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
except Exception as e:
    debug_print(f"\tmake failed: Error: {str(e)}", "ERROR")
    debug_print(f"\tCurrent PATH: {os.environ.get('PATH')}", "INFO")  # Print the current PATH, if make is not here, it will not run
    exit(1) # exit with error

# Run the program
debug_print("- Running program, output below:", "INFO")
try:
    ret = subprocess.run([app_path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         timeout=RUN_TIMEOUT)
    output = ret.stdout.decode("utf-8")
    print(output)
except Exception as e:
    debug_print(f"Failed while running: {str(e)}", "ERROR")
    exit(1) # exit with error

exit(0)  # no errors!
