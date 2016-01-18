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
        self.file_export = open("output/"+str(version)+"/Tibia"+"."+extension, "wb")
        self.read1 = 0
        self.read16 = 0
        self.read32 = 0
        self.readstr = 0
        self.written1 = 0
        self.written16 = 0
        self.written32 = 0
        self.writtenstr = 0
        self.cont = 0

    def __del__(self):
        self.file.close()

    def read_int32(self):
        chunck = self.file.read(4)
        self.read32 = self.read32 + 4
        return struct.unpack('I',chunck)[0]

    def read_int16(self):
        chunck = self.file.read(2)
        self.read16 = self.read16 + 2
        return struct.unpack('H',chunck)[0]

    def read_byte(self):
        chunck = self.file.read(1)
        self.read1 = self.read1 + 1
        return struct.unpack('B',chunck)[0]

    def read_string(self, size):
        chunck = self.file.read(size)
        self.readstr = self.readstr + size
        return str(chunck, "iso-8859-1")

    def write_int32(self, value):
        chunck = struct.pack('=I', value)
        self.written32 = self.written32 + 4
        self.file_export.write(chunck)
        return

    def write_int16(self, value):
        chunck = struct.pack('H', value)
        self.written16 = self.written16 + 2
        self.file_export.write(chunck)
        return

    def write_byte(self, value):
        chunck = struct.pack('B', value)
        self.written1 = self.written1 + 1
        self.cont = self.cont + 1
        #print("escreveu ", value)
        self.file_export.write(chunck)
        return

    def write_string(self, value):
        self.writtenstr = self.writtenstr + len(value)
        self.file_export.write(value.encode("iso-8859-1"))
        return
