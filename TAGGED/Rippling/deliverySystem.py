"""
Problem: Build a delivery cost tracking system
Asked in 3 parts:

Cost Calculation
add_driver(driverId)
add_delivery(driverId, startTime, endTime)
get_total_cost()
Discussed approach, data structures, and time complexity before coding.

Payment Tracking
pay_up_to_time(upToTime)
get_cost_to_be_paid()
Analytics
get_max_active_drivers_in_last_24_hours(currentTime)
Didn’t implement fully due to time, but the approach was discussed and accepted.
"""

from collections import defaultdict

class CostTracker:

    def __init__(self):
        self.drivers = defaultdict(list)
        self.rate = 15
    
    def add_driver(self, driverId):
        if driverId not in self.drivers:
            self.drivers[driverId] = []

    def add_delivery(self, driverId, startTime, endTime):
        self.drivers[driverId].append((startTime, endTime))

    def get_total_cost(self):
        total_cost = 0

        for driver in self.drivers.keys():
            for startTime, endTime in self.drivers[driver]:
                adjusted_end_time = endTime if endTime > startTime else endTime + 24
                total_cost += (adjusted_end_time - startTime) * self.rate
        
        return total_cost
    
    def pay_up_to_time(self, upToTime):
        total_paid = 0
        
        for driverId in list(self.drivers.keys()):
            new_deliveries = []
            for startTime, endTime in self.drivers[driverId]:
                adjusted_end_time = endTime if endTime > startTime else endTime + 24

                if upToTime <= startTime:
                    new_deliveries.append((startTime, endTime))
                elif adjusted_end_time > upToTime > startTime:
                    total_paid += (upToTime - startTime) * self.rate
                    new_deliveries.append((upToTime, endTime))
                else:
                    total_paid += (adjusted_end_time - startTime) * self.rate
            
            self.drivers[driverId] = new_deliveries
        
        return total_paid

    def get_cost_to_be_paid(self):
        return self.get_total_cost()

    def get_max_active_drivers_in_last_24_hours(self, currentTime):
        active_driver = 0

        for deliveries in self.drivers.values():
            for startTime, endTime in deliveries:
                adjusted_end_time = endTime if endTime > startTime else endTime + 24
                adjusted_start_time = startTime

                if adjusted_start_time <= currentTime and adjusted_end_time >= currentTime - 24:
                    active_driver += 1
                    break
        
        return active_driver