################################################################################
## Flyweight                                                                  ##
##                                                                            ##
## Flyweight patterns share similar attributes as a base model with created   ##
## instances expanding on the same, underlying model. Great pattern for       ##
## graphics as loading the same mesh and patterns repeatedly is very CPU      ##
## intensive and absurd when variations are minor.                            ##
##                                                                            ##
################################################################################


class BaseEntity:
    # Class-level variables that are shared
    _mesh = None
    _texture = None

    # The base constructor
    # Using graphic actor as example
    def __init__(self, mesh=None, texture=None):
        # Instance level mesh and textures
        if not BaseEntity._mesh:
            BaseEntity._mesh = mesh

        if not BaseEntity._texture:
            BaseEntity._texture = texture

    # Possible functions
    def set_position(self, x=0, y=0, z=0):
        self.position = [x, y, z]

    def translate_position(self, x=0, y=0, z=0):
        if self.position:
            self.position[0] += x
            self.position[1] += y

            if len(self.position) >= 3:
                self.position[2] += z


class Actor(BaseEntity):
    def __init__(role_id, action, height):
        self.role_id = role_id
        self.action = action
        self.height = height
