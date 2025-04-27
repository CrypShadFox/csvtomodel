import bpy
import csv
import math

filepath = "C:/Path/to/File.csv"
merge_threshold = 0.01
vertices = []
merged_vertices = []
vertex_mapping = {}

def are_vertices_close(v1, v2, threshold):
    return math.dist(v1, v2) < threshold

with open(filepath, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x = float(row[' IN_Pos0.x'])
        y = float(row[' IN_Pos0.y'])
        z = float(row[' IN_Pos0.z'])
        # May require you to adjust the row names based on your CSV structure
        vertices.append((x, y, z))

for v in vertices:
    found = False
    for i, mv in enumerate(merged_vertices):
        if are_vertices_close(v, mv, merge_threshold):
            vertex_mapping[v] = mv
            found = True
            break
    if not found:
        merged_vertices.append(v)
        vertex_mapping[v] = v

faces = []
for i in range(0, len(vertices) - 2, 3):
    face = []
    for j in range(3):
        original_vertex = vertices[i + j]
        merged_vertex = vertex_mapping[original_vertex]
        merged_index = merged_vertices.index(merged_vertex)
        face.append(merged_index)
    faces.append(tuple(face))

if merged_vertices and faces:
    mesh = bpy.data.meshes.new("MergedMesh")
    obj = bpy.data.objects.new("MergedObject", mesh)
    bpy.context.collection.objects.link(obj)
    mesh.from_pydata(merged_vertices, [], faces)
    mesh.update()
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
else:
    print("No valid data to create a mesh.")