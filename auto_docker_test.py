import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        sys.exit(1)

def main():
    # Build the Docker image
    print("Building Docker image...")
    run_command("docker build -t test_unit .")

    # Run the Docker container
    print("Running Docker container...")
    run_command("docker run --rm test_unit")

    # Delete the Docker image
    print("Deleting Docker image...")
    run_command("docker rmi test_unit")

if __name__ == "__main__":
    main()
