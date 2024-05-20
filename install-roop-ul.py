import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True)
    return result

# Update package lists
run_command("apt-get -y update")

# Install CUDA Toolkit 11.8
run_command("apt-get -y install cuda-toolkit-11-8")

# Install ffmpeg
run_command("apt-get -y install ffmpeg")

# Clone the roop-unleashed repository
run_command("git clone https://github.com/C0untFloyd/roop-unleashed.git")

# Change directory to roop-unleashed
run_command("cd roop-unleashed")

# Install Python requirements
run_command("pip install -r roop-unleashed/requirements.txt")

# Run the run.py script
run_command("python roop-unleashed/run.py")
