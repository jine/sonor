#!/usr/bin/env python3 -i
'''
https://github.com/u-boot/u-boot/blob/master/arch/arm/include/asm/arch-meson/
'''

def AXG_AO_ADDR(off):
    return ((AXG_AOBUS_BASE) + ((off) << 2))


SZ_1K=0x00000400

AXG_AOBUS_BASE=0xff800000

AXG_AO_BOOT_DEVICE=0xF
AXG_AO_MEM_SIZE_MASK=0xFFFF0000
AXG_AO_MEM_SIZE_SHIFT=16
AXG_AO_BL31_RSVMEM_SIZE_MASK=0xFFFF0000
AXG_AO_BL31_RSVMEM_SIZE_SHIFT=16
AXG_AO_BL32_RSVMEM_SIZE_MASK=0xFFFF

AXG_AO_SEC_GP_CFG0=AXG_AO_ADDR(0x90)
AXG_AO_SEC_GP_CFG3=AXG_AO_ADDR(0x93)
AXG_AO_SEC_GP_CFG4=AXG_AO_ADDR(0x94)
AXG_AO_SEC_GP_CFG5=AXG_AO_ADDR(0x95)


print('[-] 0x{0:0x}'.format(AXG_AO_SEC_GP_CFG0))
