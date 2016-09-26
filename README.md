# luis.ai

Natural language "bot" interfaces for a Health Fitness Tracking Application (SuperTracker 3000) and a Sleep Tracking & Alarm Clock Application (SleepTracker) using [Luis.ai](https://www.luis.ai).

## SuperTracker 3000

### Core Features
- Start Tracking Activity
- End Tracking Activity
- Set Target Heart Rate

### Intents
- SetHRtarget
- StopActivity
- StartActivity
- None

### Entities
- ActivityType
- Prebuilt: number

### Phrase List Features
- Activities: walk, run, swim, bike, ride, hike, workout, cycle, lift, sprint, jog, exercise

## SleepTracker

### Core Features
- track and analyze one's sleeping patterns / circadian rhythms
- set an alarm for a specific time / time range
- wake one up during their lightest sleeping phase
- snooze (for a specific time)
- when prompted, respond with the current time

### Intents
- SetAlarm
- EndAlarm
- StartTracking
- EndTracking
- CurrentTime
- Snooze
- None

### Entities
- ActivityType
- Product
- Prebuilt: datetime
