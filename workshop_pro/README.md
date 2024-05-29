## Workshop 4 - Solution

This is a workshop related with a backend system to provide a vehicles catalog using python and patterns design.

Inside the folder workshop_pro there is the readme who will be the technical report

## Requirements

The requirements for this workshop are presented as follows:

- The rest of the requirements were mentioned on the last 3 workshops
- You should log all the actions made by the users, so you could track both the changes
made in the vehicles and searches performed
- Make unit tests for each subsystem
- Use the code smells
- Check the logs in order to figure out the functionalities
- Apply the pattern observer for a newsletter
- Make cache memory about the last three searchs made in the system
- Recovery the last deleted vehicle
- Add a new engine, a hybrid engine
- Implement the pattern chain of responsabilities


## Business Rules

- Every vehicle just have chassis of type A or B.
- Gas consumption is based on engine information...
- Gas consumption is based on next equation. 
  `1.1 ∗ engine.potency + 0.2 ∗ engine.weight - (0.3 if A or 0.5 if B)`
- Make the code more flexible

## Technical Views

- This file will have the reports in a simple way, the detail document will be 'TechnicalReport.pdf'

- The program give by the teacher had some problems, such as the execution, authentication with files JSON and some logic inside the system

- To solve the first problem i found out, i was necessary to implement a code on 'pyproject.toml' with the purpose to indicate the begin of the project, then the project must be initialized on CMD due to the dependencies.

- The next problem i found out was the path of the 'users.json', the path must be absolute

- For some problemos presented on the workshop it is necessary to implement some behavioral pattern such as, observer, chain of responsability and maybe, memento. 

- The chain of responsability is used for make validations of an object, if the object pass all the validations the object will be correct, if not it is necessary to raise an error

- For make the unit test, with pytest, where the main test of each file is show that the object is created corretly and with the interface could be implementing a liskov sustitution, if the code pass those tests, the code will be working correctly.
