#!/usr/bin/python

# Basic 3D Mesh Slicer
# Written by Daniel Fitzgerald
# 08/25/2017

import sys
import numpy
from mayavi import mlab


class Point3D():
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z 

def load_obj(filename):
    """Loads an .obj file and parses the data into a mesh.
    
    The mesh is specified by parallel x,y,z vertex coordinate lists a traingles list of 3-tuples corresponding to vertex indeces.
    
    Args:
        filename: The full path name of the file to open.
        
    Returns:
        Three parallel lists containing x,y,z coordinates of the verteces and one array of 3-tuples specifying the indeces of the verteces of the triangles.
        
    Raises:
        none
    """
    print("Loading OBJ file '{0}'".format(filename))

    
    # Vert4eces lists for x,y,z
    x = [0.0, 1.0, 1.0, 0.0]
    y = [0.0, 0.0, 1.0, 1.0]
    z = [0.0, 0.0, 0.0, 0.0]
    
    triangles = [(0,1,2), (0,2,3)]
    
    return x,y,z,triangles

def render_mesh(x,y,z,triangles):
    """Plots the given mesh on the default figure.
    
    The mesh is specified by parallel x,y,z vertex coordinate lists a traingles list of 3-tuples corresponding to vertex indeces.
    
    Args:
        Three parallel lists containing x,y,z coordinates of the verteces and one array of 3-tuples specifying the indeces of the verteces of the triangles.
        
    Returns:
        none
        
    Raises:
        none
    """
    print("Rendering mesh...")
    
    mesh_color = (0.5, 0.5 ,0.9)
    mesh_opacity = 0.5
    mesh_line_width = 1.0
    mesh_representation = "mesh"
    mlab.triangular_mesh(x,y,z,triangles, color=mesh_color, line_width = mesh_line_width, opacity=mesh_opacity, representation=mesh_representation)
    mlab.show()
    
def main():
    print("Main...")
    
    # load the obj file given as the first command line argument
    obj_file_name = sys.argv[1]
    
    # convert the 3D data to a mayavi mesh
    x,y,z,triangles = load_obj(obj_file_name)
    
    # render the mesh
    render_mesh(x,y,z,triangles)
    
if __name__ == "__main__":
    main()
