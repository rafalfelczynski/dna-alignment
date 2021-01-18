from Models.object3D import *
from PySide2.QtCore import *
import copy


class MtlLoader:

    @staticmethod
    def loadMaterial(fileName):
        materials = dict()
        file = QFile(fileName)
        if file.open(QFile.ReadOnly):
            lastMaterial = Material()
            materialStarted = False
            lines = file.readAll().data().decode("utf-8").splitlines()
            for line in lines:
                line = line.strip()
                lineSpl = line.split(" ")
                if len(lineSpl) > 0:
                    i=1
                    if lineSpl[0] == "newmtl":
                        if materialStarted:
                            materials[lastMaterial.name] = copy.copy(lastMaterial)
                        materialStarted = True
                        i=succeedInd(lineSpl, i)
                        lastMaterial.name = lineSpl[i]
                    elif lineSpl[0] == "Ka":  # ambient
                        lastMaterial.ambientColor = fetchColor(lineSpl)
                    elif lineSpl[0] == "Kd":  # diffuse
                        lastMaterial.diffuseColor = fetchColor(lineSpl)
                    elif lineSpl[0] == "Ks":  # specular
                        lastMaterial.specularColor = fetchColor(lineSpl)
                    elif lineSpl[0] == "Ns":
                        i=succeedInd(lineSpl, i)
                        lastMaterial.shininess = float(lineSpl[i])
                    elif lineSpl[0] == "Ke":
                        lastMaterial.emission = fetchColor(lineSpl)
                    elif lineSpl[0] == "d":
                        i=succeedInd(lineSpl, i)
                        lastMaterial.transparency = float(lineSpl[i])
                    elif lineSpl[0] == "Tr":
                        i=succeedInd(lineSpl, i)
                        lastMaterial.transparency = 1 - float(lineSpl[i])
            if materialStarted:
                materials[lastMaterial.name] = copy.copy(lastMaterial)
            file.close()
        else:
            print("Error in MtlLoader. Cannot open file ", fileName)
        return materials


def succeedInd(lineSpl, i):
    while i < len(lineSpl) and lineSpl[i] == "":
        i+=1
    return i


def fetchColor(lineSpl) -> Color:
    color = Color()
    i=1
    i=succeedInd(lineSpl, i)
    color.r = float(lineSpl[i])
    i += 1
    i=succeedInd(lineSpl, i)
    color.g = float(lineSpl[i])
    i += 1
    i=succeedInd(lineSpl, i)
    color.b = float(lineSpl[i])
    i += 1
    return color


class ObjLoader:

    @staticmethod
    def loadObj(filePath):
        object = Object3D()
        file = QFile(filePath)
        if file.exists():
            if file.open(QFile.ReadOnly):
                vertices = []
                uvs = []
                normals = []
                vertIndexes, uvIndexes, normIndexes, polylines = [], [], [], []
                materialNames = []
                materialFile = ""
                lastMaterialName = ""
                fRegTheSimplest = QRegExp("[0-9]+")
                fRegSimpler = QRegExp("[0-9]+/[0-9]+")
                fReg = QRegExp("[0-9]+/[0-9]*/[0-9]+")
                lines = file.readAll().data().decode("utf-8").splitlines()
                for line in lines:
                    line = line.strip()
                    lineSpl = line.split(" ")
                    if len(lineSpl) > 0:
                        if lineSpl[0] == "vn":
                            parseVec3(normals, lineSpl)
                        elif lineSpl[0] == "vt":  # uvs
                            parseVec3(uvs, lineSpl)
                        elif lineSpl[0] == "v":  # vertices
                            parseVec3(vertices, lineSpl)
                        elif lineSpl[0] == "f":  # face
                            vertInds = []
                            uvInds = []
                            normInds = []
                            for i in range(1, len(lineSpl)):
                                s = lineSpl[i]
                                if fReg.exactMatch(s):
                                    numbers = s.split("/")
                                    vertInds.append(int(numbers[0]))
                                    if numbers[1] != "":
                                        uvInds.append(int(numbers[1]))
                                    normInds.append(int(numbers[2]))
                                elif fRegSimpler.exactMatch(s):
                                    numbers = s.split("/")
                                    vertInds.append(int(numbers[0]))
                                    uvInds.append(int(numbers[1]))
                                elif fRegTheSimplest.exactMatch(s):
                                    vertInds.append(int(s))
                            materialNames.append(lastMaterialName)
                            vertIndexes.append(vertInds)
                            uvIndexes.append(uvInds)
                            normIndexes.append(normInds)
                        elif lineSpl[0] == "l":  # polyline
                            vertInds = []
                            for i in range(1, len(lineSpl)):
                                vertInds.append(int(lineSpl[i]))
                            polylines.append(vertInds)
                        elif lineSpl[0] == "mtllib":  # // material file name
                            info = QFileInfo(filePath)
                            s = ""
                            for i in range(1, len(lineSpl)):
                                s = s + lineSpl[i] + " "
                            s = s.strip()
                            materialFile = info.path()+"/" + s
                        elif lineSpl[0] == "usemtl":  # material name
                            s = ""
                            for i in range(1, len(lineSpl)):
                                s = s + lineSpl[i] + " "
                            s = s.strip()
                            lastMaterialName = s
                for i in range(0, len(vertIndexes)):
                    object.figs.append(Figure())
                for i in range(0, len(vertIndexes)):
                    fig = object.figs[i]
                    fig.materialName = materialNames[i]
                    for v in vertIndexes[i]:
                        fig.addVert(vertices[v - 1])
                    for v in uvIndexes[i]:
                        fig.addUV(uvs[v-1])
                    for v in normIndexes[i]:
                        fig.addNorm(normals[v - 1])
                mtlLoader = MtlLoader()
                object.materialsSource = mtlLoader.loadMaterial(materialFile)
                file.close()
                print(".obj file loaded successfully")
            else:
                print("Error in ObjLoader. Cannot open file ", filePath)
        else:
            print(f"obj file {filePath} does not exist!")
        return object


def parseVec3(container, lineSpl):
    i = 1
    vec = vec3()
    # If empty, succ index.
    i = succeedInd(lineSpl, i)
    vec.x = float(lineSpl[i])
    i+=1
    i = succeedInd(lineSpl, i)
    vec.y = float(lineSpl[i])
    i+=1
    if len(lineSpl) > 3:
        i = succeedInd(lineSpl, i)
        vec.z = float(lineSpl[i])
    else:
        vec.z = 0
    container.append(vec)


def parseVec2(container, lineSpl):
    i = 1
    vec = vec2()
    i = succeedInd(lineSpl, i)
    vec.x = float(lineSpl[i])
    i += 1
    i = succeedInd(lineSpl, i)
    vec.y = float(lineSpl[i])
    container.append(vec)


