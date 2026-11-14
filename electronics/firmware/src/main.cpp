// Standalone ESP32 reference firmware, NOT WLED. NOT COMPILED OR BENCH TESTED.
// ESP32-WROOM-32 DevKit: GPIO16 -> 5V level shifter -> 330R -> LED DIN.
// GPIO25 (mode) / GPIO26 (action): momentary normally-open switches to GND.
// 5V fused bank, common ground, 1000uF capacitor, strain relief required.
#include <Arduino.h>
#include <Adafruit_NeoPixel.h>
#include <math.h>
constexpr int LED_PIN=16, MODE_PIN=25, ACTION_PIN=26;
constexpr int RING=21, HAND=14, CRYSTAL=4, COUNT=RING+HAND+CRYSTAL;
constexpr uint32_t FRAME_MS=25, DEBOUNCE_MS=35, LONG_MS=850, DOUBLE_MS=360, FLASH_MS=350;
const uint8_t BRIGHT[]={32,64,96,128}; // brightness cap, NOT hard current limit
Adafruit_NeoPixel led(COUNT,LED_PIN,NEO_GRB+NEO_KHZ800);
enum Effect:uint8_t { BREATH, CHARGE, CHASE, SURGE, FLASH, SPARK };
Effect effect=BREATH, resumeEffect=BREATH;
bool on=true;
uint8_t level=1, palette=0, spark[COUNT]={};
uint32_t effectAt=0, flashAt=0, frameAt=0;
struct Button {int pin; bool raw=false,stable=false,longDone=false; uint8_t clicks=0; uint32_t changed=0,pressed=0,released=0;};
Button a{MODE_PIN},b{ACTION_PIN};
uint8_t u8(float x){return x<0?0:x>255?255:uint8_t(x+0.5f);}
void rgb(uint8_t &r,uint8_t &g,uint8_t &b){
  if(palette==0){r=0;g=120;b=255;}
  else if(palette==1){r=130;g=20;b=255;}
  else{r=230;g=30;b=190;}
}
void put(int i,float r,float g,float b,float intensity){
  if(i<0||i>=COUNT)return;
  float f=BRIGHT[level]/255.0f*intensity;
  led.setPixelColor(i,led.Color(u8(r*f),u8(g*f),u8(b*f)));
}
void setEffect(Effect e){effect=e;effectAt=millis();if(e==SPARK)memset(spark,0,sizeof(spark));}
void shortPress(bool mode){
  if(mode){
    if(effect==FLASH)effect=resumeEffect;
    setEffect(effect==SPARK?BREATH:Effect(uint8_t(effect)+1));
    if(effect==FLASH)setEffect(SPARK); // FLASH is triggered only by double action
  } else level=(level+1)%4;
}
void longPress(bool mode){if(mode)on=!on;else palette=(palette+1)%3;}
void doublePress(bool mode){
  if(mode)shortPress(true);
  else{if(effect!=FLASH)resumeEffect=effect;effect=FLASH;flashAt=millis();}
}
void poll(Button &x,bool isMode,uint32_t now){
  bool raw=digitalRead(x.pin)==LOW;
  if(raw!=x.raw){x.raw=raw;x.changed=now;}
  if(raw!=x.stable&&now-x.changed>=DEBOUNCE_MS){
    x.stable=raw;
    if(raw){x.pressed=now;x.longDone=false;}
    else if(!x.longDone){x.clicks++;x.released=now;if(x.clicks>=2){x.clicks=0;doublePress(isMode);}}
  }
  if(x.stable&&!x.longDone&&now-x.pressed>=LONG_MS){x.longDone=true;x.clicks=0;longPress(isMode);}
  if(!x.stable&&x.clicks==1&&now-x.released>=DOUBLE_MS){x.clicks=0;shortPress(isMode);}
}
void draw(uint32_t now){
  led.clear();
  if(!on){led.show();return;}
  if(effect==FLASH&&now-flashAt>=FLASH_MS)setEffect(resumeEffect);
  uint8_t r,g,b;rgb(r,g,b);uint32_t t=now-effectAt;
  if(effect==BREATH){
    float v=.30f+.24f*sinf(t*.0028f);
    for(int i=0;i<COUNT;i++)put(i,r,g,b,v*(i>=RING+HAND?1.3f:i>=RING?.65f:1.0f));
  }else if(effect==CHARGE){
    float v=(t%2600UL)/2600.0f;
    for(int i=0;i<RING;i++)put(i,r,g,b,i/float(RING)<v?.95f:.02f);
    for(int i=0;i<HAND;i++)put(RING+i,r,g,b,i/float(HAND)<v?.65f:.02f);
    for(int i=RING+HAND;i<COUNT;i++)put(i,r,g,b,v>.84f?1.0f:v*.3f);
  }else if(effect==CHASE){
    int head=(t/65UL)%RING, handHead=(t/95UL)%HAND;
    for(int i=0;i<RING;i++){int d=(head-i+RING)%RING;put(i,r,g,b,d<5?1.0f-d*.2f:.02f);}
    for(int i=0;i<HAND;i++){int d=(handHead-i+HAND)%HAND;put(RING+i,r,g,b,d<4?.8f-d*.2f:.02f);}
    for(int i=RING+HAND;i<COUNT;i++)put(i,r,g,b,.25f+.2f*sinf(t*.009f));
  }else if(effect==SURGE){
    uint32_t p=t%1650UL;float v=p<190?1.0f-p/250.0f:.11f;
    for(int i=0;i<COUNT;i++)put(i,r,g,b,v);
  }else if(effect==FLASH){
    float v=(now-flashAt)%95UL<50UL?1.0f:.12f;
    for(int i=0;i<COUNT;i++)put(i,185,220,255,v);
  }else if(effect==SPARK){
    for(int i=0;i<COUNT;i++){spark[i]=uint8_t(spark[i]*.77f);put(i,r,g,b,.07f+spark[i]/255.0f);}
    spark[random(COUNT)]=255;spark[random(COUNT)]=185;
  }
  led.show();
}
void setup(){
  pinMode(MODE_PIN,INPUT_PULLUP);pinMode(ACTION_PIN,INPUT_PULLUP);
  led.begin();led.clear();led.show();randomSeed(esp_random());effectAt=millis();
}
void loop(){
  uint32_t now=millis();poll(a,true,now);poll(b,false,now);
  if(now-frameAt>=FRAME_MS){frameAt=now;draw(now);}
}
