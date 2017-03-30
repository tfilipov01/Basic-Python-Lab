a = raw_input("text:")

print "-*"*len(a)
print a
print "-*"*len(a)


a = {"first_name":"Ivan", "sure_name":"Vazov", "age":45, "city":"sofia"}

ts_epoch = 1490781600
ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
ts
