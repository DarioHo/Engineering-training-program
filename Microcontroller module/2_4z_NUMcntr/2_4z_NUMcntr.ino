int ev1, ev2;
byte cx,sx;
byte dg[]={9,2,8};
int cntr;
//----------- pgfedcba pgfedcba pgfedcba pgfedcba
const byte dx[] = { B0111111,  B0000110,   B1011011, B1001111,  
                    B1100110,  B1101101,   B1111101, B0000111,  
                    B1111111,  B1101111,   B1110111, B1111100,
                    B1011000,  B1011110,   B1111001, B1110001};

void setup() {
Serial.begin(9600);
DDRC = 0x3F; //PC[0..5] as output
DDRB = 0x3F; //PB[0..5] as output
}
void loop() {
sx = dx[dg[cx]];
PORTB = PORTB|B011100;
PORTC = sx & 0x3F;
PORTB = ((PORTB&0xFC)|(sx>>6));
PORTB = PORTB&(~(4<<cx));
cx=++cx%3;
ev1++;ev2++;

if (ev1==20) {
  ev1=0;
  cntr = ++cntr % 1000;
  dg[0] = cntr%10;
  dg[2] = cntr/100;
  dg[1] = (cntr/10)%10;
}

if (ev2==400) {
  ev2=0;
  cntr=0; 
  dg[0]=0; 
  dg[1]=0; 
  dg[2]=0;
}

delay(5); //50-10
}
