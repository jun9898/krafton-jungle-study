//
// Created by 전병준 on 24. 4. 4.
//
long mult2(long x, long y);

void multstore(long x, long y, long *dest) {
    long t = mult2(x, y);
    *dest = t;
}