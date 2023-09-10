import os
import subprocess

# Settings
TEST_DIR = "./tests/average"
CODE_FILE = "main.cpp"
COMPILER_TIMEOUT = 10  # Time in seconds before the compiler is killed
RUN_TIMEOUT = 10  # Time in seconds before the program is killed

# Create absolute paths (python is relative path)
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

# Print paths for debugging
print(f"Current working directory: {os.getcwd()}")
print(f"Code path: {code_path}")
print(f"App path: {app_path}")

# Compile the code
print("Building code...")

try:
        ret = subprocess.run(["g++", code_path, "-o", app_path, "-I./tools/cpputest/include", "-L./tools/cpputest/lib", "-lCppUTest"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=COMPILER_TIMEOUT)

except Exception as e:
    print("ERROR: Failed while compiling: ", str(e))
    exit(1)

# Parse the output
output = ret.stdout.decode("utf-8")
print("Compiler STDOUT:", output)
output = ret.stderr.decode("utf-8")
print("Compiler STDERR:", output)

# Check if the compiler completed successfully
if ret.returncode != 0:
    print("ERROR: Failed while compiling")
    exit(1)

# Try to run the program, sets timeout and print error if fails
print(f"All tests passed, return code: {ret.returncode}")

try:
    ret = subprocess.run([app_path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         timeout=RUN_TIMEOUT)
except Exception as e:
    print("ERROR: Failed while running: ", str(e))
    exit(1)

# Parse the output
output = ret.stdout.decode("utf-8")
print("Program Output:", output)

# All tests have passed
print("All tests passed")
exit(0)  # no errors!
