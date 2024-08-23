# A-to-D
```Plan``` your ```work time``` with your new on-screen time planner.

# Setup
To use ```A-to-D``` you need to download and install [python](https://www.python.org/downloads/).

After installing ```python```, run following command to install ```PyQt5```
```
pip install PyQt5
```

# Usage
```A-to-D``` is a ```gui``` tool. ```A-to-D``` window stays always on top, to always stay in action. To use ```A-to-D``` just run provided script ( a-to-d.pyw ).

You will see this window.

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/1.jpg?raw=true)

This window consist of active ```tasks``` ( [adding tasks](#add-task) ), ```close``` button (pink one) and ```expand``` button (purple one).

Click ```expand``` button to reveal other ```panels```, each one with a different set of functionalities.

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/2.jpg?raw=true)

# Right Panel
```Right panel``` is responsible for managing ```tasks```:

- [```Add Task```](#add-task)
- [```Remove Task```](#remove-task)
- [```Reset All Tasks```](#reset-all-tasks)
- [```Export Tasks```](#export-tasks)
- [```Import Tasks```](#import-tasks)

## Add Task
There are two ```type``` of ```tasks```:
- time defined ```tasks```

> ```Tasks``` with estaminated execution time.

> For eg. estaminated time for "check e-mails" ```task``` is 5 minutes.

- non time defined ```tasks```

> ```Tasks``` with no estaminated execution time.

> For eg. you can't tell how much time ```task``` "wait for email response" will take.

### Time Defined Tasks
Time defined ```task``` consist of task ```name```, and task ```duration```.

For eg. this is how you plan to "read" for 1 hour and 0 minutes

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/3.jpg?raw=true)

Than press

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/4.jpg?raw=true)

For time defined ```tasks``` you can check how much time is left to finish it

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/5.jpg?raw=true)

### Non Time Defined Tasks
Non time defined ```task``` consist of task ```name```.

For eg. this is how you plan to "wait for email response"

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/6.jpg?raw=true)

Than press

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/7.jpg?raw=true)

## Remove Task
This function will remove last added task.

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/8.jpg?raw=true)

## Reset All Tasks
This function will remove all tasks.

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/9.jpg?raw=true)

## Export Tasks
You can export current tasks to file, to use it on another device, share it with another users, or [import it as routine](#import-routines)

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/10.jpg?raw=true)

## Import Tasks
You can import previously exported tasks

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/11.jpg?raw=true)

# Main Panel
```Main panel``` is responsible for:
- ```showing active tasks and time left```
- [```removing finished tasks```](#removing-finished-tasks)

## Removing finished tasks
In this ```panel``` you are able to remove any selected ```task``` that is displayied.

To remove that ```task``` just grab it with the mouse and slide it outside the window

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/12.jpg?raw=true)

# Left Panel
```Left panel``` is responsible for managing ```routines```:

- [```Save As Routine```](#save-as-routine)
- [```Load Routine```](#load-routine)
- [```Edit Routine Name```](#edit-routine-name)
- [```Delete Routine```](#delete-routine)
- [```Import Routines```](#import-routines)

> ```Routines``` are sets of ```tasks``` that are often used

> Eg. if you check emails and read news on every monday,

> you can add ```routine``` named "monday",

> that consist of ```tasks``` "check emails" and "read news".

> To use some ```routine```, [load it](#load-routine) as normal ```task``` set

## Save As Routine
Save all active ```tasks``` to a ```routine```

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/13.jpg?raw=true)

## Load Routine
To load the ```routine```, just click on ```routine``` name, and all ```tasks``` will be displayied in ```main panel```

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/14.jpg?raw=true)

## Edit Routine Name
To change ```routine``` name, click button on the left of the name of ```routine```

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/15.jpg?raw=true)

## Delete Routine
To delete ```routine```, click button on the right of the name of ```routine```

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/16.jpg?raw=true)

## Import Routines
You can import ```routine``` from previously [```exported tasks```](#export-tasks) file.

![](https://github.com/sbartoszuk/A-to-D/blob/main/read_me_images/17.jpg?raw=true)
