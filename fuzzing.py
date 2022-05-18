import time

def detect():
    attack =1
    while (attack):
        counting = 0 
        with  open("/var/log/auth.log", "r") as file:
         file.seek(0,2)
         for line in file:
                    while True:
                     if ("error" in line or( "Protocol major versions" in line)
                     or( "Connection closed by" in line)
                     or( "closed" in line)
                     or( "banner exchange" in line)
                     or( "Invalid SSH " in line)):
                        counting=  counting+1
                        if counting>=5:
                            print("Fuzzing detected")
                            exit(0)
                        else:
                            time.sleep(5)
if __name__ == "__main__":
    detect()
