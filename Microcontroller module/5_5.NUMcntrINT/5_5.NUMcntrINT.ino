int ev=0;
byte cx=0,sx;
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

//Setup & Config Timer

TCCR2A = 0x02; //setup Timer#2 as CTC
TCCR2B = B111; //prescaler with clk/64
OCR2A = 128;
TIMSK2 = 0x02; //enable OCR2A interrupt
sei();

pinMode(2,INPUT_PULLUP);
attachInterrupt(digitalPinToInterrupt(2), CLEAR_int0, FALLING);
pinMode(3,INPUT_PULLUP);
attachInterrupt(digitalPinToInterrupt(3), LOAD_int1, FALLING);
}

ISR(TIMER2_COMPA_vect) {
sx = dx[dg[cx]];
PORTB = PORTB|B011100;
PORTC = sx & 0x3F;
PORTB = ((PORTB&0xFC)|(sx>>6));
PORTB = PORTB&(~(4<<cx));
cx=++cx%3;
}

void LOAD_int1() {
attachInterrupt(digitalPinToInterrupt(3), LOAD_int1, FALLING);
}

void CLEAR_int0() {
attachInterrupt(digitalPinToInterrupt(2), CLEAR_int0, FALLING);
}

void loop() {
cntr=++cntr%1000;
dg[0]=cntr%10;
dg[2]=cntr/100;
dg[1]=(cntr/10)%10;
delay(200);
}
