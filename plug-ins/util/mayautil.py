__author__ = 'Haarm-Pieter Duiker'
__copyright__ = 'Copyright (C) 2016 - Duiker Research Corp'
__license__ = ''
__maintainer__ = 'Haarm-Pieter Duiker'
__email__ = 'support@duikerresearch.org'
__status__ = 'Production'

__major_version__ = '1'
__minor_version__ = '0'
__change_version__ = '0'
__version__ = '.'.join((__major_version__,
                        __minor_version__,
                        __change_version__))

def createMelPythonCallback(module, function, options=False, parametersList=None, 
    returnType=None, returnTypeIsArray=False):
    mel = ""

    # Arbitrary parameter list and return type
    if parametersList:
        mel += "global proc "

        # return value
        if returnType is None:
            mel += "string"
        else:
            mel += returnType

        if returnTypeIsArray:
            mel += "[]"

        # function name
        mel += " melPythonCallbackOptions_%s_%s(" % (module, function)

        # parameter list
        paramString = ""
        for (paramType, paramName) in parametersList:
            paramString = paramString + ("%s $%s" % (paramType, paramName)) + ", "
        paramString = paramString[:-2]
        mel += "%s) { " % paramString

        # return type
        if returnType is None:
            mel += "    string $result"
        else:
            mel += "    %s $result" % returnType

        if returnTypeIsArray:
            mel += "[]"

        # python module and function
        mel += " = python( \"import %s; %s.%s(" % (module, module, function)

        # arguments for python function
        for (paramType, paramName) in parametersList:
            mel += "\\\"\" + $%s + \"\\\"," % paramName

        mel += ")\" ); " 
        mel += "    return $result; "
        mel += "} "

        # mel function call
        mel += "melPythonCallbackOptions_%s_%s" % (module, function)

    # Return value for python mel command is documented as string[] but seems to return
    # string in some cases. Commands that don't have options are assumed to return string.
    # Commands with options are assumed to return string[]
    elif options:

        mel += "global proc string[] melPythonCallbackOptions_%s_%s(string $options) { " % (module, function)
        mel += "    string $result[] = python( \"import %s; %s.%s(\\\"\" + $options + \"\\\")\" ); " % (module, module, function)
        mel += "    return $result; "
        mel += "} "
        mel += "melPythonCallbackOptions_%s_%s" % (module, function)
    else:
        mel += "global proc string melPythonCallback_%s_%s() { " % (module, function)
        mel += "    string $result = `python( \"import %s; %s.%s()\" )`; " % (module, module, function)
        mel += "    return $result; "
        mel += "} "
        mel += "melPythonCallback_%s_%s" % (module, function)

    return mel