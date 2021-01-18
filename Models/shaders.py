VERTEX_SHADER =\
            "#version 330 \n"\
            "in vec3 vertex;\n"\
            "in vec3 normal;\n"\
            "in vec3 ambient;\n"\
            "in vec3 diffuse;\n"\
            "in vec3 specular;\n"\
            "in float transparency;\n"\
            "in float shininess;\n"\
            "out vec3 vert;\n"\
            "out vec3 vertNormal;\n"\
            "uniform mat4 projMatrix;\n"\
            "uniform mat4 mvMatrix;\n"\
            "uniform mat4 cameraMatrix;\n"\
            "uniform mat4 modelMatrix;\n"\
            "uniform mat3 normalMatrix;\n"\
            "out vec3 colorA;\n"\
            "out vec3 colorD;\n"\
            "out vec3 colorS;\n"\
            "out float colorSh;\n"\
            "out vec3 fragPosition;\n"\
            "out float transp;\n"\
            "void main() {\n"\
            "   vert = vertex;\n"\
            "   vertNormal = normalize(normalMatrix * normal);\n"\
            "	colorA = ambient;\n"\
            "	colorD = diffuse;\n"\
            "	colorS = specular;\n"\
            "	colorSh = shininess;\n"\
            "	fragPosition = vec3(mvMatrix * vec4(vert, 1.0));"\
            "	transp = transparency;\n"\
            "   gl_Position = (projMatrix * cameraMatrix * modelMatrix * vec4(vert,1));\n"\
            "}\n"

FRAGMENT_SHADER =\
            "#version 330 \n"\
            "in highp vec3 vert;\n"\
            "in highp vec3 vertNormal;\n"\
            "uniform highp vec3 lightPos;\n"\
            "in vec3 colorA;\n"\
            "in vec3 colorD;\n"\
            "in vec3 colorS;\n"\
            "in float colorSh;\n"\
            "in vec3 fragPosition;\n"\
            "in float transp;\n"\
            "out vec4 FragColor;\n"\
            "void light(vec3 position, vec3 norm, out vec3 ambient, out vec3 diffuse, out vec3 spec )\n"\
            "{\n"\
            "	vec3 n = normalize(norm);\n"\
            "	vec3 s = normalize(lightPos - position);\n"\
            "	vec3 v = normalize(-position);\n"\
            "	vec3 r = normalize(reflect(-s, n));\n"\
            "	ambient = 0.1 *colorA;\n"\
            "	float sDotN = max(dot(s,n), 0.0);\n"\
            "	diffuse = 1.0 *colorD *sDotN;\n"\
            "	spec = 1.0 *colorS *pow(max(dot(r,v), 0.0), colorSh);\n"\
            "}\n"\
            "void main() {\n"\
            "	vec3 ambientSum = vec3(0);\n"\
            "	vec3 diffuseSum = vec3(0);\n"\
            "	vec3 specSum = vec3(0);\n"\
            "	vec3 ambient, diffuse, spec;\n"\
            "	if(gl_FrontFacing){\n"\
            "		light(vert, vertNormal, ambient, diffuse, spec );\n"\
            "		ambientSum += ambient;\n"\
            "		diffuseSum += diffuse;\n"\
            "		specSum += spec;\n"\
            "	}else{\n"\
            "		light(vert, -vertNormal, ambient, diffuse, spec );\n"\
            "		ambientSum += ambient;\n"\
            "		diffuseSum += diffuse;\n"\
            "		specSum += spec;\n"\
            "	}\n"\
            "	FragColor = vec4(ambientSum + diffuseSum, transp) + vec4(specSum, 0.0);\n"\
            "}\n"\


