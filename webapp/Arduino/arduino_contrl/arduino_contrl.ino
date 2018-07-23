void setup(){
  pinMode(8,OUTPUT); //RED LED
  pinMode(12,OUTPUT);//BLUE LED
  pinMode(7,OUTPUT); //MOTOR

  Serial.begin(9600); //通信速度
}

void loop(){

  int inputchar;    
  inputchar = Serial.read();  

  if(inputchar!=-1){
    switch(inputchar){
      case 'a':
        digitalWrite(12,HIGH);
        break;

      case 'b':
        digitalWrite(12,LOW);
        break;
      case 'c':
        digitalWrite(8,HIGH);
        break;
      case 'd':
        digitalWrite(8,LOW);
       break;
      case 'e':
        digitalWrite(7,HIGH);
        break;
      case 'f':
        digitalWrite(7,LOW);
        break;

    }
  }
  else{
  }
}
