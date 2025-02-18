import subprocess
import sys

def install_packages():
    try:
        import streamlit
        import pandas
        import sklearn
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "app.py", "--server.port=8501"])

if __name__ == "__main__":
    install_packages()
    run_streamlit()
