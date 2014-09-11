from mclauncher.implementation.common import Platform

if __name__ == '__main__':
    p = Platform.Platform()
    print p.getWorkingDirectory()
    p.setWorkingDirectory("TestDir")
    print p.getWorkingDirectory()