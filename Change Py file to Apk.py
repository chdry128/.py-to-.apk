# Import the required modules
import os
import subprocess

# Set the path of the input and output files
input_file = "my_python_file.py"
output_file = "my_android_app.apk"

# Create a temporary directory for the build process
temp_dir = "temp_build_dir"
os.makedirs(temp_dir, exist_ok=True)

# Use the buildozer tool to build the APK file
cmd = [
    "buildozer",
    "--profile", "android",
    "--android-entrypoint", "main",
    "--app", input_file,
    "--package", "org.example.my_app",
    "--name", "My Android App",
    "--version", "1.0.0",
    "--orientation", "landscape",
    "--window",
    "--permission", "INTERNET",
    "--build-dir", temp_dir,
    "--release",
    "--output", output_file,
]
subprocess.run(cmd)

# Clean up the temporary directory
os.rmdir(temp_dir)
