mvavg_daily_sales = itertools.imap(average, windows(daily_sales, 7, 6))
