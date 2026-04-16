import os
import json
from datetime import datetime

def generate_html(design_spec: dict, code: str, project_name: str) -> str:
    """Generate a complete HTML file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{project_name.replace(' ", '_')}_{timestamp}.html"
    
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)
    
    return filepath