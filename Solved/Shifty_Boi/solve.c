#include <stdio.h>
#include <stdint.h>

// Make a 5 bit register
typedef struct REGISTER {
    unsigned REG0:1;
    unsigned REG1:1;
    unsigned REG2:1;
    unsigned REG3:1;
    unsigned REG4:1;
    unsigned REG5:1;
} REGISTER;

// On every clock signal, update the state of the register
void Reg_Clock(REGISTER * r) {
	uint8_t feedback = r->REG4 ^ r->REG1;
	r->REG0 = r->REG1;
	r->REG1 = r->REG2;
	r->REG2 = r->REG3;
	r->REG3 = r->REG4;
	r->REG4 = r->REG5;
	r->REG5 = feedback != 0;
}

// This sets the initial seed value
void Reg_SetValue(REGISTER * r, uint8_t value) {
	r->REG0 = (value & (1<<0)) != 0;
	r->REG1 = (value & (1<<1)) != 0;
	r->REG2 = (value & (1<<2)) != 0;
	r->REG3 = (value & (1<<3)) != 0;
	r->REG4 = (value & (1<<4)) != 0;
	r->REG5 = (value & (1<<5)) != 0;
}

// Retrieve bits and convert to value
uint8_t Reg_GetValue(REGISTER * r) {
	uint8_t value = 0;
	value |= r->REG0 << 0;
	value |= r->REG1 << 1;
	value |= r->REG2 << 2;
	value |= r->REG3 << 3;
	value |= r->REG4 << 4;
	value |= r->REG5 << 5;
	return value;
}

// Retrieve output from REG0
uint8_t Reg_GetOutput(REGISTER * r) {
	return r->REG0;
}

// Main
int main(void) {
	REGISTER reg;

	// Set seed
	Reg_SetValue(&reg, 0xFF);

	// Given hint array
	uint8_t hint[16] = {
		0xbc, 0x1c, 0x56, 0x06,
		0xab, 0xb5, 0x61, 0xa0,
		0xe2, 0x8b, 0x55, 0xed,
		0x74, 0xdd, 0x2f, 0x60
	};

	// Array for decoded bytes
	uint8_t solved[17];

	// Through experimentation, I found out that
	// the bit order is from last to first.
	for (int x = 15; x >= 0; x--) {
		// Clock 8 times to get byte value
		// Through experimentation, I found out that
		// the 0th bit is the LSB and the 7th bit is the MSB
		uint8_t value = 0;
		for (int i = 0; i < 8; i++) {
			value = value | Reg_GetOutput(&reg) << i; // LSB first
			// value = value << 1 | Reg_GetOutput(&reg); // MSB first
			printf("-%02x", value);
			Reg_Clock(&reg);
		}

		// Decode the hint using XOR cipher
		uint8_t decode = value ^ hint[x];
		solved[x] = decode;
		printf("-> 0x%1$02x = %1$c \n", decode);
	}
	solved[16] = 0;

	printf("Flag = %s\n", solved);
	return 0;
}