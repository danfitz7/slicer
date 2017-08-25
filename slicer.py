#!/usr/bin/python

# Basic 3D Mesh Slicer
# Written by Daniel Fitzgerald
# 08/25/2017
import os
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

    swapyz=False

    vertices = []
    normals = []
    texcoords = []
    faces = []
    
    # Much of this code is borrowed from https://www.pygame.org/wiki/OBJFileLoader
    if (os.path.exists(filename)):
        with open(filename) as f:
            lines  = f.readlines()
    
            for line in lines:
                if line.startswith('#'): continue
                values = line.split()
                if not values: continue
                
                if values[0] == 'v':
                    #v = map(float, values[1:4])
                    v = [float(values[1]), float(values[2]), float(values[3])]
                    if swapyz:
                        v = v[0], v[2], v[1]
                    vertices.append(v)
                elif values[0] == 'vn':
                    #v = map(float, values[1:4])
                    v= [float(values[1]), float(values[2]), float(values[3])]
                    if swapyz:
                        v = v[0], v[2], v[1]
                        normals.append(v)
                    elif values[0] == 'vt':
                        texcoords.append(map(float, values[1:3]))
                    #elif values[0] in ('usemtl', 'usemat'):
                    #    material = values[1]
                    #elif values[0] == 'mtllib':
                    #    mtl = MTL(values[1])
                elif values[0] == 'f':
                    face = []
                    texcoords = []
                    norms = []
                    for v in values[1:]:
                        w = v.split('/')
                        face.append(int(w[0]) - 1) # subtract 1 to convert from 1-based indexing (.obj) to 0-based (Python)
                        if len(w) >= 2 and len(w[1]) > 0:
                            texcoords.append(int(w[1]))
                        else:
                            texcoords.append(0)
                        if len(w) >= 3 and len(w[2]) > 0:
                            norms.append(int(w[2]))
                        else:
                            norms.append(0)
                    faces.append((face, norms, texcoords))
    
    print("\n{0} Vertices: ".format(len(vertices)))
    #for vertex in vertices:
    #    print("V<{0},{1},{2}>".format(vertex[0],vertex[1],vertex[2]))
    
    print("\n{0} faces: ".format(len(faces)))
    #for face in faces:
    #    print("F[{0},{1},{2}]".format(face[0][0], face[0][1], face[0][2]))
    
    # Vert4eces lists for x,y,z
    x = [vertex[0] for vertex in vertices]
    y = [vertex[1] for vertex in vertices]
    z = [vertex[2] for vertex in vertices]
    
    # Triangles array extracts the first three indeces of the face part of each of the faces, ignoring texture coordinates, norms, and vertex indeces past the third.
    triangles = [(face[0][0], face[0][1], face[0][2]) for face in faces]
    
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
