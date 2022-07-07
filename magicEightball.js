let userName = "Yuri";
let userQuestion = "Does my code suck?";
let randomNumber = Math.floor(Math.random() * 8);
let eightBall = "";

userName ? console.log(`Hello, ${userName}!`) : console.log("Hello!");
console.log(`${userName} asked: ${userQuestion}`);

switch(randomNumber){
  case 1:
    console.log('Magic Eight Ball says, It is certain');
    break;
  case 2:
    console.log('Magic Eight Ball says, It is decidedly so');
    break;
  case 3:
    console.log('Magic Eight Ball says, Reply hazy try again');
    break;
  case 4:
    console.log('Magic Eight Ball says, Cannot predict now');
    break;
  case 5:
    console.log('Magic Eight Ball says, Do not count on it');
    break;
  case 6:
    console.log('Magic Eight Ball says, My sources say no');
    break;
  case 7:
    console.log('Magic Eight Ball says, Outlook not so good');
    break;
  case 8:
    console.log('Magic Eight Ball says, Signs point to yes');
    break;
  default:
    console.log('Magic Eight Ball says, You are now posessed');

}
