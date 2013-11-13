log_path = "/usr/local/nusphere/apache/logs/access_log"
print "Percentage of requests that were client-cached: " + str(
       clientCachePercentage(log_path)) + '%'
