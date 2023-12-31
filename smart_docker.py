import subprocess
import sys
import os

# ANSI escape codes for colored text
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Settings
DEBUG = True  # Debug flag, set to True to enable debug prints

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

def run_command(command, capture_output=False):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=capture_output, text=True)
        if capture_output:
            return result.stdout
    except subprocess.CalledProcessError as e:
        debug_print(f"Command failed with error: {e}", "ERROR")
        sys.exit(1)

def image_exists(image_name):
    docker_images_output = run_command("docker images --format '{{.Repository}}'", capture_output=True)
    return image_name in docker_images_output.splitlines()

def main():
    image_name = "your-image-name"
    host_path = os.getcwd()  # Get the current working directory
    container_path = "/app"

    # Check if the Docker image already exists
    if image_exists(image_name):
        debug_print(f"Image {image_name} already exists. Skipping build.", "SUCCESS")
    else:
        # Build the Docker image
        debug_print("Building Docker image...", "INFO")
        run_command(f"docker build -t {image_name} .")

    # Run the Docker container with volume but without port forwarding
    debug_print("Running Docker container with volume...", "INFO")
    run_command(f"docker run --rm -v {host_path}:{container_path} {image_name}")
  
    # List all available Docker images
    debug_print("Listing all available Docker images:", "INFO")
    run_command("docker images")

    # List all running Docker containers
    debug_print("Listing all running Docker containers:", "INFO")
    run_command("docker ps")

    # Optionally, delete the Docker image
    delete_image = input("Do you want to delete the Docker image? (y/n): ")
    if delete_image.lower() == 'y':
        debug_print("Deleting Docker image...", "INFO")
        run_command(f"docker rmi {image_name}")


if __name__ == "__main__":
    main()
