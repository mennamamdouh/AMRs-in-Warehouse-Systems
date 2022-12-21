from Map2D import Map2D
from Robot import Robot
from Shelf import Shelf


map_size_x = 8
map_size_y = 8

map = Map2D(size_x=map_size_x, size_y=map_size_y)
map.show_map()

S1 = Shelf(id = 'S1', intial_location = [5,4], map_size = [map_size_x, map_size_y])
S2 = Shelf(id = 'S2', intial_location = [2,2], map_size = [map_size_x, map_size_y])

map.update_objects_locations({S1.id:S1.locations, S2.id:S2.locations})
map.show_map()


R1 = Robot(id = 'R1', intial_location = [3,3], intial_orientation = 'right', speed=1, map_size = [map_size_x, map_size_y])
R2 = Robot(id = 'R2', intial_location = [0,3], intial_orientation = 'left', speed=1, map_size = [map_size_x, map_size_y])

map.update_objects_locations({R1.id:R1.locations, R2.id:R2.locations})
map.show_map()

R1.move_forward()
R2.move_forward()
map.update_objects_locations({R1.id:R1.locations, R2.id:R2.locations})
map.show_map()


R1.rotate_90_degree_clock_wise()
R2.rotate_90_degree_anti_clock_wise()
R1.move_forward()
R2.move_forward()
map.update_objects_locations({R1.id:R1.locations, R2.id:R2.locations})
map.show_map()
