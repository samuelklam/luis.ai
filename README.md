# luis.ai

## Part A - Building LUIS application

Published End Point: https://api.projectoxford.ai/luis/v1/application?id=7ef18924-6aee-44d7-be98-1aa2a7428282&subscription-key=f5ff50ec30804649a7f1c52dc782c089.

### Task 0:

#### Adding Test Utterances

##### Start Activity
- ```start tracking my run```
- ```begin```
- ```start```
- ```begin tracking```
- ```I am starting```
- ```I'm starting my run```

##### Stop Activity
- ```end tracking my run```
- ```stop```
- ```end```
- ```I am finished```
- ```I finished my run```

##### None
- ```direct me home```
- ```lead me to a route```
- ```I love running```

### Task 1

##### Recognize command to set a target heart rate
- ```set heart rate target```
- ```track my heart rate```
- ```keep track of my heart rate```

To run ```test_tracker.py```:
```
python test_tracker.py --basic
```

Output:
```
------- SUMMARY ------------------
Total tested: 25
Intent correct: 16 - 64.0%
Entity correct: 5 - 20.0%

Correct Examples:
end all
all done
I am quite happy with my result. Would you please wrap up the currently active activity tracker
ok - heavy breathing - done
set heart rate to 170

Examples with wrong intent:
set hr to 130
I choose you pikachu
could you please follow my stroll
driving directions to home
im running now
a large fries and coke please
order a drink
commence swimming
skydiving go

Examples with wrong entity:
could you please follow my stroll
finished with that jog
commence swimming
just ended my walk
order a drink
driving directions to home
walk start
done with my hike
I want to start my run
end my chess game
```
