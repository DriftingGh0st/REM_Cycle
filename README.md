# REM_Cycle

**REM_Cycle** is a Python program designed to calculate the approximate number of REM (Rapid Eye Movement) sleep cycles based on a user-defined sleep schedule within a 24-hour period. REM sleep is essential for restorative rest, with each cycle typically lasting around 90 minutes. The program helps users estimate their REM sleep based on intended sleep and wake-up times.

## Background

**REM_Cycle** was developed as an early coding project, inspired by personal observations of sleep quality. Tracking REM sleep can support health and productivity by helping users adjust their schedules for optimal rest.

## Features

- **User-Friendly Input**: Prompts for bedtime and wake-up time in a simple format, supporting both 12-hour AM/PM notation.
- **Cycle Calculation**: Calculates total sleep duration between bedtime and wake-up time, then estimates the number of full REM cycles by dividing by 90 minutes.
- **24-Hour Flexibility**: Accommodates overnight shifts that span AM and PM, supporting any sleep schedule within a 24-hour period.

## Usage

1. **Start the Program**: Run the script in any Python environment.
2. **Enter Bedtime and Wake-Up Time**:
   - Enter the bedtime hour, minute (e.g., `10 30` for 10:30), and AM/PM.
   - Similarly, enter the wake-up time in hour, minute, and AM/PM format.
3. **Receive Output**: The program calculates and displays the approximate number of REM sleep cycles for the defined schedule.

### Example

```plaintext
REM is approximately 90 minutes.
How much REM you can get with your sleep schedule in a 24 hr span.

Enter when you're going to bed with two numbers: 10 30
10 AM or PM: PM
Enter when you would like to wake up with two numbers: 6 45
6 AM or PM: AM

This gives you approximately 4 full cycles.
```
## Code Walkthrough

The core logic involves:

- **Input Validation**: Ensures valid times are entered in the 12-hour AM/PM format.
- **Time Conversion**: Converts user input into total minutes for calculating sleep duration.
- **REM Calculation**: Divides total sleep time by 90 (the length of one REM cycle) to determine the number of complete cycles.

## Motivation

This project emerged from a desire to better understand sleep quality through consistent REM tracking. **REM_Cycle** serves as a practical tool for those looking to improve sleep by optimizing REM cycles.

## Future Improvements

Future versions could include:

- Calculations for partial REM cycles.
- Enhanced validation for 24-hour time input.
- Expanded sleep analysis, including other sleep stages.
