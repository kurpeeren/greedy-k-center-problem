class Point:
    def __init__(self, id, x, y, demand, assigned_facility_id = None):
        self.id = id
        self.x = x
        self.y = y
        self.demand = demand
        self.assigned_facility_id = assigned_facility_id