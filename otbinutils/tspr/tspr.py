from otbinutils.fileutils import fileutils
import json

SPRITE_SIZE = 32
SPRITE_DATA_SIZE = SPRITE_SIZE * SPRITE_SIZE * 4


class TSpr():
    def __init__(self, version):
        self.version = version
        self.file = fileutils.File(version, "spr")
        self.__read_file()

    def __iter__(self):
        for key, value in list(self.__dict__.items()):
            if key == "file":
                continue
            else:
                yield (key, value)

    def __read_file(self):
        self.spr_version = self.file.read_int32()
        self.spr_count = self.file.read_int32()
        sprite_offset = self.file.tell()
        self.sprites = []

        for sprite_id in range(self.spr_count):
            self.file.seek(sprite_id * 4 + sprite_offset)
            sprite_address = self.file.read_int32()
            
            if sprite_address == 0:
                continue

            self.file.seek(sprite_address)

            for _ in range(3):
                self.file.read_byte()

            pixel_data_size = self.file.read_int16()
            read = 0
            write_pos = 0
            pixels = [0] * SPRITE_DATA_SIZE

            while(read < pixel_data_size and write_pos < SPRITE_SIZE):
                transparent_pixels = self.file.read_int16()
                colored_pixels = self.file.read_int16()

                pixel = 0
                while pixel < transparent_pixels and write_pos < SPRITE_DATA_SIZE:
                    pixel = pixel + 1
                    write_pos = write_pos + 4

                pixel = 0
                while pixel < colored_pixels and write_pos < SPRITE_DATA_SIZE:                   
                    pixels[write_pos + 0] = self.file.read_int16()
                    pixels[write_pos + 1] = self.file.read_int16()
                    pixels[write_pos + 2] = self.file.read_int16()
                    pixel = pixel + 1
                    write_pos = write_pos + 4


                read = read + 3 * colored_pixels

            self.sprites.append(pixels)



        print("version:", self.spr_version)
        print("count:", self.spr_count)

        print("ae")

    def to_json(self):
        with open("output/"+str(self.version)+"/tspr.json", 'w+') as outfile:
            json.dump(self, outfile, default=lambda o: dict(o), sort_keys=True, indent=4, ensure_ascii=False)