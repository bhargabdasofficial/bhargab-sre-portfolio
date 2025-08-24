

---

Python Fundamentals Refresher

### DAY 1 ###

1. Hello World
```

print("Hello, SRE!")

```
2. Variables

```

name = 'bhargab'
uptime = 99.99
alerts_enabled = True

print(name, uptime, alerts_enabled)

```
3. Data Types

```

# string
server = "prod-app-01"

# integer
users = 120

# float
cpu_load = 23.5

# Boolean
is_active = True
 
# List
server = ["app1", "app2", "app3"]

# Dictionary
server_status = {
	"name": "app1",
	"uptime": 99.9,
	"status": "healthy"
}

```

4. Loops

```
# for loop

servers =["app1", "app2", "db"]

for i in servers:
	print("Checking servers", i)

# whilw loop
count = 0
while count < 3:
	print("Retry" , count)
	count += 1

```

5. Conditions

```

cpu_usage = 85

if cpu_usage > 90:
	print(" CPU usage has exceeded critical threshold!")
elif cpu_usage > 85:
	print("CPU Usage has exceeded major threshold!")
else:
    	print("CPU Ok")

```

6. Functions

```

def check_cpu(threshold):
	cpu_usage = 75
	if cpu_usage > threshold:
		return " Alert: CPU High!"
	return " CPU Ok"

print(check_cpu(70))

```
