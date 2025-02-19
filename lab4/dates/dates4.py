from datetime import datetime

date1 = datetime(2025, 2, 1, 14, 30, 0)
date2 = datetime.now()

difference_in_seconds = (date2 - date1).total_seconds()

print("Difference in seconds:", difference_in_seconds)
