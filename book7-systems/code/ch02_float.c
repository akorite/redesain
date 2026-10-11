/* ch02_float.c -- IEEE-754 single-precision decoder (no punning UB) */
#include <stdint.h>
#include <stdio.h>
int main(void) {
    uint32_t b = 0x40490FDBu;           /* bits of pi */
    int s = b >> 31, e = (b >> 23) & 0xFF;
    uint32_t m = b & 0x7FFFFFu;
    double mant = 1.0;
    for (int k = 22; k >= 0; k--) if (m & (1u << k)) mant += 1.0 / (1u << (23 - k));
    printf("sign=%d exp=%d(E-%d) frac=0x%06x\n", s, e, e - 127, m);
    printf("value = %s%.10g\n", s ? "-" : "", mant * (double)(1u << (e - 127)));
    return 0;
}
