
const EventEmitter = require('events');
class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('WaterFull', () => {
  console.log('Please turn off the motor')
  setTimeout(() => {
    console.log('Again reminding, turn off the motor')
  }, 3000);
});

myEmitter.emit('WaterFull');
