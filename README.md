# T - Rex Reinforcement Learning
The T-Rex game is the offline pastime for many people using the chrome browser. This repository creates a bot that's as good as you at it, and over time exceeds even that.

Many ML solutions have been created solve this problem and it a classic RL problem. The key difference is that the focus of this repository is on the user interface individuals use to "train" this RL model. The goal is that they won't need any ML experience at all.

This solution can also generalize to many other games, simply select various regions of the screen (gameplay, score, reset, and start) and define particular keystrokes (up, down, left, right, and spacebar). The RL program should take care of the rest.

## Sub Projects

 - [x] Screen Capture
 - [x] I/O Recognition
 - [ ] ML Model
 - [x] Robotic Automation
 - [ ] Training Loop

## Screen Capture

Capture parts of the screen to use in the RL Model

## IO Recognition

Use OCR to detect things like the score of the game.

## ML Model

Use the ML Model to define the RL architecture of the model.

## Robotic Automation

Use Robotic automation to type and click in various regions of the screen.

## Training Loop

The loop that ties all of these parts together.
