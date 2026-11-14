#pragma once
#include <cstdint>
#include <cstdlib>
#include <cmath>
#define LOW 0
#define HIGH 1
#define INPUT_PULLUP 2
unsigned long g_ms=0; int g_pin[64];
inline uint32_t millis(){return (uint32_t)g_ms;}
inline int digitalRead(int p){return g_pin[p];}
inline void pinMode(int,int){}
inline long random(long n){return rand()%n;}
inline void randomSeed(unsigned long){}
inline uint32_t esp_random(){return 1;}
