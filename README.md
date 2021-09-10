# cccc

Claims first unclaimed student in a CAT-SOOP Queue.

At MIT, some subjects running [CAT-SOOP](https://catsoop.mit.edu/website) sites have *help queues* where students ask for help or for "checkoffs." You'll be interested in this simple script if you're a lab assistant or TA or plan to be one for such a class and you know what at all I'm referring to.

Currently, the script is only for Windows OS (due to the `pwin32` module), and it looks for the help queue on either Firefox or Google Chrome (read script for how it does this).

Use with discretion. This gives you an arguably unfair advantage if you and the people you work with are the kind to enjoy your job as a LA/TA and helping the students in general.

### Starting up

1. Install the dependencies (`pywin32`, `keyboard`)
2. Have the Queue open in your browser like this:

![Empty Queue](https://i.imgur.com/eM6dEvB.jpg)

3. Run `cccc.py`
4. If the script sees that the browser showing the Queue is the active window, it will wait for students to add themselves
5. When there's an unclaimed student, the script presses `c` on your keyboard for you until the student is claimed
6. `Ctrl+C` to quit
