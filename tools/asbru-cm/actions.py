#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr", "/etc"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf asbru-cm_6.2.2-1.deb")
    shelltools.system("tar xvf data.tar.xz")
def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "etc")
