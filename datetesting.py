from datetime import datetime, timedelta

dt = datetime.now()
dt_30daysago = dt - timedelta(days=30)

date = datetime.strptime(str(dt_30daysago), '%Y-%d-%m %H:%M:%S.%f')


print(f'{date.day}-{date.month}')