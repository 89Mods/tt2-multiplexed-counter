set ::env(DESIGN_NAME) tt2_tholin_multiplexed_counter
set ::env(VERILOG_FILES) "\
    $::env(DESIGN_DIR)/toplevel/logisimTopLevelShell.v \
    $::env(DESIGN_DIR)/circuit/main.v \
    $::env(DESIGN_DIR)/circuit/bcd_to_seg.v \
    $::env(DESIGN_DIR)/circuit/seconds_counter.v \
    $::env(DESIGN_DIR)/circuit/full_counter.v \
    $::env(DESIGN_DIR)/circuit/custom_counter_3.v \
    $::env(DESIGN_DIR)/circuit/custom_counter_4.v \
    $::env(DESIGN_DIR)/circuit/custom_counter_10.v \
    $::env(DESIGN_DIR)/arith/Comparator.v \
    $::env(DESIGN_DIR)/gates/AND_GATE.v \
    $::env(DESIGN_DIR)/gates/OR_GATE.v \
    $::env(DESIGN_DIR)/memory/D_FLIPFLOP.v \
    $::env(DESIGN_DIR)/plexers/Multiplexer_bus_4.v"
