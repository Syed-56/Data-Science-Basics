import datetime, bday_messages

today = datetime.date.today()
next_bday = datetime.date(2025,10,30)
time_diff = next_bday - today

if today == next_bday:
  print(bday_messages.random_msg)
else:
  print(f"Next birthday is {time_diff}")