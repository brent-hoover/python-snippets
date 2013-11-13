weekly_sales = itertools.imap(sum, windows(daily_sales, 7))
