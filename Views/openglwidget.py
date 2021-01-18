from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from OpenGL import GL
from Models.object3D import Object3D
from Controllers.objDrawer import ObjectDrawer


class MyOpenGLWidget(QOpenGLWidget, QOpenGLFunctions):

    NUM_OF_SAMPLES = 16
    ALPHA_BUFFER_SIZE = 8
    DEPTH_BUFFER_SIZE = 8
    STARTING_CAMERA_XROTATION = 0

    DISTANCE_FROM_CAM_TO_OBJECT_TOP = 350
    CAMERA_PROJECTION_ANGLE = 45.0
    CAMERA_NEAR_CLIP = 1.0
    CAMERA_FAR_CLIP = 2000.0
    ANIMATION_MILISECONDS_INTERVAL = 20.0

    def __init__(self, parent=None):
        QOpenGLWidget.__init__(self, parent)
        QOpenGLFunctions.__init__(self)
        self.lastYRot = 0
        self.lastXRot = 0
        self.xRotation = self.STARTING_CAMERA_XROTATION
        self.yRotation = 0
        self.zoomFactor = 1
        self.lastYpos = 0
        self.lastXpos = 0
        self.xCenterEyePosition = 0
        self.yCenterEyePosition = 0
        self.zCenterEyePosition = 0
        self.xCamLookAt = 0
        self.yCamLookAt = 0
        self.zCamLookAt = 0
        self.camUpVector = QVector3D(0, 1, 0)
        self.m_lightPos = QVector3D(0, 600, 600)
        self.m_proj = QMatrix4x4()
        self.m_camera = QMatrix4x4()
        self.m_world = QMatrix4x4()
        self._currentAnimDirection = -1
        self._animationStarted = False
        self._pressedWhileAnimation = False
        self._obj3D = Object3D()
        self._objDrawer = ObjectDrawer()
        self.animationTimer = QTimer()
        self.animLambdaConnection = ...
        format = QSurfaceFormat()
        format.setProfile(format.CompatibilityProfile)
        format.setSamples(self.NUM_OF_SAMPLES)
        format.setAlphaBufferSize(sys.getsizeof(GL.GLfloat) * self.ALPHA_BUFFER_SIZE)
        format.setDepthBufferSize(sys.getsizeof(GL.GLfloat) * self.DEPTH_BUFFER_SIZE)
        format.setStereo(True)
        self.setFormat(format)
        self.lastDegPerSec = 0
        self._hiddenWhileAnimating = False

    def initializeGL(self) -> None:
        self.initializeOpenGLFunctions()
        self.glClearColor(0.2, 0.2, 0.2, 1.0)
        self._objDrawer.createShaderProgramForObj()

    def paintGL(self) -> None:
        self.makeCurrent()
        self.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        self.glEnable(GL.GL_DEPTH_TEST)
        self.glEnable(GL.GL_BLEND)
        self.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        self.m_proj.setToIdentity()
        self.m_proj.perspective(self.CAMERA_PROJECTION_ANGLE * self.zoomFactor, self.width() / self.height(),
                                self.CAMERA_NEAR_CLIP, self.CAMERA_FAR_CLIP)
        self.m_camera.setToIdentity()
        self.m_camera.lookAt(QVector3D(self.xCenterEyePosition, self.yCenterEyePosition, self.zCenterEyePosition),
                             QVector3D(self.xCamLookAt, self.yCamLookAt, self.zCamLookAt),
                             self.camUpVector)
        self.m_world.setToIdentity()
        self.m_world.translate(self.xCamLookAt, self.yCamLookAt, self.zCamLookAt)
        self.m_world.rotate(self.yRotation, 0.0, 1.0, 0.0)
        self.m_world.rotate(self.xRotation, 1.0, 0.0, 0.0)
        self.m_world.translate(-self.xCamLookAt, -self.yCamLookAt, -self.zCamLookAt)
        self._objDrawer.draw(self.m_proj, self.m_world, self.m_camera, self.m_lightPos, self)
        # Draw semi-transparent quad on whole screen to make an illusion of helix rotating in the background
        self.drawBackgroundQuad()

    def drawBackgroundQuad(self):
        GL.glBegin(GL.GL_QUADS)
        GL.glColor4f(0.0, 0.0, 0.0, 0.6)
        GL.glVertex3f(-self.x() / 2, self.y() / 2, 0)
        GL.glVertex3f(self.x() / 2, self.y() / 2, 0)
        GL.glVertex3f(self.x() / 2, -self.y() / 2, 0)
        GL.glVertex3f(-self.x() / 2, -self.y() / 2, 0)
        GL.glEnd()

    def resizeGL(self, w:int, h:int) -> None:
        super().resizeGL(w, h)

    def setObject3D(self, obj):
        self._obj3D = obj
        self.changeOpenGLCameraLookAtCoordinates()
        self._objDrawer.updateObject3D(self._obj3D)
        self.update()

    def changeOpenGLCameraLookAtCoordinates(self):
        self.xCamLookAt = self._obj3D.geometricCenter.x
        self.yCamLookAt = self._obj3D.geometricCenter.y
        self.zCamLookAt = self._obj3D.geometricCenter.z
        self.xCenterEyePosition = self._obj3D.geometricCenter.x
        self.yCenterEyePosition = self._obj3D.geometricCenter.y
        self.zCenterEyePosition = self._obj3D.geometricCenter.z + self.DISTANCE_FROM_CAM_TO_OBJECT_TOP

    def showEvent(self, event):
        if self._hiddenWhileAnimating:
            self.startAnimation(self.lastDegPerSec)

    def hideEvent(self, event):
        if self._animationStarted:
            self._hiddenWhileAnimating = True
            self.stopAnimation()

    def rotateCamera(self, pos):
        dy = (pos.y() - self.lastYRot) / 2.0
        dx = (pos.x() - self.lastXRot) / 2.0
        self.xRotation += dy
        self.yRotation += dx
        self.update()
        self.lastXRot = pos.x()
        self.lastYRot = pos.y()

    def moveCamera(self, pos):
        dy = (pos.y() - self.lastYpos) / 20.0
        dx = (pos.x() - self.lastXpos) / 20.0
        self.xCenterEyePosition += dx
        self.yCenterEyePosition -= dy
        self.xCamLookAt += dx
        self.yCamLookAt -= dy
        self.update()
        self.lastXpos = pos.x()
        self.lastYpos = pos.y()

    def storePosition(self, pos):
        self.lastXpos = pos.x()
        self.lastYpos = pos.y()

    def storeRotation(self, rot):
        self.lastXRot = rot.x()
        self.lastYRot = rot.y()

    def startAnimation(self, degPerSec):
        self.lastDegPerSec = degPerSec
        x = degPerSec / (1000 / self.ANIMATION_MILISECONDS_INTERVAL)
        if self.animLambdaConnection is not ...:
            self.animationTimer.timeout.disconnect()
        self.animationTimer.setInterval(int(self.ANIMATION_MILISECONDS_INTERVAL))
        self.animationTimer.timeout.connect(lambda: self.rotateCamera(QPointF(self.lastXRot, self.lastYRot + self._currentAnimDirection * x)))
        self.animationTimer.start()
        self._animationStarted = True

    def stopAnimation(self):
        if self._animationStarted:
            self.animationTimer.timeout.disconnect()
            self.animationTimer.stop()
            self._animationStarted = False



