

class PointsForPlace:
   
   def __init__(self):
       self.points = 0
   
   def get_points_for_place(self, place):
       self.place = place
       if self.place > 100:
           return f'Баллы начисляются только первым 100 участникам'
       elif self.place < 1:
           return f'Спортсмен не может занять нулевое или отрицательное место'
       else:
           self.points= 101 - self.place
           return self.points
       
class PointsForMeters:
    def __init__(self):
       self.points = 0

    def get_points_for_meters(self,meters):
        self.meters=meters
        if self.meters < 0:
            return f'Количество метров не может быть отрицательным'
        else:
            self.points = self.meters * 0.5
            return self.points
        
class TotalPoints(PointsForPlace, PointsForMeters):
    
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)
        self.total = 0

       
    def get_total_points(self, place, meters):
        place_result = self.get_points_for_place(place)
        meters_result = self.get_points_for_meters(meters)
        self.total = place_result + meters_result
        return self.total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))