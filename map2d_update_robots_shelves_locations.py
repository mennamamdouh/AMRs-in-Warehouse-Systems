import pandas as pd
import numpy as np
import string


class Map2D():
    """
    Map2D class creates the 2d map with 2d numpy array, and because it's based on numpy 2d array
    the location's coordinates are based on numpy convention in indexing.

    :param size_x: width of the 2d grid
    :param size_x: height of the 2d grid
    """
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.map = np.zeros((size_y, size_x))
        self.map = self.map.astype('int')
        self.map = self.map.astype('object')



    def update_objects_locations(self, object_locations):
        """
        update_objects_locations function updates the locations of objects(robots or shelves) in the 2 grid.
        
        :param object_locations: dictionary of objects, each object has 2 attributes, the object name
                                 and a list of the object previous location and current location. 
                                 example: dict {R1:[prev_location, crrent_location], R2:[prev_location, crrent_location],.., Rn:[prev_location, crrent_location]}
        """

        for object_id, locations in object_locations.items():
            prev_location = locations[0]
            crrent_location = locations[1]

            # erase prev location
            pos_x = prev_location[0]
            pos_y = prev_location[1]
            self.map[pos_x][pos_y] = 0


            # add new location
            pos_x = crrent_location[0]
            pos_y = crrent_location[1]
            self.map[pos_x][pos_y] = object_id



    def show_map(self):
        """
        show_map function prints the 2d grid to visualize the movement of objects.
        """
        letters_seqence_columns = string.ascii_uppercase[0:self.size_x]
        letters_seqence_rows = string.ascii_uppercase[0:self.size_y]
        print(pd.DataFrame(self.map,columns=list(letters_seqence_columns),index=list(letters_seqence_rows)))
            
        print('---------------------------------------')



# test the Map2D class
if __name__ == "__main__":
    map_size_x = 10
    map_size_y = 5

    map = Map2D(size_x=map_size_x, size_y=map_size_y)
    map.show_map()

    map.update_objects_locations({'S1':[[2,5],[2,5]], 'S2':[[0,0],[0,0]]})
    map.show_map()

    map.update_objects_locations({'R1':[[2,2],[2,3]], 'R2':[[0,3],[0,2]]})
    map.show_map()

    map.update_objects_locations({'R1':[[2,3],[2,4]], 'R2':[[0,2],[0,1]]})
    map.show_map()

    