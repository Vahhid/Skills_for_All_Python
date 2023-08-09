#request start hour
hour = int(input("Starting time (hours): "))
#request start minute
mins = int(input("Starting time (minutes): "))
#request duration in minutes
dura = int(input("Event duration (minutes): "))

#calculate hours after removing full days
dura_hr = (dura // 60) % 24 + (mins + dura)//60
#Calculate minutes ater removing full hours
dura_min = (mins + dura) % 60

#end hour is start hour added to net additional hours
end_hr = (hour + dura_hr) % 24
#end minute is the reminder minute
end_min = dura_min
print("hour ", end_hr)
print("minute  ", end_min)




