#pragma once
#include <cstdint>
#include <vector>
#define NEO_GRB 1
#define NEO_KHZ800 2
struct Adafruit_NeoPixel{ std::vector<uint32_t> px; int shows=0; Adafruit_NeoPixel(int n,int,int):px(n){} void begin(){} void clear(){for(auto&p:px)p=0;} void show(){shows++;}
 static uint32_t Color(uint8_t r,uint8_t g,uint8_t b){return (uint32_t(r)<<16)|(uint32_t(g)<<8)|b;} void setPixelColor(int i,uint32_t c){px.at(i)=c;} };
