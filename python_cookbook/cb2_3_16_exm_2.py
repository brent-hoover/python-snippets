US = data.find('United States Dollar')  # find the index of the currency
endofUSline = data.index('\n', US)      # find index for that line end
USline = data[US:endofUSline]           # slice to make one string 
rate = USline.split(',')[-1]            # split on ',' and return last field
