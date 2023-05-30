int ev = 0;
byte cx = 0, sx;
byte dg[] = {9, 2, 8};
int cntr;
//----------- pgfedcba pgfedcba pgfedcba
const byte dx[] = { B0111111,  B0000110,   B1011011, B1001111,
                    B1100110,  B1101101,   B1111101, B0000111,
                    B1111111,  B1101111,   B1110111, B1111100,
                    B1011000,  B1011110,   B1111001, B1110001
                  };
void setup() {
  Serial.begin(9600);
  DDRC = 0x3F; //PC[0..5] as output
  DDRB = 0x3F; //PB[0..5] as output

}

ISR(TIMER2_COMPA_vect) {
  TCCR2A = 0x02; //setup Timer#2 as CTC
  TCCR2B = B111; //prescaler with clk/64
  OCR2A = 255;
  TIMSK2 = 0x02; //enable OCR2A interrupt
  sei();
}

void loop() {
  cntr = ++cntr % 1000;
  dg[0] = cntr % 10;
  dg[2] = cntr / 100;
  dg[1] = (cntr / 10) % 10;
  delay(200); //50-10
  //delayMicroseconds(5000);
}
