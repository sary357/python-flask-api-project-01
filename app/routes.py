from app import app
from flask import jsonify
import datetime
import time
import shutil

@app.route('/time')
def get_time():
    # Get current time with local timezone
    now = datetime.datetime.now().astimezone()
    # Format: YYYY/MM/DD HH:mm:ss + timezone
    formatted_time = now.strftime('%Y/%m/%d %H:%M:%S %z')
    
    # To be safe and nicer, let's add the colon to the timezone if it's missing.
    if formatted_time[-5] in ['+', '-'] and formatted_time[-3] != ':':
        formatted_time = formatted_time[:-2] + ':' + formatted_time[-2:]
        
    return jsonify({'timestamp': formatted_time})

@app.route('/health')
def health_check():
    try:
        total, used, free = shutil.disk_usage("C:\\")
        percent_used = (used / total) * 100
        if percent_used > 80:
            return "Warning", 200
        return "OK", 200
    except Exception as e:
        return f"Error checking disk usage: {str(e)}", 500
