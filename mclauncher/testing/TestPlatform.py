from mclauncher.implementation.common import Platform

if __name__ == '__main__':
    p = Platform.Platform.Instance()  # @UndefinedVariable
    print p.getWorkingDirectory()
    p.setWorkingDirectory("TestDir")
    print p.getWorkingDirectory()