from typing import List, Dict


class Color:

    def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __repr__(self):
        return f"({str(self.r)}, {str(self.g)}, {self.b})"


class vec2:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y


class vec3(vec2):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y)
        self.z = z

    def __add__(self, other):
        super().__add__(other)
        self.z += other.z


class Figure:

    def __init__(self):
        self.verts: List[vec3] = []
        self.uvs: List[vec3] = []
        self.norms: List[vec3] = []
        self.materialName = ""

    def addVert(self, v):
        self.verts.append(v)

    def addUV(self, v):
        self.uvs.append(v)

    def addNorm(self, v):
        self.norms.append(v)


class Material:

    def __init__(self):
        self.name = ""  # name of the material in.mtl file.
        self.ambientColor = Color()
        self.diffuseColor = Color()
        self.specularColor = Color()
        self.shininess = Color()
        self.transparency = Color()
        self.density = Color()
        self.emission = Color()


class Object3D:

    def __init__(self):
        self.figs: List[Figure] = []  # QVector<figure>
        self.materialsSource: Dict[str, Material] = dict()  # QHash < QString, Material >
        self.startingPoint = vec3(0, 0, 0)
        self.baseCenter = vec3(0, 0, 0)
        self.topCenter = vec3(0, 0, 0)
        self.geometricCenter = vec3(0, 0, 0)
        self.xmin = 0
        self.xmax = 0
        self.zmin = 0
        self.zmax = 0

    def calcCharacteristicPoints(self):
        self.calcCenterOfObjBaseAndTop()
        self.calcGeometricCenter()

    def calcCenterOfObjBaseAndTop(self):
        if len(self.figs) == 0:
            return
        ymin = self.figs[0].verts[0].y
        ymax = ymin
        xmin = self.figs[0].verts[0].x
        xmax = xmin
        zmin = self.figs[0].verts[0].z
        zmax = zmin
        for i in range(0, len(self.figs)):
            for j in range(0, len(self.figs[i].verts)):
                if self.figs[i].verts[j].y < ymin:
                    ymin = self.figs[i].verts[j].y
                if self.figs[i].verts[j].y > ymax:
                    ymax = self.figs[i].verts[j].y
                if self.figs[i].verts[j].x < xmin:
                    xmin = self.figs[i].verts[j].x
                if self.figs[i].verts[j].x > xmax:
                    xmax = self.figs[i].verts[j].x
                if self.figs[i].verts[j].z < zmin:
                    zmin = self.figs[i].verts[j].z
                if self.figs[i].verts[j].z > zmax:
                    zmax = self.figs[i].verts[j].z
        base = vec3(0, 0, 0)
        counterBase = 0
        top = vec3(0, 0, 0)
        counterTop = 0
        for i in range(0, len(self.figs)):
            for j in range(0, len(self.figs[i].verts)):
                if abs(self.figs[i].verts[j].y - ymin) < 0.000001:
                    p = self.figs[i].verts[j]
                    base += p
                    counterBase +=1
                if abs(self.figs[i].verts[j].y - ymax) < 0.000001:
                    p = self.figs[i].verts[j]
                    top += p
                    counterTop +=1
        self.xmax = xmax
        self.xmin = xmin
        self.zmin = zmin
        self.zmax = zmax
        base = vec3(base.x/counterBase, base.y/counterBase, base.z/counterBase)
        top = vec3(top.x/counterTop, top.y/counterTop, top.z/counterTop)
        self.baseCenter = base
        self.topCenter = top

    def calcGeometricCenter(self):
        if len(self.figs) == 0:
            return
        sum = vec3(0, 0, 0)
        numOfEl = 0
        for fig in self.figs:
            for vert in fig.verts:
                sum += vert
            numOfEl += len(fig.verts)

        sum = vec3(sum.x/numOfEl, sum.y/numOfEl, sum.z/numOfEl)
        self.geometricCenter = sum






