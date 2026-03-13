class LCD:
    bool enableLCDPPU = False
    windowTileMap = ("$9800-$9BFF","$9C00-$9FFF")
    bool windowEnable = False
    bgWindowTiles = ("$8800-$97FF","8000-$87FF")
    bgTileMap = ("$9800-$9BFF","$9C00-$9FFF")
    objSize = ("8x8","8x16")
    bool objEnable = False
    bool bgWindowEnable = False
    bool lycIntSelect = False
    bool mode2IntSelect = False
    bool mode1IntSelect = False
    bool mode0IntSelect = False
    int lyLyc                          # Updates automatically from hardware, read only
    bool ppuMode                       # Updates automatically from hardware, read only
    int viewPortX = 0
    int viewPortY = 0
    int windowY = 0
    int windowX = 0                    # Position + 7
    int LY                             # Updates automatically from hardware, read only
    int LYC

def main():
    LCDC = LCD()
    
    while (LCDC.LY != 0xh91):
        wait()
    
    LCDC.enableLCDPPU = False
    LCDC.windowTileMap[0]
    LCDC.windowEnable = False
    LCDC.bgWindowTiles[0]
    LCDC.bgTileMap[0]
    LCDC.objSize[0]
    LCDC.objEnable = False
    LCDC.bgWindowEnable = False
    
    