return rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date).count()
