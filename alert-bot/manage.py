import time
import subprocess
import datetime as dt
import zoneinfo
from pathlib import Path

BOT_DIR = Path(__file__).resolve().parent
PYTHON_EXE = Path(r"d:\projects\webapp projects\project-upshift\venv\Scripts\python.exe")
BOT_SCRIPT = BOT_DIR / "price_alert_bot.py"
market_close_ist_tz = dt.time(15, 0, 0, tzinfo=zoneinfo.ZoneInfo("Asia/Kolkata"))

while True:
    current_time_ist_tz = dt.datetime.now(zoneinfo.ZoneInfo("Asia/Kolkata")).time().replace(microsecond=0)

    if current_time_ist_tz >= market_close_ist_tz:
        print(f"market is closed as of {current_time_ist_tz}")
        break

    print(f"market is open as of {current_time_ist_tz}")
    print("starting bot")

    result = subprocess.run(
        [str(PYTHON_EXE), str(BOT_SCRIPT)],
        cwd=str(BOT_DIR),
        check=False,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("bot exited with a non-zero status")
        print(result.stdout)
        print(result.stderr)
    else:
        print(result.stdout)

    print("sleeping for 15 minutes...\n")
    time.sleep(60 * 15)