# ME30 Project 4 - Mecanum 4WD Chassis

This project was completed with Dillan Tran and Brandon Sun as part of [Tufts University ME30 Fall 2021](http://andnowforelectronics.com/). We were tasked to build an intrepid robot that traverses through an academic building. The robot will begin on the ground floor in the atrium, near Blake Lab. It should not be tethered to a wall outlet and must complete the following tasks under 15 minutes:
- High five an LA (target hand height 105.5-107 cm), seated conveniently nearby in the atrium
- Travel to Jason Rife's office, one floor above the robot's starting position
- High five Jason Rife (target hand height 105.5-107 cm) 

We decided to build a mecanum drivetrain, remotely controlled over Tufts Wifi Network. The drivetrain successfully traversed different surfaces and accurately pressed buttons to navigate in and out of an elevator during its journey. Videos to be uploaded! 

## Controller Program in Python

This program is written in Python 3.9 and designed to run on a Raspberry Pi Model 4B connected with [L298N H-Bridge boards](https://www.amazon.com/Qunqi-Controller-Module-Stepper-Arduino/dp/B014KMHSW6) to drive [Adafruit NEMA17 stepper motors](https://www.adafruit.com/product/324). The program itself has two programs running parallel with each other: a **ReadUserInput** thread to detect keyboard presses and set the equivalent movements, and a **Main Control Loop** to step through each motor continuously given their directions. Wireless connection with the robot's drivetrain can be established via SSH into the [Pi's registered IP address under 'Tufts Wireless'](https://device-registration-prod-02.it.tufts.edu/login/aup).

### Software Setup

To retrieve the code into your directory, type `git clone https://github.com/tuenguyen004/Python-Mecanum-Drive.git`

Create a virtual environment with `python3 -m venv env` and then activate it with `source env/bin/activate`

Install depedencies by typing `pip install -r requirements.txt`

To view or change the four-pins for each stepper motor, modify each StepperMotor instance in `MecanumDrive.py`

To run the program, type into terminal `python3 main.py`


### Default Control Scheme
       SPACEBAR    = stop all movement 
       "w"         = go forward 
       "s"         = go backward 
       "a"         = strafe left 
       "d"         = strafe right
       "q"         = rotate left (CCW) 
       "e"         = rotate right (CW) 
       "o"         = decrease speed
       "p"         = increase speed
       "x"         = reset speed to default
       "z"         = disconnect from robot
       
## References
- [Seamonsters' Guide on How Mecanum Drive Works](https://seamonsters-2605.github.io/archive/mecanum/)
    - Also include this [interactive simulation](https://seamonsters-2605.github.io/sketches/mecanum/), thanks to Brandon's FRC Team!
- [Linux-compatible implementation of KBHit module](https://github.com/michelbl/intro-info/blob/feaf91940ea0f0b4c8271b391710139a02f9c36d/kbhit.py)
- [Automated the setup for pigpio module](https://raspberrypi.stackexchange.com/questions/80271/why-would-os-systemsudo-pigpiod-fail-silently-but-only-part-of-the-time)
- [A simple Python script used to test multi-threading on Raspberry Pi](http://robsraspberrypi.blogspot.com/2016/01/raspberry-pi-python-threading.html)
