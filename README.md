# OTBinUtils

OTBinUtils is a utility tool for OT binary files like dat, spr, otbm and otb. The goal of this tool is to provide a fast way of editing such files with, for example, a text editor. It parses those files and output the content in a **JSON** format.

At first, it will support the current [TFS] version of the files, but in the future it should support from version 7.4.

### Development

OTBinUtils is developed in Python and should work with Python version 3.4 and above (not tested with Python < 3.4).

### Todos

 * tdat - parse .dat file and output json file with it's content.
    * [x] parse
    * [x] output
 * tspr - parse .spr files and output json and png files with it's content.
    * [ ] parse 
    * [ ] output
 * otb - parse .otb files and output json file with it's content.
    * [ ] parse
    * [ ] output
 * otbm - parse .otbm and .xml files and output json file with it's content.
    * [ ] parse
    * [ ] output

   [TFS]: <https://github.com/otland/forgottenserver>
