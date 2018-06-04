"""
@author: Zebo Li
Use python scripts to write delegent cpp codes
"""


class CppClass:
    """ Creating a Cpp Class interface and implementations """
    _classname = None
    _privates = None
    _properties = None
    _methods = None
    _superclass = None
    _scopeindent = None

    def __init__(self, classname="Unnamed", privates={}, properties={}, methods={}, superclass=None, scopeindent=0):
        """ 
        Getting basic class informations
            classname: classname
            properties: mapping from variable names to variable types and comment (string: {string, string})
            methods:
                mapping from method names to method properties:
                    example:
                        {
                            "greeting": {
                                "type": "virtual",
                                "return": "void",
                                "comment": "sending some greeting messages."
                                "args": [
                                    "int a",
                                    "int b"
                                ]
                            }
                        }
            superclass: superclass of the current class, type: an object which has _properties and _methods
            scope, whether the class is defined in a particular scope
        """
        self._classname = classname
        self._properties = properties
        self._privates = privates
        self._methods = methods
        self._superclass = superclass
        self._scopeindent = scopeindent


    def getInterface(self):
        """ 
        Getting interface of the class
        return: string
        """
        content = ""
        indent = "\t"*self._scopeindent

        # Declare class
        content += "{INDENT}class {CN}".format(INDENT=indent, CN=self._classname) + "{\n"
        indent += "\t"

        content += "{INDENT}private:\n".format(INDENT=indent[:-1])
        # Define private variables
        for vname, vtype in self._privates.items():
            content += "{INDENT}{T} {V};".format(INDENT=indent, T=vtype["type"], V=vname)
            if "comment" in vtype["comment"]:
                content += " // {C}".format(C=vtype["comment"])
            content += "\n"
        content += "\n"

        content += "{INDENT}public:\n".format(INDENT=indent[:-1])
        # Define variables
        for vname, vtype in self._properties.items():
            content += "{INDENT}{T} {V};".format(INDENT=indent, T=vtype["type"], V=vname)
            if "comment" in vtype["comment"]:
                content += " // {C}".format(C=vtype["comment"])
            content += "\n"
        content += "\n"

        # Declare constructors
        content += "{INDENT}{CN}();\n\n".format(INDENT=indent, CN=self._classname)

        # Declare member methods
        for fun_name, fun_prop in self._methods.items():
            if "type" in fun_prop:
                content += "{INDENT}{T} {R} {F}(".format(INDENT=indent, T=fun_prop["type"], R=fun_prop["return"], F=fun_name)
            else:
                content += "{INDENT}{R} {F}(".format(INDENT=indent, R=fun_prop["return"], F=fun_name)
            for v in fun_prop["args"]:
                content += "{V}, ".format(V=v)
            if content[-1] == " ":
                content = content[:-2]
            content += ");"
            if "comment" in fun_prop:
                content += " // {C}".format(C=fun_prop["comment"])
            content += "\n\n"

        indent = indent[:-1]
        content += indent + "};\n\n"
        return content

    def getImplements(self):
        """ 
        Getting implementation blocks for each method
        return string
        """
        content = ""
        indent = "\t"*self._scopeindent

        # define functions
        for fun_name, fun_prop in self._methods.items():
            if "type" in fun_prop and fun_prop["type"] == "virtual":
                continue
            if "type" in fun_prop:
                content += "{INDENT}{T} {R} {CN}::{F}(".format(
                    INDENT=indent, T=fun_prop["type"], R=fun_prop["return"], CN=self._classname, F=fun_name)
            else:
                content += "{INDENT}{R} {CN}::{F}(".format(
                    INDENT=indent, R=fun_prop["return"], CN=self._classname, F=fun_name)
            for v in fun_prop["args"]:
                content += "{V}, ".format(V=v)
            if content[-1] == " ":
                content = content[:-2]
            content += "){\n"
            if "comment" in fun_prop:
                content += "{INDENT}// {C}\n".format(INDENT=indent, C=fun_prop["comment"])
            indent += "\t"
            content += indent + "YOU\n" + indent + "NEED\n" + indent + "DO\n";
            content += indent + "SOMETHING\n" + indent + "HERE\n";
            content += indent + "return;\n"
            indent = indent[:-1]
            content += indent + "}\n\n\n"
        return content


if __name__ == "__main__":
    kargs = {
        "classname": "SevenDeadlySins",
        "properties": {
            "meriodas": {
                "type": "int",
                "comment": "leader and captain"
            },
            "escarnor": {
                "type": "float",
                "comment": "strongest & warrier"
            }
        },
        "privates": {
            "malin": {
                "type": "bool",
                "comment": "beauty & magician"
            },
            "goodspeed": {
                "type": "string",
                "comment": "True God"
            }
        },
        "methods": {
            "fullCounter": {
                "return": "int",
                "comment": "Meriodas's skill",
                "args": [
                    "int x",
                    "float y",
                    "string z"
                ]
            },
            "crualSun": {
                "type": "inline",
                "return": "double",
                "comment": "Escarnor's skill",
                "args": [
                    "int x",
                    "float y",
                    "string z"
                ]
            },
            "perfectCub": {
                "type": "virtual",
                "return": "bool",
                "comment": "Malin's skill",
                "args": [
                    "int x",
                    "float y",
                    "string z"
                ]
            },
            "amatiros": {
                "return": "string",
                "comment": "Goodspeed's skill",
                "args": [
                    "int x",
                    "float y",
                    "string z"
                ]
            }
        }
    }
    cpp = CppClass(**kargs)
    fp = open("test.cpp", "w")
    fp.write(cpp.getInterface())
    fp.write(cpp.getImplements())
    fp.close()
        

        
        