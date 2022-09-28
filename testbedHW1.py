import numpy as np 
import trimesh
import pyglet

mesh_obj = trimesh.Trimesh([[0,0,0],[0,1,0],[0,0,1]],[0,1,2])
mesh_obj.show()