int count = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.print("I am counting to: ");
Serial.print(count);
Serial.println("Missipi. ");
count=count+1;
delay(1000);
}
