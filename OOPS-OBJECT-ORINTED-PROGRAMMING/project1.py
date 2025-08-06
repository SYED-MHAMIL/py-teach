class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model =model
        self.trafic_signal_status = None
        self.engine_status= False
        self.idling_time = 0

    def start_engine(self):
        print("started engine")
        self.engine_status =True
    
    def drive(self):
        if self.engine_status  and self.trafic_signal_status == "green":
           print(f"you are driving at a {self.brand}{self.model}")
        elif self.set_trafic_signal == "red" :
            print("you stopped at the red light wait for for the greeen light")
            self.idel_timing()
        else:
            self.start_engine() 
            print(f" you are driving a {self.brand}{self.model}")   

    def set_trafic_signal(self,signal):
        self.trafic_signal_status = signal
        if self.trafic_signal_status == "red":
            print(f"traffic signal turned out you stopped in a {self.brand}{self.model}")
            self.idel_timing()        
        elif self.trafic_signal_status == "green":
            print(f"you are driving in the {self.brand}{self.model}")
            if not self.engine_status:        
               self.start_engine()
    
    def stop(self):
        if self.engine_status:
            print(f"you stopped the {self.brand}{self.model}")
        else:
            print(f"you stopped  already the {self.brand}{self.model}")

    def idel_timing(self):
        import time 
        print("Engine is idling")
        for i in range(5):
            time.sleep(1)
            self.idling_time+=i

        if self.idling_time >=5:
           self.engine_status =False
           print("Engine stopped (idle stop) to save fule. ")



c1 =Car("Honda","Civics")
c1.start_engine()
c1.drive()
c1.set_trafic_signal("red")
# print(c1.engine_status)

    


            

        





