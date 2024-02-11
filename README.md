![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/tests/badge.svg)

# TinyTapeout 2 multiplexed counter

**UPDATE:** Rep now contains a schematic for using the design.

A TinyTypeout 2 submission of a circuit that can multiplex four 7-segment-displays in order to count time since reset up to 99 minutes and 59 seconds.
This means that, in addition to the A - G segment outputs, there is also a 'SEL' output. Every time SEL goes high, it means the next of the four displays should be selected.
Following a reset, the rightmost display should be the one select. After every SEL rising edge, the display on farther to the left should be selected. When the final displays is selected, and SEL pulses, the selection should wrap back around to the rightmost display.

## Pin Diagram

| Inputs    | --- | Outputs                   |
| -----:    | --- | :------                   |
| CLK -     | --- | - A                      |
| RST -     | --- | - B                      |
| NC -      | --- | - C                      |
| NC -      | --- | - D                      |
| NC -      | --- | - E                      |
| NC -      | --- | - F                      |
| NC -      | --- | - G                      |
| NC -      | --- | - SEL                      |
