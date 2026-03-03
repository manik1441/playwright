import os
import pytest
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Get the project root directory
    root_dir = config.rootdir
    
    # Define the reports directory
    reports_dir = os.path.join(str(root_dir), "reports")
    
    # Create the directory if it doesn't exist
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        
    # Configure HTML report path dynamically
    # This ensures the report is always generated in the project_root/reports folder
    if not config.option.htmlpath:
        config.option.htmlpath = os.path.join(reports_dir, "report.html")
        config.option.self_contained_html = True

    # Configure Log file path dynamically
    if not config.option.log_file:
        config.option.log_file = os.path.join(reports_dir, "pytest.log")
