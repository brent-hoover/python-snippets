today = datetime.date.today()
  next_year = today.replace(year=today.year+1).strftime("%Y.%m.%d")
  print next_year
