# setlog

Create workouts, track your progress. 

A lightweight, local-first workout logger written in Python. Define workouts, generate sessions, and record your sets. 

No cloud, no sign-ups.

## ✅ | Features

- Plan workouts your way - either build them manually or generate them automatically

- Keep all your workouts and logs stored locally, no accounts or cloud required

- Stay organised with separate sections for planning, generating, and logging

- Track your progress over time with a simple training diary

- Export workouts and logs into readable formats for easy reference

- Lightweight and easy to run - just Python, no extra setup needed

## 📂 | Project Layout

```bash
setlog/
├─ workouts/        # readable exports of workouts / logs
├─ data/            # cache folder
├─ main.py          # entry point / interface
├─ creator.py       # create workouts manually
├─ generator.py     # generate workouts from presets or muscle groups
├─ logger.py        # log completed sessions
└─ .gitignore
```

## 🏁 | Quick Start

1. Clone repo
   ```bash
   git clone https://github.com/gettingfunkier/setlog.git
   cd setlog
   ```

2. Run interface with Python (recommended 3.12.4)
   ```bash
   python main.py
   ```

## 🧭 | Navigating

With the setup complete, running main.py will present the SETLOG main menu:
```bash
SETLOG
-------------------------
   [1] Generator  | Random workout
   [2] Planner    | Manual setup
   [3] Logger     | Track progress

   [Q] Quit

> 
```
##### This is the central hub where you choose what you want to do.

### 💭 | Generator - *input 1*
The generator creates workouts automatically. 
You can choose a preset (like upper body, lower body, push, or pull) or select specific muscle groups. 
The program then picks random exercises from data/catalog.json, and you can assign details like sets, reps, and weight afterward.

```bash
Generate Workout...
-------
   [R] Run
   [P] Presets
   [O] Options

[.] Menu
> 
```
⤷ generator menu

**[R] Run** → lets you pick muscle groups one by one until you input '/'. For each group, the program looks in data/catalog.json and selects a random exercise.

```bash
add group ['/' to finish]: chest
add group ['/' to finish]: biceps
add group ['/' to finish]: back
add group ['/' to finish]: triceps
add group ['/' to finish]: spelling mistake
add group ['/' to finish]: shoulders
add group ['/' to finish]: reporte
add group ['/' to finish]: cardio
add group ['/' to finish]: /

 ➤ Unable to get data for 'spelling mistake': invalid group
 ➤ Unable to get data for 'reporte': invalid group

[i] Workout generated in 'workouts/generated_workout.txt'!
```
⤷ terminal input example

```bash
Dumbbell Bench Presses
Cable Curls
Deadlifts
Skull Crushers
Face Pulls
Stair Climbers
```
⤷ result in 'workouts/generated_workout.txt'

**[P] Presets** → quickly generate a workout by choosing a preset, each of which maps to a predefined set of muscle groups.

```bash
> Upper Body:
 chest, back, shoulders, triceps, biceps

> Lower Body:
 quads, hamstrings, calves, glutes, core

> Full Body:
 chest, back, shoulders, triceps, biceps, quads, hamstrings, calves, glutes, core

> Push:
 chest, shoulders, triceps, quads, calves

> Pull:
 back, biceps, hamstrings, glutes, core

> Core Glutes:
 core, glutes, hamstrings, quads

> Arms Shoulders:
 biceps, triceps, shoulders

> Legs:
 quads, hamstrings, calves, glutes

> Chest Back:
 chest, back
```
⤷ available presets

* type out the name of the preset, example 'full body'

**[O] Options** → extra tools for managing and refining workouts:

  - Add a new exercise to data/catalog.json.
  - View the full list of available muscle groups.
  - Assign more details (sets, reps, weight) to generated exercises using the creator functions, and add a title & weekdays.

### ✍️ | Planner - *input 2*
The planner (creator) lets you build workouts manually. 
You decide each exercise and enter its sets, reps, and weight one by one. 
This is useful for setting up custom routines you want to reuse or follow consistently.

```bash
Create Workout...
-------
   [V] View workout
   [A] Add exercise
   [E] Export
   [R] Reset

[.] Menu
> 
```
⤷ planner menu

**[V] View workout** → display the current workout you’re building.
```bash
Chest Press: 3 sets of 12 reps, at 40.0kg
Preacher Curls: 3 sets of 12 reps, at 7.5kg
Inclined Dumbbell Press (Warmup): 1 set of 8 reps, at 15.0kg
Inclined Dumbbell Press: 3 sets of 12 reps, at 25.0kg
Tricep Pushdowns: 3 sets of 12 reps, at 20.0kg
```
⤷ example output

**[A] Add exercise** → manually enter a new exercise with sets, reps, and weight.
```bash
name: inclined dumbbell press
sets: 3
reps: 12
weight: 25

[!] Exercise 'inclined dumbbell press' not found in catalog. Add it? [y/n]: n

[i] 'inclined dumbbell press' logged!
```
⤷ adding an exercise

* If an input exercise isn't found in data/catalog.json, the program will automatically ask if you want to add it

**[E] Export** → save the workout as a readable .txt file for reference or printing.
```bash
[>] Add title? (opt.) Upper Body
[>] Weekdays for Upper Body? (opt.) Tuesdays & Thursdays 

[i] Exported successfully to 'workouts/my_workout.txt'!
```
⤷ exporting a workout

```bash
My Upper Body Workout
To practice on Tuesdays & Thursdays:
Dumbbell Bench Presses: 3 sets of 12 reps, at 40.0kg
Deadlifts: 3 sets of 12 reps
Lateral Raises
Cable Overhead Extensions: 3 sets of 12 reps
Dumbbell Curls: 20 reps
```
⤷ result in 'workouts/my_workout.txt'

**[R] Reset** → clear the current workout and start fresh.

### 🪶 | Logger - *input 3*
The logger is your training diary. 
It records the exercises you performed in a session, along with sets, reps, and weights used. 
Over time, it builds a history of your workouts so you can track progress.

```bash
Log Session...
-------
   [V] View
   [A] Add
   [F] Filter
   [S] Stats
   [E] Export
   [D] Delete

[.] Menu
>
```
⤷ logger menu

**[V] View** → prints all logged entries.
```bash
WORKOUT LOGS:
Date         Exercise                  Sets  Reps  Weight (kg) 
---------------------------------------------------------
2025-02-10   Squat                     5     10    80.0        
2025-02-11   Deadlift                  3     6     100.0       
2025-02-11   Pull-ups                                          
2025-02-12   Bicep Curl                3     15    12.5        
2025-02-12   Lat Pulldown              4     10    50.0        
2025-02-13   Overhead Press            3     8     40.0        
2025-02-13   Leg Press                 5     12    120.0       
2025-02-14   Tricep Dips                     10                
2025-02-15   Face Pulls                3     15    20.0        
2025-02-16   Barbell Row               4           65.0        
2025-02-17   Barbell Row               4     8     65.0        
2025-03-07   chest press               3                       
2025-06-03   chest press               3     12    40.0        
2025-06-04   chest press               3     12    35.0        
2025-06-05   treadmill                                         
2025-06-05   pull-ups                        12                
2025-06-05   chest press                     25    40.0        
2025-06-06   barbell row               3           10.0        
2025-06-07   face pulls                                        
2025-06-07   chest press               3     12    35.0        
2025-06-08   chest press               3     12    50.0                    
2025-08-29   incline dumbbell press    3     12    25.0
```
⤷ example terminal print of all entries

**[A] Add** → creates a new log entry with date, exercise name, sets, reps, and weight.
```bash
date [YYYY-MM-DD]: 202-08 r1
[!] Invalid date format! Please use YYYY-MM-DD.
date [YYYY-MM-DD]: 2025-08-29
name: inclined dumbbell press
sets: 3
reps: 12
weight: 25

[i] New entry added!
```
⤷ example entry input

* sets, reps & weight are optional values, and the program works fine without them

**[F] Filter** → narrows down logs by exercise or by date.
```bash
Filter by?
1. date
2. exercise

>
```
⤷ filter sub-menu

1. By date:
   ```bash
   WORKOUT LOGS '2025-02-12':
   ------------------------------------------
   Bicep Curl                3     15    12.5        
   Lat Pulldown              4     10    50.0        
   Overhead Press            3     8     40.0        
   Leg Press                 5     12    120.0
   ```
   ⤷ entries filtered for date '2025-02-12'

2. By exercise:
   ```bash
   WORKOUT LOGS 'chest press':
   ------------------------------------------
   2025-03-07                3                       
   2025-06-03                3     12    40.0        
   2025-06-04                3     12    35.0        
   2025-06-05                      25    40.0        
   2025-06-07                3     12    35.0        
   2025-06-08                3     12    50.0
   ```
   ⤷ entries filtered for exercise 'chest press'

**[S] Stats** → displays summary stats, including number of entries and most performed exercise.
```bash
Total workouts logged: 23
Most performed exercise: chest press
```
⤷ example statistics

**[E] Export** → saves a readable version of all log entries to a separate file.
```bash
2025-02-10:
squat: 5 sets of 10 reps, at 80.0kg

2025-02-11:
deadlift: 3 sets of 6 reps, at 100.0kg
pull-ups

2025-02-12:
bicep curl: 3 sets of 15 reps, at 12.5kg
lat pulldown: 4 sets of 10 reps, at 50.0kg
overhead press: 3 sets of 8 reps, at 40.0kg
leg press: 5 sets of 12 reps, at 120.0kg

2025-02-14:
tricep dips: 10 reps

2025-02-15:
face pulls: 3 sets of 15 reps, at 20.0kg

2025-02-16:
barbell row: 4 sets, at 65.0kg

2025-02-17:
barbell row: 4 sets of 8 reps, at 65.0kg

2025-03-07:
chest press: 3 sets

2025-06-03:
chest press: 3 sets of 12 reps, at 40.0kg

2025-06-04:
chest press: 3 sets of 12 reps, at 35.0kg

2025-06-05:
treadmill
pull-ups: 12 reps
chest press: 25 reps, at 40.0kg

2025-06-06:
barbell row: 3 sets, at 10.0kg

2025-06-07:
face pulls
chest press: 3 sets of 12 reps, at 35.0kg

2025-06-08:
chest press: 3 sets of 12 reps, at 50.0kg

2025-06-10:
4 blocos: 12 sets of 35 reps

2025-08-29:
incline dumbbell press: 3 sets of 12 reps, at 25.0kg
```
⤷ export result in 'workouts/logbook.txt'

**[D] Delete** → removes entries either by exercise, by date, or by a specific exercise on a specific date.

## 🚏 | Roadmap
- Currently working on a more complete catalog structure, which includes specific areas for muscle groups (eg. upper/lower chest), and notes of how to perform each exercise

## 💾 | License
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

## 💌 | Acknowledgements

This project grew out of three separate scripts I wrote at different points in my first year of Software Engineering:

- creator.py - my earliest attempt at building something practical, done early in the year.

- **logger.py** - written much later in the academic year as I gained more confidence.

- **generator.py** - hacked together during a trip to Morocco in May.

I eventually realised they were all gym-related and decided to combine them into one project. 

This step felt huge for me, both technically and personally, as I was (and still am) very new to coding.

---

Project by [gettingfunkier](https://github.com/gettingfunkier) . 2024/25 🤍