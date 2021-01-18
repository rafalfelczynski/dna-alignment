from PySide2.QtGui import *
from OpenGL import GL
from Models.object3D import *
from Models.shaders import *
import numpy as np
import shiboken2
import copy


class ObjectDrawer:

    NUM_OF_VALUES_PER_POINT = 17

    def __init__(self):
        self._shaderProgram = QOpenGLShaderProgram()
        self.m_projMatrixLoc = 0
        self.m_mvMatrixLoc = 0
        self.m_normalMatrixLoc = 0
        self.m_lightPosLoc = 0
        self.m_modelMatrixLoc = 0
        self.m_cameraMatrixLoc = 0
        self._colorDLoc = 0
        self._colorALoc = 0
        self._colorSLoc = 0
        self._colorShLoc = 0
        self._transpLoc = 0
        self._vao = QOpenGLVertexArrayObject()
        self._trianglesBuffer = QOpenGLBuffer()
        self._quadsBuffer = QOpenGLBuffer()
        self._polygonsBuffer = QOpenGLBuffer()
        self._triangles: List[GL.GL_FLOAT] = []
        self._quads: List[GL.GL_FLOAT] = []
        self._polygons: List[GL.GL_FLOAT] = []
        self.vaoBinder = ...

    def draw(self, proj: QMatrix4x4, world: QMatrix4x4,
             camera: QMatrix4x4, lightPos: QVector3D, fun: QOpenGLFunctions):
        if len(self._triangles) == 0 and len(self._quads) == 0 and len(self._polygons) == 0:
            return
        self.bindShader(proj, world, camera, lightPos)
        self.bindBuffer(self._trianglesBuffer, fun)
        fun.glDrawArrays(GL.GL_TRIANGLES, 0, (len(self._triangles) // self.NUM_OF_VALUES_PER_POINT))
        self._trianglesBuffer.release()
        self.bindBuffer(self._quadsBuffer, fun)
        fun.glDrawArrays(GL.GL_QUADS, 0, (len(self._quads) // self.NUM_OF_VALUES_PER_POINT))
        self._quadsBuffer.release()
        self.bindBuffer(self._polygonsBuffer, fun)
        fun.glDrawArrays(GL.GL_POINTS, 0, (len(self._polygons) // self.NUM_OF_VALUES_PER_POINT))
        self._polygonsBuffer.release()
        self._shaderProgram.release()

    def createShaderProgramForObj(self):
        self._shaderProgram.removeAllShaders()
        self._shaderProgram.addShaderFromSourceCode(QOpenGLShader.Vertex, VERTEX_SHADER)
        self._shaderProgram.addShaderFromSourceCode(QOpenGLShader.Fragment, FRAGMENT_SHADER)
        self._shaderProgram.bindAttributeLocation("vertex", 0)
        self._shaderProgram.bindAttributeLocation("normal", 1)
        self._shaderProgram.bindAttributeLocation("ambient", 2)
        self._shaderProgram.bindAttributeLocation("diffuse", 3)
        self._shaderProgram.bindAttributeLocation("specular", 4)
        self._shaderProgram.bindAttributeLocation("shininess", 5)
        self._shaderProgram.bindAttributeLocation("transparency", 6)
        self._shaderProgram.link()
        self._shaderProgram.bind()
        self.m_projMatrixLoc = self._shaderProgram.uniformLocation("projMatrix")
        self.m_mvMatrixLoc = self._shaderProgram.uniformLocation("mvMatrix")
        self.m_modelMatrixLoc = self._shaderProgram.uniformLocation("modelMatrix")
        self.m_normalMatrixLoc = self._shaderProgram.uniformLocation("normalMatrix")
        self.m_lightPosLoc = self._shaderProgram.uniformLocation("lightPos")
        self.m_cameraMatrixLoc = self._shaderProgram.uniformLocation("cameraMatrix")
        if not self._vao.isCreated():
            self._vao.create()
        self.createAndAllocateBuffers()
        self._shaderProgram.release()

    def createAndAllocateBuffers(self):
        self._shaderProgram.bind()
        self.vaoBinder = QOpenGLVertexArrayObject.Binder(self._vao)
        self.createAndAllocateBuffer(self._trianglesBuffer, self._triangles)
        self.createAndAllocateBuffer(self._quadsBuffer, self._quads)
        self.createAndAllocateBuffer(self._polygonsBuffer, self._polygons)

    def createAndAllocateBuffer(self, buffer: QOpenGLBuffer, dataVector: List[GL.GLfloat]):
        buffer.create()
        buffer.bind()
        buffer.allocate(np.asarray(dataVector, dtype=GL.GLfloat), len(dataVector) * GL.sizeof(GL.GLfloat))
        buffer.release()

    def bindShader(self, proj: QMatrix4x4, world: QMatrix4x4, camera: QMatrix4x4, lightPos: QVector3D):
        self._shaderProgram.bind()
        self._shaderProgram.setUniformValue(self.m_projMatrixLoc, proj)
        self._shaderProgram.setUniformValue(self.m_modelMatrixLoc, world)
        self._shaderProgram.setUniformValue(self.m_cameraMatrixLoc, camera)
        self._shaderProgram.setUniformValue(self.m_mvMatrixLoc, camera * world)
        self._shaderProgram.setUniformValue(self.m_normalMatrixLoc, world.normalMatrix())
        self._shaderProgram.setUniformValue(self.m_lightPosLoc, lightPos)

    def bindBuffer(self, buffer: QOpenGLBuffer, fun: QOpenGLFunctions):
        buffer.bind()
        fun.glEnableVertexAttribArray(0)
        fun.glEnableVertexAttribArray(1)
        fun.glEnableVertexAttribArray(2)
        fun.glEnableVertexAttribArray(3)
        fun.glEnableVertexAttribArray(4)
        fun.glEnableVertexAttribArray(5)
        fun.glEnableVertexAttribArray(6)
        fun.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 17 * GL.sizeof(GL.GLfloat), shiboken2.VoidPtr(0))
        fun.glVertexAttribPointer(1, 3, GL.GL_FLOAT, GL.GL_FALSE, 17 * GL.sizeof(GL.GLfloat), shiboken2.VoidPtr(3 * GL.sizeof(GL.GLfloat)))
        fun.glVertexAttribPointer(2, 3, GL.GL_FLOAT, GL.GL_FALSE, 17 * GL.sizeof(GL.GLfloat), shiboken2.VoidPtr(6 * GL.sizeof(GL.GLfloat)))
        fun.glVertexAttribPointer(3, 3, GL.GL_FLOAT, GL.GL_FALSE, 17 * GL.sizeof(GL.GLfloat), shiboken2.VoidPtr(9 * GL.sizeof(GL.GLfloat)))
        fun.glVertexAttribPointer(4, 3, GL.GL_FLOAT, GL.GL_FALSE, 17 * GL.sizeof(GL.GLfloat), shiboken2.VoidPtr(12 * GL.sizeof(GL.GLfloat)))
        fun.glVertexAttribPointer(5, 1, GL.GL_FLOAT, GL.GL_FALSE, 17 * GL.sizeof(GL.GLfloat), shiboken2.VoidPtr(15 * GL.sizeof(GL.GLfloat)))
        fun.glVertexAttribPointer(6, 1, GL.GL_FLOAT, GL.GL_FALSE, 17 * GL.sizeof(GL.GLfloat), shiboken2.VoidPtr(16 * GL.sizeof(GL.GLfloat)))

    def updateObject3D(self, obj3D):
        self.transformObjectToRawData(obj3D)

    def transformObjectToRawData(self, obj3D: Object3D):
        self._triangles.clear()
        self._quads.clear()
        self._polygons.clear()
        for j in range(0, len(obj3D.figs)):
            fig = obj3D.figs[j]
            mat = obj3D.materialsSource[fig.materialName]
            target = ...
            if len(fig.verts) == 3:
                target = self._triangles
            elif len(fig.verts) == 4:
                target = self._quads
            else:
                target = self._polygons
            self.fillTargetVectorWithFigurePoints(target, fig, mat)
        self.createAndAllocateBuffers()

    def fillTargetVectorWithFigurePoints(self, target, fig: Figure, mat: Material):
        for k in range(0, len(fig.verts)):
            v: vec3 = fig.verts[k]
            target.append(v.x)
            target.append(v.y)
            target.append(v.z)
            norm = vec3()
            if len(fig.norms) < k:
                norm = vec3(0, 1, 0)
            else:
                norm = fig.norms[k]
            target.extend([norm.x, norm.y, norm.z])
            target.extend([mat.ambientColor.r, mat.ambientColor.g, mat.ambientColor.b])
            target.extend([mat.diffuseColor.r, mat.diffuseColor.g, mat.diffuseColor.b])
            target.extend([mat.specularColor.r, mat.specularColor.g, mat.specularColor.b])
            target.append(mat.shininess)
            target.append(mat.transparency)




