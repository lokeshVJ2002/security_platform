import traceback
from .apk_engine import APKScanner

def execute_scan(scan):
    scan.status = 'RUNNING'
    scan.save()

    try:
        if scan.scan_type == 'APK':
            engine = APKScanner(scan)
            engine.run_analysis()

        scan.status = 'COMPLETED'
    except Exception as e:
        print("--- SCAN FAILED WITH ERROR ---")
        traceback.print_exc()
        scan.status = 'FAILED'
    finally:
        scan.save()
