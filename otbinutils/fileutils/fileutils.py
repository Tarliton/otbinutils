#Copyright (C) 2014, 2015  Tarliton Godoy
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os
import struct

class File():
    def __init__(self, version, extension):
        self.file = open("things/"+str(version)+"/Tibia"+"."+extension, "rb")

    def __del__(self):
        self.file.close()

    def read_int32(self):
        chunck = self.file.read(4)
        return struct.unpack('I',chunck)[0]

    def read_int16(self):
        chunck = self.file.read(2)
        return struct.unpack('H',chunck)[0]

    def read_byte(self):
        chunck = self.file.read(1)
        return struct.unpack('B',chunck)[0]

    def read_string(self, size):
        chunck = self.file.read(size)
        return str(chunck, "iso-8859-1")