class Activity:

    def __init__(self, name, instructor, date, duration, capacity, plan_type, active, id_=None):
        self.name = name
        self.instructor = instructor
        self.date = date
        self.duration = duration
        self.capacity = capacity
        self.plan_type = plan_type
        self.active = active
        self.id_ = id_
