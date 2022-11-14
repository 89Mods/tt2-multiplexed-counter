import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def test_counter(dut):
	dut._log.info("start")
	dut.RST.value = 1
	clock = Clock(dut.CLK, 1, units="ms")
	cocotb.start_soon(clock.start())
	
	dut._log.info("reset")
	await ClockCycles(dut.CLK, 5)
	dut.RST.value = 0
	
	assert dut.SEL.value == 0
	await ClockCycles(dut.CLK, 5)
	assert dut.SEL.value == 1
	await ClockCycles(dut.CLK, 4)
	assert dut.SEL.value == 0

	await ClockCycles(dut.CLK, 5 * 1024 + 24)
	
	assert dut.SEL.value == 0
	assert dut.dout.value == 0b1101101
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b0111111
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b0111111
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b0111111
	await ClockCycles(dut.CLK, 8)

	await ClockCycles(dut.CLK, 55 * 1024)

	assert dut.SEL.value == 0
	assert dut.dout.value == 0b0111111
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b0111111
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b0000110
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b0111111
	await ClockCycles(dut.CLK, 8)

	await ClockCycles(dut.CLK, (11 * 60 + 34) * 1024)
	
	assert dut.SEL.value == 0
	assert dut.dout.value == 0b1100110
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b1001111
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b1011011
	await ClockCycles(dut.CLK, 8)
	assert dut.dout.value == 0b0000110
	await ClockCycles(dut.CLK, 8)
