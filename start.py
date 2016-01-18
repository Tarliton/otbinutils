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

from otbinutils import otbinutils


version = 1076
otbinutils = otbinutils.OtBinUtils(version)
print(otbinutils.t_dat.version)
print(otbinutils.t_spr.version)
otbinutils.t_dat.to_json()
otbinutils.t_dat.to_dat()
print("leu1 ",otbinutils.t_dat.file.read1)
print("leu16 ",otbinutils.t_dat.file.read16)
print("leu32 ",otbinutils.t_dat.file.read32)
print("leustr ",otbinutils.t_dat.file.readstr)
print("total ", otbinutils.t_dat.file.read1 + otbinutils.t_dat.file.read16+otbinutils.t_dat.file.read32+otbinutils.t_dat.file.readstr)
print("escreveu1",otbinutils.t_dat.file.written1)
print("escreveu16",otbinutils.t_dat.file.written16)
print("escreveu32",otbinutils.t_dat.file.written32)
print("escreveustr",otbinutils.t_dat.file.writtenstr)
print("total ", otbinutils.t_dat.file.written1 + otbinutils.t_dat.file.written16+otbinutils.t_dat.file.written32+otbinutils.t_dat.file.writtenstr)