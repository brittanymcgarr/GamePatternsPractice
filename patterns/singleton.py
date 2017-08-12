################################################################################
## Singleton.py                                                               ##
##                                                                            ##
## Singletons are the global variables of the pattern world; they had a       ##
## compelling case for use at one point, but should now be limited to few, if ##
## any at all. Good for limiting resources to one instance.                   ##
##                                                                            ##
################################################################################


class Singleton:
    # The object's instance reference
    instance = None

    # The Singleton's outer constructor
    # Ensures only one instance is active
    def __init__(self, resource):
        if not self.instance:
            Singleton.instance = Singleton.__Singleton(resource)
        else:
            Singleton.instance.resource = resource

    # Because the resource is inaccessible through Singleton alone,
    # redefine the getattr function to call on the instance
    def __getattr__(self, argument):
        return getattr(self.instance, argument)

    # A nested class for maintaining singularity
    class __Singleton:
        # Constructor for setting the resource
        def __init__(self, resource):
            self.resource = resource

        # String representation of the class
        def __str__(self):
            return repr(self) + str(self.resource)
