import subprocess
import sys




def run_step(description, command):
    print(f"===== {description} =====")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
       print(f"❌ Error during: {description}")
       sys.exit(1)
    print(f"✅ Completed: {description}")




if __name__ == "__main__":
    print("🚀 Starting Skywise Cabin Analytics Pipeline...")


# Step 1: Generate Data
run_step("Generating Dataset", "python src/data_generation.py")


# Step 2: Run Python ETL
run_step("Running Python ETL", "python src/etl_python.py")


# Step 3: Run Analytics
run_step("Running Analytics", "python src/analytics.py")


print("🎉 Pipeline completed successfully!")
print("Launching Dashboard...")


# Step 4: Launch Streamlit Dashboard
subprocess.run("streamlit run src/dashboard.py", shell=True)