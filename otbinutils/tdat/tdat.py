from otbinutils.fileutils import fileutils
from enum import IntEnum
import json

class TDat():
    def __init__(self, version):
        self.version = version
        self.file = fileutils.File(version, "dat")
        self.__read_file()

    def __iter__(self):
        for key, value in list(self.__dict__.items()):
            if key == "file":
                continue
            else:
                yield (key, value)

    def __read_file(self):
        self.dat_version = self.file.read_int32()
        self.item_count = self.file.read_int16()
        self.outfit_count = self.file.read_int16()
        self.effect_count = self.file.read_int16()
        self.projectile_count = self.file.read_int16()
        self.max_ID = self.item_count + self.outfit_count + self.effect_count + self.projectile_count
        self.items = []
        ID = 100
        count = 0
        history = []
        pos = 0
        while ID <= self.max_ID:
            current_item = ItemData()
            current_item.ID = ID
            history.append([])
            while True:
                flag = self.file.read_byte()
                history[pos].append(flag)
                if flag == DAT.Flag_Bank:
                    current_item.isBank = True
                    current_item.Waypoints = self.file.read_int16()
                elif flag == DAT.Flag_Clip:
                    current_item.isClip = True
                elif flag == DAT.Flag_Bottom:
                    current_item.isBottom = True
                elif flag == DAT.Flag_Top:
                    current_item.isTop = True
                elif flag == DAT.Flag_Container:
                    current_item.isContainer = True
                elif flag == DAT.Flag_Cumulative:
                    current_item.isCumulative = True
                elif flag == DAT.Flag_UseAble:
                    current_item.isUseAble = True
                elif flag == DAT.Flag_ForceUse:
                    current_item.isForceUse = True
                elif flag == DAT.Flag_MultiUse:
                    current_item.isMultiUse = True
                elif flag == DAT.Flag_Write:
                    current_item.isWriteable = True
                    current_item.MaxTextLength = self.file.read_int16()
                elif flag == DAT.Flag_WriteOnce:
                    current_item.isWriteableOnce = True
                    current_item.MaxTextLength = self.file.read_int16()
                elif flag == DAT.Flag_LiquidContainer :
                    current_item.isLiquidContainer = True
                elif flag == DAT.Flag_LiquidPool :
                    current_item.isLiquidPool = True
                elif flag == DAT.Flag_Unpass :
                    current_item.isUnpassable = True
                elif flag == DAT.Flag_Unmove :
                    current_item.isUnmoveable = True
                elif flag == DAT.Flag_Unsight :
                    current_item.isUnsight = True
                elif flag == DAT.Flag_Avoid :
                    current_item.isAvoid = True
                elif flag == DAT.Flag_NOMOVEMENTANIMATION :
                    current_item.noMovmentAction = True
                elif flag == DAT.Flag_Take :
                    current_item.isTakeable = True
                elif flag == DAT.Flag_Hang :
                    current_item.isHangable = True
                elif flag == DAT.Flag_HookSouth:
                    current_item.isHookSouth = True
                elif flag == DAT.Flag_HookEast:
                    current_item.isHookEast = True
                elif flag == DAT.Flag_Rotate:
                    current_item.isRotateable = True
                elif flag == DAT.Flag_Light :
                    current_item.isLight = True
                    current_item.Brightness = self.file.read_int16()
                    current_item.LightColor = self.file.read_int16()
                elif flag == DAT.Flag_DontHide :
                    current_item.isDontHide = True
                elif flag == DAT.Flag_Translucent :
                    current_item.isTranslucent = True
                elif flag == DAT.Flag_Shift :
                    current_item.isDisplaced = True
                    current_item.DisplacementX = self.file.read_int16()
                    current_item.DisplacementY = self.file.read_int16()
                elif flag == DAT.Flag_Height :
                    current_item.isHeight = True
                    current_item.Elevation = self.file.read_int16()
                elif flag == DAT.Flag_LyingObject :
                    current_item.isLyingObject = True
                elif flag == DAT.Flag_AnimateAlways :
                    current_item.isAnimateAlways = True
                elif flag == DAT.Flag_Automap :
                    current_item.isAutomap = True
                    current_item.isAutomapColor = self.file.read_int16()
                elif flag == DAT.Flag_LensHelp :
                    current_item.isLensHelp = True
                    current_item.LensHelp = self.file.read_int16()
                elif flag == DAT.Flag_FullBank :
                    current_item.isFullBank = True
                elif flag == DAT.Flag_IgnoreLook :
                    current_item.isIgnoreLook = True
                elif flag == DAT.Flag_Clothes :
                    current_item.isCloth = True
                    current_item.ClothSlot = self.file.read_int16()
                elif flag == DAT.Flag_Market :
                    current_item.isMarket = True
                    current_item.MarketCategory = self.file.read_int16()
                    current_item.MarketTradeAs = self.file.read_int16()
                    current_item.MarketShowAs = self.file.read_int16()
                    current_item.MarketNameLength = self.file.read_int16()
                    current_item.MarketName = self.file.read_string(current_item.MarketNameLength)
                    current_item.MarketRestrictProfession = self.file.read_int16()
                    current_item.MarketRestrictLevel = self.file.read_int16()
                elif flag == DAT.Flag_DefaultAction:
                    current_item.isDefaultAction = True
                    current_item.DefaultAction = self.file.read_int16()
                elif flag == DAT.BreakFlag:
                    count = count + 1
                    break
            
            current_item.FrameGroupCount = self.file.read_byte() if (ID > self.item_count and ID <= (self.item_count + self.outfit_count)) else 1
            for frame in range(current_item.FrameGroupCount):
                current_item.FrameGroupID.append( self.file.read_byte() if (ID > self.item_count and ID <= (self.item_count + self.outfit_count)) else 0)

                width = self.file.read_byte()
                height = self.file.read_byte()
                current_item.Width.append(width)
                current_item.Height.append(height)
                if width > 1 or height > 1:
                    current_item.ExactSize.append(self.file.read_byte())
                else:
                    current_item.ExactSize.append(-1)

                layers = self.file.read_byte()
                pattern_width = self.file.read_byte()
                pattern_height = self.file.read_byte()
                patter_depth = self.file.read_byte()
                phases = self.file.read_byte()
                current_item.Layers.append(layers)
                current_item.PatternWidth.append(pattern_width)
                current_item.PatternHeight.append(pattern_height)
                current_item.PatternDepth.append(patter_depth)
                current_item.Phases.append(phases)

                self.__animator_unserialize(current_item, frame)

                numSpr = current_item.Width[frame] * current_item.Height[frame]
                numSpr = numSpr * current_item.Layers[frame] * current_item.PatternWidth[frame]
                numSpr = numSpr * current_item.PatternHeight[frame] * current_item.PatternDepth[frame]
                numSpr = numSpr * current_item.Phases[frame]

                current_item.NumberOfSprites.append(numSpr)
                current_item.Sprites.append([])

                for spr in range(current_item.NumberOfSprites[frame]):
                    current_item.Sprites[frame].append(self.file.read_int32())

            self.items.append(current_item)
            ID = ID +1
            pos = pos + 1

    def __animator_unserialize(self, current_item, frame):
        if current_item.Phases[frame] > 1:
            loc8 = 0
            current_item.async.append(self.file.read_byte())
            current_item.loop_count.append(self.file.read_int32())
            current_item.start_phase.append(self.file.read_byte())
            current_item.minimum.append([])
            current_item.maximum.append([])
            while loc8 < current_item.Phases[frame]:
                current_item.minimum[frame].append(self.file.read_int32())
                current_item.maximum[frame].append(self.file.read_int32())
                loc8 = loc8 + 1
        else:
            current_item.async.append(-1)
            current_item.loop_count.append(-1)
            current_item.start_phase.append(-1)
            current_item.minimum.append([])
            current_item.maximum.append([])


    def to_json(self):
        with open("output/"+str(self.version)+"/tdat.json", 'w+') as outfile:
            json.dump(self, outfile, default=lambda o: dict(o), sort_keys=True, indent=4, ensure_ascii=False)

    def to_dat(self):
        with open("output/"+str(self.version)+"/tdat.json", 'r') as inputfile:
            data = json.load(inputfile)
            self.file.write_int32(data['dat_version'])
            self.file.write_int16(data['item_count'])
            self.file.write_int16(data['outfit_count'])
            self.file.write_int16(data['effect_count'])
            self.file.write_int16(data['projectile_count'])
            count = 0
            for item in data['items']:
                while True:
                    if "isBank" in item:
                        self.file.write_byte(DAT.Flag_Bank)
                        self.file.write_int16(item['Waypoints'])
                        item.pop('isBank')
                        item.pop('Waypoints')
                    elif "isClip" in item:
                        self.file.write_byte(DAT.Flag_Clip)
                        item.pop('isClip')
                    elif "isBottom" in item:
                        self.file.write_byte(DAT.Flag_Bottom)
                        item.pop('isBottom')
                    elif "isTop" in item:
                        self.file.write_byte(DAT.Flag_Top)
                        item.pop('isTop')
                    elif "isUseAble" in item:
                        self.file.write_byte(DAT.Flag_UseAble)
                        item.pop('isUseAble')
                    elif "isContainer" in item:
                        self.file.write_byte(DAT.Flag_Container)
                        item.pop('isContainer')
                    elif "isCumulative" in item:
                        self.file.write_byte(DAT.Flag_Cumulative)
                        item.pop('isCumulative')
                    elif "isForceUse" in item:
                        self.file.write_byte(DAT.Flag_ForceUse)
                        item.pop('isForceUse')
                    elif "isMultiUse" in item:
                        self.file.write_byte(DAT.Flag_MultiUse)
                        item.pop('isMultiUse')
                    elif "isWriteable" in item:
                        self.file.write_byte(DAT.Flag_Write)
                        self.file.write_int16(item['MaxTextLength'])
                        item.pop('isWriteable')
                    elif "isWriteableOnce" in item:
                        self.file.write_byte(DAT.Flag_WriteOnce)
                        self.file.write_int16(item['MaxTextLength'])
                        item.pop('isWriteableOnce')
                    elif "isLiquidContainer" in item:
                        self.file.write_byte(DAT.Flag_LiquidContainer)
                        item.pop('isLiquidContainer')
                    elif "isLiquidPool" in item:
                        self.file.write_byte(DAT.Flag_LiquidPool)
                        item.pop('isLiquidPool')
                    elif "isUnpassable" in item:
                        self.file.write_byte(DAT.Flag_Unpass)
                        item.pop('isUnpassable')
                    elif "isUnmoveable" in item:
                        self.file.write_byte(DAT.Flag_Unmove)
                        item.pop('isUnmoveable')
                    elif "isUnsight" in item:
                        self.file.write_byte(DAT.Flag_Unsight)
                        item.pop('isUnsight')
                    elif "isAvoid" in item:
                        self.file.write_byte(DAT.Flag_Avoid)
                        item.pop('isAvoid')
                    elif "isTakeable" in item:
                        self.file.write_byte(DAT.Flag_Take)
                        item.pop('isTakeable')
                    elif "isHangable" in item:
                        self.file.write_byte(DAT.Flag_Hang)
                        item.pop('isHangable')
                    elif "isHookSouth" in item:
                        self.file.write_byte(DAT.Flag_HookSouth)
                        item.pop('isHookSouth')
                    elif "isHookEast" in item:
                        self.file.write_byte(DAT.Flag_HookEast)
                        item.pop('isHookEast')
                    elif "isRotateable" in item:
                        self.file.write_byte(DAT.Flag_Rotate)
                        item.pop('isRotateable')
                    elif "noMovmentAction" in item:
                        self.file.write_byte(DAT.Flag_NOMOVEMENTANIMATION)
                        item.pop('noMovmentAction')
                    elif "isLight" in item:
                        self.file.write_byte(DAT.Flag_Light)
                        self.file.write_int16(item['Brightness'])
                        self.file.write_int16(item['LightColor'])
                        item.pop('isLight')
                        item.pop('Brightness')
                        item.pop('LightColor')
                    elif "isDontHide" in item:
                        self.file.write_byte(DAT.Flag_DontHide)
                        item.pop('isDontHide')
                    elif "isTranslucent" in item:
                        self.file.write_byte(DAT.Flag_Translucent)
                        item.pop('isTranslucent')
                    elif "isMarket" in item:
                        self.file.write_byte(DAT.Flag_Market)
                        self.file.write_int16(item['MarketCategory'])
                        self.file.write_int16(item['MarketTradeAs'])
                        self.file.write_int16(item['MarketShowAs'])
                        self.file.write_int16(item['MarketNameLength'])
                        self.file.write_string(item['MarketName'])
                        self.file.write_int16(item['MarketRestrictProfession'])
                        self.file.write_int16(item['MarketRestrictLevel'])
                        item.pop('isMarket')
                        item.pop('MarketCategory')
                        item.pop('MarketTradeAs')
                        item.pop('MarketShowAs')
                        item.pop('MarketNameLength')
                        item.pop('MarketName')
                        item.pop('MarketRestrictProfession')
                        item.pop('MarketRestrictLevel')
                    elif "isDisplaced" in item:
                        self.file.write_byte(DAT.Flag_Shift)
                        self.file.write_int16(item['DisplacementX'])
                        self.file.write_int16(item['DisplacementY'])
                        item.pop('isDisplaced')
                        item.pop('DisplacementX')
                        item.pop('DisplacementY')
                    elif "isHeight" in item:
                        self.file.write_byte(DAT.Flag_Height)
                        self.file.write_int16(item['Elevation'])
                        item.pop('isHeight')
                        item.pop('Elevation')
                    elif "isLyingObject" in item:
                        self.file.write_byte(DAT.Flag_LyingObject)
                        item.pop('isLyingObject')
                    elif "isAnimateAlways" in item:
                        self.file.write_byte(DAT.Flag_AnimateAlways)
                        item.pop('isAnimateAlways')
                    elif "isAutomap" in item:
                        self.file.write_byte(DAT.Flag_Automap)
                        self.file.write_int16(item['isAutomapColor'])
                        item.pop('isAutomap')
                        item.pop('isAutomapColor')
                    elif "isLensHelp" in item:
                        self.file.write_byte(DAT.Flag_LensHelp)
                        self.file.write_int16(item['LensHelp'])
                        item.pop('isLensHelp')
                        item.pop('LensHelp')
                    elif "isFullBank" in item:
                        self.file.write_byte(DAT.Flag_FullBank)
                        item.pop('isFullBank')
                    elif "isIgnoreLook" in item:
                        self.file.write_byte(DAT.Flag_IgnoreLook)
                        item.pop('isIgnoreLook')
                    elif "isCloth" in item:
                        self.file.write_byte(DAT.Flag_Clothes)
                        self.file.write_int16(item['ClothSlot'])
                        item.pop('isCloth')
                        item.pop('ClothSlot')
                    elif "isDefaultAction" in item:
                        self.file.write_byte(DAT.Flag_DefaultAction)
                        self.file.write_int16(item['DefaultAction'])
                        item.pop('isDefaultAction')
                        item.pop('DefaultAction')
                    else:
                        self.file.write_byte(DAT.BreakFlag)
                        count = count +1
                        break

                if item['ID'] > data['item_count'] and item['ID'] <= (data['item_count'] + data['outfit_count']):
                    self.file.write_byte(item['FrameGroupCount'])

                for frame in range(item['FrameGroupCount']):
                    if item['ID'] > data['item_count'] and item['ID'] <= (data['item_count'] + data['outfit_count']):
                        self.file.write_byte(item['FrameGroupID'][frame])

                    self.file.write_byte(item['Width'][frame])
                    self.file.write_byte(item['Height'][frame])
                    if item['Width'][frame] > 1 or item['Height'][frame] > 1:
                        self.file.write_byte(item['ExactSize'][frame])

                    self.file.write_byte(item['Layers'][frame])
                    self.file.write_byte(item['PatternWidth'][frame])
                    self.file.write_byte(item['PatternHeight'][frame])
                    self.file.write_byte(item['PatternDepth'][frame])
                    self.file.write_byte(item['Phases'][frame])

                    if item['Phases'][frame] > 1:
                        self.file.write_byte(item['async'][frame])
                        self.file.write_int32(item['loop_count'][frame])
                        self.file.write_byte(item['start_phase'][frame])
                        for unknown in range(item['Phases'][frame]):
                            self.file.write_int32(item['minimum'][frame][unknown])
                            self.file.write_int32(item['maximum'][frame][unknown])

                    for spr in range(item['NumberOfSprites'][frame]):
                        self.file.write_int32(item['Sprites'][frame][spr])

                item.pop('FrameGroupCount')
                

class DAT(IntEnum):
    def __str__(self):
        return str(self.value)

    Flag_Bank = 0
    Flag_Clip = 1
    Flag_Bottom = 2
    Flag_Top = 3
    Flag_Container = 4
    Flag_Cumulative = 5
    Flag_ForceUse = 6
    Flag_MultiUse = 7
    Flag_Write = 8
    Flag_WriteOnce = 9
    Flag_LiquidContainer = 10
    Flag_LiquidPool = 11
    Flag_Unpass = 12
    Flag_Unmove = 13
    Flag_Unsight = 14
    Flag_Avoid = 15
    Flag_NOMOVEMENTANIMATION = 16
    Flag_Take = 17
    Flag_Hang = 18
    Flag_HookSouth = 19
    Flag_HookEast = 20
    Flag_Rotate = 21
    Flag_Light = 22
    Flag_DontHide = 23
    Flag_Translucent = 24
    Flag_Shift = 25
    Flag_Height = 26
    Flag_LyingObject = 27
    Flag_AnimateAlways = 28
    Flag_Automap = 29
    Flag_LensHelp = 30
    Flag_FullBank = 31
    Flag_IgnoreLook = 32
    Flag_Clothes = 33
    Flag_Market = 34
    Flag_DefaultAction = 35
    Flag_UseAble = 254
    BreakFlag = 255


class MarketCategory(IntEnum):
    Armors = 1
    Amulets = 2
    Boots = 3
    Containers = 4
    Decoration = 5
    Food = 6
    Helmets_Hats = 7
    Legs = 8
    Others = 9
    Potions = 10
    Rings = 11
    Runes = 12
    Shields = 13
    Tools = 14
    Valuables = 15
    Ammunition = 16
    Axes = 17
    Clubs = 18
    DistanceWeapons = 19
    Swords = 20
    Wands_Rods = 21
    MetaWeapons = 22
    PremiumScroll = 23
        


class ItemData():

    def __init__(self):
        self.ID = -1
        self.isBank = -1
        self.Waypoints = -1
        self.isClip = -1
        self.isBottom = -1
        self.isTop = -1
        self.isContainer = -1
        self.isCumulative = -1
        self.isUseAble = -1
        self.isForceUse = -1
        self.isMultiUse = -1
        self.isWriteable = -1
        self.MaxTextLength = -1
        self.isWriteableOnce = -1
        self.isLiquidContainer = -1
        self.isLiquidPool = -1
        self.isUnpassable = -1
        self.isUnmoveable = -1
        self.isUnsight = -1
        self.isAvoid = -1
        self.isTakeable = -1
        self.isHangable = -1
        self.isHookSouth = -1
        self.isHookEast = -1
        self.isRotateable = -1
        self.noMovmentAction = -1
        self.isLight = -1
        self.Brightness = -1
        self.LightColor = -1
        self.isDontHide = -1
        self.isTranslucent = -1
        self.isDisplaced = -1
        self.DisplacementX = -1
        self.DisplacementY = -1
        self.isHeight = -1
        self.Elevation = -1
        self.isLyingObject = -1
        self.isAnimateAlways = -1
        self.isAutomap = -1
        self.isAutomapColor = -1
        self.isLensHelp = -1
        self.LensHelp = -1
        self.isFullBank = -1
        self.isIgnoreLook = -1
        self.isCloth = -1
        self.FloorChangeUp = -1
        self.FloorChangeDown = -1
        self.RequireUse = -1
        self.RequireShovel = -1
        self.RequireRope = -1
        self.ClothSlot = -1
        self.isMarket = -1
        self.MarketCategory = -1
        self.MarketTradeAs = -1
        self.MarketShowAs = -1
        self.MarketNameLength = -1
        self.MarketName = ""
        self.MarketRestrictProfession = -1
        self.MarketRestrictLevel = -1
        self.isDefaultAction = -1
        self.DefaultAction = -1
        self.Width = []
        self.Height = []
        self.ExactSize = []
        self.Layers = []
        self.PatternWidth = []
        self.PatternHeight = []
        self.PatternDepth = []
        self.Phases = []
        self.NumberOfSprites = []
        self.async = []
        self.loop_count = []
        self.start_phase = []
        self.minimum = []
        self.maximum = []
        self.FrameGroupID = []

        self.Sprites = []

    def __iter__(self):
        for key, value in list(self.__dict__.items()):
            if value == -1 or value == "":
                continue
            else:
                yield (key, value)

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)