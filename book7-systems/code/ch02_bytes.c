/* ch02_bytes.c -- the same 4 bytes, three different worlds */
#include <stdint.h>
#include <stdio.h>
#include <string.h>
int main(void) {
    uint32_t u = 0x0A0B0C0Du;
    unsigned char *p = (unsigned char *)&u;
    printf("bytes (LE order): %02x %02x %02x %02x\n", p[0],p[1],p[2],p[3]);
    int32_t  i; memcpy(&i, &u, 4); printf("as int32 : %d\n", i);
    float    f; memcpy(&f, &u, 4); printf("as float : %g\n", (double)f);
    /* a float you know: 0x3FC00000 */
    uint32_t fb = 0x3FC00000u; float g; memcpy(&g, &fb, 4);
    printf("0x3FC00000 as float: %g\n", (double)g);
    return 0;
}
