# cccc

Claims first unclaimed student in a CAT-SOOP Queue.

At MIT, some subjects running [CAT-SOOP](https://catsoop.mit.edu/website) sites have "queues" where students ask for help or for "checkoffs." You'll be interested in this simple script if you're a lab assistant or TA or plan to be one for such a class and you know what I'm referring to.

### How it works:

* Have the Queue open in your browser like below
![Empty Queue](queue.png)

* Run `cccc.py`
* If the script sees that the browser showing the Queue is the active window, it will wait for a student to add theirself
* At that point, the script presses `c` on your keyboard for you until the student is claimed
* `Ctrl+C` to quit

Use with discretion. This gives you an arguably unfair advantage if you and the people you work with are the kind to enjoy giving checkoffs and helping the students in general.

### Assumes:

* Windows OS
* Firefox browser

The latter assumption should be straightforward to change if desired.

### Dependencies:

* `pywin32`
* `keyboard`
