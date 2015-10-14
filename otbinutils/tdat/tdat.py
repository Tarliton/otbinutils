from otbinutils.fileutils import fileutils
from enum import IntEnum
import json

class TDat():
    def __init__(self, version):
        self.version = version
        self.file = fileutils.File(version, "dat")
        self.__read_file()

    def __read_file(self):
        self.dat_version = self.file.read_int32()
        self.item_count = self.file.read_int16()
        self.outfit_count = self.file.read_int16()
        self.effect_count = self.file.read_int16()
        self.projectile_count = self.file.read_int16()
        self.max_ID = self.item_count + self.outfit_count + self.effect_count + self.projectile_count
        self.items = []
        ID = 100
        flag = DAT.Flag_Bank
        while ID < self.max_ID:
            current_item = ItemData()
            current_item.ID = ID
            while True:
                flag = self.file.read_byte()
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
                    MarketNameLength = self.file.read_int16()
                    current_item.MarketName = self.file.read_string(MarketNameLength)
                    current_item.MarketRestrictProfession = self.file.read_int16()
                    current_item.MarketRestrictLevel = self.file.read_int16()
                elif flag == DAT.Flag_DefaultAction:
                    current_item.DefaultAction = True
                    action = self.file.read_int16()
                elif flag == DAT.BreakFlag:
                    break
            FrameGroupCount = self.file.read_byte() if (ID > self.item_count and ID <= (self.item_count + self.outfit_count)) else 1
            for frame in range(FrameGroupCount):

                FrameGroupID = self.file.read_byte() if (ID > self.item_count and ID <= (self.item_count + self.outfit_count)) else 0

                current_item.Width = self.file.read_byte()
                current_item.Height = self.file.read_byte()
                if current_item.Width > 1 or current_item.Height > 1:
                    current_item.ExactSize = self.file.read_byte()

                current_item.Layers = self.file.read_byte()
                current_item.PatternWidth = self.file.read_byte()
                current_item.PatternHeight = self.file.read_byte()
                current_item.PatternDepth = self.file.read_byte()
                current_item.Phases = self.file.read_byte()

                if current_item.Phases > 1:
                    loc8 = 0
                    unknown1 = self.file.read_byte()
                    unknown2 = self.file.read_int32()
                    unknown3 = self.file.read_byte()
                    while loc8 < current_item.Phases:
                        unknown4 = self.file.read_int32()
                        unknown5 = self.file.read_int32();
                        loc8 = loc8 + 1

                numSpr = current_item.Width * current_item.Height
                numSpr = numSpr * current_item.Layers * current_item.PatternWidth
                numSpr = numSpr * current_item.PatternHeight * current_item.PatternDepth
                numSpr = numSpr * current_item.Phases

                current_item.NumberOfSprites = numSpr

                for spr in range(current_item.NumberOfSprites):
                    current_item.Sprites.append(self.file.read_int32())
            self.items.append(current_item)
            ID = ID +1


    def to_json(self):
        with open("output/"+str(self.version)+"/tdat.json", 'w') as outfile:
            json.dump(self, outfile, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)



class DAT(IntEnum):
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
        self.MarketName = ""
        self.MarketRestrictProfession = -1
        self.MarketRestrictLevel = -1
        self.DefaultAction = -1
        self.Width = -1
        self.Height = -1
        self.ExactSize = -1
        self.Layers = -1
        self.PatternWidth = -1
        self.PatternHeight = -1
        self.PatternDepth = -1
        self.Phases = -1
        self.NumberOfSprites = -1

        self.Sprites = []

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)