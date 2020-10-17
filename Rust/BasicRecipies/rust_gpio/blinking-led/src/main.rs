// GPIO library
use rust_gpiozero::*;

// optional, for using the standard library for time dilation
use std::thread::sleep;
use std::time::Duration;

// using the keyboard press to stop the blinking light
use::std::io;
use::std::io::prelude::*;

fn main() {

	// FOREVER LOOPS OF BLINKING LED

	// led power is connected to pin 18
	// let led = LED::new(18);

	
	// infinite loop, using standard library
	//loop{
	//	led.on();
	//	sleep(Duration::from_secs(1)); // second pause
	//	led.off();
	//	sleep(Duration::from_secs(1));
	//}
	
	// using the built in rust_gpio library functions
//	let mut led18 = LED::new(18);
	// .blink(on_time, off_time)
//	led18.blink(2.1,1.25);
	

	// prevents the program from exiting immediately,
	// and keeps it going indefinitely (need to look more into the docs for this)
//	led18.wait();
	
// pulse width modulation -> typically in RGB
//	let mut pwm_led18 = PWMLED::new(18);

	// setting number of times for led to blink
//	pwm_led18.set_blink_count(10);
//	pwm_led18.blink(2.0, 2.0, 1.0, 1.0);

	// keyboard press
//	let _ = io::stdin().read(&mut [0u8]).unwrap();


}


