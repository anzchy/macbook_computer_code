# Harvard CS50x Course Notes

# Lecture 0-Scratch



+   [Welcome!](#welcome)
+   [What’s Ahead](#whats-ahead)
+   [Community!](#community)
+   [Computer Science](#computer-science)
+   [ASCII](#ascii)
+   [Unicode](#unicode)
+   [Representation](#representation)
+   [Algorithms](#algorithms)
+   [Pseudocode](#pseudocode)
+   [Artificial Intelligence](#artificial-intelligence)
+   [Scratch](#scratch)
+   [Hello World](#hello-world)
+   [Hello, You](#hello-you)
+   [Meow and Abstraction](#meow-and-abstraction)
+   [Conditionals](#conditionals)
+   [Oscartime](#oscartime)
+   [Ivy’s Hardest Game](#ivys-hardest-game)
+   [Summing Up](#summing-up)

## Welcome!

+   This class is about more than computer programming!
+   Indeed, this class is about problem-solving in a way that is exceedingly empowering! You will likely take the problem solving that you learn here will likely be instantly applicable to your work beyond this course and even your career as a whole!
+   However, it will not be easy! You will be “drinking from the firehose” of knowledge during this course. You’ll be amazed at what you will be able to accomplish in the coming weeks.
+   This course is far more about you advancing “you” from “where you are today” than hitting some imagined standard.
+   The most important opening consideration in this course: Give the time you need to learn through this course. Everyone learns differently. If something does not work out well at the start, know that with time you will grow and grow in your skill.
+   Don’t be scared if this is your first computer science class! For most of your peers, this is their first computer science class too!

## What’s Ahead

+   You will be learning this week about Scratch, a visual programming language.
+   Then, in future weeks, you will learn about C. That will look something like this:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
      printf("hello, world\n");
    }
    ```
    
+   Further, as the weeks progress, you will learn about algorithms.
+   You will learn about memory.
+   You will learn about buggy code and what causes computer crashes.
+   You will learn about data structures such as a hash table.
+   Then, we will transition to a new, higher-level language called *Python*. Your code will look something like this:
    
+   This class will give you a strong understanding of how recent programming languages developed from the earlier ones.
+   You will learn SQL, JavaScript, HTML, and CSS.
+   We will also be looking at how we can use databases and third-party frameworks to build web applications.

## Community!

+   You are part of a community of those taking this course at Harvard College, Harvard Extension School, and via edX.org.
+   Puzzle Day and the CS50 Fair
+   You can attend CS50 Lunches and CS50 Hackathon, if you are student on Harvard’s campus.

## Computer Science

+   Essentially, computer programming is about taking some input and creating some output - thus solving a problem. What happens in between the input and output, what we could call *a black box,* is the focus of this course.
    
    ![Black box with input and output](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide38.png "Black box with input and output")
    
+   For example, we may need to take attendance for a class. We could use a system called *unary* to count, one finger at a time.
+   Computers today count using a system called *binary*. It’s from the term *binary digit* that we get a familiar term called *bit*. A *bit* is a zero or one: on or off.
+   Computers only speak in terms of zeros and ones. Zeros represent *off.* Ones represent *on.* Computers are millions, and perhaps billions, of transistors that are being turned on and off.
+   If you imagine using a light bulb, a single bulb can only count from zero to one.
+   However, if you were to have three light bulbs, there are more options open to you!
+   Using three light bulbs, the following could represent zero:
    
+   Similarly, the following would represent one:
    
+   By this logic, we could propose that the following equals two:
    
+   Extending this logic further, the following represents three:
    
+   Four would appear as:
    
+   We could, in fact, using only three light bulbs count as high as seven!
    
+   As a heuristic, we could imagine that the following values represent each possible place in our *binary digit*:
    
+   Computers use ‘base-2’ to count. This can be pictured as follows:
    
+   Therefore, you could say that it would require three bits (the four’s place, the two’s place, and the one’s place) to represent a number as high as seven.
+   Computers generally use eight bits (also known as a *byte*) to represent a number. For example, `00000101` is the number 5 in *binary*. `11111111` represents the number 255.

## ASCII

+   Just as numbers are binary patterns of ones and zeros, letters are represented using ones and zeros too!
+   Since there is an overlap between the ones and zeros that represent numbers and letters, the *ASCII* standard was created to map specific letters to specific numbers.
+   For example, the letter `A` was decided to map to the number 65. `01000001` represents the number 65 in binary.
+   If you received a text message, the binary under that message might represent the numbers 72, 73, and 33. Mapping these out to ASCII, your message would look as follows:
    
+   Thank goodness for standards like ASCII that allow us to agree upon these values!
+   Here is an expanded map of ASCII values:
    
    ![ASCII map](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide93.png "ASCII map")
    
+   If you wish, you can learn more about [ASCII](https://en.wikipedia.org/wiki/ASCII).
+   Since binary can only count up to *255* we are limited to the number of characters represented by ASCII.

## Unicode

+   As time has rolled on, there are more and more ways to communicate via text.
+   Since there were not enough digits in binary to represent all the various characters that could be represented by humans, the *Unicode* standard expanded the number of bits that can be transmitted and understood by computers. Unicode includes not only special characters, but emoji as well.
+   There are emoji that you probably use every day. The following may look familiar to you:
    
    ![emoji](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide103.png "emoji")
    
+   Computer scientists faced a challenge when wanting to assign various skin tones to each emoji to allow the communication to be further personalized. In this case, the creators and contributors of emoji decided that the initial bits would be the structure of the emoji itself, followed by skin tone.
+   For example, the unicode for a generic thumbs up is `U+1F44D`. However, the following represents the same thumbs up with a different skin tone: `U+1F44D U+1F3FD`.
+   More and more features are being added to the Unicode standard to represent further characters and emoji.
+   If you wish, you can learn more about [Unicode](https://en.wikipedia.org/wiki/Unicode).
+   If you wish, you can learn more about [emoji](https://en.wikipedia.org/wiki/Emoji).

## Representation

+   Zeros and ones can be used to represent color.
+   Red, green, and blue (called `RGB`) is a combination of three numbers.
    
    ![red green blue boxes](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide118.png "red green blue boxes")
    
+   Taking our previously used 72, 73, and 33, which said `HI!` via text, would be interpreted by image readers as a light shade of yellow. The red value would be 72, the green value would be 73, and the blue would be 33.
    
    ![yellow box](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide120.png "yellow box")
    
+   Further, zeros and ones can be used to represent images, videos, and music!
+   Images are simply collections of RGB values.
+   Videos are sequences of many images that are stored together, just like a flipbook.
+   Music can be represented through MIDI data.

## Algorithms

+   Problem-solving is central to computer science and computer programming.
+   Imagine the basic problem of trying to locate a single name in a phone book.
+   How might you go about this?
+   One approach could be to simply read from page one to the next to the next until reaching the last page.
+   Another approach could be to search two pages at a time.
+   A final and perhaps better approach could be to go to the middle of the phone book and ask, “Is the name I am looking for to the left or to the right?” Then, repeat this process, cutting the problem in half and half and half.
+   Each of these approaches could be called algorithms. The speed of each of these algorithms can be pictured as follows in what is called *big-O notation*:
    
    ![big o notation](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide141.png "big o notation")
    
    Notice that the first algorithm, highlighted in red, has a big-O of `n` because if there are 100 names in the phone book, it could take up to 100 tries to find the correct name. The second algorithm, where two pages were searched at a time, has a big-O of ‘n/2’ because we searched twice as fast through the pages. The final algorithm has a big-O of log2n as doubling the problem would only result in one more step to solve the problem.
    

## Pseudocode

+   The ability to create *pseudocode* is central to one’s success in both this class and in computer programming.
+   Pseudocode is a human-readable version of your code. For example, considering the third algorithm above, we could compose pseudocode as follows:
    
    ```auto
    1  Pick up phone book
    2  Open to middle of phone book
    3  Look at page
    4  If person is on page
    5      Call person
    6  Else if person is earlier in book
    7      Open to middle of left half of book
    8      Go back to line 3
    9  Else if person is later in book
    10     Open to middle of right half of book
    11     Go back to line 3
    12 Else
    13     Quit
    ```
    
+   Pseudocoding is such an important skill for at least two reasons. First, when you pseudocode before you create formal code, it allows you to think through the logic of your problem in advance. Second, when you pseudocode, you can later provide this information to others that are seeking to understand your coding decisions and how your code works.
+   Notice that the language within our pseudocode has some unique features. First, some of these lines begin with verbs like *pick up,* *open,* *look at.* Later, we will call these *functions*.
+   Second, notice that some lines include statements like `if` or `else if.` These are called *conditionals*.
+   Third, notice how there are expressions that can be stated as *true* or *false,* such as “person is earlier in the book.” We call these *boolean expressions*.
+   Finally, notice how these statements like “go back to line 3.” We call these *loops*.
+   These building blocks are the fundamentals of programming.
+   In the context of *Scratch*, which is discussed below, we will use each of the above basic building blocks of programming.

## Artificial Intelligence

+   Consider how we can utilize the building blocks above to start creating our own artificial intelligence. Look at the following pseudocode:
    
    ```auto
    If student says hello
        Say hello back
    Else if student says goodbye
        Say goodbye back
    Else if student asks how you are
        Say you're well
    Else if student asks why 111 in binary is 7 in decimal
    ...
    ```
    
    Notice how just to program a handful of interactions, many lines of code would be required. How many lines of code would be required for thousands or tens of thousands of possible interactions?
    
+   `large language models` look at patterns in large blocks of language. Such language models attempt to create a best guess of what words come after one another or alongside one another.
+   As very useful in many avenues of life and work, we stipulate that the utilization of AI-based software other than CS50’s own is *not reasonable*.
+   CS50’s own AI-based software tool called [CS50 Duck](https://cs50.ai/) is an AI helper that you can use during this course. It will help you, but not give away the entire answers to the course’s problems.

## Scratch

+   *Scratch* is a visual programming language developed by MIT.
+   Scratch utilizes the same essential coding building blocks that we covered earlier in this lecture.
+   Scratch is a great way to get into computer programming because it allows you to play with these building blocks in a visual manner, not having to be concerned about the syntax of curly braces, semicolons, parentheses, and the like.
+   Scratch `IDE` (integrated development environment) looks like the following:
    
    ![scratch interface](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide162.png "scratch interface")
    
    Notice that on the left, there are *building blocks* that you can use in your programming. To the immediate right of the building blocks, there is the area to which you can drag blocks to build a program. To the right of that, you see the *stage* where a cat stands. The stage is where your programming comes to life.
    
+   Scratch operates on a coordinate system as follows:
    
    ![scratch coordinate system](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide167.png "scratch coordinate system")
    
    Notice that the center of the stage is at coordinate (0,0). Right now, the cat’s position is at that same position.
    

## Hello World

+   To begin, drag the “when green flag clicked” building block to the programming area. Then, drag the `say` building block to the programming area and attach it to the previous block.
    
    ```scratch
    when green flag clicked
    say [hello, world]
    ```
    
    Notice that when you click the green flag now, on the stage, the cat says, “hello world.”
    
+   This illustrates quite well what we were discussing earlier regarding programming:
    
    ![scratch with black box](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Slide172.png "scratch with black box")
    
    Notice that the input `hello world` is passed to the function `say`, and the *side effect* of that function running is the cat saying `hello world`.
    

## Hello, You

+   We can make your program more interactive by having the cat say `hello` to someone specific. Modify your program as below:
    
    ```scratch
    when green flag clicked
    ask [What's your name?] and wait
    say (join [hello,] (answer))
    ```
    
    Notice that when the green flag is clicked, the function `ask` is run. The program prompts you, the user, `What's your name?` It then stores that name in the *variable* called `answer`. The program then passes `answer` to a special function called `join`, which combines two strings of text `hello`, and whatever name was provided. These collectively are passed to the `say` function. The cat says, `Hello,` and a name. Your program is now interactive.
    
+   Quite similarly, we can modify our program as follows:
    
    ```scratch
    when green flag clicked
    ask [What's your name?] and wait
    speak (join [hello,] (answer))
    ```
    
    Notice that this program, when the green flag is clicked, passes the same variable, joined with `hello`, to a function called `speak`.
    

## Meow and Abstraction

+   Along with pseudocoding, *abstraction* is an essential skill and concept within computer programming.
+   Abstraction is the act of simplifying a problem into smaller and smaller problems.
+   For example, if you were hosting a huge dinner for your friends, the *problem* of having to cook the entire meal could be quite overwhelming! However, if you break down the task of cooking the meal into smaller and smaller tasks (or problems), the big task of creating this delicious meal might feel less challenging.
+   In programming, and even within Scratch, we can see abstraction in action. In your programming area, program as follows:
    
    ```scratch
    when green flag clicked
    play sound (Meow v) until done
    wait (1) seconds
    play sound (Meow v) until done
    wait (1) seconds
    play sound (Meow v) until done
    ```
    
    Notice that you are doing the same thing over and over again. Indeed, if you see yourself repeatedly coding the same statements, it’s likely the case that you could program more artfully – abstracting away this repetitive code.
    
+   You can modify your code as follows:
    
    ```scratch
    when green flag clicked
    repeat (3)
    play sound (Meow v) until done
    wait (1) seconds
    ```
    
    Notice that the loop does exactly as the previous program did. However, the problem is simplified by abstracting away the repetition to a block that *repeats* the code for us.
    
+   We can even advance this further by using the `define` block, where you can create your own block (your own function)! Write code as follows:
    
    ```scratch
    define meow
    play sound (Meow v) until done
    wait (1) seconds
    
    when green flag clicked
    repeat (3)
    meow
    ```
    
    Notice that we are defining our own block called `meow`. The function plays the sound `meow`, then waits one second. Below that, you can see that when the green flag is clicked, our meow function is repeated three times.
    
+   We can even provide a way by which the function can take an input `n` and repeat a number of times:
    
    ```scratch
    define meow n times
    repeat (n)
     play sound [meow v] until done
     wait (1) seconds
    ```
    
    Notice how `n` is taken from “meow n times.” `n` is passed to the meow function through the `define` block.
    
+   The cat, by the way, we can call a `sprite` – a general term used in game programming for an object or character on the screen with which the player will interact.

## Conditionals

+   *conditionals* are an essential building block of programming, where the program looks to see if a specific condition has been met. If a condition is met, the program does something.
+   To illustrate a conditional, write code as follows:
    
    ```scratch
    when green flag clicked
    forever
    if <touching (mouse-pointer v)?> then
    play sound (Meow v) until done
    ```
    
    Notice that the `forever` block is utilized such that the `if` block is triggered over and over again, such that it can check continuously if the cat is touching the mouse pointer.
    
+   We can modify our program as follows to integrate video sensing:
    
    ```scratch
    when video motion > (50)
    play sound (Meow v) until done
    ```
    
+   Remember, programming is often a process of trial and error. If you get frustrated, take time to talk yourself through the problem at hand. What is the specific problem that you are working on right now? What is working? What is not working?

## Oscartime

+   We showed you in this lecture a number of Scratch programs to stoke your imagination.
+   *Oscartime* is one of David’s own Scratch programs – though the music may haunt him because of the number of hours he listened to it while creating this program. Take a few moments to play through the game yourself.
+   Building Oscartime ourselves, we first add the lamp post.
    
    ![oscartime interface](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week0Scratch10.png "oscartime interface")
    
+   Then, write code as follows:
    
    ```scratch
    when green flag clicked
    switch costume to (oscar1 v)
    forever
    if <touching (mouse-pointer v)?> then
    switch costume to (oscar2 v)
    else
    switch costume to (oscar1 v)
    ```
    
    Notice that moving your mouse over Oscar changes his costume. You can learn more by [exploring these code blocks](https://scratch.mit.edu/projects/565100517).
    
+   Then, modify your code as follow to create a falling piece of trash:
    
    ```scratch
    when green flag clicked
    go to x: (pick random (-240) to (240)) y: (180)
    forever
    if <(distance to (floor v)) > (0)> then
    change y by (-3)
    ```
    
    Notice that the trash’s position on the y-axis always begins at 180. The x position is randomized. While the trash is above the floor, it goes down 3 pixels at a time. You can learn more by [exploring these code blocks](https://scratch.mit.edu/projects/565117390).
    
+   Next, modify your code as follows to allow for the possibility of dragging trash.
    
    ```scratch
    when green flag clicked
    forever
    if <<mouse down?> and <touching (mouse-pointer v) ?>> then
    go to (mouse-pointer v)
    ```
    
    You can learn more by [exploring these code blocks](https://scratch.mit.edu/projects/565119737).
    
+   Next, we can implement the scoring variables as follows:
    
    ```scratch
    when green flag clicked
    forever
    if <touching (Oscar v) ?> then
    change (score) by (1)
    go to x: (pick random (-240) to (240)) y: (180)
    ```
    
    You can learn more by [exploring these code blocks](https://scratch.mit.edu/projects/565472267).
    
+   Go try the full game [Oscartime](https://scratch.mit.edu/projects/277537196).

## Ivy’s Hardest Game

+   Moving away from Oscartime to Ivy’s Hardest Game, we can now imagine how to implement movement within our program.
+   Our program has three main components.
+   First, write code as follows:
    
    ```scratch
    when green flag clicked
    go to x: (0) y: (0)
    forever
    listen for keyboard
    feel for walls
    ```
    
    Notice that when the green flag is clicked, our sprite moves to the center of the stage at coordinates (0,0) and then listens for the keyboard and checks for walls forever.
    
+   Second, add this second group of code blocks:
    
    ```scratch
    define listen for keyboard
    if <key (up arrow v) pressed?> then
    change y by (1)
    end
    if <key (down arrow v) pressed?> then
    change y by (-1)
    end
    if <key (right arrow v) pressed?> then
    change x by (1)
    end
    if <key (left arrow v) pressed?> then
    change x by (-1)
    end
    ```
    
    Notice how we have created a custom `listen for keyboard` script. For each of our arrow keys on the keyboard, it will move the sprite around the screen.
    
+   Finally, add this group of code blocks:
    
    ```scratch
    define feel for walls
    if <touching (left wall v) ?> then
    change x by (1)
    end
    if <touching (right wall v) ?> then
    change x by (-1)
    end
    ```
    
    Notice how we also have a custom `feel for walls` script. When a sprite touches a wall, it moves it back to a safe position – preventing it from walking off the screen.
    
+   You can learn more by [exploring these code blocks](https://scratch.mit.edu/projects/326129433).
+   Go try the full game [Ivy’s Hardest Game](https://scratch.mit.edu/projects/326129433/).
+   Scratch allows for many sprites to be on the screen at once.
+   Adding another sprite, add the following code blocks to your program:
    
    ```scratch
    when green flag clicked
    go to x: (0) y: (0)
    point in direction (90)
    forever
    if <<touching (left wall v)?> or <touching (right wall v)?>> then
    turn right (180) degrees
    end
    move (1) steps
    end
    ```
    
    Notice how the Yale sprite seems to get in the way of the Harvard sprite by moving back and forth. When it bumps into a wall, it turns around until it bumps the wall again. You can learn more by [exploring these code blocks](https://scratch.mit.edu/projects/565127193).
    
+   You can even make a sprite follow another sprite. Adding another sprite, add the following code blocks to your program:
    
    ```scratch
    when green flag clicked
    go to (random position v)
    forever
    point towards (Harvard v)
    move (1) steps
    ```
    
    Notice how the MIT logo now seems to follow around the Harvard one. You can learn more by [exploring these code blocks](https://scratch.mit.edu/projects/565479840).
    
+   Go try the full game [Ivy’s Hardest Game](https://scratch.mit.edu/projects/565742837).

## Summing Up

In this lesson, you learned how this course sits in the wide world of computer science and programming. You learned…

+   Few students come to this class with prior programming experience!
+   You are not alone! You are part of a community.
+   Problem solving is the essence of the work of computer scientists.
+   This course is not simply about programming – this course will introduce you to a new way of learning that you can apply to almost every area of life.
+   How numbers, text, images, music, and video are understood by computers.
+   The fundamental programming skill of pseudocoding.
+   Reasonable and unreasonable ways to utilize AI in this course.
+   How abstraction will play a role in your future work in this course.
+   The basic building blocks of programming, including functions, conditionals, loops, and variables.
+   How to build a project in Scratch.

See you next time!


# Lecture 1-C programming



+   [Welcome!](#welcome)
+   [Hello World](#hello-world)
+   [Functions](#functions)
+   [Variables](#variables)
+   [Conditionals](#conditionals)
+   [Loops](#loops)
+   [Operators and Abstraction](#operators-and-abstraction)
+   [Linux and the Command Line](#linux-and-the-command-line)
+   [Mario](#mario)
+   [Comments](#comments)
+   [Types](#types)
+   [Summing Up](#summing-up)

## Welcome!

+   In our previous session, we learned about Scratch, a visual programming language.
+   Indeed, all the essential programming concepts presented in Scratch will be utilized as you learn how to program any programming language.
+   Recall that machines only understand binary. Where humans write *source code*, a list of instructions for the computer that is human readable, machines only understand what we can now call *machine code*. This machine code is a pattern of ones and zeros that produces a desired effect.
+   It turns out that we can convert *source code* into `machine code` using a very special piece of software called a *compiler*. Today, we will be introducing you to a compiler that will allow you to convert source code in the programming language *C* into machine code.
+   Today, in addition to learning about how to code, you will be learning about how to write good code.
+   Code can be evaluated upon three axes. First, *correctness* refers to “does the code run as intended?” Second, *design* refers to “how well is the code designed?” Finally, *style* refers to “how aesthetically pleasing and consistent is the code?”

## Hello World

+   The integrated development environment (IDE) that is utilized for this course is *Visual Studio Code*, affectionately referred to as , which can be accessed via that same url, or simply as \*VS Code.\*
+   One of the most important reasons we utilize VS Code is that it has all the software required for the course already pre-loaded on it. This course and the instructions herein were designed with VS Code in mind.
+   Manually installing the necessary software for the course on your own computer is a cumbersome headache. Best always to utilize VS Code for assignments in this course.
+   You can open VS Code at [cs50.dev](https://cs50.dev/).
+   The compiler can be divided into a number of regions:
    
    ![IDE](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week1Slide017.png "IDE") Notice that there is a *file explorer* on the left side where you can find your files. Further, notice that there is a region in the middle called a *text editor* where you can edit your program. Finally, there is a `command line interface`, known as a *CLI*, *command line*, or *terminal window* where we can send commands to the computer in the cloud.
    
+   We will be using three commands to write, compile, and run our first program:
    
    ```auto
    code hello.c
    
    make hello
    
    ./hello
    
    ```
    
    The first command, `code hello.c` creates a file and allows us to type instructions for this program. The second command, `make hello`, *compiles* the file from our instructions in C and creates an executable file called `hello`. The last command, `./hello`, runs the program called `hello`.
    
+   We can build your first program in C by typing `code hello.c` into the terminal window. Notice that we deliberately lowercased the entire filename and included the `.c` extension. Then, in the text editor that appears, write code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        printf("hello, world\n");
    }
    ```
    
    Note that every single character above serves a purpose. If you type it incorrectly, the program will not run. `printf` is a function that can output a line of text. Notice the placement of the quotes and the semicolon. Further, notice that the `\n` creates a new line after the words `hello, world`.
    
+   Clicking back in the terminal window, you can compile your code by executing `make hello`. Notice that we are omitting `.c`. `make` is a compiler that will look for our `hello.c` file and turn it into a program called `hello`. If executing this command results in no errors, you can proceed. If not, double-check your code to ensure it matches the above.
+   Now, type `./hello` and your program will execute saying `hello, world`.
+   Now, open the *file explorer* on the left. You will notice that there is now both a file called `hello.c` and another file called `hello`. `hello.c` is able to be read by the compiler: It’s where your code is stored. `hello` is an executable file that you can run, but cannot be read by the compiler.

## Functions

+   In Scratch, we utilized the `say` block to display any text on the screen. Indeed, in C, we have a function called `printf` that does exactly this.
+   Notice our code already invokes this function:
    
    ```auto
    printf("hello, world\n");
    ```
    
    Notice that the printf function is called. The argument passed to printf is ‘hello, world\\n’. The statement of code is closed with a `;`.
    
+   A common error in C programming is the omission of a semicolon. Modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        printf("hello, world\n")
    }
    ```
    
    Notice the semicolon is now gone.
    
+   In your terminal window, run `make hello`. You will now be met with numerous errors! Placing the semicolon back in the correct position and running `make hello` again, the errors go away.
+   Notice also the special symbol `\n` in your code. Try removing those characters and *making* your program again by executing `make hello`. Typing `./hello` in the terminal window, how did your program change? This `\` character is called an *escape character* that tells the compiler that `\n` is a special instruction.
+   Restore your program to the following:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        printf("hello, world\n");
    }
    ```
    
    Notice the semicolon and `\n` have been restored.
    
+   The statement at the start of the code `#include <stdio.h>` is a very special command that tells the compile that you want to use the capabilities of a *library* called `stdio.h`, a *header file*. This allows you, among many other things, to utilize the `printf` function. You can read about all the capabilities of this library on the [Manual Pages](https://manual.cs50.io/). The Manual Pages provide a means by which to better understand what various commands do and how they function.
+   Libraries are collections of pre-written functions that others have written in the past that we can utilize in our code.
+   It turns out that CS50 has its own library called `cs50.h`. Let’s use this library in your program.

## Variables

+   Recall that in Scratch, we had the ability to ask the user “What’s your name?” and say “hello” with that name appended to it.
+   In C, we can do the same. Modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        string answer = get_string("What's your name? ");
        printf("hello, %s\n", answer);
    }
    ```
    
    The `get_string` function is used to get a string from the user. Then, the variable `answer` is passed to the `printf` function. `%s` tells the `printf` function to prepare itself to receive a `string`.
    
+   `answer` is a special holding place we call a *variable*. `answer` is of type `string` and can hold any string within it. There are many *data types*, such as `int`, `bool`, `char`, and many others.
+   `%s` is a placeholder called a *format code* that tells the `printf` function to prepare to receive a `string`. `answer` is the `string` being passed to `%s`.
+   Running `make hello` again in the terminal window, notice that numerous errors appear.
+   Looking at the errors `string` and `get_string` are not recognized by the compiler. We have to teach the compiler these features by adding a library called `cs50.h`:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string answer = get_string("What's your name? ");
        printf("hello, %s\n", answer);
    }
    ```
    
    Notice that `#include <cs50.h>` has been added to the top of your code.
    
+   Now running `make hello` again in the terminal window, you can run your program by typing `./hello`. The program now asks for your name and then says hello with your name attached, as intended.
+   `printf` allows for many format codes. Here is a noncomprehensive list of ones you may utilize in this course:
    
    `%s` is used for `string` variables. `%i` is used for `int` or integer variables. You can find out more about this on the [Manual Pages](https://manual.cs50.io/)
    

## Conditionals

+   Another building block you utilized within Scratch was that of *conditionals*. For example, you might want to do one thing if x is greater than y. Further, you might want to do something else if that condition is not met.
+   We look at a few examples from Scratch.
+   In C, you can assign a value to an `int` or integer as follows:
    
    Notice how a variable called `counter` of type `int` is assigned the value `0`.
    
+   C can also be programmed to add one to `counter` as follows:
    
    Notice how `1` is added to the value of `counter`.
    
+   This can be represented also as:
    
    Notice how `1` is added to the value of `counter`. However the `++` is used instead of `counter + 1`.
    
+   You can also subtract one from `counter` as follows:
    
    Notice how `1` is removed to the value of `counter`.
    
+   Using this new knowledge about how to assign values to variables, you can program your first conditional statement.
+   In the terminal window, type `code compare.c` and write code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        int x = get_int("What's x? ");
        int y = get_int("What's y? ");
    
        if (x < y)
        {
            printf("x is less than y\n");
        }
    }
    ```
    
    Notice that we create two variables, an `int` or integer called `x` and another called `y`. The values of these are populated using the `get_int` function.
    
+   You can run your code by executing `make compare` in the terminal window, followed by `./compare`. If you get any error messages, check your code for errors.
+   *Flow charts* are a way by which you can examine how a computer program functions. Such charts can be used to examine the efficiency of our code.
+   Looking at a flow chart of the above code, we can notice numerous shortcomings.
+   We can improve your program by coding as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        int x = get_int("What's x? ");
        int y = get_int("What's y? ");
    
        if (x < y)
        {
            printf("x is less than y\n");
        }
        else if (x > y)
        {
            printf("x is greater than y\n");
        }
        else
        {
            printf("x is equal to y\n");
        }
    }
    ```
    
    Notice that all potential outcomes are now accounted for.
    
+   You can re-make and re-run your program and test it out.
+   Examining this program on a flow chart, you can see the efficiency of our code design decisions.
+   Considering another data type called a `char` we can start a new program by typing `code agree.c` into the terminal window.
+   Where a `string` is a series of characters, a `char` is a single character.
+   In the text editor, write code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user to agree
        char c = get_char("Do you agree? ");
    
        // Check whether agreed
        if (c == 'Y' || c == 'y')
        {
            printf("Agreed.\n");
        }
        else if (c == 'N' || c == 'n')
        {
            printf("Not agreed.\n");
        }
    }
    ```
    
    Notice that single quotes are utilized for single characters. Further, notice that `==` ensure that something *is equal* to something else, where a single equal sign would have a very different function in C. Finally, notice that `||` effectively means *or*.
    
+   You can test your code by typing `make agree` into the terminal window, followed by `./agree`.

## Loops

+   We can also utilize the loops building block from Scratch in our C programs.
+   We look at a few examples from Scratch. Consider the following code:
    
    ```auto
    int counter = 3;
    while (counter > 0)
    {
        printf("meow\n");
        counter = counter - 1;
    }
    ```
    
    Notice that his code assigns the value of `3` to the `counter` variable. Then, the `while` loop says `meow` and removes one from the counter for each iteration. Once the counter is not greater than zero, the loop ends.
    
+   In your terminal window, type `code meow.c` and write code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        printf("meow\n");
        printf("meow\n");
        printf("meow\n");
    }
    ```
    
    Notice this does as intended but has an opportunity for better design.
    
+   We can improve our program by modifying your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int i = 3;
        while (i > 0)
        {
            printf("meow\n");
            i--;
        }
    }
    ```
    
    Notice that we create an `int` called `i` and assign it the value `3`. Then, we create a `while` loop that will run as long as `i > 0`. Then, the loop runs. Every time `1` is subtracted to `i` using the `i--` statement.
    
+   Similarly, we can implement a count-up of sorts by modifying our code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int i = 1;
        while (i <= 3)
        {
            printf("meow\n");
            i++;
        }
    }
    ```
    
    Notice how our counter `i` is started at `1`. Each time the loop runs, it will increment the counter by `1`. Once the counter is greater than `3`, it will stop the loop.
    
+   Generally, in computer science we count from zero. Best to revise your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int i = 0;
        while (i < 3)
        {
            printf("meow\n");
            i++;
        }
    }
    ```
    
    Notice we now count from zero.
    
+   Another tool in our toolbox for looping is a `for` loop.
+   You can further improve the design of our `meow.c` program using a `for` loop. Modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            printf("meow\n");
        }
    }
    ```
    
    Notice that the `for` loop includes three arguments. The first argument `int i = 0` starts our counter at zero. The second argument `i < 3` is the condition that is being checked. Finally, the argument `i++` tells the loop to increment by one each time the loop runs.
    
+   We can even loop forever using the following code:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        while (true)
        {
            printf("meow\n");
        }
    }
    ```
    
    Notice that `true` will always be the case. Therefore, the code will always run. You will lose control of your terminal window by running this code. You can break from an infinite by hitting `control-C` on your keyboard.
    
+   While we will provide much more guidance later, you can create your own function within C as follows:
    
    ```auto
    void meow(void)
    {
        printf("meow\n");
    }
    ```
    
    The initial `void` means that the function does not return any values. The `(void)` means that no values are being provided to the function.
    
+   This function can be used in the main function as follows:
    
    ```auto
    #include <stdio.h>
    
    void meow(void);
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            meow();
        }
    }
    
    void meow(void)
    {
        printf("meow\n");
    }
    ```
    
    Notice how the `meow` function is called with the `meow()` instruction. This is possible because the `meow` function is defined at the bottom of the code and the *prototype* of the function is provided at the top of the code as `void meow(void)`.
    
+   Your `meow` function can be further modified to accept input:
    
    ```auto
    #include <stdio.h>
    
    void meow(int n);
    
    int main(void)
    {
        meow(3);
    }
    
    // Meow some number of times
    void meow(int n)
    {
        for (int i = 0; i < n; i++)
        {
            printf("meow\n");
        }
    }
    ```
    
    Notice that the prototype has changed to `void meow(int n)` to show that `meow` accepts an `int` as its input.
    

## Operators and Abstraction

+   You can implement a calculator in C. In your terminal, type `code calculator.c` and write code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user for x
        int x = get_int("x: ");
    
        // Prompt user for y
        int y = get_int("y: ");
    
        // Perform addition
        printf("%i\n", x + y);
    }
    ```
    
    Notice how the `get_int` function is utilized to obtain an integer from the user twice. One integer is stored in the `int` variable called `x`. Another is stored in the `int` variable called `y`. Then, the `printf` function prints the value of `x + y`, designated by the `%i` symbol.
    
+   *Operators* refer to the mathematical operations that are supported by your compiler. In C, these mathematical operators include:
    
    +   `+` for addition
    +   `-` for subtraction
    +   `*` for multiplication
    +   `/` for division
    +   `%` for remainder
+   *Abstraction* is the art of simplifying our code such that it deals with smaller and smaller problems.
+   Expanding on our previously acquired knowledge about functions, we could *abstract away* the addition into a function. Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int add(int a, int b);
    
    int main(void)
    {
        // Prompt user for x
        int x = get_int("x: ");
    
        // Prompt user for y
        int y = get_int("y: ");
    
        // Perform addition
        int z = add(x, y);
        printf("%i\n", z);
    }
    
    int add(int a, int b)
    {
        int c = a + b;
        return c;
    }
    ```
    
    Notice that the `add` function takes two variables as its input. These values are assigned to `a` and `b` and preforms a calculation, returning the value of `c`. Further, notice that the *scope* (or context in which variables exist) of `x` is the `main` function. The variable `c` is only within the scope of the `add` function.
    
+   The design of this program can be further improved as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int add(int a, int b);
    
    int main(void)
    {
        // Prompt user for x
        int x = get_int("x: ");
    
        // Prompt user for y
        int y = get_int("y: ");
    
        // Perform addition
        printf("%i\n", add(x, y));
    }
    
    int add(int a, int b)
    {
        return a + b;
    }
    ```
    
    Notice that `c` in the `add` function is removed entirely.
    
+   While very useful to be able to abstract away to an `add` function, you can also perform addition through *truncation* as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user for x
        long x = get_long("x: ");
    
        // Prompt user for y
        long y = get_long("y: ");
    
        // Perform addition
        printf("%li\n", x + y);
    }
    ```
    
    Notice that the addition is performed within the `printf` function.
    
+   Similarly, division can be performed as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user for x
        int x = get_int("x: ");
    
        // Prompt user for y
        int y = get_int("y: ");
    
        // Divide x by y
        printf("%i\n", x / y);
    }
    ```
    
    Notice that division is performed within the `printf` function.
    

## Linux and the Command Line

+   *Linux* is an operating system that is accessible via the command line in the terminal window in VS Code.
+   Some common command-line arguments we may use include:
    +   `cd`, for changing our current directory (folder)
    +   `cp`, for copying files and directories
    +   `ls`, for listing files in a directory
    +   `mkdir`, for making a directory
    +   `mv`, for moving (renaming) files and directories
    +   `rm`, for removing (deleting) files
    +   `rmdir`, for removing (deleting) directories
+   The most commonly used is `ls` which will list all the files in the current directory or directory. Go ahead and type `ls` into the terminal window and hit `enter`. You’ll see all the files in the current folder.
+   Another useful command is `mv`, where you can move a file from one file to another. For example, you could use this command to rename `Hello.c` (notice the uppercase `H`) to `hello.c` by typing `mv Hello.c hello.c`.
+   You can also create folders. You can type `mkdir pset1` to create a directory called `pset1`.
+   You can then use `cd pset1` to change your current directory to `pset1`.

## Mario

+   Everything we’ve discussed today has focused on various building-blocks of your work as an emerging computer scientist.
+   The following will help you orient toward working on a problem set for this class in general: How does one approach a computer science related problem?
+   Imagine we wanted to emulate the visual of the game Super Mario Bros. Considering the four question-blocks pictured, how could we create code that roughly represents these four horizontal blocks?
    
    ![Mario Question Marks](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week1Slide123.png "Mario Question Marks")
    
+   In the terminal window, type `code mario.c` and code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i < 4; i++)
        {
            printf("?");
        }
        printf("\n");
    }
    ```
    
    Notice how four question marks are printed here using a loop.
    
+   Similarly, we can apply this same logic to be able to create three vertical blocks.
    
    ![Mario Blocks](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week1Slide125.png "Mario Blocks")
    
+   To accomplish this, modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            printf("#\n");
        }
    }
    ```
    
    Notice how three vertical bricks are printed using a loop.
    
+   What if we wanted to combine these ideas to create a three-by-three group of blocks?
    
    ![Mario Grid](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week1Slide127.png "Mario Grid")
    
+   We can follow the logic above, combining the same ideas. Modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
    ```
    
    Notice that one loop is inside another. The first loop defines what vertical row is being printed. For each row, three columns are printed. After each row, a new line is printed.
    
+   What if we wanted to ensure that the number of blocks to be *constant*, that is, unchangeable? Modify your code as follows:
    
    ```auto
    int main(void)
    {
        const int n = 3;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
    ```
    
    Notice how `n` is now a constant. It can never be changed.
    
+   As illustrated earlier in this lecture, we can make our code prompt the user for the size of the grid. Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        int n = get_int("Size: ");
    
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
    ```
    
    Notice that `get_int` is used to prompt the user.
    
+   A general piece of advice within programming is that you should never fully trust your user. They will likely misbehave, typing incorrect values where they should not. We can protect our program from bad behavior by checking to make sure the user’s input satisfies our needs. Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        int n;
        do
        {
            n = get_int("Size: ");
        }
        while (n < 1);
    
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
    ```
    
    Notice how the user is continuously prompted for the size until the user’s input is 1 or greater.
    

## Comments

+   Comments are fundamental parts of a computer program, where you leave explanatory remarks to yourself and others that may be collaborating with you regarding your code.
+   All code you create for this course must include robust comments.
+   Typically each comment is a few words or more, providing the reader an opportunity to understand what is happening in a specific block of code. Further, such comments serve as a reminder for you later when you need to revise your code.
+   Comments involve placing `//` into your code, followed by a comment. Modify your code as follows to integrate comments:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user for positive integer
        int n;
        do
        {
            n = get_int("Size: ");
        }
        while (n < 1);
    
        // Print an n-by-n grid of bricks
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
    ```
    
    Notice how each comment begins with a `//`.
    

## Types

+   One of C’s shortcomings is the ease by which it managing memory. While C provides you immense control over how memory is utilized, programmers have to be very aware of potential pitfalls of memory management.
+   Types refer to the possible data that can be stored within a variable. For example, a `char` is designed to accommodate a single character like `a` or `2`.
+   Types are very important because each type has specific limits. For example, because of the limits in memory, the highest value of an `int` can be `4294967295`. If you attempt to count an `int` higher, *integer overflow* will result where an incorrect value will be stored in this variable.
+   The number of bits limits how high and low we can count.
+   Types with which you might interact during this course include:
    
    +   `bool`, a Boolean expression of either true or false
    +   `char`, a single character like a or 2
    +   `double`, a floating-point value with more digits than a float
    +   `float`, a floating-point value, or real number with a decimal value
    +   `int`, integers up to a certain size, or number of bits
    +   `long`, integers with more bits, so they can count higher than an int
    +   `string`, a string of characters
+   As you are coding, pay special attention to the types of variables you are using to avoid problems within your code.
+   We examined some examples of disasters that can occur through memory-related errors.

## Summing Up

In this lesson, you learned how to apply the building blocks you learned in Scratch to the C programming language. You learned…

+   How to create your first program in C.
+   Predefined functions that come natively with C and how to implement your own functions.
+   How to use variables, conditionals, and loops.
+   How to approach abstraction to simplify and improve your code.
+   How to approach problem-solving for a computer science problem.
+   How to use the Linux command line.
+   How to integrate comments into your code.
+   How to utilize types and operators.

See you next time!

+   


# Lecture 2-Arrays



+   [Welcome!](#welcome)
+   [Compiling](#compiling)
+   [Debugging](#debugging)
+   [Arrays](#arrays)
+   [Strings](#strings)
+   [String Length](#string-length)
+   [Command-Line Arguments](#command-line-arguments)
+   [Exit Status](#exit-status)
+   [Cryptography](#cryptography)
+   [Summing Up](#summing-up)

## Welcome!

+   In our previous session, we learned about C, a text-based programming language.
+   This week, we are going to take a deeper look at additional building-blocks that will support our goals of learning more about programming from the bottom up.
+   Fundamentally, in addition to the essentials of programming, this course is about problem-solving. Accordingly, we will also focus further on how to approach computer science problems.

## Compiling

+   *Encryption* is the act of hiding plain text from prying eyes. *decrypting*, then, is the act of taking an encrypted piece of text and returning it to a human-readable form.
+   An encrypted piece of text may look like the following:
    
    ![encryption](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide008-20240811152537859.png "encryption")
    
+   Recall that last week you learned about a *compiler*, a specialized computer program that converts *source code* into *machine code* that can be understood by a computer.
+   For example, you might have a computer program that looks like this:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        printf("hello, world\n");
    }
    ```
    
+   A compiler will take the above code and turn it into the following machine code:
    
    ![machine code](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide012.png "machine code")
    
+   *VS Code*, the programming environment provided to you as a CS50 student, utilizes a compiler called `clang` or *c language*.
+   If you were to type `make hello`, it runs a command that executes clang to create an output file that you can run as a user.
+   VS Code has been pre-programmed such that `make` will run numerous command line arguments along with clang for your convenience as a user.
+   Consider the following code:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string name = get_string("What's your name? ");
        printf("hello, %s\n", name);
    }
    ```
    
+   You can attempt to enter into the terminal window: `clang -o hello hello.c`. You will be met by an error that indicates that clang does not know where to find the `cs50.h` library.
+   Attempting again to compile this code, run the following command in the terminal window: `clang -o hello hello.c -lcs50`. This will enable the compiler to access the `cs50.h` library.
+   Running in the terminal window `./hello`, your program will run as intended.
+   While the above is offered as an illustration, such that you can understand more deeply the process and concept of compiling code, using `make` in CS50 is perfectly fine and the expectation!
+   Compiling involves major steps, including the following:
    +   First, *preprocessing* is where the header files in your code, designated by a `#` (such as `#include <cs50.h>`) are effectively copied and pasted into your file. During this step, the code from `cs50.h` is copied into your program. Similarly, just as your code contains `#include <stdio.h>`, code contained within `stdio.h` somewhere on your computer is copied to your program. This step can be visualized as follows:
        
        ```auto
        string get_string(string prompt);
        int printf(string format, ...);
        
        int main(void)
        {
            string name = get_string("What's your name? ");
            printf("hello, %s\n", name);
        }
        ```
        
    +   Second, *compiling* is where your program is converted into assembly code. This step can be visualized as follows:
        
        ![compiling](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide033-20240811152537979.png "compiling")
        
    +   Third, *assembling* involves the compiler converting your assembly code into machine code. This step can be visualized as follows:
        
        ![assembling](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide038.png "assembling")
        
    +   Finally, during the *linking* step, code from your included libraries are converted also into machine code and combined with your code. The final executable file is then outputted.
        
        ![linking](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide049.png "linking")
        

## Debugging

+   Everyone will make mistakes while coding.
+   Consider the following image from last week:
    
    ![mario](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide061.png "mario")
    
+   Further, consider the following code that has a bug purposely inserted within it:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i <= 3; i++)
        {
            printf("#\n");
        }
    }
    ```
    
+   Type `code buggy0.c` into the terminal window and write the above code.
+   Running this code, four bricks appear instead of the intended three.
+   `printf` is a very useful way of debugging your code. You could modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i <= 3; i++)
        {
            printf("i is %i\n", i);
            printf("#\n");
        }
    }
    ```
    
+   Running this code, you will see numerous statements, including `i is 0`, `i is 1`, `i is 2`, and `i is 3`. Seeing this, you might realize that Further code needs to be corrected as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            printf("#\n");
        }
    }
    ```
    
    Notice the `<=` has been replaced with `<`.
    
+   This code can be further improved as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    void print_column(int height);
    
    int main(void)
    {
        int h = get_int("Height: ");
        print_column(h);
    }
    
    void print_column(int height)
    {
        for (int i = 0; i <= height; i++)
        {
            printf("#\n");
        }
    }
    ```
    
    Notice that compiling and running this code still results in a bug.
    
+   To address this bug, we will use a new tool at our disposal.
+   A second tool in debugging is called a *debugger*, a software tool created by programmers to help track down bugs in code.
+   In VS Code, a preconfigured debugger has been provided to you.
+   To utilize this debugger, first set a *breakpoint* by clicking to the left of a line of your code, just to the left of the line number. When you click there, you will see a red dot appearing. Imagine this as a stop sign, asking the compiler to pause such that you can consider what’s happening in this part of your code.
    
    ![break point](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Debugging.png "break point")
    
+   Second, run `debug50 ./buggy0`. You will notice that after the debugger comes to life that a line of your code will illuminate in a gold-like color. Quite literally, the code has *paused* at this line of code. Notice in the top left corner how all local variables are being displayed, including `h`, which has a current does not have a value. At the top of your window, you can click the `step over` button and it will keep moving through your code. Notice how the value of `h` increases.
+   While this tool will not show you where your bug is, it will help you slow down and see how your code is running step by step. You can use `step into` as a way to look further into the details of your buggy code.
+   A final form of debugging is called *rubber duck debugging*. When you are having challenges with your code, consider how speaking out loud to, quite literally, a rubber duck about the code problem. If you’d rather not talk to a small plastic duck, you are welcome to speak to a human near you! They need not understand how to program: Speaking with them is an opportunity for you to speak about your code.

## Arrays

+   In Week 0, we talked about *data types* such as `bool`, `int`, `char`, `string`, etc.
+   Each data type requires a certain amount of system resources:
    +   `bool` 1 byte
    +   `int` 4 bytes
    +   `long` 8 bytes
    +   `float` 4 bytes
    +   `double` 8 bytes
    +   `char` 1 byte
    +   `string` ? bytes
+   Inside of your computer, you have a finite amount of memory available.
    
    ![memory](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide084.png "memory")
    
+   Physically, on the memory of your computer, you can imagine how specific types of data are stored on your computer. You might imagine that a `char`, which only requires 1 byte of memory, may look as follows:
    
    ![1 byte](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide087.png "1 byte")
    
+   Similarly, an `int`, which requires 4 bytes might look as follows:
    
    ![4 bytes](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide088.png "4 bytes")
    
+   We can create a program that explores these concepts. Inside your terminal, type `code scores.c` and write code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        // Scores
        int score1 = 72;
        int score2 = 73;
        int score3 = 33;
    
        // Print average
        printf("Average: %f\n", (score1 + score2 + score3) / 3.0);
    }
    ```
    
    Notice that the number on the right is a floating point value of `3.0`, such that the calculation is rendered as a floating point value in the end.
    
+   Running `make scores`, the program runs.
+   You can imagine how these variables are stored in memory:
    
    ![scores in memory](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide098-20240811152539099.png "scores in memory")
    
+   *Arrays* are a way of storing data back-to-back in memory such that this data is easily accessible.
+   `int scores[3]` is a way of telling the compiler to provide you three back-to-back places in memory of size `int` to store three `scores`. Considering our program, you can revise your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Get scores
        int scores[3];
        scores[0] = get_int("Score: ");
        scores[1] = get_int("Score: ");
        scores[2] = get_int("Score: ");
    
        // Print average
        printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
    }
    ```
    
    Notice that `score[0]` examines the value at this location of memory by `indexing into` the array called `scores` at location `0` to see what value is stored there.
    
+   You can see how while the above code works, there is still an opportunity for improving our code. Revise your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Get scores
        int scores[3];
        for (int i = 0; i < 3; i++)
        {
            scores[i] = get_int("Score: ");
        }
    
        // Print average
        printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
    }
    ```
    
    Notice how we index into `scores` by using `scores[i]` where `i` is supplied by the `for` loop.
    
+   We can simplify or *abstract away* the calculation of the average. Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    // Constant
    const int N = 3;
    
    // Prototype
    float average(int length, int array[]);
    
    int main(void)
    {
        // Get scores
        int scores[N];
        for (int i = 0; i < N; i++)
        {
            scores[i] = get_int("Score: ");
        }
    
        // Print average
        printf("Average: %f\n", average(N, scores));
    }
    
    float average(int length, int array[])
    {
        // Calculate average
        int sum = 0;
        for (int i = 0; i < length; i++)
        {
            sum += array[i];
        }
        return sum / (float) length;
    }
    ```
    
    Notice that a new function called `average` is declared. Further, notice that a `const` or constant value of `N` is declared. Most importantly, notice how the `average` function takes `int array[]`, which means that the compiler passes an array to this function.
    
+   Not only can arrays be containers: They can be passed between functions.

## Strings

+   A `string` is simply an array of variables of type `char`: an array of characters.
+   Considering the following image, you can see how a string is an array of characters that begins with the first character and ends with a special character called a `NUL character`:
    
    ![hi with terminator](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide116-20240811152539394.png "hi with terminator")
    
+   Imagining this in decimal, your array would look like the following:
    
    ![hi with decimal](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide117-20240811152539457.png "hi with decimal")
    
+   Implementing this in your own code, type `code hi.c` in the terminal window and write code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        char c1 = 'H';
        char c2 = 'I';
        char c3 = '!';
    
        printf("%c%c%c\n", c1, c2, c3);
    }
    ```
    
    Notice that this will output a string of characters.
    
+   Similarly, make the following modification to your code:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        char c1 = 'H';
        char c2 = 'I';
        char c3 = '!';
    
        printf("%i %i %i\n", c1, c2, c3);
    }
    ```
    
    Notice that that ASCII codes are printed by replacing `%c` with `%i`.
    
+   To further understand how a `string` works, revise your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string s = "HI!";
        printf("%c%c%c\n", s[0], s[1], s[2]);
    }
    ```
    
    Notice how the `printf` statement presents three values from our array called `s`.
    
+   As before, we can replace `%c` with `%i` as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string s = "HI!";
        printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]);
    }
    ```
    
    Notice that this prints the string’s ASCII codes, including NUL.
    
+   Let’s imagine we want to say both `HI!` and `BYE!`. Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string s = "HI!";
        string t = "BYE!";
    
        printf("%s\n", s);
        printf("%s\n", t);
    }
    ```
    
    Notice that two strings are declared and used in this example.
    
+   You can visualize this as follow:
    
    ![hi and bye](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide126-20240811152539241.png "hi and bye")
    
+   We can further improve this code. Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string words[2];
    
        words[0] = "HI!";
        words[1] = "BYE!";
    
        printf("%s\n", words[0]);
        printf("%s\n", words[1]);
    }
    ```
    
    Notice that both strings are stored within a single array of type `string`.
    

## String Length

+   A common problem within programming, and perhaps C more specifically, is to discover the length of an array. How could we implement this in code? Type `code length.c` in the terminal window and code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt for user's name
        string name = get_string("Name: ");
    
        // Count number of characters up until '\0' (aka NUL)
        int n = 0;
        while (name[n] != '\0')
        {
            n++;
        }
        printf("%i\n", n);
    }
    ```
    
    Notice that this code loops until the `NUL` character is found.
    
+   This code can ben improved by abstracting away the counting as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int string_length(string s);
    
    int main(void)
    {
        // Prompt for user's name
        string name = get_string("Name: ");
        int length = string_length(name);
        printf("%i\n", length);
    }
    
    int string_length(string s)
    {
        // Count number of characters up until '\0' (aka NUL)
        int n = 0;
        while (s[n] != '\0')
        {
            n++;
        }
        return n;
    }
    ```
    
+   Since this is such a common problem within programming, other programmers have created code in the `string.h` library to find the length of a string. You can find the length of a string by modifying your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        // Prompt for user's name
        string name = get_string("Name: ");
        int length = strlen(name);
        printf("%i\n", length);
    }
    ```
    
    Notice that this code uses the `string.h` library, declared at the top of the file. Further, it uses a function from that library called `strlen`, which calculates the length of the string passed to it.
    
+   `ctype.h` is another library that is quite useful. Imagine we wanted to create a program that converted all lowercase characters to uppercase ones. In the terminal window type `code uppercase.c` and write code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        string s = get_string("Before: ");
        printf("After:  ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            if (s[i] >= 'a' && s[i] <= 'z')
            {
                printf("%c", s[i] - 32);
            }
            else
            {
                printf("%c", s[i]);
            }
        }
        printf("\n");
    }
    ```
    
    Notice that this code *iterates* through each value in the string. The program looks at each character. If the character is lowercase, it subtracts the value 32 from it to convert it to uppercase.
    
+   Recalling our previous work from last week, you might remember this ASCII values chart:
    
    ![ascii](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide120.png "ascii")
    
+   When a lowercase character has `32` subtracted from it, it results in an uppercase version of that same character.
+   While the program does what we want, there is an easier way using the `ctype.h` library. Modify your program as follows:
    
    ```auto
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        string s = get_string("Before: ");
        printf("After:  ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            if (islower(s[i]))
            {
                printf("%c", toupper(s[i]));
            }
            else
            {
                printf("%c", s[i]);
            }
        }
        printf("\n");
    }
    ```
    
    Notice that the program iterates through each character of the string. The `toupper` function is passed `s[i]`. Each character (if lowercase) is converted to uppercase.
    
+   It’s worth mentioning that `toupper` automatically knows to uppercase only lowercase characters. Hence, your code can be simplified as follows:
    
    ```auto
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        string s = get_string("Before: ");
        printf("After:  ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            printf("%c", toupper(s[i]));
        }
        printf("\n");
    }
    ```
    
    Notice that this code uppercases a string using the `ctype` library.
    
+   You can read about all the capabilities of the `ctype` library on the [Manual Pages](https://manual.cs50.io/#ctype.h).

## Command-Line Arguments

+   `Command-line arguments` are those arguments that are passed to your program at the command line. For example, all those statements you typed after `clang` are considered command line arguments. You can use these arguments in your own programs!
+   In your terminal window, type `code greet.c` and write code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string answer = get_string("What's your name? ");
        printf("hello, %s\n", answer);
    }
    ```
    
    Notice that this says `hello` to the user.
    
+   Still, would it not be nice to be able to take arguments before the program even runs? Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(int argc, string argv[])
    {
        if (argc == 2)
        {
            printf("hello, %s\n", argv[1]);
        }
        else
        {
            printf("hello, world\n");
        }
    }
    ```
    
    Notice that this program knows both `argc`, the number of command line arguments, and `argv` which is an array of the characters passed as arguments at the command line.
    
+   Therefore, using the syntax of this program, executing `./greet David` would result in the program saying `hello, David`.

## Exit Status

+   When a program ends, a special exit code is provided to the computer.
+   When a program exits without error, a status code of `0` is provided the computer. Often, when an error occurs that results in the program ending, a status of `1` is provided by the computer.
+   You could write a program as follows that illustrates this by typing `code status.c` and writing code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(int argc, string argv[])
    {
        if (argc != 2)
        {
            printf("Missing command-line argument\n");
            return 1;
        }
        printf("hello, %s\n", argv[1]);
        return 0;
    }
    ```
    
    Notice that if you fail to provide `./status David`, you will get an exit status of `1`. However, if you do provide `./status David`, you will get an exit status of `0`.
    
+   You can imagine how you might use portions of the above program to check if a user provided the correct number of command-line arguments.

## Cryptography

+   Cryptography is the art of ciphering and deciphering a message.
+   `plaintext` and a `key` are provided to a `cipher`, resulting in ciphered text.
    
    ![cryptography](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week2Slide153.png "cryptography")
    
+   The key is a special argument passed to the cipher along with the plaintext. The cipher uses the key to make decisions about how to implement its cipher algorithm.

## Summing Up

In this lesson, you learned more details about compiling and how data is stored within a computer. Specifically, you learned…

+   Generally, how a compiler works.
+   How to debug your code using four methods.
+   How to utilize arrays within your code.
+   How arrays store data in back to back portions of memory.
+   How strings are simply arrays of characters.
+   How to interact with arrays in your code.
+   How command-line arguments can be passed to your programs.
+   The basic building-blocks of cryptography.

See you next time!


# Lecture 3-Algorithms



+   [Welcome!](#welcome)
+   [Linear Search](#linear-search)
+   [Binary Search](#binary-search)
+   [Running Time](#running-time)
+   [search.c](#searchc)
+   [Data Structures](#data-structures)
+   [Sorting](#sorting)
+   [Bubble Sort](#bubble-sort)
+   [Recursion](#recursion)
+   [Merge Sort](#merge-sort)
+   [Summing Up](#summing-up)

## Welcome!

+   In week zero, we introduced the idea of an *algorithm*: a black box that may take an input and creates an output.
+   This week, we are going to expand upon our understanding of algorithms through pseudocode and into code itself.
+   Also, we are going to consider the efficiency of these algorithms. Indeed, we are going to be building upon our understanding of how to use some of the *lower-level* concepts we discussed last week in building algorithms.
+   Recall back to earlier in the course when we introduced the following graph:
    
    ![chart with: "size of problem" as x-axis; "time to solve" as y-axis; red, steep straight line from origin to top of graph close to yellow, less steep straight line from origin to top of graph both labeled "n"; green, curved line that gets less and less steep from origin to right of graph labeled "log n)](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week3Slide010.png "complexity")
    
+   As we step into this week, you should consider how the way an algorithm works with a problem may determine the time it takes to solve a problem! Algorithms can be designed to be more and more efficient, to a limit.
+   Today, we will focus upon the design of algorithms and how to measure their efficiency.

## Linear Search

+   Recall that last week you were introduced to the idea of an *array*, blocks of memory that are consecutive: side-by-side with one another.
+   You can metaphorically imagine an array like a series of seven red lockers as follows:
    
    ![Seven red lockers side by side](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week3Slide018-20240811153957551.png "lockers")
    
+   We can imagine that we have an essential problem of wanting to know, “Is the number 50 inside an array?” A computer must look at each locker to be able to see if the number 50 is inside. We call this process of finding such a number, character, string, or other item *searching*.
+   We can potentially hand our array to an algorithm, wherein our algorithm will search through our lockers to see if the number 50 is behind one of the doors: Returning the value true or false.
    
    ![seven red lockers pointing to an empty box. Out of the empty box comes and output of bool](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week3Slide022-20240811153957279.png "lockers as algorithm")
    
+   We can imagine various instructions we might provide our algorithm to undertake this task as follows:
    
    ```auto
    For each door from left to right
        If 50 is behind door
            Return true
    Return false
    ```
    
    Notice that the above instructions are called *pseudocode*: A human-readable version of the instructions that we could provide the computer.
    
+   A computer scientist could translate that pseudocode as follows:
    
    ```auto
    For i from 0 to n-1
        If 50 is behind doors[i]
            Return true
    Return false
    ```
    
    Notice that the above is still not code, but it is a pretty close approximation of what the final code might look like.
    

## Binary Search

+   *Binary search* is another *search algorithm* that could be employed in our task of finding the 50.
+   Assuming that the values within the lockers have been arranged from smallest to largest, the pseudocode for binary search would appear as follows:
    
    ```auto
    If no doors left
        Return false
    If 50 is behind middle door
        Return true
    Else if 50 < middle door
        Search left half
    Else if 50 > middle door
        Search right half
    ```
    
+   Using the nomenclature of code, we can further modify our algorithm as follows:
    
    ```auto
    If no doors left
        Return false
    If 50 is behind doors[middle]
        Return true
    Else if 50 < doors[middle]
        Search doors[0] through doors[middle - 1]
    Else if 50 > doors[middle]
        Search doors[middle + 1] through doors[n - 1]
    ```
    
    Notice, looking at this approximation of code, you can nearly imagine what this might look like in actual code.
    

## Running Time

+   *running time* involves an analysis using *big O* notation. Take a look at the following graph:
    
    ![chart with: "size of problem" as x-axis; "time to solve" as y-axis; red, steep straight line from origin to top of graph close to yellow, less steep straight line from origin to top of graph both labeled "O(n)"; green, curved line that gets less and less steep from origin to right of graph labeled "O(log n)](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week3Slide042.png "big o graphed")
    
+   Rather than being ultra-specific about the mathematical efficiency of an algorithm, computer scientists discuss efficiency in terms of *the order of* various running times.
+   In the above graph, the first algorithm is \\(O(n)\\) or *in the order of n*. The second is in \\(O(n)\\) as well. The third is in \\(O(\\log n)\\).
+   It’s the shape of the curve that shows the efficiency of an algorithm. Some common running times we may see are:
    
    +   \\(O(n^2)\\)
    +   \\(O(n \\log n)\\)
    +   \\(O(n)\\)
    +   \\(O(\\log n)\\)
    +   \\(O(1)\\)
+   Of the running times above, \\(O(n^2)\\) is considered the worst running time, \\(O(1)\\) is the fastest.
+   Linear search was of order \\(O(n)\\) because it could take *n* steps in the worst case to run.
+   Binary search was of order \\(O(\\log n)\\) because it would take fewer and fewer steps to run even in the worst case.
+   Programmers are interested in both the worst case, or *upper bound*, and the best case, or *lower bound*.
+   The \\(\\Omega\\) symbol is used to denote the best case of an algorithm, such as \\(\\Omega(\\log n)\\).
+   The \\(\\Theta\\) symbol is used to denote where the upper bound and lower bound are the same, where the best case and the worst case running times are the same.
+   As you continue to develop your knowledge in computer science, you will explore these topics in more detail in future courses.

## search.c

+   You can implement linear search ourselves by typing `code search.c` in your terminal window and by writing code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // An array of integers
        int numbers[] = {20, 500, 10, 5, 100, 1, 50};
    
        // Search for number
        int n = get_int("Number: ");
        for (int i = 0; i < 7; i++)
        {
            if (numbers[i] == n)
            {
                printf("Found\n");
                return 0;
            }
        }
        printf("Not found\n");
        return 1;
    }
    ```
    
    Notice that the line beginning with `int numbers[]` allows us to define the values of each element of the array as we create it. Then, in the `for` loop, we have an implementation of linear search. `return 0` is used to indicate success and exit the program. `return 1` is used to exist the program with an error (failure).
    
+   We have now implemented linear search ourselves in C!
+   What if we wanted to search for a string within an array? Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        // An array of strings
        string strings[] = {"battleship", "boot", "cannon", "iron", "thimble", "top hat"};
    
        // Search for string
        string s = get_string("String: ");
        for (int i = 0; i < 6; i++)
        {
            if (strcmp(strings[i], s) == 0)
            {
                printf("Found\n");
                return 0;
            }
        }
        printf("Not found\n");
        return 1;
    }
    ```
    
    Notice that we cannot utilize `==` as in our previous iteration of this program. Instead, we use `strcmp`, which comes from the `string.h` library. `strcmp` will return `0` if the strings are the same.
    
+   Indeed, running this code allows us to iterate over this array of strings to see if a certain string was within it. However, if you see a *segmentation fault*, where a part of memory was touched by your program that it should not have access to, do make sure you have `i < 6` noted above instead of `i < 7`.
    
+   We can combine these ideas of both numbers and strings into a single program. Type `code phonebook.c` into your terminal window and write code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        // Arrays of strings
        string names[] = {"Carter", "David", "John"};
        string numbers[] = {"+1-617-495-1000", "+1-617-495-1000", "+1-949-468-2750"};
    
        // Search for name
        string name = get_string("Name: ");
        for (int i = 0; i < 3; i++)
        {
            if (strcmp(names[i], name) == 0)
            {
                printf("Found %s\n", numbers[i]);
                return 0;
            }
        }
        printf("Not found\n");
        return 1;
    }
    ```
    
    Notice that Carter’s number begins with `+1-617`, David’s phone number starts with `+1-617`, and John’s number starts with `+1-949`. Therefore, `names[0]` is Carter and `numbers[0]` is Carter’s number. This code will allow us to search the phonebook to for a person’s specific number.
    
+   While this code works, there are numerous inefficiencies. Indeed, there is a chance that people’s names and numbers may not correspond. Wouldn’t be nice if we could create our own data type where we could associate a person with the phone number?

## Data Structures

+   It turns out that C allows a way by which we can create our own data types via a `struct`.
+   Would it not be useful to create our own data type called a `person`, that has inside of it a `name` and `number`.
+   Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    typedef struct
    {
        string name;
        string number;
    }
    person;
    
    int main(void)
    {
        person people[3];
    
        people[0].name = "Carter";
        people[0].number = "+1-617-495-1000";
    
        people[1].name = "David";
        people[1].number = "+1-617-495-1000";
    
        people[2].name = "John";
        people[2].number = "+1-949-468-2750";
    
        // Search for name
        string name = get_string("Name: ");
        for (int i = 0; i < 3; i++)
        {
            if (strcmp(people[i].name, name) == 0)
            {
                printf("Found %s\n", people[i].number);
                return 0;
            }
        }
        printf("Not found\n");
        return 1;
    }
    ```
    
    Notice that the code begins with `typedef struct` where a new datatype called `person` is defined. Inside a `person` is a string called `name` and a `string` called number. In the `main` function, begin by creating an array called `people` that is of type `person` that is a size of 3. Then, we update the names and phone numbers of the two people in our `people` array. Most important, notice how the *dot notation* such as `people[0].name` allows us to access the `person` at the 0th location and assign that individual a name.
    

## Sorting

+   *Sorting* is the act of taking an unsorted list of values and transforming this list into a sorted one.
+   When a list is sorted, searching that list is far less taxing on the computer. Recall that we can use binary search on a sorted list, but not on an unsorted one.
+   It turns out that there are many different types of sorting algorithms.
+   *Selection sort* is one such search algorithm.
+   We can represent an array as follows:
    
    ![Seven red lockers side by side with the last labeled as n-1](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week3Slide104-20240811153957751.png "red lockers")
    
+   The algorithm for selection sort in pseudocode is:
    
    ```auto
    For i from 0 to n–1
        Find smallest number between numbers[i] and numbers[n-1]
        Swap smallest number with numbers[i]
    ```
    
+   Summarizing those steps, the first time iterating through the list took `n - 1` steps. The second time, it took `n - 2` steps. Carrying this logic forward, the steps required could be represented as follows:
    
    ```auto
    (n - 1) + (n - 2) + (n - 3) + ... + 1
    ```
    
+   This could be simplified to n(n-1)/2 or, more simply, \\(O(n^2)\\).

## Bubble Sort

+   *Bubble sort* is another sorting algorithm that works by repeatedly swapping elements to “bubble” larger elements to the end.
+   The pseudocode for bubble sort is:
    
    ```auto
    Repeat n-1 times
        For i from 0 to n–2
            If numbers[i] and numbers[i+1] out of order
                Swap them
        If no swaps
            Quit
    ```
    
+   As we further sort the array, we know more and more of it becomes sorted, so we only need to look at the pairs of numbers that haven’t been sorted yet.
+   Analyzing selection sort, we made only seven comparisons. Representing this mathematically, where *n* represents the number of cases, it could be said that selection sort can be analyzed as:
    
    ```auto
      (n - 1) + (n - 2) + (n - 3) + ... + 1
    ```
    
    or, more simply \\(n^2/2 - n/2\\).
    
+   Considering that mathematical analysis, n2 is really the most influential factor in determining the efficiency of this algorithm. Therefore, selection sort is considered to be of the order of \\(O(n^2)\\) in the worst case where all values are unsorted. Even when all values are sorted, it will take the same number of steps. Therefore, the best case can be noted as \\(\\Omega(n^2)\\). Since both the upper bound and lower bound cases are the same, the efficiency of this algorithm as a whole can be regarded as \\(\\Theta(n^2)\\).
+   Analyzing bubble sort, the worst case is \\(O(n^2)\\). The best case is \\(\\Omega(n)\\).
+   You can [visualize](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html) a comparison of these algorithms.

## Recursion

+   How could we improve our efficiency in our sorting?
+   *Recursion* is a concept within programming where a function calls itself. We saw this earlier when we saw…
    
    ```auto
    If no doors left
        Return false
    If number behind middle door
        Return true
    Else if number < middle door
        Search left half
    Else if number > middle door
        Search right half
    ```
    
    Notice that we are calling `search` on smaller and smaller iterations of this problem.
    
+   Similarly, in our pseudocode for Week 0, you can see where recursion was implemented:
    
    ```auto
    1  Pick up phone book
    2  Open to middle of phone book
    3  Look at page
    4  If person is on page
    5      Call person
    6  Else if person is earlier in book
    7      Open to middle of left half of book
    8      Go back to line 3
    9  Else if person is later in book
    10     Open to middle of right half of book
    11     Go back to line 3
    12 Else
    13     Quit
    ```
    
+   This code could have been simplified, to highlight its recursive properties as follows:
    
    ```auto
    1  Pick up phone book
    2  Open to middle of phone book
    3  Look at page
    4  If person is on page
    5      Call person
    6  Else if person is earlier in book
    7      Search left half of book
    9  Else if person is later in book
    10     Search right half of book
    12 Else
    13     Quit
    ```
    
+   Consider how in Week 1 we wanted to create a pyramid structure as follows:
    
+   To implement this using recursion, type `code recursion.c` into your terminal window and write code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    void draw(int n);
    
    int main(void)
    {
        draw(1);
    }
    
    void draw(int n)
    {
        for (int i = 0; i < n; i++)
        {
            printf("#");
        }
        printf("\n");
    
        draw(n + 1);
    }
    ```
    
    Notice that the draw function calls itself. Further, note that your code may get caught in an infinite loop. To break from this loop, if you get stuck, hit `ctrl-c` on your keyboard. The reason this creates an infinite loop is that there is nothing telling the program to end. There is no case where the program is done.
    
+   We can correct our code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    void draw(int n);
    
    int main(void)
    {
        // Get height of pyramid
        int height = get_int("Height: ");
    
        // Draw pyramid
        draw(height);
    }
    
    void draw(int n)
    {
        // If nothing to draw
        if (n <= 0)
        {
            return;
        }
    
        // Draw pyramid of height n - 1
        draw(n - 1);
    
        // Draw one more row of width n
        for (int i = 0; i < n; i++)
        {
            printf("#");
        }
        printf("\n");
    }
    ```
    
    Notice the *base case* will ensure the code does not run forever. The line `if (n <= 0)` terminates the recursion because the problem has been solved. Every time `draw` calls itself, it calls itself by `n-1`. At some point, `n-1` will equal `0`, resulting in the `draw` function returning and the program will end.
    

## Merge Sort

+   We can now leverage recursion in our quest for a more efficient sort algorithm and implement what is called *merge sort*, a very efficient sort algorithm.
+   The pseudocode for merge sort is quite short:
    
    ```auto
    If only one number
        Quit
    Else
        Sort left half of number
        Sort right half of number
        Merge sorted halves
    ```
    
+   Consider the following list of numbers:
    
+   First, merge sort asks, “is this one number?” The answer is “no,” so the algorithm continues.
    
+   Second, merge sort will now split the numbers down the middle (or as close as it can get) and sort the left half of numbers.
    
+   Third, merge sort would look at these numbers on the left and ask, “is this one number?” Since the answer is no, it would then split the numbers on the left down the middle.
    
+   Fourth, merge sort will again ask , “is this one number?” The answer is yes this time! Therefore, it will quit this task and return to the last task it was running at this point:
    
+   Fifth, merge sort will sort the numbers on the left.
    
+   Now, we return to where we left off in the pseudocode now that the left side has been sorted. A similar process of steps 3-5 will occur with the right-hand numbers. This will result in:
    
+   Both halves are now sorted. Finally, the algorithm will merge both sides. It will look at the first number on the left and the first number on the right. It will put the smaller number first, then the second smallest. The algorithm will repeat this for all numbers, resulting in:
    
+   Merge sort is complete, and the program quits.
+   Merge sort is a very efficient sort algorithm with a worst case of \\(O(n \\log n)\\). The best case is still \\(\\Omega(n \\log n)\\) because the algorithm still must visit each place in the list. Therefore, merge sort is also \\(\\Theta(n \\log n)\\) since the best case and worst case are the same.
+   A final [visualization](https://www.youtube.com/watch?v=ZZuD6iUe3Pc) was shared.

## Summing Up

In this lesson, you learned about algorithmic thinking and building your own data types. Specifically, you learned…

+   Algorithms.
+   Big *O* notation.
+   Binary search and linear search.
+   Various sort algorithms, including bubble sort, selection sort, and merge sort.
+   Recursion.

See you next time!


# Lecture 4-Memory



+   [Welcome!](#welcome)
+   [Pixel Art](#pixel-art)
+   [Hexadecimal](#hexadecimal)
+   [Memory](#memory)
+   [Pointers](#pointers)
+   [Strings](#strings)
+   [Pointer Arithmetic](#pointer-arithmetic)
+   [String Comparison](#string-comparison)
+   [Copying](#copying)
+   [malloc and Valgrind](#malloc-and-valgrind)
+   [Garbage Values](#garbage-values)
+   [Pointer Fun with Binky](#pointer-fun-with-binky)
+   [Swap](#swap)
+   [Overflow](#overflow)
+   [`scanf`](#scanf)
+   [File I/O](#file-io)
+   [Summing Up](#summing-up)

## Welcome!

+   In previous weeks, we talked about images being made of smaller building blocks called pixels.
+   Today, we will go into further detail about the zeros and ones that make up these images. In particular, we will be going deeper into the fundamental building blocks that make up files, including images.
+   Further, we will discuss how to access the underlying data stored in computer memory.

## Pixel Art

+   Pixels are squares, individual dots, of color that are arranged on an up-down, left-right grid.
+   You can imagine as an image as a map of bits, where zeros represent black and ones represent white.
    
    ![Zeros and ones being converted to a black and white smiley](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide015.png "smiley")
    
+   *RGB*, or *red, green, blue*, are numbers that represent the amount of each of these colors. In Adobe Photoshop, you can see these settings as follows:
    
    ![A photoshop panel with RGB values and hexidecimal input](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide016.png "hex in photoshop")
    
    Notice how the amount of red, blue, and green changes the color selected.
    
+   You can see by the image above that color is not just represented in three values. At the bottom of the window, there is a special value made up of numbers and characters. `255` is represented as `FF`. Why might this be?

## Hexadecimal

+   *Hexadecimal* is a system of counting that has 16 counting values. They are as follows:
    
    ```auto
      0 1 2 3 4 5 6 7 8 9 a b c d e f
    ```
    
    Notice that `F` represents `15`.
    
+   Hexadecimal is also known as *base-16*.
+   When counting in hexadecimal, each column is a power of 16.
+   The number `0` is represented as `00`.
+   The number `1` is represented as `01`.
+   The number `9` is represented by `09`.
+   The number `10` is represented as `0A`.
+   The number `15` is represented as `0F`.
+   The number `16` is represented as `10`.
+   The number `255` is represented as `FF`, because 16 x 15 (or `F`) is 240. Add 15 more to make 255. This is the highest number you can count using a two-digit hexadecimal system.
+   Hexadecimal is useful because it can be represented using fewer digits. Hexadecimal allows us to represent information more succinctly.

## Memory

+   In weeks past, you may recall our artist rendering of concurrent blocks of memory. Applying hexadecimal numbering to each of these blocks of memory, you can visualize these as follows:
    
    ![Blocks of memory numbered in hex](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide065-20240811154040385.png "memory hex")
    
+   You can imagine how there may be confusion regarding whether the `10` block above may represent a location in memory or the value `10`. Accordingly, by convention, all hexadecimal numbers are often represented with the `0x` prefix as follows:
    
    ![blocks of memory numbered in hex with 0x](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide066.png "0x")
    
+   In your terminal window, type `code addresses.c` and write your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int n = 50;
        printf("%i\n", n);
    }
    ```
    
    Notice how `n` is stored in memory with the value `50`.
    
+   You can visualize how this program stores this value as follows:
    
    ![the value 50 stored in a memory location with hex](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide070-20240811154041145.png "hex")
    
+   The `C` language has two powerful operators that relate to memory:
    
    ```auto
      & Provides the address of something stored in memory.
      * Instructs the compiler to go to a location in memory.
    ```
    
+   We can leverage this knowledge by modifying our code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int n = 50;
        printf("%p\n", &n);
    }
    ```
    
    Notice the `%p`, which allows us to view the address of a location in memory. `&n` can be literally translated as “the address of `n`.” Executing this code will return an address of memory beginning with `0x`.
    

## Pointers

+   A *pointer* is a variable that contains the address of some value. Most succinctly, a pointer is an address in your computer’s memory.
+   Consider the following code:
    
    Notice that `p` is a pointer that contains the address of an integer `n`.
    
+   Modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int n = 50;
        int *p = &n;
        printf("%p\n", p);
    }
    ```
    
    Notice that this code has the same effect as our previous code. We have simply leveraged our new knowledge of the `&` and `*` operators.
    
+   To illustrate the use of the `*` operator, consider the following:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int n = 50;
        int *p = &n;
        printf("%i\n", *p);
    }
    ```
    
    Notice that the `printf` line prints the integer at the location of `p`. `int *p` creates a pointer whose job is to store the memory address of an integer.
    
+   You can visualize our code as follows:
    
    ![Same value of 50 in a memory location with a pointer value stored elsewhere](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide078.png "pointer")
    
    Notice the pointer seems rather large. Indeed, a pointer is usually stored as an 8-byte value. `p` is storing the address of the `50`.
    
+   You can more accurately visualize a pointer as one address that points to another:
    
    ![A pointer as an arrow, pointing from one location of memory to another](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide079-20240811154040656.png "pointer")
    

## Strings

+   Now that we have a mental model for pointers, we can peel back a level of simplification that was offered earlier in this course.
+   Recall that a string is simply an array of characters. For example, `string s = "HI!"` can be represented as follows:
    
    ![The string HI with an exclaimation point stored in memory](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide085-20240811154041039.png "hi")
    
+   However, what is `s` really? Where is the `s` stored in memory? As you can imagine, `s` needs to be stored somewhere. You can visualize the relationship of `s` to the string as follows:
    
    ![Same string HI with a pointer pointing to it](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide086-20240811154040698.png "hi pointer")
    
    Notice how a pointer called `s` tells the compiler where the first byte of the string exists in memory.
    
+   Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string s = "HI!";
        printf("%p\n", s);
        printf("%p\n", &s[0]);
        printf("%p\n", &s[1]);
        printf("%p\n", &s[2]);
        printf("%p\n", &s[3]);
    }
    ```
    
    Notice the above prints the memory locations of each character in the string `s`. The `&` symbol is used to show the address of each element of the string. When running this code, notice that elements `0`, `1`, `2`, and `3` are next to one another in memory.
    
+   Likewise, you can modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        char *s = "HI!";
        printf("%s\n", s);
    }
    ```
    
    Notice that this code will present the string that starts at the location of `s`. This code effectively removes the training wheels of the `string` data type offered by `cs50.h`. This is raw C code, without the scaffolding of the cs50 library.
    
+   You can imagine how a string, as a data type, is created.
+   Last week, we learned how to create your own data type as a struct.
+   The cs50 library includes a struct as follows: `typedef char *string`
+   This struct, when using the cs50 library, allows one to use a custom data type called `string`.

## Pointer Arithmetic

+   You can modify your code to accomplish the same thing in a longer form as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        char *s = "HI!";
        printf("%c\n", s[0]);
        printf("%c\n", s[1]);
        printf("%c\n", s[2]);
    }
    ```
    
    Notice that we are printing each character at the location of `s`.
    
+   Further, you can modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        char *s = "HI!";
        printf("%c\n", *s);
        printf("%c\n", *(s + 1));
        printf("%c\n", *(s + 2));
    }
    ```
    
    Notice that the first character at the location of `s` is printed. Then, the character at the location `s + 1` is printed, and so on.
    

## String Comparison

+   A string of characters is simply an array of characters identified by its first byte.
+   Earlier in the course, we considered the comparison of integers. We could represent this in code by typing `code compare.c` into the terminal window and writing code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Get two integers
        int i = get_int("i: ");
        int j = get_int("j: ");
    
        // Compare integers
        if (i == j)
        {
            printf("Same\n");
        }
        else
        {
            printf("Different\n");
        }
    }
    ```
    
    Notice that this code takes two integers from the user and compares them.
    
+   In the case of strings, however, one cannot compare two strings using the `==` operator.
+   Utilizing the `==` operator in an attempt to compare strings will attempt to compare the memory locations of the strings instead of the characters therein. Accordingly, we recommended the use of `strcmp`.
+   To illustrate this, modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Get two strings
        char *s = get_string("s: ");
        char *t = get_string("t: ");
    
        // Compare strings' addresses
        if (s == t)
        {
            printf("Same\n");
        }
        else
        {
            printf("Different\n");
        }
    }
    ```
    
    Noticing that typing in `HI!` for both strings still results in the output of `Different`.
    
+   Why are these strings seemingly different? You can use the following to visualize why:
    
    ![two strings stored separately in memory](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide115-20240811154041212.png "two strings")
    
+   Therefore, the code for `compare.c` above is actually attempting to see if the memory addresses are different: not the strings themselves.
+   Using `strcmp`, we can correct our code:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        // Get two strings
        char *s = get_string("s: ");
        char *t = get_string("t: ");
    
        // Compare strings
        if (strcmp(s, t) == 0)
        {
            printf("Same\n");
        }
        else
        {
            printf("Different\n");
        }
    }
    ```
    
    Notice that `strcmp` can return `0` if the strings are the same.
    
+   To further illustrate how these two strings are living in two locations, modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Get two strings
        char *s = get_string("s: ");
        char *t = get_string("t: ");
    
        // Print strings
        printf("%s\n", s);
        printf("%s\n", t);
    }
    ```
    
    Notice how we now have two separate strings stored likely at two separate locations.
    
+   You can see the locations of these two stored strings with a small modification:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Get two strings
        char *s = get_string("s: ");
        char *t = get_string("t: ");
    
        // Print strings' addresses
        printf("%p\n", s);
        printf("%p\n", t);
    }
    ```
    
    Notice that the `%s` has been changed to `%p` in the print statement.
    

## Copying

+   A common need in programming is to copy one string to another.
+   In your terminal window, type `code copy.c` and write code as follows:
    
    ```auto
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        // Get a string
        string s = get_string("s: ");
    
        // Copy string's address
        string t = s;
    
        // Capitalize first letter in string
        t[0] = toupper(t[0]);
    
        // Print string twice
        printf("s: %s\n", s);
        printf("t: %s\n", t);
    }
    ```
    
    Notice that `string t = s` copies the address of `s` to `t`. This does not accomplish what we are desiring. The string is not copied – only the address is.
    
+   You can visualize the above code as follows:
    
    ![two pointers pointing at the same memory location with a string](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide124-20240811154041360.png "two strings")
    
    Notice that `s` and `t` are still pointing at the same blocks of memory. This is not an authentic copy of a string. Instead, these are two pointers pointing at the same string.
    
+   Before we address this challenge, it’s important to ensure that we don’t experience a *segmentation fault* through our code, where we attempt to copy `string s` to `string t`, where `string t` does not exist. We can employ the `strlen` function as follows to assist with that:
    
    ```auto
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        // Get a string
        string s = get_string("s: ");
    
        // Copy string's address
        string t = s;
    
        // Capitalize first letter in string
        if (strlen(t) > 0)
        {
            t[0] = toupper(t[0]);
        }
    
        // Print string twice
        printf("s: %s\n", s);
        printf("t: %s\n", t);
    }
    ```
    
    Notice that `strlen` is used to make sure `string t` exists. If it does not, nothing will be copied.
    
+   To be able to make an authentic copy of the string, we will need to introduce two new building blocks. First, `malloc` allows you, the programmer, to allocate a block of a specific size of memory. Second, `free` allows you to tell the compiler to *free up* that block of memory you previously allocated.
    
+   We can modify our code to create an authentic copy of our string as follows:
    
    ```auto
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    int main(void)
    {
        // Get a string
        char *s = get_string("s: ");
    
        // Allocate memory for another string
        char *t = malloc(strlen(s) + 1);
    
        // Copy string into memory, including '\0'
        for (int i = 0; i <= strlen(s); i++)
        {
            t[i] = s[i];
        }
    
        // Capitalize copy
        t[0] = toupper(t[0]);
    
        // Print strings
        printf("s: %s\n", s);
        printf("t: %s\n", t);
    }
    ```
    
    Notice that `malloc(strlen(s) + 1)` creates a block of memory that is the length of the string `s` plus one. This allows for the inclusion of the *null* `\0` character in our final, copied string. Then, the `for` loop walks through the string `s` and assigns each value to that same location on the string `t`.
    
+   It turns out that there is an inefficiency in our code. Modify your code as follows:
    
    ```auto
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    int main(void)
    {
        // Get a string
        char *s = get_string("s: ");
    
        // Allocate memory for another string
        char *t = malloc(strlen(s) + 1);
    
        // Copy string into memory, including '\0'
        for (int i = 0, n = strlen(s); i <= n; i++)
        {
            t[i] = s[i];
        }
    
        // Capitalize copy
        t[0] = toupper(t[0]);
    
        // Print strings
        printf("s: %s\n", s);
        printf("t: %s\n", t);
    }
    ```
    
    Notice that `n = strlen(s)` is defined now in the left-hand side of the `for loop`. It’s best not to call unneeded functions in the middle condition of the `for` loop, as it will run over and over again. When moving `n = strlen(s)` to the left-hand side, the function `strlen` only runs once.
    
+   The `C` Language has a built-in function to copy strings called `strcpy`. It can be implemented as follows:
    
    ```auto
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    int main(void)
    {
        // Get a string
        char *s = get_string("s: ");
    
        // Allocate memory for another string
        char *t = malloc(strlen(s) + 1);
    
        // Copy string into memory
        strcpy(t, s);
    
        // Capitalize copy
        t[0] = toupper(t[0]);
    
        // Print strings
        printf("s: %s\n", s);
        printf("t: %s\n", t);
    }
    ```
    
    Notice that `strcpy` does the same work that our `for` loop previously did.
    
+   Both `get_string` and `malloc` return `NULL`, a special value in memory, in the event that something goes wrong. You can write code that can check for this `NULL` condition as follows:
    
    ```auto
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    int main(void)
    {
        // Get a string
        char *s = get_string("s: ");
        if (s == NULL)
        {
            return 1;
        }
    
        // Allocate memory for another string
        char *t = malloc(strlen(s) + 1);
        if (t == NULL)
        {
            return 1;
        }
    
        // Copy string into memory
        strcpy(t, s);
    
        // Capitalize copy
        if (strlen(t) > 0)
        {
            t[0] = toupper(t[0]);
        }
    
        // Print strings
        printf("s: %s\n", s);
        printf("t: %s\n", t);
    
        // Free memory
        free(t);
        return 0;
    }
    ```
    
    Notice that if the string obtained is of length `0` or malloc fails, `NULL` is returned. Further, notice that `free` lets the computer know you are done with this block of memory you created via `malloc`.
    

## malloc and Valgrind

+   *Valgrind* is a tool that can check to see if there are memory-related issues with your programs wherein you utilized `malloc`. Specifically, it checks to see if you `free` all the memory you allocated.
+   Consider the following code for `memory.c`:
    
    ```auto
    #include <stdio.h>
    #include <stdlib.h>
    
    int main(void)
    {
        int *x = malloc(3 * sizeof(int));
        x[1] = 72;
        x[2] = 73;
        x[3] = 33;
    }
    ```
    
    Notice that running this program does not cause any errors. While `malloc` is used to allocate enough memory for an array, the code fails to `free` that allocated memory.
    
+   If you type `make memory` followed by `valgrind ./memory`, you will get a report from valgrind that will report where memory has been lost as a result of your program. One error that valgrind reveals is that we attempted to assign the value of `33` at the 4th position of the array, where we only allocated an array of size `3`. Another error is that we never freed `x`.
+   You can modify your code as follows:
    
    ```auto
    #include <stdio.h>
    #include <stdlib.h>
    
    int main(void)
    {
        int *x = malloc(3 * sizeof(int));
        x[0] = 72;
        x[1] = 73;
        x[2] = 33;
        free(x);
    }
    ```
    
    Notice that running valgrind again now results in no memory leaks.
    

## Garbage Values

+   When you ask the compiler for a block of memory, there is no guarantee that this memory will be empty.
+   It’s very possible that this memory that you allocated was previously utilized by the computer. Accordingly, you may see *junk* or *garbage values*. This is a result of you getting a block of memory but not initializing it. For example, consider the following code for `garbage.c`:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int scores[1024];
        for (int i = 0; i < 1024; i++)
        {
            printf("%i\n", scores[i]);
        }
    }
    ```
    
    Notice that running this code will allocate `1024` locations in memory for your array, but the `for` loop will likely show that not all values therein are `0`. It’s always best practice to be aware of the potential for garbage values when you do not initialize blocks of memory to some other value like zero or otherwise.
    

## Pointer Fun with Binky

+   We watched a [video from Stanford University](https://www.youtube.com/watch?v=5VnDaHBi8dM) that helped us visualize and understand pointers.

## Swap

+   In the real world, a common need in programming is to swap two values. Naturally, it’s hard to swap two variables without a temporary holding space. In practice, you can type `code swap.c` and write code as follows to see this in action:
    
    ```auto
    #include <stdio.h>
    
    void swap(int a, int b);
    
    int main(void)
    {
        int x = 1;
        int y = 2;
    
        printf("x is %i, y is %i\n", x, y);
        swap(x, y);
        printf("x is %i, y is %i\n", x, y);
    }
    
    void swap(int a, int b)
    {
        int tmp = a;
        a = b;
        b = tmp;
    }
    ```
    
    Notice that while this code runs, it does not work. The values, even after being sent to the `swap` function, do not swap. Why?
    
+   When you pass values to a function, you are only providing copies. In previous weeks, we discussed the concept of *scope*. The values of `x` and `y` created in the curly `{}` braces of the `main` function only have the scope of the `main` function. Consider the following image:
    
    ![a rectangle with machine code at top followed by globals heap and stack](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide163-20240811154041360.png "stack and heap")
    
    Notice that *global* variables, which we have not used in this course, live in one place in memory. Various functions are stored in the `stack` in another area of memory.
    
+   Now, consider the following image:
    
    ![a rectangle with main function at bottom and swap function directly above it](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide167-20240811154041129.png "frames")
    
    Notice that `main` and `swap` have two separate *frames* or areas of memory. Therefore, we cannot simply pass the values from one function to another to change them.
    
+   Modify your code as follows:
    
    ```auto
    #include <stdio.h>
    
    void swap(int *a, int *b);
    
    int main(void)
    {
        int x = 1;
        int y = 2;
    
        printf("x is %i, y is %i\n", x, y);
        swap(&x, &y);
        printf("x is %i, y is %i\n", x, y);
    }
    
    void swap(int *a, int *b)
    {
        int tmp = *a;
        *a = *b;
        *b = tmp;
    }
    ```
    
    Notice that variables are not passed by *value* but by *reference*. That is, the addresses of `a` and `b` are provided to the function. Therefore, the `swap` function can know where to make changes to the actual `a` and `b` from the main function.
    
+   You can visualize this as follows:
    
    ![a and b stored in main function being passed by reference to the swap function](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week4Slide198-20240811154041418.png "swap by reference")
    

## Overflow

+   A *heap overflow* is when you overflow the heap, touching areas of memory you are not supposed to.
+   A *stack overflow* is when too many functions are called, overflowing the amount of memory available.
+   Both of these are considered *buffer overflows*.

## `scanf`

+   In CS50, we have created functions like `get_int` to simplify the act of getting input from the user.
+   `scanf` is a built-in function that can get user input.
+   We can reimplement `get_int` rather easily using `scanf` as follows:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        int x;
        printf("x: ");
        scanf("%i", &x);
        printf("x: %i\n", x);
    }
    ```
    
    Notice that the value of `x` is stored at the location of `x` in the line `scanf("%i", &x)`.
    
+   However, attempting to reimplement `get_string` is not easy. Consider the following:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        char *s;
        printf("s: ");
        scanf("%s", s);
        printf("s: %s\n", s);
    }
    ```
    
    Notice that no `&` is required because strings are special. Still, this program will not function. Nowhere in this program do we allocate the amount of memory required for our string. Indeed, we don’t know how long of a string may be inputted by the user!
    
+   Further, your code could be modified as follows. However, we have to pre-allocate a certain amount of memory for a string:
    
    ```auto
    #include <stdio.h>
    #include <stdlib.h>
    
    int main(void)
    {
        char *s = malloc(4);
        if (s == NULL)
        {
            return 1;
        }
        printf("s: ");
        scanf("%s", s);
        printf("s: %s\n", s);
        free(s);
        return 0;
    }
    ```
    
    Notice that if a string that is six bytes is provided you *might* get an error.
    
+   Simplifying our code as follows we can further understand this essential problem of pre-allocation:
    
    ```auto
    #include <stdio.h>
    
    int main(void)
    {
        char s[4];
        printf("s: ");
        scanf("%s", s);
        printf("s: %s\n", s);
    }
    ```
    
    Notice that if we pre-allocate an array of size `4`, we can type `cat` and the program functions. However, a string larger than this *could* create an error.
    
+   Sometimes, the compiler or the system running it may allocate more memory than we indicate. Fundamentally, though, the above code is unsafe. We cannot trust that the user will input a string that fits into our pre-allocated memory.

## File I/O

+   You can read from and manipulate files. While this topic will be discussed further in a future week, consider the following code for `phonebook.c`:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        // Open CSV file
        FILE *file = fopen("phonebook.csv", "a");
    
        // Get name and number
        char *name = get_string("Name: ");
        char *number = get_string("Number: ");
    
        // Print to file
        fprintf(file, "%s,%s\n", name, number);
    
        // Close file
        fclose(file);
    }
    ```
    
    Notice that this code uses pointers to access the file.
    
+   You can create a file called `phonebook.csv` in advance of running the above code. After running the above program and inputting a name and phone number, you will notice that this data persists in your CSV file.
+   If we want to ensure that `phonebook.csv` exists prior to running the program, we can modify our code as follows:
    
    ```auto
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        // Open CSV file
        FILE *file = fopen("phonebook.csv", "a");
        if (!file)
        {
            return 1;
        }
    
        // Get name and number
        char *name = get_string("Name: ");
        char *number = get_string("Number: ");
    
        // Print to file
        fprintf(file, "%s,%s\n", name, number);
    
        // Close file
        fclose(file);
    }
    ```
    
    Notice that this program protects against a `NULL` pointer by invoking `return 1`.
    
+   We can implement our own copy program by typing `code cp.c` and writing code as follows:
    
    ```auto
    #include <stdio.h>
    #include <stdint.h>
    
    typedef uint8_t BYTE;
    
    int main(int argc, char *argv[])
    {
        FILE *src = fopen(argv[1], "rb");
        FILE *dst = fopen(argv[2], "wb");
    
        BYTE b;
    
        while (fread(&b, sizeof(b), 1, src) !=0)
        {
            fwrite(&b, sizeof(b), 1, dst);
        }
    
        fclose(dst);
        fclose(src);
    }
    ```
    
    Notice that this file creates our own data type called a `BYTE` that is the size of a `uint8_t`. Then, the file reads a `BYTE` and writes it to a file.
    
+   BMPs are also assortments of data that we can examine and manipulate. This week, you will be doing just that in your problem sets!

## Summing Up

In this lesson, you learned about pointers that provide you with the ability to access and manipulate data at specific memory locations. Specifically, we delved into…

+   Pixel art
+   Hexadecimal
+   Memory
+   Pointers
+   Strings
+   Pointer Arithmetic
+   String Comparison
+   Copying
+   malloc and Valgrind
+   Garbage values
+   Swapping
+   Overflow
+   `scanf`
+   File I/O

See you next time!


# Lecture 5-Data Structures



- [Welcome!](https://cs50.harvard.edu/x/2024/notes/5/#welcome)
- [Data Structures](https://cs50.harvard.edu/x/2024/notes/5/#data-structures)
- [Stacks and Queues](https://cs50.harvard.edu/x/2024/notes/5/#stacks-and-queues)
- [Jack Learns the Facts](https://cs50.harvard.edu/x/2024/notes/5/#jack-learns-the-facts)
- [Resizing Arrays](https://cs50.harvard.edu/x/2024/notes/5/#resizing-arrays)
- [Linked Lists](https://cs50.harvard.edu/x/2024/notes/5/#linked-lists)
- [Trees](https://cs50.harvard.edu/x/2024/notes/5/#trees)
- [Dictionaries](https://cs50.harvard.edu/x/2024/notes/5/#dictionaries)
- [Hashing and Hash Tables](https://cs50.harvard.edu/x/2024/notes/5/#hashing-and-hash-tables)
- [Tries](https://cs50.harvard.edu/x/2024/notes/5/#tries)
- [Summing Up](https://cs50.harvard.edu/x/2024/notes/5/#summing-up)



## [Welcome!](https://cs50.harvard.edu/x/2024/notes/5/#welcome)

- All the prior weeks have presented you with the fundamental building blocks of programming.
- All you have learned in C will enable you to implement these building blocks in higher-level programming languages such as Python.
- Today, we are going to talk about organizing data in memory and design possibilities that emerge from your growing knowledge.



## [Data Structures](https://cs50.harvard.edu/x/2024/notes/5/#data-structures)

- *Data structures* essentially are forms of organization in memory.
- There are many ways to organize data in memory.
- *Abstract data structures* are those that we can conceptually imagine. When learning about computer science, it’s often useful to begin with these conceptual data structures. Learning these will make it easier later to understand how to implement more concrete data structures.



## [Stacks and Queues](https://cs50.harvard.edu/x/2024/notes/5/#stacks-and-queues)

- *Queues* are one form of abstract data structure.

- Queues have specific properties. Namely, they are *FIFO* or “first in first out.” You can imagine yourself in a line for a ride at an amusement park. The first person in the line gets to go on the ride first. The last person gets to go on the ride last.

- Queues have specific actions associated with them. For example, an item can be *enqueued*; that is, the item can join the line or queue. Further, an item can be *dequeued* or leave the queue once it reaches the front of the line.

- Queues contrast a *stack*. Fundamentally, the properties of a stack are different than a queue. Specifically, it is *LIFO* or “last in first out.” Just like stacking trays in a cafeteria, a tray that is placed in a stack last is the first that may be picked up.

- Stacks have specific actions associated with them. For example, *push* places something on top of a stack. *Pop* is removing something from the top of the stack.

- 

  In code, you might imagine a stack as follows:

  ```
  typedef struct
  {
      person people[CAPACITY];
      int size;
  }
  stack;
  ```

  Notice that an array called people is of type `person`. The `CAPACITY` is how high the stack could be. The integer `size` is how full the stack actually is, regardless of how much it *could* hold.

- You might imagine that the above code has a limitation. Since the capacity of the array is always predetermined in this code. Therefore, the stack may always be oversized. You might imagine only using one place in the stack out of 5000.

- It would be nice for our stack to be dynamic – able to grow as items are added to it.



## [Jack Learns the Facts](https://cs50.harvard.edu/x/2024/notes/5/#jack-learns-the-facts)

- We watched a video called [Jack Learns the Facts](https://www.youtube.com/watch?v=ItAG3s6KIEI) by Professor Shannon Duvall of Elon University.



## [Resizing Arrays](https://cs50.harvard.edu/x/2024/notes/5/#resizing-arrays)

- Rewinding to Week 2, we introduced you to your first data structure.

- An array is a block of contiguous memory.

- 

  You might imagine an array as follows:

  ![three boxes with 1 2 3](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide019-20240811153850828.png)

- 

  In memory, there are other values being stored by other programs, functions, and variables. Many of these may be unused garbage values that were utilized at one point but are available now for use.

  ![three boxes with 1 2 3 among lots of other memory elements](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide022.png)

- 

  Imagine you wanted to store a fourth value `4` in our array? What would be needed is to allocate a new area of memory and move the old array to a new one. Initially, this new area of memory would be populated with garbage values.

  ![Three boxes with 1 2 3 above four boxes with garbage values](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide025.png)

- 

  As values are added to this new area of memory, old garbage values would be overwritten.

  ![Three boxes with 1 2 3 above four boxes with 1 2 3 and a garbage value](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide026.png)

- 

  Eventually, all old garbage values would be overwritten with our new data.

  ![Three boxes with 1 2 3 above four boxes with 1 2 3 4](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide027.png)

- One of the drawbacks of this approach is that it’s bad design: Every time we add a number, we have to copy the array item by item.

- Wouldn’t it be nice if we were able to put the `4` somewhere else in memory? By definition, this would no longer be an array because `4` would no longer be in contiguous memory.

- 

  In your terminal, type `code list.c` and write code as follows:

  ```
  // Implements a list of numbers with an array of fixed size
  
  #include <stdio.h>
  
  int main(void)
  {
      // List of size 3
      int list[3];
  
      // Initialize list with numbers
      list[0] = 1;
      list[1] = 2;
      list[2] = 3;
  
      // Print list
      for (int i = 0; i < 3; i++)
      {
          printf("%i\n", list[i]);
      }
  }
  ```

  Notice that the above is very much like what we learned earlier in this course. We have memory being preallocated for three items.

- 

  Building upon our knowledge obtained more recently, we can leverage our understanding of pointers to create a better design in this code. Modify your code as follows:

  ```
  // Implements a list of numbers with an array of dynamic size
  
  #include <stdio.h>
  #include <stdlib.h>
  
  int main(void)
  {
      // List of size 3
      int *list = malloc(3 * sizeof(int));
      if (list == NULL)
      {
          return 1;
      }
  
      // Initialize list of size 3 with numbers
      list[0] = 1;
      list[1] = 2;
      list[2] = 3;
  
      // List of size 4
      int *tmp = malloc(4 * sizeof(int));
      if (tmp == NULL)
      {
          free(list);
          return 1;
      }
  
      // Copy list of size 3 into list of size 4
      for (int i = 0; i < 3; i++)
      {
          tmp[i] = list[i];
      }
  
      // Add number to list of size 4
      tmp[3] = 4;
  
      // Free list of size 3
      free(list);
  
      // Remember list of size 4
      list = tmp;
  
      // Print list
      for (int i = 0; i < 4; i++)
      {
          printf("%i\n", list[i]);
      }
  
      // Free list
      free(list);
      return 0;
  }
  ```

  Notice that a list of size three integers is created. Then, three memory addresses can be assigned the values `1`, `2`, and `3`. Then, a list of size four is created. Next, the list is copied from the first to the second. The value for the `4` is added to the `tmp` list. Since the block of memory that `list` points to is no longer used, it is freed using the command `free(list)`. Finally, the compiler is told to point `list` pointer now to the block of memory that `tmp` points to. The contents of `list` are printed and then freed.

- It’s useful to think about `list` and `tmp` as both signs that point at a chunk of memory. As in the example above, `list` at one point *pointed* to an array of size 3. By the end, `list` was told to point to a chunk of memory of size 4. Technically, by the end of the above code, `tmp` and `list` both pointed to the same block of memory.

- One may be tempted to allocate way more memory than required for the list, such as 30 items instead of the required 3 or 4. However, this is bad design as it taxes system resources when they are not potentially needed. Further, there is little guarantee that memory for more than 30 items will be needed eventually.



## [Linked Lists](https://cs50.harvard.edu/x/2024/notes/5/#linked-lists)

- In recent weeks, you have learned about three useful primitives. A `struct` is a data type that you can define yourself. A `.` in *dot notation* allows you to access variables inside that structure. The `*` operator is used to declare a pointer or dereference a variable.

- Today, you are introduced to the `->` operator. It is an arrow. This operator goes to an address and looks inside of a structure.

- A *linked list* is one of the most powerful data structures within C. A linked list allows you to include values that are located at varying areas of memory. Further, they allow you to dynamically grow and shrink the list as you desire.

- 

  You might imagine three values stored at three different areas of memory as follows:

  ![Three boxes with 1 2 3 in separate areas of memory](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide036.png)

- How could one stitch together these values in a list?

- 

  We could imagine this data pictured above as follows:

  ![Three boxes with 1 2 3 in separate areas of memory with smaller boxes attached](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide037-20240811153851089.png)

- 

  We could utilize more memory to keep track of where the next item is.

  ![Three boxes with 1 2 3 in separate areas of memory with smaller boxes attached where memory addresses are in those attached boxes](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide041-20240811153851315.png)

  Notice that NULL is utilized to indicate that nothing else is *next* in the list.

- 

  By convention, we would keep one more element in memory, a pointer, that keeps track of the first item in the list.

  ![Three boxes with 1 2 3 in separate areas of memory with smaller boxes attached where memory addresses are in those attached boxes now with a final box with the memory address of the first box](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide042.png)

- 

  Abstracting away the memory addresses, the list would appear as follows:

  ![Three boxes with in separate areas of memory with smaller boxes with a final box where the one box points to another and another until the end of the boxes](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide043.png)

- 

  These boxes are called *nodes*. A *node* contains both an *item* and a pointer called *next*. In code, you can imagine a node as follows:

  ```
  typedef struct node
  {
      int number;
      struct node *next;
  }
  node;
  ```

  Notice that the item contained within this node is an integer called `number`. Second, a pointer to a node called `next` is included, which will point to another node somewhere in memory.

- 

  Conceptually, we can imagine the process of creating a linked list. First, `node *list` is declared, but it is of a garbage value.

  ![One garbage value](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide055.png)

- 

  Next, a node called `n` is allocated in memory.

  ![One garbage value called n with another pointer called list](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide059-20240811153851815.png)

- 

  Next, the `number` of node is assigned the value `1`.

  ![n pointing to a node with 1 as the number and garbage value as the next](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide064.png)

- 

  Next, the node’s `next` field is assigned `NULL`.

  ![n pointing to a node with 1 as the number and null as the value of next](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide066.png)

- 

  Next, `list` is pointed at the memory location to where `n` points. `n` and `list` now point to the same place.

  ![n and list both pointing to a node with 1 as the number and null as the value of next](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide068-20240811153851850.png)

- 

  A new node is then created. Both the `number` and `next` field are both filled with garbage values.

  ![list pointing to a node with 1 as the number and null as the value of next and n pointing to a new node with garbage values](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide073.png)

- 

  The `number` value of `n`’s node (the new node) is updated to `2`.

  ![list pointing to a node with 1 as the number and null as the value of next and n pointing to a new node with 2 as the number and garbage as the next](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide075.png)

- 

  Also, the `next` field is updated as well.

  ![list pointing to a node with 1 as the number and null as the value of next and n pointing to a new node with 2 as the number and null as the next](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide077.png)

- 

  Most important, we do not want to lose our connection to any of these nodes lest they be lost forever. Accordingly, `n`’s `next` field is pointed to the same memory location as `list`.

  ![list pointing to a node with 1 as the number and null as the value of next and n pointing to a new node with 2 as the number and null as the next](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide084.png)

- 

  Finally, `list` is updated to point at `n`. We now have a linked list of two items.

  ![list pointing to a node with 1 as the number and next pointing to a node with an n pointing the same place the node with one points to a node with 2 as the number and null as the next](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide086.png)

- 

  To implement this in code, modify your code as follows:

  ```
  // Prepends numbers to a linked list, using while loop to print
  
  #include <cs50.h>
  #include <stdio.h>
  #include <stdlib.h>
  
  typedef struct node
  {
      int number;
      struct node *next;
  }
  node;
  
  int main(int argc, char *argv[])
  {
      // Memory for numbers
      node *list = NULL;
  
      // For each command-line argument
      for (int i = 1; i < argc; i++)
      {
          // Convert argument to int
          int number = atoi(argv[i]);
  
          // Allocate node for number
          node *n = malloc(sizeof(node));
          if (n == NULL)
          {
              return 1;
          }
          n->number = number;
          n->next = NULL;
  
          // Prepend node to list
          n->next = list;
          list = n;
      }
  
      // Print numbers
      node *ptr = list;
      while (ptr != NULL)
      {
          printf("%i\n", ptr->number);
          ptr = ptr->next;
      }
  
      // Free memory
      ptr = list;
      while (ptr != NULL)
      {
          node *next = ptr->next;
          free(ptr);
          ptr = next;
      }
  }
  ```

  Notice that what the user inputs at the command line is put into the `number` field of a node called `n`, and then that node is added to the `list`. For example, `./list 1 2` will put the number `1` into the `number` field of a node called `n`, then put a pointer to `list` into the `next` field of the node, and then update `list` to point to `n`. That same process is repeated for `2`. Next, `node *ptr = list` creates a temporary variable that points at the same spot that `list` points to. The `while` prints what at the node `ptr` points to, and then updates `ptr` to point to the `next` node in the list. Finally, all the memory is freed.

- In this example, inserting into the list is always in the order of O(1), as it only takes a very small number of steps to insert at the front of a list.

- Considering the amount of time required to search this list, it is in the order of O(n), as in the worst case the entire list must always be searched to find an item. The time complexity for adding a new element to the list will depend on where that element is added. This is illustrated in the examples below.

- Linked lists are not stored in a contiguous block of memory. They can grow as large as you wish, provided that enough system resources exist. The downside, however, is that more memory is required to keep track of the list instead of an array. This is because for each element, you must store not just the value of the element, but also a pointer to the next node. Further, linked lists cannot be indexed into like is possible in an array because we need to pass through the first n−1 elements to find the location of the nth element. Because of this, the list pictured above must be linearly searched. Binary search, therefore, is not possible in a list constructed as above.

- 

  Further, you could place numbers at the end of the list as illustrated in this code:

  ```
  // Implements a list of numbers using a linked list
  
  #include <cs50.h>
  #include <stdio.h>
  #include <stdlib.h>
  
  typedef struct node
  {
      int number;
      struct node *next;
  }
  node;
  
  int main(int argc, char *argv[])
  {
      // Memory for numbers
      node *list = NULL;
  
      // For each command-line argument
      for (int i = 1; i < argc; i++)
      {
          // Convert argument to int
          int number = atoi(argv[i]);
  
          // Allocate node for number
          node *n = malloc(sizeof(node));
          if (n == NULL)
          {
              return 1;
          }
          n->number = number;
          n->next = NULL;
  
          // If list is empty
          if (list == NULL)
          {
              // This node is the whole list
              list = n;
          }
  
          // If list has numbers already
          else
          {
              // Iterate over nodes in list
              for (node *ptr = list; ptr != NULL; ptr = ptr->next)
              {
                  // If at end of list
                  if (ptr->next == NULL)
                  {
                      // Append node
                      ptr->next = n;
                      break;
                  }
              }
          }
      }
  
      // Print numbers
      for (node *ptr = list; ptr != NULL; ptr = ptr->next)
      {
          printf("%i\n", ptr->number);
      }
  
      // Free memory
      node *ptr = list;
      while (ptr != NULL)
      {
          node *next = ptr->next;
          free(ptr);
          ptr = next;
      }
  }
  ```

  Notice how this code *walks down* this list to find the end. When appending an element, (adding to the end of the list) our code will run in O(n), as we have to go through our entire list before we can add the final element.

- 

  Further, you could sort your list as items are added:

  ```
  // Implements a sorted list of numbers using a linked list
  
  #include <cs50.h>
  #include <stdio.h>
  #include <stdlib.h>
  
  typedef struct node
  {
      int number;
      struct node *next;
  }
  node;
  
  int main(int argc, char *argv[])
  {
      // Memory for numbers
      node *list = NULL;
  
      // For each command-line argument
      for (int i = 1; i < argc; i++)
      {
          // Convert argument to int
          int number = atoi(argv[i]);
  
          // Allocate node for number
          node *n = malloc(sizeof(node));
          if (n == NULL)
          {
              return 1;
          }
          n->number = number;
          n->next = NULL;
  
          // If list is empty
          if (list == NULL)
          {
              list = n;
          }
  
          // If number belongs at beginning of list
          else if (n->number < list->number)
          {
              n->next = list;
              list = n; 
          }
  
          // If number belongs later in list
          else
          {
              // Iterate over nodes in list
              for (node *ptr = list; ptr != NULL; ptr = ptr->next)
              {
                  // If at end of list
                  if (ptr->next == NULL)
                  {
                      // Append node
                      ptr->next = n;
                      break;
                  }
  
                  // If in middle of list
                  if (n->number < ptr->next->number)
                  {
                      n->next = ptr->next;
                      ptr->next = n;
                      break;
                  }
              }
          }
      }
  
      // Print numbers
      for (node *ptr = list; ptr != NULL; ptr = ptr->next)
      {
          printf("%i\n", ptr->number);
      }
  
      // Free memory
      node *ptr = list;
      while (ptr != NULL)
      {
          node *next = ptr->next;
          free(ptr);
          ptr = next;
      }
  }
  ```

  Notice how this list is sorted as it is built. To insert an element in this specific order, our code will still run in O(n) for each insertion, as in the worst case we will have to look through all current elements.



## [Trees](https://cs50.harvard.edu/x/2024/notes/5/#trees)

- *Binary search trees* are another data structure that can be used to store data more efficiently such that it can be searched and retrieved.

- 

  You can imagine a sorted sequence of numbers.

  ![1 2 3 4 5 6 7 in boxes next to each other](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide118.png)

- 

  Imagine then that the center value becomes the top of a tree. Those that are less than this value are placed to the left. Those values that are more than this value are to the right.

  ![1 2 3 4 5 6 7 in boxes arranged in a hierarchy 4 is at the top 3 and 5 are below that and 1 2 6 7 are below those](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide119.png)

- 

  Pointers can then be used to point to the correct location of each area of memory such that each of these nodes can be connected.

  ![1 2 3 4 5 6 7 in boxes arranged in a hierarchy 4 is at the top 3 and 5 are below that and 1 2 6 7 are below those arrows connect them in a tree formation](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide120.png)

- 

  In code, this can be implemented as follows.

  ```
  // Implements a list of numbers as a binary search tree
  
  #include <stdio.h>
  #include <stdlib.h>
  
  // Represents a node
  typedef struct node
  {
      int number;
      struct node *left;
      struct node *right;
  }
  node;
  
  void free_tree(node *root);
  void print_tree(node *root);
  
  int main(void)
  {
      // Tree of size 0
      node *tree = NULL;
  
      // Add number to list
      node *n = malloc(sizeof(node));
      if (n == NULL)
      {
          return 1;
      }
      n->number = 2;
      n->left = NULL;
      n->right = NULL;
      tree = n;
  
      // Add number to list
      n = malloc(sizeof(node));
      if (n == NULL)
      {
          free_tree(tree);
          return 1;
      }
      n->number = 1;
      n->left = NULL;
      n->right = NULL;
      tree->left = n;
  
      // Add number to list
      n = malloc(sizeof(node));
      if (n == NULL)
      {
          free_tree(tree);
          return 1;
      }
      n->number = 3;
      n->left = NULL;
      n->right = NULL;
      tree->right = n;
  
      // Print tree
      print_tree(tree);
  
      // Free tree
      free_tree(tree);
      return 0;
  }
  
  void free_tree(node *root)
  {
      if (root == NULL)
      {
          return;
      }
      free_tree(root->left);
      free_tree(root->right);
      free(root);
  }
  
  void print_tree(node *root)
  {
      if (root == NULL)
      {
          return;
      }
      print_tree(root->left);
      printf("%i\n", root->number);
      print_tree(root->right);
  }
  ```

  Notice this search function begins by going to the location of `tree`. Then, it uses recursion to search for `number`. The `free_tree` function recursively frees the tree. `print_tree` recursively prints the tree.

- A tree like the above offers dynamism that an array does not offer. It can grow and shrink as we wish.

- Further, this structure offers a search time of O(logn).



## [Dictionaries](https://cs50.harvard.edu/x/2024/notes/5/#dictionaries)

- *Dictionaries* are another data structure.

- Dictionaries, like actual book-form dictionaries that have a word and a definition, have a *key* and a *value*.

- 

  The *holy grail* of algorithmic time complexity is O(1) or *constant time*. That is, the ultimate is for access to be instantaneous.

  ![a graph of various time comlexities where O of log n is second best and O of 1 is best](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide151.png)

- Dictionaries can offer this speed of access through hashing.



## [Hashing and Hash Tables](https://cs50.harvard.edu/x/2024/notes/5/#hashing-and-hash-tables)

- *Hashing* is the idea of taking a value and being able to output a value that becomes a shortcut to it later.

- For example, hashing *apple* may hash as a value of `1`, and *berry* may be hashed as `2`. Therefore, finding *apple* is as easy as asking the *hash* algorithm where *apple* is stored. While not ideal in terms of design, ultimately, putting all *a*’s in one bucket and *b*’s in another, this concept of *bucketizing* hashed values illustrates how you can use this concept: a hashed value can be used to shortcut finding such a value.

- A *hash function* is an algorithm that reduces a larger value to something small and predictable. Generally, this function takes in an item you wish to add to your hash table, and returns an integer representing the array index in which the item should be placed.

- A *hash table* is a fantastic combination of both arrays and linked lists. When implemented in code, a hash table is an *array* of *pointers* to *node*s.

- 

  A hash table could be imagined as follows:

  ![a verticle column of 26 boxes one for each letter of the alphabet](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide157.png)

  Notice that this is an array that is assigned each value of the alphabet.

- 

  Then, at each location of the array, a linked list is used to track each value being stored there:

  ![a verticle column of 26 boxes one for each letter of the alphabet with various names from themario unverise emerging to the right luigi is with l and mario is with m](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide169.png)

- *Collisions* are when you add values to the hash table, and something already exists at the hashed location. In the above, collisions are simply appended to the end of the list.

- 

  Collisions can be reduced by better programming your hash table and hash algorithm. You can imagine an improvement upon the above as follows:

  ![a verticle column of various boxeds arranged by L A K and L I N with lakitu emerging from L A K and link emerging from L I N](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide184.png)

- 

  Consider the following example of a hash algorithm:

  ![luigi being given to a hash algorithm outputting 11](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide173.png)

- 

  This could be implemented in code as:

  ```
  #include <ctype.h>
  
  unsigned int hash(const char *word)
  {
      return toupper(word[0]) - 'A';
  }
  ```

  Notice how the hash function returns the value of `toupper(word[0]) - 'A'`.

- You, as the programmer, have to make a decision about the advantages of using more memory to have a large hash table and potentially reducing search time or using less memory and potentially increasing search time.



## [Tries](https://cs50.harvard.edu/x/2024/notes/5/#tries)

- *Tries* are another form of data structure.

- *Tries* are always searchable in constant time.

- One downside to *Tries* is that they tend to take up a large amount of memory. Notice that we need 26×4=104 `node`s just to store *Toad*!

- 

  *Toad* would be stored as follows:

  ![toad being spelled with one letter at a time where one letter is associated with one list T from one list O from another and so on ](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide207.png)

- 

  *Tom* would then be stored as follows:

  ![toad being spelled with one letter at a time where one letter is associated with one list T from one list O from another and so on and tom being spelled similarly where toad and tom share a two common letters T and O](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week5Slide209.png)

- The downside of this structure is how many resources are required to use it.



## [Summing Up](https://cs50.harvard.edu/x/2024/notes/5/#summing-up)

In this lesson, you learned about using pointers to build new data structures. Specifically, we delved into…

- Data structures
- Stacks and queues
- Resizing arrays
- Linked lists
- Dictionaries
- Tries

See you next time!


# Lecture 6-Python



+   [Welcome!](#welcome)
+   [Python](#python)
+   [Hello](#hello)
+   [Speller](#speller)
+   [Filter](#filter)
+   [CS50 Library](#cs50-library)
+   [Strings](#strings)
+   [Variables](#variables)
+   [Types](#types)
+   [Calculator](#calculator)
+   [Conditionals](#conditionals)
+   [Object-Oriented Programming](#object-oriented-programming)
+   [Loops](#loops)
+   [Abstraction](#abstraction)
+   [Truncation and Floating Point Imprecision](#truncation-and-floating-point-imprecision)
+   [Exceptions](#exceptions)
+   [Mario](#mario)
+   [Lists](#lists)
+   [Searching and Dictionaries](#searching-and-dictionaries)
+   [Command-Line Arguments](#command-line-arguments)
+   [Exit Status](#exit-status)
+   [Third-Party Libraries](#third-party-libraries)
+   [Summing Up](#summing-up)

## Welcome!

+   In previous weeks, you were introduced to the fundamental building blocks of programming.
+   You learned about programming in a lower-level programming language called C.
+   Today, we are going to work with a higher-level programming language called *Python*.
+   As you learn this new language, you’re going to find that you are going to be more able to teach yourself new programming languages.

## Python

+   Humans, over the decades, have seen how previous design decisions could be improved upon.
+   Python is a programming language that builds upon what you have already learned in C.
+   Unlike in C, Python is an interpreted language, where you need not separately compile your program. Instead, you run your program in the *Python Interpreter*.

## Hello

+   Up until this point, the code has looked like this:
    
    ```auto
    // A program that says hello to the world
    
    #include <stdio.h>
    
    int main(void)
    {
        printf("hello, world\n");
    }
    ```
    
+   Today, you’ll find that the process of writing and compiling code has been simplified.
+   For example, the above code will be rendered in Python as:
    
    ```auto
    # A program that says hello to the world
    
    print("hello, world")
    ```
    
    Notice that the semicolon is gone and that no library is needed.
    
+   Python notably can implement what was quite complicated in C with relative simplicity.

## Speller

+   To illustrate this simplicity, let’s type ‘code dictionary.py’ in the terminal window and write code as follows:
    
    ```auto
    # Words in dictionary
    words = set()
    
    
    def check(word):
        """Return true if word is in dictionary else false"""
        return word.lower() in words
    
    
    def load(dictionary):
        """Load dictionary into memory, returning true if successful else false"""
        with open(dictionary) as file:
            words.update(file.read().splitlines())
        return True
    
    
    def size():
        """Returns number of words in dictionary if loaded else 0 if not yet loaded"""
        return len(words)
    
    
    def unload():
        """Unloads dictionary from memory, returning true if successful else false"""
        return True
    ```
    
    Notice that there are four functions above. In the `check` function, if a `word` is in `words`, it returns `True`. So much easier than an implementation in C! Similarly, in the `load` function the dictionary file is opened. For each line in that file, we add that line to `words`. Using `rstrip`, the trailing new line is removed from the added word. `size` simply returns the `len` or length of `words`. `unload` only needs to return `True` because Python handles memory management on its own.
    
+   The above code illustrates why higher-level languages exist: To simplify and allow you to write code more easily.
+   However, speed is a tradeoff. Because C allows you, the programmer, to make decisions about memory management, it may run faster than Python – depending on your code. While C only runs your lines of code, Python runs all the code that comes under the hood with it when you call Python’s built-in functions.
+   You can learn more about functions in the [Python documentation](https://docs.python.org/3/library/functions.html)

## Filter

+   To further illustrate this simplicity, create a new file by typing `code blur.py` in your terminal window and write code as follows:
    
    ```auto
    # Blurs an image
    
    from PIL import Image, ImageFilter
    
    # Blur image
    before = Image.open("bridge.bmp")
    after = before.filter(ImageFilter.BoxBlur(1))
    after.save("out.bmp")
    ```
    
    Notice that this program imports modules `Image` and `ImageFilter` from a library called `PIL`. This takes an input file and creates and output file.
    
+   Further, you can create a new file called `edges.py` as follows:
    
    ```auto
    # Finds edges in an image
    
    from PIL import Image, ImageFilter
    
    # Find edges
    before = Image.open("bridge.bmp")
    after = before.filter(ImageFilter.FIND_EDGES)
    after.save("out.bmp")
    ```
    
    Notice that this code is a small adjustment to your `blur` code, but produces a dramatically different result.
    
+   Finally, you can even do face detection as follows:
    
    ```auto
    # Find faces in picture
    # https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py
    
    from PIL import Image
    import face_recognition
    
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file("office.jpg")
    
    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)
    
    for face_location in face_locations:
    
        # Print the location of each face in this image
        top, right, bottom, left = face_location
    
        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
    ```
    
    Notice how this file uses a third-party library called face\_recognition. This is enabled by running `pip install face_recognition` in one’s terminal window.
    
+   Python allows you to abstract away programming that would be much more complicated within C and other *lower-level* programming languages.
    

## CS50 Library

+   As with C, the CS50 library can be utilized within Python.
+   The following functions will be of particular use:
    
    ```auto
      get_float
      get_int
      get_string
    ```
    
+   You also have the option of importing only specific functions from the CS50 library as follows:
    
    ```auto
    from CS50 import get_float, get_int, get_string
    ```
    

## Strings

+   In C, you might remember this code:
    
    ```auto
    // get_string and printf with %s
    
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        string answer = get_string("What's your name? ");
        printf("hello, %s\n", answer);
    }
    ```
    
+   This code is transformed in Python to:
    
    ```auto
    # get_string and print, with concatenation
    
    from cs50 import get_string
    
    answer = get_string("What's your name? ")
    print("hello, " + answer)
    ```
    
    You can write this code by executing `code hello.py` in the terminal window. Then, you can execute this code by running `python hello.py`. Notice how the `+` sign concatenates `"hello, "` and `answer`.
    
+   Similarly, you could implement the above code as:
    
    ```auto
    # get_string and print, with format strings
    
    from cs50 import get_string
    
    answer = get_string("What's your name? ")
    print(f"hello, {answer}")
    ```
    
    Notice how the curly braces allow for the `print` function to interpolate the `answer` such that `answer` appears within. The `f` is required to include the `answer` properly formatting.
    

## Variables

+   Variable declaration is simplified too. In C, you might have `int counter = 0;`. In Python, this same line would read `counter = 0`. You need not declare the type of the variable.
+   Python favors `counter += 1` to increment by one, losing the ability found in C to type `counter++`.

## Types

+   Data types in Python do not need to be explicitly declared. For example, you saw how `answer` above is a string, but we did not have to tell the interpreter this was the case: It knew on its own.
+   In Python, commonly used types include:
    
    Notice that `long` and `double` are missing. Python will handle what data type should be used for larger and smaller numbers.
    
+   Some other data types in Python include:
    
    ```auto
      range
      list
      tuple
      dict
      set
    ```
    
+   Each of these data types can be implemented in C, but in Python they can be implemented more simply.

## Calculator

+   You might recall `calculator.c` from earlier in the course:
    
    ```auto
    // Addition with int
    
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user for x
        int x = get_int("x: ");
    
        // Prompt user for y
        int y = get_int("y: ");
    
        // Perform addition
        printf("%i\n", x + y);
    }
    ```
    
+   We can implement a simple calculator just as we did within C. Type `code calculator.py` into the terminal window and write code as follows:
    
    ```auto
    # Addition with int [using get_int]
    
    from cs50 import get_int
    
    # Prompt user for x
    x = get_int("x: ")
    
    # Prompt user for y
    y = get_int("y: ")
    
    # Perform addition
    print(x + y)
    ```
    
    Notice how the CS50 library is imported. Then, `x` and `y` are gathered from the user. Finally, the result is printed. Notice that the `main` function that would have been seen in a C program is gone entirely! While one could utilize a `main` function, it is not required.
    
+   It’s possible for one to remove the training wheels of the CS50 library. Modify your code as follows:
    
    ```auto
    # Addition with int [using input]
    
    # Prompt user for x
    x = input("x: ")
    
    # Prompt user for y
    y = input("y: ")
    
    # Perform addition
    print(x + y)
    ```
    
    Notice how executing the above code results in strange program behavior. Why might this be so?
    
+   You may have guessed that the interpreter understood `x` and `y` to be strings. You can fix your code by employing the `int` function as follows:
    
    ```auto
    # Addition with int [using input]
    
    # Prompt user for x
    x = int(input("x: "))
    
    # Prompt user for y
    y = int(input("y: "))
    
    # Perform addition
    print(x + y)
    ```
    
    Notice how the input for `x` and `y` is passed to the `int` function which converts it to an integer. Without converting `x` and `y` to be integers, the characters will concatenate.
    

## Conditionals

+   In C, you might remember a program like this:
    
    ```auto
    // Conditionals, Boolean expressions, relational operators
    
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user for integers
        int x = get_int("What's x? ");
        int y = get_int("What's y? ");
    
        // Compare integers
        if (x < y)
        {
            printf("x is less than y\n");
        }
        else if (x > y)
        {
            printf("x is greater than y\n");
        }
        else
        {
            printf("x is equal to y\n");
        }
    }
    ```
    
+   In Python, it would appear as follows:
    
    ```auto
    # Conditionals, Boolean expressions, relational operators
    
    from cs50 import get_int
    
    # Prompt user for integers
    x = get_int("What's x? ")
    y = get_int("What's y? ")
    
    # Compare integers
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")
    ```
    
    Notice that there are no more curly braces. Instead, indentations are utilized. Second, a colon is utilized in the `if` statement. Further, `elif` replaces `else if`. Parentheses are also no longer required in the `if` and `elif` statements.
    
+   In C, we faced challenges when we wanted to compare two values. Consider the following code:
    
    ```auto
    // Conditionals, Boolean expressions, relational operators
    
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user for integers
        int x = get_int("What's x? ");
        int y = get_int("What's y? ");
    
        // Compare integers
        if (x < y)
        {
            printf("x is less than y\n");
        }
        else if (x > y)
        {
            printf("x is greater than y\n");
        }
        else
        {
            printf("x is equal to y\n");
        }
    }
    ```
    
+   In Python, we can execute the above as follows:
    
    ```auto
    # Conditionals, Boolean expressions, relational operators
    
    from cs50 import get_int
    
    # Prompt user for integers
    x = get_int("What's x? ")
    y = get_int("What's y? ")
    
    # Compare integers
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")
    ```
    
    Notice that the CS50 library is imported. Further, minor changes exist in the `if` statement.
    
+   Further looking at comparisons, consider the following code in C:
    
    ```auto
    // Logical operators
    
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user to agree
        char c = get_char("Do you agree? ");
    
        // Check whether agreed
        if (c == 'Y' || c == 'y')
        {
            printf("Agreed.\n");
        }
        else if (c == 'N' || c == 'n')
        {
            printf("Not agreed.\n");
        }
    }
    ```
    
+   The above can be implemented as follows:
    
    ```auto
    # Logical operators
    
    from cs50 import get_string
    
    # Prompt user to agree
    s = get_string("Do you agree? ")
    
    # Check whether agreed
    if s == "Y" or s == "y":
        print("Agreed.")
    elif s == "N" or s == "n":
        print("Not agreed.")
    ```
    
    Notice that the two vertical bars utilized in C is replaced with `or`. Indeed, people often enjoy Python because it is more readable by humans. Also, notice that `char` does not exist in Python. Instead, `str`s are utilized.
    
+   Another approach to this same code could be as follows using *lists*:
    
    ```auto
    # Logical operators, using lists
    
    from cs50 import get_string
    
    # Prompt user to agree
    s = get_string("Do you agree? ")
    
    # Check whether agreed
    if s in ["y", "yes"]:
        print("Agreed.")
    elif s in ["n", "no"]:
        print("Not agreed.")
    ```
    
    Notice how we are able to express multiple keywords like `y` and `yes` in a `list`.
    

## Object-Oriented Programming

+   Up until this point, our programs in this course have been linear: sequential.
+   It’s possible to have certain types of values not only have properties or attributes inside of them but have functions as well. In Python, these values are known as *objects*
+   In C, we could create a `struct` where you could associate multiple variables inside a single self-created data type. In Python, we can do this and also include functions in a self-created data type. When a function belongs to a specific *object*, it is known as a *method*.
+   For example, `strs` in Python have a built-in *methods*. Therefore, you could modify your code as follows:
    
    ```auto
    # Logical operators, using lists
    
    from cs50 import get_string
    
    # Prompt user to agree
    s = get_string("Do you agree? ").lower()
    
    # Check whether agreed
    if s.lower() in ["y", "yes"]:
        print("Agreed.")
    elif s.lower() in ["n", "no"]:
        print("Not agreed.")
    ```
    
    Notice how the old value of `s` is overwritten with the result of `s.lower()`, a built-in method of `strs`.
    
+   In this class, we will only scratch the surface of Python. Therefore, the [Python documentation](https://docs.python.org/) will be of particular importance as you continue.
+   You can learn more about string methods in the [Python documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)

## Loops

+   Loops in Python are very similar to C. You may recall the following code in C:
    
    ```auto
    // Demonstrates while loop
    
    #include <stdio.h>
    
    int main(void)
    {
        int i = 0;
        while (i < 3)
        {
            printf("meow\n");
            i++;
        }
    }
    ```
    
+   In Python, this code appears as:
    
    ```auto
    # Demonstrates while loop
    
    i = 0
    while i < 3:
        print("meow")
        i += 1
    ```
    
+   `for` loops can be implemented in Python as follows:
    
    ```auto
    # Better design
    
    for i in range(3):
        print("meow")
    ```
    
    Notice that `i` is never explicitly used. However, Python will increment the value of `i`.
    
+   Similarly, one could express the above code as:
    
    ```auto
    # Abstraction with parameterization
    
    def main():
        meow(3)
    
    
    # Meow some number of times
    def meow(n):
        for i in range(n):
            print("meow")
    
    
    main()
    ```
    
    Notice that a function is utilized to abstract away the meowing.
    
+   Finally, a `while` loop could be implemented as follows:
    
    ```auto
    # Demonstrates while loop
    
    i = 0
    while i < 3:
        print("meow")
        i += 1
    ```
    
+   To further our understanding of loops and iteration in Python, let’s create a new file called `uppercase.py` as follows:
    
    ```auto
    # Uppercases string one character at a time
    
    before = input("Before: ")
    print("After:  ", end="")
    for c in before:
        print(c.upper(), end="")
    print()
    ```
    
    Notice how `end=` is used to pass a parameter to the `print` function that continues the line without a line ending. This code passes one string at a time.
    
+   Reading the documentation, we discover that Python has methods that can be implemented upon the entire string as follows:
    
    ```auto
    # Uppercases string all at once
    
    before = input("Before: ")
    after = before.upper()
    print(f"After:  {after}")
    ```
    
    Notice how `.upper` is applied to the entire string.
    

## Abstraction

+   As we hinted at earlier today, you can further improve upon our code using functions and abstracting away various code into functions. Modify your earlier-created `meow.py` code as follows:
    
    ```auto
    # Abstraction
    
    def main():
        for i in range(3):
            meow()
    
    # Meow once
    def meow():
        print("meow")
    
    
    main()
    ```
    
    Notice that the `meow` function abstracts away the `print` statement. Further, notice that the `main` function appears at the top of the file. At the bottom of the file, the `main` function is called. By convention, it’s expected that you create a `main` function in Python.
    
+   Indeed, we can pass variables between our functions as follows:
    
    ```auto
    # Abstraction with parameterization
    
    def main():
        meow(3)
    
    
    # Meow some number of times
    def meow(n):
        for i in range(n):
            print("meow")
    
    
    main()
    ```
    
    Notice how `meow` now takes a variable `n`. In the `main` function, you can call `meow` and pass a value like `3` to it. Then, `meow` utilizes the value of `n` in the `for` loop.
    
+   Reading the above code, notice how you, as a C programmer, are able to quite easily make sense of the above code. While some conventions are different, the building blocks you previously learned are very apparent in this new programming language.
    

## Truncation and Floating Point Imprecision

+   Recall that in C, we experienced truncation where one integer being divided by another could result in an inprecise result.
+   You can see how Python handles such division as follows by modifying your code for `calculator.py`:
    
    ```auto
    # Division with integers, demonstration lack of truncation
    
    # Prompt user for x
    x = int(input("x: "))
    
    # Prompt user for y
    y = int(input("y: "))
    
    # Divide x by y
    z = x / y
    print(z)
    ```
    
    Notice that executing this code results in a value, but that if you were to see more digits after `.333333` you’d see that we are faced with *floating-point imprecision*. Truncation does not occur.
    
+   We can reveal this imprecision by modifying our codes slightly:
    
    ```auto
    # Floating-point imprecision
    
    # Prompt user for x
    x = int(input("x: "))
    
    # Prompt user for y
    y = int(input("y: "))
    
    # Divide x by y
    z = x / y
    print(f"{z:.50f}")
    ```
    
    Notice that this code reveals the imprecision. Python still faces this issue, just as C does.
    

## Exceptions

+   Let’s explore more about exceptions that can occur when we run Python code.
+   Modify `calculator.py` as follows:
    
    ```auto
    # Implements get_int
    
    def get_int(prompt):
        return int(input(prompt))
    
    
    def main():
    
        # Prompt user for x
        x = get_int("x: ")
    
        # Prompt user for y
        y = get_int("y: ")
    
        # Perform addition
        print(x + y)
    
    
    main()
    ```
    
    Notice that inputting the wrong data could result in an error.
    
+   We can `try` to handle and *catch* potential exceptions by modifying our code as follows:
    
    ```auto
    # Implements get_int with a loop
    
    def get_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Not an integer")
    
    
    def main():
    
        # Prompt user for x
        x = get_int("x: ")
    
        # Prompt user for y
        y = get_int("y: ")
    
        # Perform addition
        print(x + y)
    
    
    main()
    ```
    
    Notice that the above code repeatedly tries to get the correct type of data, providing additional prompts when needed.
    

## Mario

+   Recall a few weeks ago our challenge of building three blocks on top of one another, like in Mario.
    
    ![three vertical blocks](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week6Slide073.png "mario blocks")
    
+   In Python, we can implement something akin to this as follows:
    
    ```auto
    # Prints a column of 3 bricks with a loop
    
    for i in range(3):
        print("#")
    ```
    
+   In C, we had the advantage of a `do-while` loop. However, in Python it is convention to utilize a `while` loop, as Python does not have a `do while` loop. You can write code as follows in a file called `mario.py`:
    
    ```auto
    # Prints a column of n bricks with a loop
    
    from cs50 import get_int
    
    while True:
        n = get_int("Height: ")
        if n > 0:
            break
    
    for i in range(n):
        print("#")
    ```
    
    Notice how the while loop is used to obtain the height. Once a height greater than zero is inputted, the loop breaks.
    
+   Consider the following image:
    
    ![four horizontal question blocks](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week6Slide075.png "mario blocks")
    
+   In Python, we could implement by modifying your code as follows:
    
    ```auto
    # Prints a row of 4 question marks with a loop
    
    for i in range(4):
        print("?", end="")
    print()
    ```
    
    Notice that you can override the behavior of the `print` function to stay on the same line as the previous print.
    
+   Similar in spirit to previous iterations, we can further simplify this program:
    
    ```auto
    # Prints a row of 4 question marks without a loop
    
    print("?" * 4)
    ```
    
    Notice that we can utilize `*` to multiply the print statement to repeat `4` times.
    
+   What about a large block of bricks?
    
    ![three by three block of mario blocks](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week6Slide078.png "mario blocks")
    
+   To implement the above, you can modify your code as follows:
    
    ```auto
    # Prints a 3-by-3 grid of bricks with loops
    
    for i in range(3):
        for j in range(3):
            print("#", end="")
        print()
    ```
    
    Notice how one `for` loop exists inside another. The `print` statement adds a new line at the end of each row of bricks.
    
+   You can learn more about the `print` function in the [Python documentation](https://docs.python.org/3/library/functions.html#print)
    

## Lists

+   `list`s are a data structure within Python.
+   `list`s have built in methods or functions within them.
+   For example, consider the following code:
    
    ```auto
    # Averages three numbers using a list
    
    # Scores
    scores = [72, 73, 33]
    
    # Print average
    average = sum(scores) / len(scores)
    print(f"Average: {average}")
    ```
    
    Notice that you can use the built-in `sum` method to calculate the average.
    
+   You can even utilize the following syntax to get values from the user:
    
    ```auto
    # Averages three numbers using a list and a loop
    
    from cs50 import get_int
    
    # Get scores
    scores = []
    for i in range(3):
        score = get_int("Score: ")
        scores.append(score)
    
    # Print average
    average = sum(scores) / len(scores)
    print(f"Average: {average}")
    ```
    
    Notice that this code utilizes the built-in `append` method for lists.
    
+   You can learn more about lists in the [Python documentation](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
+   You can also learn more about `len` in the [Python documentation](https://docs.python.org/3/library/functions.html#len)

## Searching and Dictionaries

+   We can also search within a data structure.
+   Consider a program called `phonebook.py` as follows:
    
    ```auto
    # Implements linear search for names using loop
    
    # A list of names
    names = ["Carter", "David", "John"]
    
    # Ask for name
    name = input("Name: ")
    
    # Search for name
    for n in names:
        if name == n:
            print("Found")
            break
    else:
        print("Not found")
    ```
    
    Notice how this implements linear search for each name.
    
+   However, we don’t need to iterate through a list. In Python, we can execute linear search as follows:
    
    ```auto
    # Implements linear search for names using `in`
    
    # A list of names
    names = ["Carter", "David", "John"]
    
    # Ask for name
    name = input("Name: ")
    
    # Search for name
    if name in names:
        print("Found")
    else:
        print("Not found")
    ```
    
    Notice how `in` is used to implement linear search.
    
+   Still, this code could be improved.
+   Recall that a *dictionary* or `dict` is a collection of *key* and *value* pairs.
+   You can implement a dictionary in Python as follows:
    
    ```auto
    # Implements a phone book as a list of dictionaries, without a variable
    
    from cs50 import get_string
    
    people = [
        {"name": "Carter", "number": "+1-617-495-1000"},
        {"name": "David", "number": "+1-617-495-1000"},
        {"name": "John", "number": "+1-949-468-2750"},
    ]
    
    # Search for name
    name = get_string("Name: ")
    for person in people:
        if person["name"] == name:
            print(f"Found {person['number']}")
            break
    else:
        print("Not found")
    ```
    
    Notice that the dictionary is implemented having both `name` and `number` for each entry.
    
+   Even better, strictly speaking, we don’t need both a `name` and a `number`. We can simplify this code as follows:
    
    ```auto
    # Implements a phone book using a dictionary
    
    from cs50 import get_string
    
    people = {
        "Carter": "+1-617-495-1000",
        "David": "+1-617-495-1000",
        "John": "+1-949-468-2750",
    }
    
    # Search for name
    name = get_string("Name: ")
    if name in people:
        print(f"Number: {people[name]}")
    else:
        print("Not found")
    ```
    
    Notice that the dictionary is implemented using curly braces. Then, the statement `if name in people` searches to see if the `name` is in the `people` dictionary. Further, notice how, in the `print` statement, we can index into the people dictionary using the value of `name`. Very useful!
    
+   Python has done their best to get to *constant time* using their built-in searches.
+   You can learn more about dictionaries in the [Python documentation](https://docs.python.org/3/library/stdtypes.html#dict)

## Command-Line Arguments

+   As with C, you can also utilize command-line arguments. Consider the following code:
    
    ```auto
    # Prints a command-line argument
    
    from sys import argv
    
    if len(argv) == 2:
        print(f"hello, {argv[1]}")
    else:
        print("hello, world")
    ```
    
    Notice that `argv[1]` is printed using a *formatted string*, noted by the `f` present in the `print` statement.
    
+   You can print all the arguments in `argv` as follows:
    
    ```auto
    # Printing command-line arguments, indexing into argv
    
    from sys import argv
    
    for i in range(len(argv)):
        print(argv[i])
    ```
    
    Notice that the above will not present the word `python` if executed, and the first argument will be the name of the file you are running. You can think of the word `python` as being analogous to `./` when we were running programs in C.
    
+   You can slice pieces of lists away. Consider the following code:
    
    ```auto
    # Printing command-line arguments
    
    from sys import argv
    
    for arg in argv:
        print(arg)
    ```
    
    Notice that executing this code will result in the name of the file you are running being sliced away.
    
+   You can learn more about the `sys` library in the [Python documentation](https://docs.python.org/3/library/sys.html)
    

## Exit Status

+   The `sys` library also has built-in methods. We can use `sys.exit(i)` to exit the program with a specific exit code:
    
    ```auto
    # Exits with explicit value, importing sys
    
    import sys
    
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    
    print(f"hello, {sys.argv[1]}")
    sys.exit(0)
    ```
    
    Notice that dot-notation is used to utilize the built-in functions of `sys`.
    

## Third-Party Libraries

+   One of the advantages of Python is its massive user-base and similarly large number of third-party libraries.
+   For example, David demoed the use of `cowsay` and `qrcode` libraries.

## Summing Up

In this lesson, you learned how the building blocks of programming from prior lessons can be implemented within Python. Further, you learned about how Python allowed for more simplified code. Also, you learned how to utilize various Python libraries. In the end, you learned that your skills as a programmer are not limited to a single programming language. Already, you are seeing how you are discovering a new way of learning through this course that could serve you in any programming language – and, perhaps, in nearly any avenue of learning! Specifically, we discussed…

+   Python
+   Variables
+   Conditionals
+   Loops
+   Types
+   Object-Oriented programming
+   Truncation and floating point imprecision
+   Exceptions
+   Dictionaries
+   Command-line arguments
+   Third-Party libraries

See you next time!



# lecture 6.5-Artificial Intelligence

## Artificial Intelligence

+   [Welcome!](#welcome)
+   [Image Generation](#image-generation)
+   [ChatGPT](#chatgpt)
+   [Prompt Generation](#prompt-generation)
+   [CS50.ai](#cs50ai)
+   [Generative AI](#generative-ai)
+   [Decision Trees](#decision-trees)
+   [Minimax](#minimax)
+   [Machine Learning](#machine-learning)
+   [Deep Learning](#deep-learning)
+   [Generative Artificial Intelligence](#generative-artificial-intelligence)
+   [Summing Up](#summing-up)

## Welcome!

+   In computer science and programming circles, *rubber ducking* or *rubber duck debugging* is the act of speaking to an inanimate object to be able to *talk through* a challenging problem.
+   Most recently, CS50 created our own rubber duck debugger at [cs50.ai](https://cs50.ai/), which uses artificial intelligence as a way by which to interact with students to help them with their own challenging problems.
+   Students engaging with this tool can begin understanding the potential of what AI can offer the world.

## Image Generation

+   Numerous AI tools have created the potential for artificially generated images to enter the world.
+   Up until recently, most of these tools had numerous tells that might indicate to an observer that an image is AI-generated.
+   However, tools are becoming exceedingly good at generating these images.
+   Indeed, as technology improves, it will soon be almost, if not entirely, impossible for such images to be detected with the naked eye.
+   Software has also gained the ability to mutate individual images within video.

## ChatGPT

+   A very well-known bleeding-edge tool is the text generation tool *chatGPT*.
+   In CS50, we do not allow the use of ChatGPT. However, we do allow the use of our own rubber duck debugger at [cs50.ai](https://cs50.ai/).
+   In CS50, we leverage the tools of Azure and OpenAI, along with our own vector database that holds very recent information from our most recent lectures and offerings, to provide our rubber duck debugger toll.

## Prompt Generation

+   *Prompt generation* is the way by which an individual can communicate with an AI platform.
+   We use a *system prompt* to teach the AI how to interact with users. We teach the AI how to work with students.
+   *User prompts* are those provided by users to interact with the AI. With these prompts, students interact with the AI.

## CS50.ai

+ Our [rubber duck debugger](https://cs50.ai/) can provide conceptual help with computer science concepts.

+ Further, the [rubber duck debugger](https://cs50.ai/) can help students write more efficient code.

+ Additionally, the [rubber duck debugger](https://cs50.ai/) can help when a student is stuck in one of their assignments. For example, students may encounter errors that prevent them from progressing in their assignments. When students hit a wall, they don’t have to wait for support staff to be available.

+ The [rubber duck debugger](https://cs50.ai/) does stipulate, however, that it is an AI and that it is experimental. Students should be conscious of the degree to which they blindly trust the AI. Consider the following image:

  ![rubber duck giving an answer with a disclaimer](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50AiLectureSlide060.png)

+ AI has an inhuman level of patience.

## Generative AI

+   AI has been with us for much time! Software has long adapted to users. Algorithms look for patterns in junk mail, images saved on your phone, and to play games.
+   In games, for example, step-by-step instructions may allow a computerized adversary play a game of Breakout.

## Decision Trees

+ *Decision trees* are used by an algorithm to decide what decision to make.

+ For example, in Breakout, an algorithm may consider what choice to make based on the instructions in the code:

  ```auto
  While game is ongoing:
  If ball is left of paddle:
    Move paddle left
  Else if ball is right of padding:
    Move paddle right
  Else:
    Don't move paddle
  ```

+ With most games, they attempt to minimize the number of calculations required to compete with the player.

## Minimax

+ You can imagine where an algorithm may score outcomes as positive, negative, and neutral.

+ In tic-tac-toe, the AI may consider a board where the computer wins as `1` and one where the computer loses as `-1`.

+ You can imagine how a computer may look at a decision tree of potential outcomes and assign scores to each potential move.

+ The computer will attempt to win by maximizing its own score.

+ In the context of tic-tac-toe, the algorithm may conceptualize this as follows:

  ```auto
  If player is X:
  For each possible move:
    Calculate score for board
  Choose move with highest score
  
  Else if player is O:
    For each possible move:
      Calculate score for board
    Choose move with lowest score
  ```

+ This could be pictured as follows:

  ![tictactoe with outcomes as 1 or -1 or 0](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50AiLectureSlide132.png)

+ Because computers are so powerful, they can crunch massive potential outcomes. However, the computers in our pockets or on our desks may not be able to calculate trillions of options. This is where machine learning can help.

## Machine Learning

+   Machine learning is a way by which a computer can learn through reinforcement.
+   A computer can learn how to flip a pancake.
+   A computer can learn how to play Mario.
+   A computer can learn how to play The Floor is Lava.
+   The computer repeats trial after trial after trial to discover what behaviors to repeat and those not to repeat.
+   Within much of AI-based algorithms, there are concepts of *explore vs. exploit*, where the AI may randomly try something that may not be considered optimal. Randomness can yield better outcomes.

## Deep Learning

+ *Deep learning* uses neural networks whereby problems and solutions are explored.

+ For example, deep learning may attempt to predict whether a blue or red dot will appear somewhere on a graph. Consider the following image:

  ![blue dots and red dots separated by a line](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50AiLectureSlide208.png)

+ Existing training data is used to predict an outcome. Further, more training data may be created by the AI to discover further patterns.

+ Deep learning creates nodes (pictured below), which associate inputs and outputs.

  ![Nodes connected to notes](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50AiLectureSlide210.png)

## Generative Artificial Intelligence

+   *Large language models* are massive models that make predictions based on huge amounts of training.
+   Just a few years ago, AI was not very good at completing and generating sentences.
+   The AI encodes words into *embeddings* to find relationships between words. Thus, through a huge amount of training, a massive neural network can predict the association between words - resulting in the ability for generative AI to generate content and even have conversations with users.
+   These technologies are what is behind our [rubber duck debugger](https://cs50.ai/).

## Summing Up

In this lesson, you learned about some of the technology behind our own [rubber duck debugger](https://cs50.ai/). Specifically, we discussed…

+   Image Generation
+   ChatGPT
+   Prompt Generation
+   CS50.ai
+   Generative AI
+   Decision Trees
+   Minimax
+   Machine Learning
+   Deep Learning
+   Generative Artificial Intelligence

This was CS50!




# Lecture 7-SQL

## 

+   [Welcome!](#welcome)
+   [Flat-File Database](#flat-file-database)
+   [Relational Databases](#relational-databases)
+   [Shows](#shows)
+   [`JOIN`s](#joins)
+   [Indexes](#indexes)
+   [Using SQL in Python](#using-sql-in-python)
+   [Race Conditions](#race-conditions)
+   [SQL Injection Attacks](#sql-injection-attacks)
+   [Summing Up](#summing-up)

## Welcome!

+   In previous weeks, we introduced you to Python, a high-level programming language that utilized the same building blocks we learned in C. However, we introduced this new language not for the purpose of learning “just another language.” Instead, we do so because some tools are better for some jobs and not so great for others!
+   This week, we will be continuing more syntax related to Python.
+   Further, we will be integrating this knowledge with data.
+   Finally, we will be discussing *SQL* or *Structured Query Language*.
+   Overall, one of the goals of this course is to learn to program generally – not simply how to program in the languages described in this course.

## Flat-File Database

+   As you have likely seen before, data can often be described in patterns of columns and rows.
+   Spreadsheets like those created in Microsoft Excel and Google Sheets can be outputted to a `csv` or *comma-separated values* file.
+   If you look at a `csv` file, you’ll notice that the file is flat in that all of our data is stored in a single table represented by a text file. We call this form of data a *flat-file database*.
+   Python comes with native support for `csv` files.
+   First, download [favorites.csv](https://cdn.cs50.net/2023/fall/lectures/7/src7/favorites/favorites.csv) and upload it to your file explorer inside [cs50.dev](https://cs50.dev/). Second, in your terminal window, type `code favorites.py` and write code as follows:
    
    ```auto
    # Prints all favorites in CSV using csv.reader
    
    import csv
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create reader
        reader = csv.reader(file)
    
        # Skip header row
        next(reader)
    
        # Iterate over CSV file, printing each favorite
        for row in reader:
            print(row[1])
    ```
    
    Notice that the `csv` library is imported. Further, we created a `reader` that will hold the result of `csv.reader(file)`. The `csv.reader` function reads each row from the file, and in our code we store the results in `reader`. `print(row[1])`, therefore, will print the language from the `favorites.csv` file.
    
+   You can improve your code as follows:
    
    ```auto
    # Stores favorite in a variable
    
    import csv
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create reader
        reader = csv.reader(file)
    
        # Skip header row
        next(reader)
    
        # Iterate over CSV file, printing each favorite
        for row in reader:
            favorite = row[1]
            print(favorite)
    ```
    
    Notice that `favorite` is stored and then printed. Also notice that we use the `next` function to skip to the next line of our reader.
    
+   One of the disadvantages of the above approach is that we are trusting that `row[1]` is always the favorite. However, what would happen if the columns have been moved around?
+   We can fix this potential issue. Python also allows you to index by the keys of a list. Modify your code as follows:
    
    ```auto
    # Prints all favorites in CSV using csv.DictReader
    
    import csv
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Iterate over CSV file, printing each favorite
        for row in reader:
            favorite = row["language"]
            print(favorite)
    ```
    
    Notice that this example directly utilizes the `language` key in the print statement.
    
+   This could be further simplified to:
    
    ```auto
    # Prints all favorites in CSV using csv.DictReader
    
    import csv
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Iterate over CSV file, printing each favorite
        for row in reader:
            print(row["language"])
    ```
    
+   To count the number of favorite languages expressed in the `csv` file, we can do the following:
    
    ```auto
    # Counts favorites using variables
    
    import csv
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Counts
        scratch, c, python = 0, 0, 0
    
        # Iterate over CSV file, counting favorites
        for row in reader:
            favorite = row["language"]
            if favorite == "Scratch":
                scratch += 1
            elif favorite == "C":
                c += 1
            elif favorite == "Python":
                python += 1
    
    # Print counts
    print(f"Scratch: {scratch}")
    print(f"C: {c}")
    print(f"Python: {python}")
    ```
    
    Notice that each language is counted using `if` statements. Further notice the double equal `==` signs in those `if` statements.
    
+   Python allows us to use a dictionary to count the `counts` of each language. Consider the following improvement upon our code:
    
    ```auto
    # Counts favorites using dictionary
    
    import csv
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Counts
        counts = {}
    
        # Iterate over CSV file, counting favorites
        for row in reader:
            favorite = row["language"]
            if favorite in counts:
                counts[favorite] += 1
            else:
                counts[favorite] = 1
    
    # Print counts
    for favorite in counts:
        print(f"{favorite}: {counts[favorite]}")
    ```
    
    Notice that the value in `counts` with the key `favorite` is incremented when it exists already. If it does not exist, we define `counts[favorite]` and set it to 1. Further, the formatted string has been improved to present the `counts[favorite]`.
    
+   Python also allows sorting `counts`. Improve your code as follows:
    
    ```auto
    # Sorts favorites by key
    
    import csv
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Counts
        counts = {}
    
        # Iterate over CSV file, counting favorites
        for row in reader:
            favorite = row["language"]
            if favorite in counts:
                counts[favorite] += 1
            else:
                counts[favorite] = 1
    
    # Print counts
    for favorite in sorted(counts):
        print(f"{favorite}: {counts[favorite]}")
    ```
    
    Notice the `sorted(counts)` at the bottom of the code.
    
+   If you look at the parameters for the `sorted` function in the Python documentation, you will find it has many built-in parameters. You can leverage some of these built-in parameters as follows:
    
    ```auto
    # Sorts favorites by value using .get
    
    import csv
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Counts
        counts = {}
    
        # Iterate over CSV file, counting favorites
        for row in reader:
            favorite = row["language"]
            if favorite in counts:
                counts[favorite] += 1
            else:
                counts[favorite] = 1
    
    # Print counts
    for favorite in sorted(counts, key=counts.get, reverse=True):
        print(f"{favorite}: {counts[favorite]}")
    ```
    
    Notice the arguments passed to `sorted`. The `key` argument allows you to tell Python the method you wish to use to sort items. In this case `counts.get` is used to sort by the values. `reverse=True` tells `sorted` to sort from largest to smallest.
    
+   Python has numerous libraries that we can utilize in our code. One of these libraries is `collections`, from which we can import `Counter`. `Counter` will allow you to access the counts of each language without the headaches of all the `if` statements seen in our previous code. You can implement as follows:
    
    ```auto
    # Sorts favorites by value using .get
    
    import csv
    
    from collections import Counter
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Counts
        counts = Counter()
    
        # Iterate over CSV file, counting favorites
        for row in reader:
            favorite = row["language"]
            counts[favorite] += 1
    
    # Print counts
    for favorite, count in counts.most_common():
        print(f"{favorite}: {count}")
    ```
    
    Notice how `counts = Counter()` enables the use of this imported `Counter` class from `collections`.
    
+   We can change the column we are examining, focusing on our favorite problem instead:
    
    ```auto
    # Favorite problem instead of favorite language
    
    import csv
    
    from collections import Counter
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Counts
        counts = Counter()
    
        # Iterate over CSV file, counting favorites
        for row in reader:
            favorite = row["problem"]
            counts[favorite] += 1
    
    # Print counts
    for favorite, count in counts.most_common():
        print(f"{favorite}: {count}")
    ```
    
    Notice that `problem` replaced `language`.
    
+   We can also get the count of the popularity of a specific problem in the course:
    
    ```auto
    # Gets a specific count
    
    import csv
    
    from collections import Counter
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Counts
        counts = Counter()
    
        # Iterate over CSV file, counting favorites
        for row in reader:
            favorite = row["problem"]
            counts[favorite] += 1
    
    # Print count
    favorite = input("Favorite: ")
    print(f"{favorite}: {counts[favorite]}")
    ```
    
    Notice how compact our code is compared to our experience in C.
    

## Relational Databases

+   Google, Twitter, and Meta all use relational databases to store their information at scale.
+   Relational databases store data in rows and columns in structures called *tables*.
+   SQL allows for four types of commands:
    
    ```auto
      Create
      Read
      Update
      Delete
    ```
    
+   These four operations are affectionately called *CRUD*.
+   We can create a SQL database at the terminal by typing `sqlite3 favorites.db`. Upon being prompted, we will agree that we want to create `favorites.db` by pressing `y`.
+   You will notice a different prompt as we are now inside a program called `sqlite3`.
+   We can put `sqlite3` into `csv` mode by typing `.mode csv`. Then, we can import our data from our `csv` file by typing `.import favorites.csv favorites`. It seems that nothing has happened!
+   We can type `.schema` to see the structure of the database.
+   You can read items from a table using the syntax `SELECT columns FROM table`.
+   For example, you can type `SELECT * FROM favorites;` which will iterate every row in `favorites`.
+   You can get a subset of the data using the command `SELECT language FROM favorites;`.
+   SQL supports many commands to access data, including:
    
    ```SQL
      AVG
      COUNT
      DISTINCT
      LOWER
      MAX
      MIN
      UPPER
    ```
    
+   For example, you can type `SELECT COUNT(language) FROM favorites;`. Further, you can type `SELECT DISTINCT(language) FROM favorites;` to get a list of the individual languages within the database. You could even type `SELECT COUNT(DISTINCT(language)) FROM favorites;` to get a count of those.
+   SQL offers additional commands we can utilize in our queries:
    
    ```auto
      WHERE       -- adding a Boolean expression to filter our data
      LIKE        -- filtering responses more loosely
      ORDER BY    -- ordering responses
      LIMIT       -- limiting the number of responses
      GROUP BY    -- grouping responses together
    ```
    
    Notice that we use `--` to write a comment in SQL.
    
+   For example, we can execute `SELECT COUNT(*) FROM favorites WHERE language = 'C';`. A count is presented.
+   Further, we could type `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem = 'Hello, World;`. Notice how the `AND` is utilized to narrow our results.
+   Similarly, we could execute `SELECT language, COUNT(*) FROM favorites GROUP BY language;`. This would offer a temporary table that would show the language and count.
+   We could improve this by typing `SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);`. This will order the resulting table by the `count`.
+   We can also `INSERT` into a SQL database utilizing the form `INSERT INTO table (column...) VALUES(value, ...);`.
+   We can execute `INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');`.
+   `DELETE` allows you to delete parts of your data. For example, you could `DELETE FROM favorites WHERE Timestamp IS NULL;`.
+   We can also utilize the `UPDATE` command to update your data.
+   For example, you can execute `UPDATE favorites SET language = 'SQL', problem = 'Fiftyville';`. This will result in overwriting all previous statements where C was the favorite programming language.
+   Notice that these queries have immense power. Accordingly, in the real-world setting, you should consider who has permissions to execute certain commands.

## Shows

+   We can imagine a database that we might want to create to catalog various TV shows. We could create a spreadsheet with columns like `title`, `star`, `star`, `star`, `star`, and more stars. A problem with this approach is this approach has a lot of wasted space. Some shows may have one star. Others may have dozens.
+   We could separate our database into multiple sheets. We could have a `shows` sheet and a `people` sheet. On the `people` sheet, each person could have a unique `id`. On the `shows` sheet, each show could have a unique `id` too. On a third sheet called `stars` we could relate how each show has people for each show by having a `show_id` and `person_id`. While this is an improvement, this is not an ideal database.
+   IMDb offers a database of people, shows, writers, stars, genres, and ratings. Each of these tables is related to one another as follows:
    
    ![six boxes that represent various sql tables arrows are drawn to each showing their many relationships with one another](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week7Slide025.png "imdb relationships")
    
+   After downloading [`shows.db`](https://github.com/cs50/lectures/blob/2022/fall/7/src7/imdb/shows.db), you can execute `sqlite3 shows.db` in your terminal window.
+   Let’s zero in on the relationship between two tables within the database called `shows` and `ratings`. The relationship between these two tables can be illustrated as follows:
    
    ![two boxes one called shows and the other called ratings](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week7Slide032.png "imdb shows and ratings")
    
+   To illustrate the relationship between these tables, we could execute the following command: `SELECT * FROM ratings LIMIT 10;`. Examining the output, we could execute `SELECT * FROM shows LIMIT 10;`.
+   To understand the database, upon executing `.schema` you will find not only each of the tables but the individual fields inside each of these fields.
+   As you can see, `shows` has an `id` field. The `genres` table has a `show_id` field which has data that is common between it and the `shows` table.
+   Further, `show_id` exists in all of the tables. In the `shows` table, it is simply called `id`. This common field between all the fields is called a *key*. Primary keys are used to identify a unique record in a table. *Foreign keys* are used to build relationships between tables by pointing to the primary key in another table.
+   By storing data in a relational database, as above, data can be more efficiently stored.
+   In *sqlite*, we have five datatypes, including:
    
    ```auto
      BLOB       -- binary large objects that are groups of ones and zeros
      INTEGER    -- an integer
      NUMERIC    -- for numbers that are formatted specially like dates
      REAL       -- like a float
      TEXT       -- for strings and the like
    ```
    
+   Additionally, columns can be set to add special constraints:
    
+   We could execute `SELECT * FROM stars LIMIT 10;`. `show_id` is a foreign key in this final query because `show_id` corresponds to the unique `id` field in `shows`. `person_id` corresponds to the unique `id` field in the `people` column.
+   We can further play with this data to understand these relationships. Execute `SELECT * FROM ratings;`. There are a lot of ratings!
+   We can further limit this data down by executing `SELECT show_id FROM ratings WHERE rating >= 6.0 LIMIT 10;`. From this query, you can see that there are 10 shows presented. However, we don’t know what show each `show_id` represents.
+   You can discover what shows these are by executing `SELECT * FROM shows WHERE id = 626124;`
+   We can further our query to be more efficient by executing:
    
    ```auto
    SELECT title
    FROM shows
    WHERE id IN (
        SELECT show_id
        FROM ratings
        WHERE rating >= 6.0
        LIMIT 10
    )
    ```
    
    Notice that this query nests together two queries. An inner query is used by an outer query.
    

## `JOIN`s

+   We are pulling data from `shows` and `ratings`.
+   How could we combine tables temporarily? Tables could be joined together using the `JOIN` command.
+   Execute the following command:
    
    ```auto
    SELECT * FROM shows
      JOIN ratings on shows.id = ratings.show_id
      WHERE rating >= 6.0
      LIMIT 10;
    ```
    
    Notice this results in a wider table than we have previously seen.
    
+   Where the previous queries have illustrated the *one-to-one* relationship between these keys, let’s examine some *one-to-many* relationships. Focusing on the `genres` table, execute the following:
    
    ```auto
    SELECT * FROM genres
    LIMIT 10;
    ```
    
    Notice how this provides us a sense of the raw data. You might notice that one shows have three values. This is a one-to-many relationship.
    
+   We can learn more about the `genres` table by typing `.schema genres`.
+   Execute the following command to learn more about the various comedies in the database:
    
    ```auto
    SELECT title FROM shows
    WHERE id IN (
      SELECT show_id FROM genres
      WHERE genre = 'Comedy'
      LIMIT 10
    );
    ```
    
    Notice how this produces a list of comedies, including *Catweazle*.
    
+   To learn more about Catweazle, by joining various tables through a join:
    
    ```auto
    SELECT * FROM shows
    JOIN genres
    ON shows.id = genres.show_id
    WHERE id = 63881;
    ```
    
    Notice that this results in a temporary table. It is fine to have duplicate table.
    
+   A final relationship is a *many-to-many* relationship.
+   We can learn more about the show *The Office* by executing the following command:
    
    ```auto
    SELECT person_id FROM stars
    WHERE show_id = (
      SELECT id FROM shows
      WHERE title = 'The Office' AND year = 2005
    );
    ```
    
    Notice that this results in a table that includes the `person_id`s of various stars.
    
+   I could learn more about this group of actors by executing the following:
    
    ```auto
    SELECT name FROM people
    WHERE id IN (
        SELECT person_id FROM stars
        WHERE show_id = (
          SELECT id FROM shows
          WHERE title = 'The Office' AND year = 2005
        )
    );
    ```
    
    This results in a top-billed stars.
    
+   We can further understand this data by executing:
    
    ```auto
    SELECT title from shows
    WHERE id IN (
      SELECT show_id FROM stars
      WHERE person_id = (
        SELECT id FROM people
        WHERE name = 'Steve Carell'
      )
    );
    ```
    
    This results in a list of titles of shows wherein Steve Carell stared.
    
+   The wildcard `%` operator can be used to find all people whose names start with `Steve C` one could employ the syntax `SELECT * FROM people WHERE name LIKE 'Steve C%';`.

## Indexes

+   While relational databases have the ability to be more fast and more robust than utilizing a `CSV` file, data can be optimized within a table using *indexes*.
+   Indexes can be utilized to speed up our queries.
+   We can track the speed of our queries by executing `.timer on` in `sqlite3`.
+   To understand how indexes can speed up our queries, run the following: `SELECT * FROM shows WHERE title = 'The Office';` Notice the time that displays after the query executes.
+   Then, we can create an index with the syntax `CREATE INDEX title_index on shows (title);`. This tells `sqlite3` to create an index and perform some special under-the-hood optimization relating to this column `title`.
+   This will create a data structure called a *B Tree*, a data structure that looks similar to a binary tree. However, unlike a binary tree, there can be more than two child notes.
    
    ![one node at the top from which come four children and below that there are three children coming from one of the nodes and two from another two from another and three from another](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week7Slide039.png "b tree")
    
+   Running the query `SELECT * FROM shows WHERE title = 'The Office';`, you will notice that the query runs much more quickly!
+   Unfortunately, indexing all columns would result in utilizing more storage space. Therefore, there is a tradeoff for enhanced speed.

## Using SQL in Python

+   To assist in working with SQL in this course, the CS50 Library can be utilized as follows in your code:
    
+   Similar to previous uses of the CS50 Library, this library will assist with the complicated steps of utilizing SQL within your Python code.
+   You can read more about the CS50 Library’s SQL functionality in the [documentation](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL).
+   Recall where we last left off in `favorites.py`. Your code should appear as follows:
    
    ```auto
    # Gets a specific count
    
    import csv
    
    from collections import Counter
    
    # Open CSV file
    with open("favorites.csv", "r") as file:
    
        # Create DictReader
        reader = csv.DictReader(file)
    
        # Counts
        counts = Counter()
    
        # Iterate over CSV file, counting favorites
        for row in reader:
            favorite = row["problem"]
            counts[favorite] += 1
    
    # Print count
    favorite = input("Favorite: ")
    print(f"{favorite}: {counts[favorite]}")
    ```
    
    Notice how this code is exactly as we left it prior.
    
+   Modify your code as follows:
    
    ```auto
    # Searches database popularity of a problem
    
    import csv
    
    from cs50 import SQL
    
    # Open database
    db = SQL("sqlite:///favorites.db")
    
    # Prompt user for favorite
    favorite = input("Favorite: ")
    
    # Search for title
    rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem LIKE ?", favorite)
    
    # Get first (and only) row
    row = rows[0]
    
    # Print popularity
    print(row["n"])
    ```
    
    Notice that `db = SQL("sqlite:///favorites.db")` provide Python the location of the database file. Then, the line that begins with `rows` executes SQL commands utilizing `db.execute`. Indeed, this command passes the syntax within the quotation marks to the `db.execute` function. We can issue any SQL command using this syntax. Further, notice that `rows` is returned as a list of dictionaries. In this case, there is only one result, one row, returned to the rows list as a dictionary.
    

## Race Conditions

+   Utilization of SQL can sometimes result in some problems.
+   You can imagine a case where multiple users could be accessing the same database and executing commands at the same time.
+   This could result in glitches where code is interrupted by other people’s actions. This could result in a loss of data.
+   Built-in SQL features such as `BEGIN TRANSACTION`, `COMMIT`, and `ROLLBACK` help avoid some of these race condition problems.

## SQL Injection Attacks

+   Now, still considering the code above, you might be wondering what the `?` question marks do above. One of the problems that can arise in real-world applications of SQL is what is called an *injection attack*. An injection attack is where a malicious actor could input malicious SQL code.
+   For example, consider a login screen as follows:
    
    ![harvard key login screen with username and password fields](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week7Slide051-20240811153308167.png "harvard key login screen")
    
+   Without the proper protections in our own code, a bad actor could run malicious code. Consider the following:
    
    ```auto
    rows = db.execute("SELECT COUNT(*) FROM users WHERE username = ? AND password = ?", username, password)
    ```
    
    Notice that because the `?` is in place, validation can be run on `favorite` before it is blindly accepted by the query.
    
+   You never want to utilize formatted strings in queries as above or blindly trust the user’s input.
+   Utilizing the CS50 Library, the library will *sanitize* and remove any potentially malicious characters.

## Summing Up

In this lesson, you learned more syntax related to Python. Further, you learned how to integrate this knowledge with data in the form of flat-file and relational databases. Finally, you learned about *SQL*. Specifically, we discussed…

+   Flat-file databases
+   Relational databases
+   SQL
+   Primary and foreign keys
+   `JOIN`s
+   Indexes
+   Using SQL in Python
+   Race conditions
+   SQL injection attacks

See you next time!


# Lecture 8-Html&CSS

## 

+   [Welcome!](#welcome)
+   [Routers](#routers)
+   [DNS](#dns)
+   [HTTP](#http)
+   [HTML](#html)
+   [Regular Expressions](#regular-expressions)
+   [CSS](#css)
+   [Frameworks](#frameworks)
+   [JavaScript](#javascript)
+   [Summing Up](#summing-up)

## Welcome!

+   In previous weeks, we introduced you to Python, a high-level programming language that utilized the same building blocks we learned in C. Today, we will extend those building blocks further in HTML, CSS, and JavaScript.
+   The internet is a technology that we all use.
+   Using our skills from previous weeks, we can build our own web pages and applications.
+   The *ARPANET* connected the first points on the internet to one another.
+   Dots between two points could be considered *routers*.

## Routers

+   To route data from one place to another, we need to make *routing decisions*. That is, someone needs to program how data is transferred from point A to point B.
+   You can imagine how data could take multiple paths from point A and point B, such that when a router is congested, data can flow through another path. *Packets* of data are transferred from one router to another, from one computer to another.
+   *TCP/IP* are two protocols that allow computers to transfer data between them over the internet.
+   *IP* or *internet protocol* is a way by which computers can identify one another across the internet. Every computer has a unique address in the world. Addresses are in this form:
    
+   Numbers range from `0` to `255`. IP addresses are 32-bits, meaning that these addresses could accommodate over 4 billion addresses. Newer versions of IP addresse, implementing 128-bits, can accommodate far more computers!
+   In the real world, servers do a lot of work for us.
+   Packets are structured as follows:
    
    ![ascii art of a packet](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week8Slide014.png "packets")
    
+   Packets are standardized. The source and destination are held within each packet.
+   *TCP*, or transmission control protocol, is used to distinguish web services from one another. For example, `80` is used to denote HTTP and `443` is used to denote HTTPS. These numbers are *port numbers*.
+   When information is sent from one location to another, a source IP address, a destination IP address, and TCP port number are sent.
+   These protocols are also used to fragment large files into multiple parts or packets. For example, a large photo of a cat can be sent in multiple packets. When a packet is lost, TCP/IP can request missing packets again from the origin server.
+   TCP will acknowledge when all the data has been transmitted and received.

## DNS

+   It would be very tedious if you needed to remember an IP address to visit a website.
+   *DNS*, or *domain name systems*, is a collection of servers on the internet that are used to route website addresses like *harvard.edu* to a specific IP address.
+   DNS simply hold a table or database that links specific, fully qualified domain names to specific IP addresses.

## HTTP

+   *HTTP* or *hypertext transfer protocol* is an application-level protocol that developers use to build powerful and useful things through the transferring of data from one place to another.
+   When you see an address such as `https://www.example.com` you are actually implicitly visiting that address with a `/` at the end of it.
+   The *path* is what exists after that slash. For example, `https://www.example.com/folder/file.html` visits `example.com` and browses to the `folder` folder and then visits the file named `file.html`.
+   The `.com` is called a *top-level domain* that is used to denote the location or type of organization associated with this address.
+   `https` in this address is the protocol that is used to connect to that web address. By protocol, we mean that HTTP utilizes `GET` or `POST` *requests* to ask for information from a server. For example, you can launch Google Chrome, right-click, and click `inspect`. When you open the `developer tools` and visit `Network`, selecting `Preserve log`, you will see `Request Headers`. You’ll see mentions of `GET`. This is possible in other browsers as well, using slightly different methods.
+   For example, when issuing a GET request, your computer may send the following to a server:
    
    ```auto
      GET / HTTP/2
      Host: www.harvard.edu
    ```
    
    Notice that this requests via HTTP the content served on www.harvard.edu
    
+   Generally, after making a request a server, you will receive the following in `Response Headers`:
    
    ```auto
      HTTP/2 200
      Content-Type: text/html
    ```
    
+   This approach to inspecting these logs may be a bit more complicated than need be. You can analyze the work of HTTP protocols at [cs50.dev](https://cs50.dev/). For example, type the following in your terminal window:
    
    ```auto
      curl -I https://www.harvard.edu/
    ```
    
    Notice that the output of this command returns all the header values of the responses of the server.
    
+   Via developer tools in your web browser, you can see all the HTTP requests when browsing to the above website.
+   Further, execute the following command in your terminal window:
    
    ```auto
      curl -I https://harvard.edu
    ```
    
    Notice that you will see a `301` response, providing a hint to a browser of where it can find the correct website.
    
+   Similarly, execute the following in your terminal window:
    
    ```auto
      curl -I http://www.harvard.edu/
    ```
    
    Notice that the `s` in `https` has been removed. The server response will show that the response is `301`, meaning that the website has permanently moved.
    
+   Similar to `301`, a code of `404` means that a specified URL has not been found. There are numerous other response codes, such as:
    
    ```auto
      200 OK
      301 Moved Permanently
      302 Found
      304 Not Modified
      304 Temporary Redirect
      401 Unauthorized
      403 Forbidden
      404 Not Found
      418 I'm a Teapot
      500 Internal Server Error
      503 Service Unavailable
    ```
    
+   It’s worth mentioning that `500` errors are always your fault as the developer. This will be especially important for next week’s problem set, and potentially for your final project!

## HTML

+   *HTML* or *hypertext markup language* is made up of *tags*, each of which may have some *attributes* that describe it.
+   In your terminal, type `code hello.html` and write code as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates HTML -->
    
    <html lang="en">
        <head>
            <title>hello, title</title>
        </head>
        <body>
            hello, body
        </body>
    </html>
    ```
    
    Notice that the `html` tag both opens and closes this file. Further, notice the `lang` attribute, which modifies the behavior of the `html` tag. Also, notice that there are both `head` tags and `body` tags. Indentation is not required but does suggest a hierarchy.
    
+   You can serve your code by typing `http-server`. This serve is now available on a very long URL. If you click it, you can visit the website with your own code.
+   When you visit this URL, notice that the file name `hello.html` appears at the end of this URL. Further, notice, based upon the URL, that the server is serving via port 8080.
+   The hierarchy of tags can be represented as follows:
    
    ![html code next to a hierarchy showing parent and child nodes](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week8Slide065.png "DOM")
    
+   Knowledge of this hierarchy will be useful later as we learn JavaScript.
+   The browser will read your HTML file top to bottom and left to right.
+   Because whitespace and indentation is effectively ignored in HTML, you will need to use `<p>` paragraph tags to open and close a paragraph. Consider the following:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates paragraphs -->
    
    <html lang="en">
        <head>
            <title>paragraphs</title>
        </head>
        <body>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
            </p>
            <p>
                Mauris ut dui in eros semper hendrerit. Morbi vel elit mi. Sed sit amet ex non quam dignissim dignissim et vel arcu. Pellentesque eget elementum orci. Morbi ac cursus ex. Pellentesque quis turpis blandit orci dapibus semper sed non nunc. Nulla et dolor nec lacus finibus volutpat. Sed non lorem diam. Donec feugiat interdum interdum. Vivamus et justo in enim blandit fermentum vel at elit. Phasellus eu ante vitae ligula varius aliquet. Etiam id posuere nibh.
            </p>
            <p>
                Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet. Nunc egestas sem quis nisl mattis semper. Pellentesque ut magna congue lorem eleifend sodales. Donec tortor tortor, aliquam vitae mollis sed, interdum ut lectus. Mauris non purus quis ipsum lacinia tincidunt.
            </p>
            <p>
                Integer at justo lacinia libero blandit aliquam ut ut dui. Quisque tincidunt facilisis venenatis. Nullam dictum odio quis lorem luctus, vel malesuada dolor luctus. Aenean placerat faucibus enim a facilisis. Maecenas eleifend quis massa sed eleifend. Ut ultricies, dui ac vulputate hendrerit, ex metus iaculis diam, vitae fermentum libero dui et ante. Phasellus suscipit, arcu ut consequat sagittis, massa urna accumsan massa, eu aliquet nulla lorem vitae arcu. Pellentesque rutrum felis et metus porta semper. Nam ac consectetur mauris.
            </p>
            <p>
                Suspendisse rutrum vestibulum odio, sed venenatis purus condimentum sed. Morbi ornare tincidunt augue eu auctor. Vivamus sagittis ac lectus at aliquet. Nulla urna mauris, interdum non nibh in, vehicula porta enim. Donec et posuere sapien. Pellentesque ultrices scelerisque ipsum, vel fermentum nibh tincidunt et. Proin gravida porta ipsum nec scelerisque. Vestibulum fringilla erat at turpis laoreet, nec hendrerit nisi scelerisque.
            </p>
            <p>
                Sed quis malesuada mi. Nam id purus quis augue sagittis pharetra. Nulla facilisi. Maecenas vel fringilla ante. Cras tristique, arcu sit amet blandit auctor, urna elit ultricies lacus, a malesuada eros dui id massa. Aliquam sem odio, pretium vel cursus eget, scelerisque at urna. Vestibulum posuere a turpis consectetur consectetur. Cras consequat, risus quis tempor egestas, nulla ipsum ornare erat, nec accumsan nibh lorem nec risus. Integer at iaculis lacus. Integer congue nunc massa, quis molestie felis pellentesque vestibulum. Nulla odio tortor, aliquam nec quam in, ornare aliquet sapien.
            </p>
        </body>
    </html>
    ```
    
    Notice that paragraphs start with a `<p>` tag and end with a `</p>` tag.
    
+   HTML allows for the representation of headings:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates headings (for chapters, sections, subsections, etc.) -->
    
    <html lang="en">
    
        <head>
            <title>headings</title>
        </head>
    
        <body>
    
            <h1>One</h1>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
            </p>
    
            <h2>Two</h2>
            <p>
                Mauris ut dui in eros semper hendrerit. Morbi vel elit mi. Sed sit amet ex non quam dignissim dignissim et vel arcu. Pellentesque eget elementum orci. Morbi ac cursus ex. Pellentesque quis turpis blandit orci dapibus semper sed non nunc. Nulla et dolor nec lacus finibus volutpat. Sed non lorem diam. Donec feugiat interdum interdum. Vivamus et justo in enim blandit fermentum vel at elit. Phasellus eu ante vitae ligula varius aliquet. Etiam id posuere nibh.
            </p>
    
            <h3>Three</h3>
            <p>
                Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet. Nunc egestas sem quis nisl mattis semper. Pellentesque ut magna congue lorem eleifend sodales. Donec tortor tortor, aliquam vitae mollis sed, interdum ut lectus. Mauris non purus quis ipsum lacinia tincidunt.
            </p>
    
            <h4>Four</h4>
            <p>
                Integer at justo lacinia libero blandit aliquam ut ut dui. Quisque tincidunt facilisis venenatis. Nullam dictum odio quis lorem luctus, vel malesuada dolor luctus. Aenean placerat faucibus enim a facilisis. Maecenas eleifend quis massa sed eleifend. Ut ultricies, dui ac vulputate hendrerit, ex metus iaculis diam, vitae fermentum libero dui et ante. Phasellus suscipit, arcu ut consequat sagittis, massa urna accumsan massa, eu aliquet nulla lorem vitae arcu. Pellentesque rutrum felis et metus porta semper. Nam ac consectetur mauris.
            </p>
    
            <h5>Five</h5>
            <p>
                Suspendisse rutrum vestibulum odio, sed venenatis purus condimentum sed. Morbi ornare tincidunt augue eu auctor. Vivamus sagittis ac lectus at aliquet. Nulla urna mauris, interdum non nibh in, vehicula porta enim. Donec et posuere sapien. Pellentesque ultrices scelerisque ipsum, vel fermentum nibh tincidunt et. Proin gravida porta ipsum nec scelerisque. Vestibulum fringilla erat at turpis laoreet, nec hendrerit nisi scelerisque.
            </p>
    
            <h6>Six</h6>
            <p>
                Sed quis malesuada mi. Nam id purus quis augue sagittis pharetra. Nulla facilisi. Maecenas vel fringilla ante. Cras tristique, arcu sit amet blandit auctor, urna elit ultricies lacus, a malesuada eros dui id massa. Aliquam sem odio, pretium vel cursus eget, scelerisque at urna. Vestibulum posuere a turpis consectetur consectetur. Cras consequat, risus quis tempor egestas, nulla ipsum ornare erat, nec accumsan nibh lorem nec risus. Integer at iaculis lacus. Integer congue nunc massa, quis molestie felis pellentesque vestibulum. Nulla odio tortor, aliquam nec quam in, ornare aliquet sapien.
            </p>
    
        </body>
    
    </html>
    ```
    
    Notice that `<h1>`, `<h2>`, and `<h3>` denote different levels of headings.
    
+   We can also create unordered lists within HTML:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates (ordered) lists -->
    
    <html lang="en">
        <head>
            <title>list</title>
        </head>
        <body>
            <ul>
                <li>foo</li>
                <li>bar</li>
                <li>baz</li>
            </ul>
        </body>
    </html>
    ```
    
    Notice that the `<ul>` tag creates an unordered list containing three items.
    
+   We can also create ordered lists within HTML:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates (ordered) lists -->
    
    <html lang="en">
        <head>
            <title>list</title>
        </head>
        <body>
            <ol>
                <li>foo</li>
                <li>bar</li>
                <li>baz</li>
            </ol>
        </body>
    </html>
    ```
    
    Notice that the `<ol>` tag creates an ordered list containing three items.
    
+   We can also create a table in HTML:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates table -->
    
    <html lang="en">
        <head>
            <title>table</title>
        </head>
        <body>
            <table>
                <tr>
                    <td>1</td>
                    <td>2</td>
                    <td>3</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>5</td>
                    <td>6</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>8</td>
                    <td>9</td>
                </tr>
                <tr>
                    <td>*</td>
                    <td>0</td>
                    <td>#</td>
                </tr>
            </table>
        </body>
    </html>
    ```
    
    Tables also have tags that open and close each element within. Also, notice the syntax for comments in HTML.
    
+   Images can also be utilized within HTML:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates image -->
    
    <html lang="en">
        <head>
            <title>image</title>
        </head>
        <body>
            <img alt="photo of bridge" src="bridge.png">
        </body>
    </html>
    ```
    
    Notice that `src="bridge.png"` indicates the path where the image file can be located.
    
+   Videos can also be included in HTML:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates video -->
    
    <html lang="en">
        <head>
            <title>video</title>
        </head>
        <body>
            <video controls muted>
                <source src="video.mp4" type="video/mp4">
            </video>
        </body>
    </html>
    ```
    
    Notice that the `type` attribute designates that this is a video of type `mp4`. Further, notice how `controls` and `muted` are passed to `video`.
    
+   You can also link between various web pages:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates link -->
    
    <html lang="en">
        <head>
            <title>link</title>
        </head>
        <body>
           Visit <a href="https://www.harvard.edu">Harvard</a>.
        </body>
    </html>
    ```
    
    Notice that the `<a>` or *anchor* tag is used to make `Harvard` a linkable text.
    
+   Meta tags are used to hold information about the data within the HTML file. Consider the following:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates responsive design -->
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>meta</title>
        </head>
        <body>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
        </body>
    </html>
    ```
    
    Notice this set of `meta` attributes makes this page mobile-friendly.
    
+   There are numerous `meta` key-value pairs that you can use:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates Open Graph tags -->
    
    <html lang="en">
        <head>
            <meta property="og:title" content="CS50">
            <meta property="og:description" content="Introduction to the intellectual enterprises of computer science and the art of programming.">
            <meta property="og:image" content="cat.jpg">
            <title>meta</title>
        </head>
        <body>
            ...
        </body>
    </html>
    ```
    
    Notice that these key value pairs relate to the `title` and `description` of the web page.
    
+   You can also create forms reminiscent of Google’s search:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates form -->
    
    <html lang="en">
        <head>
            <title>search</title>
        </head>
        <body>
            <form action="https://www.google.com/search" method="get">
                <input name="q" type="search">
                <input type="submit" value="Google Search">
            </form>
        </body>
    </html>
    ```
    
    Notice that a `form` tag opens and provides the attribute of what `action` it will take. The `input` field is included, passing the name `q` and the type as `search`.
    
+   We can make this search better as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates additional form attributes -->
    
    <html lang="en">
        <head>
            <title>search</title>
        </head>
        <body>
            <form action="https://www.google.com/search" method="get">
                <input autocomplete="off" autofocus name="q" placeholder="Query" type="search">
                <button>Google Search</button>
            </form>
        </body>
    </html>
    ```
    
    Notice that `autocomplete` is turned `off`. `autofocus` is enabled.
    
+   We’ve seen just a few of many HTML elements you can add to your site. If you have an idea for something to add to your site that we haven’t seen yet (a button, an audio file, etc.) try Googling “X in HTML” to find the right syntax! Similarly, you can use [cs50.ai](https://cs50.ai/) to help you discover more HTML features!

## Regular Expressions

+   *Regular expressions* or *regexes* are a means by which to ensure that user-provided data fits a specific format.
+   We can impelement our own registration page that utilizes regexes as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates type="email" -->
    
    <html lang="en">
        <head>
            <title>register</title>
        </head>
        <body>
            <form>
                <input autocomplete="off" autofocus name="email" placeholder="Email" type="email">
                <button>Register</button>
            </form>
        </body>
    </html>
    ```
    
    Notice that the `input` tag includes attributes that designate that this is of type `email`. The browser knows to double-check that input is an email address.
    
+   While the browser uses these built-in attributes to check for an email address, we can add a `pattern` attribute to ensure that only specific data ends up in the email address:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates pattern attribute -->
    
    <html lang="en">
        <head>
            <title>register</title>
        </head>
        <body>
            <form>
                <input autocomplete="off" autofocus name="email" pattern=".+@.+\.edu" placeholder="Email" type="email">
                <button>Register</button>
            </form>
        </body>
    </html>
    ```
    
    Notice that the `pattern` attribute is handed a regular expression to denote that the email address must include an `@` symbol and a `.edu`.
    
+   You can learn more about regular expressions from [Mozilla’s documentation](https://cs50.harvard.edu/x/2024/notes/8/developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions). Further, you can make inquiries to [cs50.ai](https://cs50.ai/) for hints.

## CSS

+   `CSS`, or *cascading style sheet*, is a markup language that allows you to fine-tune the aesthetics of your HTML files.
+   CSS is filled with *properties*, which include key-value pairs.
+   In your terminal, type `code home.html` and write code as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates inline CSS with P tags -->
    
    <html lang="en">
        <head>
            <title>css</title>
        </head>
        <body>
            <p style="font-size: large; text-align: center;">
                John Harvard
            </p>
            <p style="font-size: medium; text-align: center;">
                Welcome to my home page!
            </p>
            <p style="font-size: small; text-align: center;">
                Copyright &#169; John Harvard
            </p>
        </body>
    </html>
    ```
    
    Notice that some `style` attributes are provided to the `<p>` tags. The `font-size` is set to `large`, `medium`, or `small`. Then `text-align` is set to center.
    
+   While correct, the above is not well-designed. We can remove redundancy by modifying our code as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Removes outer DIV -->
    
    <html lang="en">
        <head>
            <title>css</title>
        </head>
        <body style="text-align: center">
            <div style="font-size: large">
                John Harvard
            </div>
            <div style="font-size: medium">
                Welcome to my home page!
            </div>
            <div style="font-size: small">
                Copyright &#169; John Harvard
            </div>
        </body>
    </html>
    ```
    
    Notice that `<div>` tags are used to divide up this HTML file into specific regions. `text-align: center` is invoked on the entire body of the HTML. Because everything inside `body` is a child of `body`, the `center` attribute cascades down to those children.
    
+   It turns out that there are newer semantic tags that are included in HTML. We can modify our code as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Uses semantic tags instead of DIVs -->
    
    <html lang="en">
        <head>
            <title>css</title>
        </head>
        <body style="text-align: center">
            <header style="font-size: large">
                John Harvard
            </header>
            <main style="font-size: medium">
                Welcome to my home page!
            </main>
            <footer style="font-size: small">
                Copyright &#169; John Harvard
            </footer>
        </body>
    </html>
    ```
    
    Notice that the `header` and `footer` both have different styles assigned to them.
    
+   This practice of placing the style and information all in the same location is not good practice. We could move the elements of style to the top of the file as follows:
    
    ```auto
    <!-- Demonstrates class selectors -->
    
    <html lang="en">
        <head>
            <style>
    
                .centered
                {
                    text-align: center;
                }
    
                .large
                {
                    font-size: large;
                }
    
                .medium
                {
                    font-size: medium;
                }
    
                .small
                {
                    font-size: small;
                }
    
            </style>
            <title>css</title>
        </head>
        <body class="centered">
            <header class="large">
                John Harvard
            </header>
            <main class="medium">
                Welcome to my home page!
            </main>
            <footer class="small">
                Copyright &#169; John Harvard
            </footer>
        </body>
    </html>
    ```
    
    Notice all the style tags are placed up in the `head` in the `style` tag wrapper. Also notice that we’ve assigned *classes*, called `centered`, `large`, `medium`, and `small` to our elements, and that we select those classes by placing a dot before the name, as in `.centered`
    
+   It turns out that we can move all our style code into a special file called a *CSS* file. We can create a file called `style.css` and paste our classes there:
    
    ```auto
    .centered
    {
        text-align: center;
    }
    
    .large
    {
        font-size: large;
    }
    
    .medium
    {
        font-size: medium;
    }
    
    .small
    {
        font-size: small;
    }
    ```
    
    Notice that this is verbatim what appeared in our HTML file.
    
+   We then can tell the browser where to locate the CSS for this HTML file:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates external stylesheets -->
    
    <html lang="en">
        <head>
            <link href="style.css" rel="stylesheet">
            <title>css</title>
        </head>
        <body class="centered">
            <header class="large">
                John Harvard
            </header>
            <main class="medium">
                Welcome to my home page!
            </main>
            <footer class="small">
                Copyright &#169; John Harvard
            </footer>
        </body>
    </html>
    ```
    
    Notice that `style.css` is linked to this HTML file as a stylesheet, telling the browser where to locate the styles we created.
    

## Frameworks

+   Similar to third-party libraries we can leverage in Python, there are third-party libraries called *frameworks* that we can utilize with our HTML files.
+   *Bootstrap* is one of these frameworks that we can use to beautify our HTML and easily perfect design elements such that our pages are more readable.
+   Bootstrap can be utilized by adding the following `link` tag in the `head` of your html file:
    
    ```auto
    <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <title>favorites</title>
    </head>
    ```
    
+   Consider the following HTML:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates table -->
    
    <html lang="en">
        <head>
            <title>phonebook</title>
        </head>
        <body>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Number</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Carter</td>
                        <td>+1-617-495-1000</td>
                    </tr>
                    <tr>
                        <td>David</td>
                        <td>+1-617-495-1000</td>
                    </tr>
                    <tr>
                        <td>John</td>
                        <td>+1-949-468-2750</td>
                    </tr>
                </tbody>
            </table>
        </body>
    </html>
    ```
    
    Notice how when looking at a served version of this page, it’s quite plain.
    
+   Now consider the following HTML that implements the use of Bootstrap:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates table with Bootstrap -->
    
    <html lang="en">
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <title>phonebook</title>
        </head>
        <body>
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Number</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Carter</td>
                        <td>+1-617-495-1000</td>
                    </tr>
                    <tr>
                        <td>David</td>
                        <td>+1-949-468-2750</td>
                    </tr>
                </tbody>
            </table>
        </body>
    </html>
    ```
    
    Notice how much prettier this website is now.
    
+   Similarly, consider to the following expansion of our search page created earlier:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates layout with Bootstrap -->
    
    <html lang="en">
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <title>search</title>
        </head>
        <body>
    
            <div class="container-fluid">
    
                <ul class="m-3 nav">
                    <li class="nav-item">
                        <a class="nav-link text-dark" href="https://about.google/">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-dark" href="https://store.google.com/">Store</a>
                    </li>
                    <li class="nav-item ms-auto">
                        <a class="nav-link text-dark" href="https://www.google.com/gmail/">Gmail</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-dark" href="https://www.google.com/imghp">Images</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-dark" href="https://www.google.com/intl/en/about/products">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-grid-3x3-gap-fill" viewBox="0 0 16 16">
                                <path d="M1 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2zM1 7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V7zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V7zM1 12a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1v-2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-2z"/>
                            </svg>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="btn btn-primary" href="https://accounts.google.com/ServiceLogin" role="button">Sign in</a>
                    </li>
                </ul>
    
                <div class="text-center">
    
                    <!-- https://knowyourmeme.com/memes/happy-cat -->
                    <img alt="Happy Cat" class="img-fluid w-25" src="cat.gif">
    
                    <form action="https://www.google.com/search" class="mt-4" method="get">
                        <input autocomplete="off" autofocus class="form-control form-control-lg mb-4 mx-auto w-50" name="q" placeholder="Query" type="search">
                        <button class="btn btn-light">Google Search</button>
                        <button class="btn btn-light" name="btnI">I'm Feeling Lucky</button>
                    </form>
    
                </div>
    
            </div>
    
        </body>
    </html>
    ```
    
    This version of the page is exceedingly stylized, thanks to Bootstrap.
    
+   You can learn more about this in the [Bootstrap Documentation](https://getbootstrap.com/docs/).

## JavaScript

+   JavaScript is another programming language that allows for interactivity within web pages.
+   Consider the following implemntation of `hello.html` that includes both JavaScript and HTML:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates onsubmit -->
    
    <html lang="en">
        <head>
            <script>
    
                function greet()
                {
                    alert('hello, ' + document.querySelector('#name').value);
                }
    
            </script>
            <title>hello</title>
        </head>
        <body>
            <form onsubmit="greet(); return false;">
                <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
                <input type="submit">
            </form>
        </body>
    </html>
    ```
    
    Notice how this form uses an `onsubmit` property to trigger a `script` found at the top of the file. The script uses `alert` to create an alert pop-up. `#name.value` goes to the textbox on the page and obtains the value typed by the user.
    
+   Generally, it’s considered bad design to mix onsubmit and JavaScript. We can advance our code as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates DOMContentLoaded -->
    
    <html lang="en">
        <head>
            <script>
    
                document.addEventListener('DOMContentLoaded', function() {
                    document.querySelector('form').addEventListener('submit', function(e) {
                        alert('hello, ' + document.querySelector('#name').value);
                        e.preventDefault();
                    });
                });
    
            </script>
            <title>hello</title>
        </head>
        <body>
            <form>
                <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
                <input type="submit">
            </form>
        </body>
    </html>
    ```
    
    Notice that this version of the code creates an `addEventListener` to listen to the form `submit` being triggered. Notice how `DOMContentLoaded` ensures that the whole page is loaded before executing the JavaScript.
    
+   JavaScript allows you to dynamically read and modify the html document loaded into memory such that the user need not reload to see changes.
+   Consider the following HTML:
    
    ```auto
    <!DOCTYPE html>
    
    <!-- Demonstrates programmatic changes to style -->
    
    <html lang="en">
        <head>
            <title>background</title>
        </head>
        <body>
            <button id="red">R</button>
            <button id="green">G</button>
            <button id="blue">B</button>
            <script>
    
                let body = document.querySelector('body');
                document.querySelector('#red').addEventListener('click', function() {
                    body.style.backgroundColor = 'red';
                });
                document.querySelector('#green').addEventListener('click', function() {
                    body.style.backgroundColor = 'green';
                });
                document.querySelector('#blue').addEventListener('click', function() {
                    body.style.backgroundColor = 'blue';
                });
    
            </script>
        </body>
    </html>
    ```
    
    Notice that JavaScript listens for when a specific button is clicked. Upon such a click, certain style attributes on the page are changed. `body` is defined as the body of the page. Then, an event listener waits for the clicking of one of the buttons. Then, the `body.style.backgroundColor` is changed.
    
+   Similarly, consider the following:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <script>
    
                // Toggles visibility of greeting
                function blink()
                {
                    let body = document.querySelector('body');
                    if (body.style.visibility == 'hidden')
                    {
                        body.style.visibility = 'visible';
                    }
                    else
                    {
                        body.style.visibility = 'hidden';
                    }
                }
    
                // Blink every 500ms
                window.setInterval(blink, 500);
    
            </script>
            <title>blink</title>
        </head>
        <body>
            hello, world
        </body>
    </html>
    ```
    
    This example blinks a text at a set interval. Notice that `window.setInterval` takes in two arguments: A function to be called and a wait period (in milliseconds) between function calls.
    
+   Consider the following:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
    
        <head>
            <title>autocomplete</title>
        </head>
    
        <body>
    
            <input autocomplete="off" autofocus placeholder="Query" type="text">
    
            <ul></ul>
    
            <script src="large.js"></script>
            <script>
          
                let input = document.querySelector('input');
                input.addEventListener('keyup', function(event) {
                    let html = '';
                    if (input.value) {
                        for (word of WORDS) {
                            if (word.startsWith(input.value)) {
                                html += `<li>${word}</li>`;
                            }
                        }
                    }
                    document.querySelector('ul').innerHTML = html;
                });
    
            </script>
    
        </body>
    </html>
    ```
    
    This is a JavaScript implementation of autocomplete. This pulls from a file (not pictured here) called `large.js` that is a list of words.
    
+   Interestingly, we can also geolocate using JavaScript:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <title>geolocation</title>
        </head>
        <body>
            <script>
              
                navigator.geolocation.getCurrentPosition(function(position) {
                    document.write(position.coords.latitude + ", " + position.coords.longitude);
                });
    
            </script>
        </body>
    </html>
    ```
    
    Notice that `navigator.geolocation` is used to `getCurrentPosition`. This will not work if your computer or browser does not allow for location tracking.
    
+   The capabilities of JavaScript are many and can be found in the [JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript).

## Summing Up

In this lesson, you learned how to create your own HTML files, style them, leverage third-party frameworks, and utilize JavaScript. Specifically, we discussed…

+   TCP/IP
+   DNS
+   HTML
+   Regular expressions.
+   CSS
+   Frameworks
+   JavaScript

See you next time!


# Lecture 9-Flask



+   [Welcome!](#welcome)
+   [Static to Dynamic](#static-to-dynamic)
+   [Flask](#flask)
+   [Forms](#forms)
+   [Layout](#layout)
+   [POST](#post)
+   [Frosh IMs](#frosh-ims)
+   [Flask and SQL](#flask-and-sql)
+   [Session](#session)
+   [Shopping Cart](#shopping-cart)
+   [Shows](#shows)
+   [AJAX and APIs](#ajax-and-apis)
+   [JSON](#json)
+   [Summing Up](#summing-up)

## Welcome!

+   In previous weeks, you have learned numerous programming languages, techniques, and strategies.
+   Indeed, this class has been far less of a *C class* or *Python class* and far more of a *programming class*, such that you can go on to follow future trends.
+   In these past several weeks, you have learned *how to learn* about programming.
+   Today, we will be moving from HTML and CSS into combining HTML, CSS, SQL, Python, and JavaScript so you can create your own web applications.

## Static to Dynamic

+   Up until this point, all HTML you saw was pre-written and static.
+   In the past, when you visited a page, the browser downloaded an HTML page, and you were able to view it. These are considered *static* pages, in that what programmed in the HTML is exactly what the user sees and downloads to their internet browser.
+   Dynamic pages refer to the ability of Python and similar languages to create HTML files on-the-fly. Accordingly, you can have web pages that are generated by options selected by your user.
+   You have used `http-server` in the past to serve your web pages. Today, we are going to utilize a new server that can parse out a web address and perform actions based on the URL provided.

## Flask

+   *Flask* is a third-party library that allows you to host web applications using the Flask framework, or a micro-framework, within Python.
+   You can run flask by executing `flask run` in your terminal window in [cs50.dev](https://cs50.dev/).
+   To do so, you will need a file called `app.py` and a folder called `templates`.
+   To get started, create a folder called `templates` and create a file called `index.html` with the following code:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>hello</title>
        </head>
        <body>
            hello, {{ name }}
        </body>
    </html>
      
    ```
    
    Notice the double `{{ name }}` that is a placeholder for something that will be later provided by our Flask server.
    
+   Then, in the same folder that the `templates` folder appears, create a file called `app.py` and add the following code:
    
    ```auto
    # Uses request.args.get
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    
    @app.route("/")
    def index():
        name = request.args.get("name", "world")
        return render_template("index.html", name=name)
    ```
    
    +   Notice that this code defines `app` as the Flask application. Then, it defines the `/` route of `app` as returning the contents of `index.html` with the argument of `name`. By default, the `request.args.get` function will look for the `name` being provided by the user. If no name is provided, it will default to `world`.
    +   `@app.route` is otherwise known as a decorator.
+   Finally, add a final file in the same folder as `app.py` called `requirements.txt` that has only a single line of code:
    
    Notice only `Flask` appears in this file.
    
+   You can run this file by typing `flask run` in the terminal window. If Flask does not run, ensure that your syntax is correct in each of the files above. Further, if Flask will not run, make sure your files are organized as follows:
    
    ```auto
    /templates
        index.html
    app.py
    requirements.txt
    ```
    
+   Once you get it running, you will be prompted to click a link. Once you navigate to that webpage, try adding `?name=[Your Name]` to the base URL in your browser’s URL bar.

## Forms

+   Improving upon our program, we know that most users will not type arguments into the address bar. Instead, programmers rely upon users to fill out forms on web pages. Accordingly, we can modify index.html as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>hello</title>
        </head>
        <body>
            <form action="/greet" method="get">
                <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
                <button type="submit">Greet</button>
            </form>
        </body>
    </html>
    ```
    
    Notice that a form is now created that takes the user’s name and then passes it off to a route called `/greet`.
    
+   Further, we can change `app.py` as follows:
    
    ```auto
    # Adds a form, second route
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    
    @app.route("/greet")
    def greet():
        return render_template("greet.html", name=request.args.get("name", "world"))
    ```
    
    Notice that the default path will display a form for the user to input their name. The `/greet` route will pass the `name` to that web page.
    
+   To finalize this implementation, you will need another template for `greet.html` in the `templates` folder as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>hello</title>
        </head>
        <body>
            hello, {{ name }}
        </body>
    </html>
    ```
    
    Notice that this route will now render the greeting to the user, followed by their name.
    

## Layout

+   Both of our web pages, `index.html` and `greet.html`, have much of the same data. Wouldn’t it be nice to allow the body to be unique, but copy the same layout from page to page?
+   First, create a new template called `layout.html` and write code as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>hello</title>
        </head>
        <body>
            {% block body %}{% endblock %}
        </body>
    </html>
    ```
    
    Notice that the `{% block body %}{% endblock %}` allows for the insertion of other code from other HTML files.
    
+   Then, modify your `index.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
    
        <form action="/greet" method="get">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
            <button type="submit">Greet</button>
        </form>
    
    {% endblock %}
    ```
    
    Notice that the line `{% extends "layout.html" %}` tells the server where to get the layout of this page. Then, the `{% block body %}{% endblock %}` tells what code to be inserted into `layout.html`.
    
+   Finally, change `greet.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        hello, {{ name }}
    {% endblock %}
    ```
    
    Notice how this code is shorter and more compact.
    

## POST

+   You can imagine scenarios where it is not safe to utilize `get`, as usernames and passwords would show up in the URL.
+   We can utilize the method `post` to help with this problem by modifying `app.py` as follows:
    
    ```auto
    # Switches to POST
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    
    @app.route("/greet", methods=["POST"])
    def greet():
        return render_template("greet.html", name=request.form.get("name", "world"))
    ```
    
    Notice that `POST` is added to the `/greet` route, and that we use `request.form.get` rather than `request.args.get`.
    
+   This tells the server to look *deeper* in the virtual envelope and not reveal the items in `post` in the URL.
+   Still, this code can be advanced further by utilizing a single route for both `get` and `post`. To do this, modify `app.py` as follows:
    
    ```auto
    # Uses a single route
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            return render_template("greet.html", name=request.form.get("name", "world"))
        return render_template("index.html")
    ```
    
    Notice that both `get` and `post` are done in a single routing. However, `request.method` is utilized to properly route based upon the type of routing requested by the user.
    
+   Accordingly, you can modify your `index.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
    
        <form action="/" method="post">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
            <button type="submit">Greet</button>
        </form>
    
    {% endblock %}
    ```
    
    Notice that the form `action` is changed.
    
+   Still, there is a bug still in this code. With our new implementation, when someone types in no name into the form, `Hello,` is displayed without a name. We can improve our code by editing `app.py` as follows:
    
    ```auto
    # Moves default value to template
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            return render_template("greet.html", name=request.form.get("name"))
        return render_template("index.html")
    ```
    
    Notice that `name=request.form.get("name"))` is changed.
    
+   Finally, change `greet.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
    
        hello, {% if name %}{{ name }}{% else %}world{% endif %}
    
    {% endblock %}
    ```
    
    Notice how `hello,` is changed to allow for a default output when no name is identified.
    
+   As we’ve been changing many files, you may wish to compare your final code with [our final code](https://cdn.cs50.net/2023/fall/lectures/9/src9/hello8/).

## Frosh IMs

+   Frosh IMs or *froshims* is a web application that allows students to register for intramural sports.
+   Close all your `hello` related windows and create a folder by typing `mkdir froshims` in the terminal window. Then, type `cd froshims` to browse to this folder. Within, create a directory called templates by typing `mkdir templates`. Finally, type `code app.py` and write code as follows:
    
    ```auto
    # Implements a registration form using a select menu, validating sport server-side
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    SPORTS = [
        "Basketball",
        "Soccer",
        "Ultimate Frisbee"
    ]
    
    
    @app.route("/")
    def index():
        return render_template("index.html", sports=SPORTS)
    
    
    @app.route("/register", methods=["POST"])
    def register():
    
        # Validate submission
        if not request.form.get("name") or request.form.get("sport") not in SPORTS:
            return render_template("failure.html")
    
        # Confirm registration
        return render_template("success.html")
    ```
    
    Notice that a `failure` option is provided, such that a failure message will be displayed to the user if the `name` or `sport` field is not properly filled out.
    
+   Next, create a file in the `templates` folder called `index.html` by typing `code templates/index.html` and write code as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        <h1>Register</h1>
        <form action="/register" method="post">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
            <select name="sport">
                <option disabled selected value="">Sport</option>
                {% for sport in sports %}
                    <option value="{{ sport }}">{{ sport }}</option>
                {% endfor %}
            </select>
            <button type="submit">Register</button>
        </form>
    {% endblock %}
    ```
    
+   Next, create a file called `layout.html` by typing `code templates/layout.html` and write code as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>froshims</title>
        </head>
        <body>
            {% block body %}{% endblock %}
        </body>
    </html>
    ```
    
+   Fourth, create a file in templates called `success.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        You are registered!
    {% endblock %}
    ```
    
+   Finally, create a file in templates called `failure.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        You are not registered!
    {% endblock %}
    ```
    
+   You can imagine how we might want to see the various registration options using radio buttons. We can improve `index.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        <h1>Register</h1>
        <form action="/register" method="post">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
            {% for sport in sports %}
                <input name="sport" type="radio" value="{{ sport }}"> {{ sport }}
            {% endfor %}
            <button type="submit">Register</button>
        </form>
    {% endblock %}
    ```
    
+   Executing `flask run` you can see how the interface has now changed.
+   We can further improve upon our program by enabling checkboxes. Modify `index.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        <h1>Register</h1>
        <form action="/register" method="post">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
            {% for sport in sports %}
                <input name="sport" type="checkbox" value="{{ sport }}"> {{ sport }}
            {% endfor %}
            <button type="submit">Register</button>
        </form>
    {% endblock %}
    ```
    
    Notice that `type` is changed to `checkbox`.
    
+   To implement this, we will need to modify `app.py`:
    
    ```auto
    # Implements a registration form using checkboxes
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    SPORTS = [
        "Basketball",
        "Soccer",
        "Ultimate Frisbee"
    ]
    
    
    @app.route("/")
    def index():
        return render_template("index.html", sports=SPORTS)
    
    
    @app.route("/register", methods=["POST"])
    def register():
    
        # Validate submission
        if not request.form.get("name"):
            return render_template("failure.html")
        for sport in request.form.getlist("sport"):
            if sport not in SPORTS:
                return render_template("failure.html")
    
        # Confirm registration
        return render_template("success.html")
    ```
    
    Notice how `for sport in` allows iteration through all the sports selected by the user.
    
+   You can imagine how we might want to accept the registration of many different registrants. We can improve `app.py` as follows:
    
    ```auto
    # Implements a registration form, storing registrants in a dictionary, with error messages
    
    from flask import Flask, redirect, render_template, request
    
    app = Flask(__name__)
    
    REGISTRANTS = {}
    
    SPORTS = [
        "Basketball",
        "Soccer",
        "Ultimate Frisbee"
    ]
    
    
    @app.route("/")
    def index():
        return render_template("index.html", sports=SPORTS)
    
    
    @app.route("/register", methods=["POST"])
    def register():
    
        # Validate name
        name = request.form.get("name")
        if not name:
            return render_template("error.html", message="Missing name")
    
        # Validate sport
        sport = request.form.get("sport")
        if not sport:
            return render_template("error.html", message="Missing sport")
        if sport not in SPORTS:
            return render_template("error.html", message="Invalid sport")
    
        # Remember registrant
        REGISTRANTS[name] = sport
    
        # Confirm registration
        return redirect("/registrants")
    
    
    @app.route("/registrants")
    def registrants():
        return render_template("registrants.html", registrants=REGISTRANTS)
    ```
    
    Notice that a dictionary called `REGISTRANTS` is used to log the `sport` selected by `REGISTRANTS[name]`. Also, notice that `registrants=REGISTRANTS` passes the dictionary on to this template.
    
+   Additionally, we can implement `error.html`:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        <h1>Error</h1>
        <p>{{ message }}</p>
        <img alt="Grumpy Cat" src="/static/cat.jpg">
    {% endblock %}
    ```
    
+   Further, create a new template called `registrants.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        <h1>Registrants</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Sport</th>
                </tr>
            </thead>
            <tbody>
                {% for name in registrants %}
                    <tr>
                        <td>{{ name }}</td>
                        <td>{{ registrants[name] }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endblock %}
    ```
    
    Notice that `{% for name in registrants %}...{% endfor %}` will iterate through each of the registrants. Very powerful to be able to iterate on a dynamic web page!
    
+   You now have a web application! However, there are some security flaws! Because everything is client-side, an adversary could change the HTML and *hack* a website. Further, this data will not persist if the server is shut down. Could there be some way we could have our data persist even when the server restarts?

## Flask and SQL

+   Just as we have seen how Python can interface with a SQL database, we can combine the power of Flask, Python, and SQL to create a web application where data will persist!
+   To implement this, you will need to take a number of steps.
+   First, modify `requirements.txt` as follows:
    
+   Modify `index.html` as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        <h1>Register</h1>
        <form action="/register" method="post">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
            {% for sport in sports %}
                <input name="sport" type="radio" value="{{ sport }}"> {{ sport }}
            {% endfor %}
            <button type="submit">Register</button>
        </form>
    {% endblock %}
    ```
    
+   Modify `layout.html` as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>froshims</title>
        </head>
        <body>
            {% block body %}{% endblock %}
        </body>
    </html>
    ```
    
+   Ensure `failure.html` appears as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        You are not registered!
    {% endblock %}
    ```
    
+   Modify `registrants.html` to appear as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
        <h1>Registrants</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Sport</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {% for registrant in registrants %}
                    <tr>
                        <td>{{ registrant.name }}</td>
                        <td>{{ registrant.sport }}</td>
                        <td>
                            <form action="/deregister" method="post">
                                <input name="id" type="hidden" value="{{ registrant.id }}">
                                <button type="submit">Deregister</button>
                            </form>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endblock %}
    ```
    
    Notice that a hidden value `registrant.id` is included such that it’s possible to use this `id` later in `app.py`
    
+   Finally, modify `app.py` as follows:
    
    ```auto
    # Implements a registration form, storing registrants in a SQLite database, with support for deregistration
    
    from cs50 import SQL
    from flask import Flask, redirect, render_template, request
    
    app = Flask(__name__)
    
    db = SQL("sqlite:///froshims.db")
    
    SPORTS = [
        "Basketball",
        "Soccer",
        "Ultimate Frisbee"
    ]
    
    
    @app.route("/")
    def index():
        return render_template("index.html", sports=SPORTS)
    
    
    @app.route("/deregister", methods=["POST"])
    def deregister():
    
        # Forget registrant
        id = request.form.get("id")
        if id:
            db.execute("DELETE FROM registrants WHERE id = ?", id)
        return redirect("/registrants")
    
    
    @app.route("/register", methods=["POST"])
    def register():
    
        # Validate submission
        name = request.form.get("name")
        sport = request.form.get("sport")
        if not name or sport not in SPORTS:
            return render_template("failure.html")
    
        # Remember registrant
        db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
    
        # Confirm registration
        return redirect("/registrants")
    
    
    @app.route("/registrants")
    def registrants():
        registrants = db.execute("SELECT * FROM registrants")
        return render_template("registrants.html", registrants=registrants)
    ```
    
    Notice that the `cs50` library is utilized. A route is included for `register` for the `post` method. This route will take the name and sport taken from the registration form and execute a SQL query to add the `name` and the `sport` to the `registrants` table. The `deregister` routes to a SQL query that will grab the user’s `id` and utilize that information to deregister this individual.
    
+   You can read more in the [Flask documentation](https://flask.palletsprojects.com/).

## Session

+   While the above code is useful from an administrative standpoint, where a back-office administrator could add and remove individuals from the database, one can imagine how this code is not safe to implement on a public server.
+   For one, bad actors could make decisions on behalf of other users by hitting the deregister button – effectively deleting their recorded answer from the server.
+   Web services like Google use login credentials to ensure users only have access to the right data.
+   We can actually implement this itself using *cookies*. Cookies are small files that are stored on your computer, such that your computer can communicate with the server and effectively say, “I’m an authorized user that has already logged in.” This authorization through this cookie is called a *session*.
+   In the simplest form, we can implement this by creating a folder called `login` and then adding the following files.
+   First, create a file called `requirements.txt` that reads as follows:
    
    Notice that in addition to `Flask`, we also include `Flask-Session`, which is required to support login sessions.
    
+   Second, in a `templates` folder, create a file called `layout.html` that appears as follows:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>login</title>
        </head>
        <body>
            {% block body %}{% endblock %}
        </body>
    </html>
    ```
    
    Notice this provides a very simple layout with a title and a body.
    
+   Third, create a file in the `templates` folder called `index.html` that appears as follows:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
    
        {% if name %}
            You are logged in as {{ name }}. <a href="/logout">Log out</a>.
        {% else %}
            You are not logged in. <a href="/login">Log in</a>.
        {% endif %}
    
    {% endblock %}
    ```
    
    Notice that this file looks to see if `session["name"]` exists (elaborated further in `app.py` below). If it does, it will display a welcome message. If not, it will recommend you browse to a page to log in.
    
+   Fourth, create a file called `login.html` and add the following code:
    
    ```auto
    {% extends "layout.html" %}
    
    {% block body %}
    
        <form action="/login" method="post">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
            <button type="submit">Log In</button>
        </form>
    
    {% endblock %}
    ```
    
    Notice this is the layout of a basic login page.
    
+   Finally, create a file called `app.py` and write code as follows:
    
    ```auto
    from flask import Flask, redirect, render_template, request, session
    from flask_session import Session
    
    # Configure app
    app = Flask(__name__)
    
    # Configure session
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    
    
    @app.route("/")
    def index():
        return render_template("index.html", name=session.get("name"))
    
    
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            session["name"] = request.form.get("name")
            return redirect("/")
        return render_template("login.html")
    
    
    @app.route("/logout")
    def logout():
        session.clear()
        return redirect("/")
    ```
    
    Notice the modified *imports* at the top of the file, including `session`, which will allow for you to support sessions. Most important, notice how `session["name"]` is used in the `login` and `logout` routes. The `login` route will assign the login name provided and assign it to `session["name"]`. However, in the `logout` route, the logging out is implemented by clearing the value of `session`.
    
+   You can read more about sessions in the [Flask documentation](https://flask.palletsprojects.com/en/2.2.x/api/?highlight=session#flask.session).

## Shopping Cart

+   Moving on to a final example of utilizing Flask’s ability to enable a session.
+   We examined the following code for `store` in `app.py`. The following code was shown:
    
    ```auto
    from cs50 import SQL
    from flask import Flask, redirect, render_template, request, session
    from flask_session import Session
    
    # Configure app
    app = Flask(__name__)
    
    # Connect to database
    db = SQL("sqlite:///store.db")
    
    # Configure session
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    
    
    @app.route("/")
    def index():
        books = db.execute("SELECT * FROM books")
        return render_template("books.html", books=books)
    
    
    @app.route("/cart", methods=["GET", "POST"])
    def cart():
    
        # Ensure cart exists
        if "cart" not in session:
            session["cart"] = []
    
        # POST
        if request.method == "POST":
            book_id = request.form.get("id")
            if book_id:
                session["cart"].append(book_id)
            return redirect("/cart")
    
        # GET
        books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
        return render_template("cart.html", books=books)
    ```
    
    Notice that `cart` is implemented using a list. Items can be added to this list using the `Add to Cart` buttons in `books.html`. When clicking such a button, the `post` method is invoked, where the `id` of the item is appended to the `cart`. When viewing the cart, invoking the `get` method, SQL is executed to display a list of the books in the cart.
    
+   You can see the rest of the files that power this `flask` implementation in the [source code](https://cdn.cs50.net/2023/fall/lectures/9/src9/).

## Shows

+   We looked at a pre-designed program called `shows`, in `app.py`:
    
    ```auto
    # Searches for shows using LIKE
    
    from cs50 import SQL
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    db = SQL("sqlite:///shows.db")
    
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    
    @app.route("/search")
    def search():
        shows = db.execute("SELECT * FROM shows WHERE title LIKE ?", "%" + request.args.get("q") + "%")
        return render_template("search.html", shows=shows)
    ```
    
    Notice how the `search` route allows for a way by which to search for a `show`. This search looks for titles `LIKE` the one provided by the user.
    
+   You can see the rest of the files of this implementation in the [source code](https://cdn.cs50.net/2023/fall/lectures/9/src9/).
    

## AJAX and APIs

+   An *application program interface* or *API* is a series of specifications that allow you to interface with another service. For example, we could utilize IMDB’s API to interface with their database. We might even integrate APIs for handling specific types of data downloadable from a server.
+   Improving upon `shows`, looking at an improvement of `app.py`, we saw the following:
    
    ```auto
    # Searches for shows using Ajax
    
    from cs50 import SQL
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    db = SQL("sqlite:///shows.db")
    
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    
    @app.route("/search")
    def search():
        q = request.args.get("q")
        if q:
            shows = db.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%")
        else:
            shows = []
        return render_template("search.html", shows=shows)
    ```
    
    Notice that the `search` route executes a SQL query.
    
+   Looking at `search.html`, you’ll notice that it is very simple:
    
    ```auto
    {% for show in shows %}
        <li>{{ show["title"] }}</li>
    {% endfor %}
    ```
    
    Notice that it provides a bulleted list.
    
+   Finally, looking at `index.html`, notice that *AJAX* code is utilized to power the search:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>shows</title>
        </head>
        <body>
    
            <input autocomplete="off" autofocus placeholder="Query" type="search">
    
            <ul></ul>
    
            <script>
          
                let input = document.querySelector('input');
                input.addEventListener('input', async function() {
                    let response = await fetch('/search?q=' + input.value);
                    let shows = await response.text();
                    document.querySelector('ul').innerHTML = shows;
                });
    
            </script>
    
        </body>
    </html>
    ```
    
    Notice an event listener is utilized to dynamically query the server to provide a list that matches the title provided. This will locate the `ul` tag in the HTML and modify the web page accordingly to include the list of the matches.
    
+   You can read more in the [AJAX documentation](https://api.jquery.com/category/ajax/).

## JSON

+   *JavaScript Object Notation* or *JSON* is text file of dictionaries with keys and values. This is a raw, computer-friendly way to get lots of data.
+   JSON is a very useful way of getting back data from the server.
+   You can see this in action in the `index.html` we examined together:
    
    ```auto
    <!DOCTYPE html>
    
    <html lang="en">
        <head>
            <meta name="viewport" content="initial-scale=1, width=device-width">
            <title>shows</title>
        </head>
        <body>
    
            <input autocomplete="off" autofocus placeholder="Query" type="text">
    
            <ul></ul>
    
            <script>
          
                let input = document.querySelector('input');
                input.addEventListener('input', async function() {
                    let response = await fetch('/search?q=' + input.value);
                    let shows = await response.json();
                    let html = '';
                    for (let id in shows) {
                        let title = shows[id].title.replace('<', '&lt;').replace('&', '&amp;');
                        html += '<li>' + title + '</li>';
                    }
                    document.querySelector('ul').innerHTML = html;
                });
    
            </script>
    
        </body>
    </html>
    ```
    
    While the above may be somewhat cryptic, it provides a starting point for you to research JSON on your own to see how it can be implemented in your own web applications.
    
+   Further, we examined `app.py` to see how the JSON response is obtained:
    
    ```auto
    # Searches for shows using Ajax with JSON
    
    from cs50 import SQL
    from flask import Flask, jsonify, render_template, request
    
    app = Flask(__name__)
    
    db = SQL("sqlite:///shows.db")
    
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    
    @app.route("/search")
    def search():
        q = request.args.get("q")
        if q:
            shows = db.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%")
        else:
            shows = []
        return jsonify(shows)
    ```
    
    Notice how `jsonify` is used to convert the result into a readable format acceptible by contemporary web applications.
    
+   You can read more in the [JSON documentation](https://www.json.org/json-en.html).

## Summing Up

In this lesson, you learned how to utilize Python, SQL, and Flask to create web applications. Specifically, we discussed…

+   GET
+   POST
+   Flask
+   Session
+   APIs
+   AJAX
+   JSON

See you next time for our final lecture!



# Lecture 10-Cybersecurity

## Cybersecurity

+   [Recap](#recap)
+   [Looking Ahead](#looking-ahead)
+   [Cybersecurity](#cybersecurity-1)
+   [Passwords](#passwords)
+   [Phone Security](#phone-security)
+   [Password Managers](#password-managers)
+   [Two-factor Authentication](#two-factor-authentication)
+   [Hashing](#hashing)
+   [Cryptography](#cryptography)
+   [Passkeys](#passkeys)
+   [Encryption](#encryption)
+   [Deletion](#deletion)
+   [Summing Up](#summing-up)

## Recap

+   Over these past ten weeks, you have been drinking from the proverbial firehose.
+   While in this course, you learned how to program many programming languages; indeed, our great hope is that you *learned how to program* in all: Regardless of the programming language.
+   Further, we hope that you *learned how to solve problems* above all else.

## Looking Ahead

+   As you journey from the work of this course to the world outside CS50, you may want to take a number of steps to prepare.
+   To be able to execute commands on the terminal, much like you did on [CS50.dev](https://cs50.dev/), you can install command-line tools on your [Mac](https://developer.apple.com/xcode/) or [PC](https://learn.microsoft.com/en-us/windows/wsl/about).
+   You can learn more about [Git](https://youtu.be/MJUJ4wbFm_A).
+   You can [download](https://code.visualstudio.com/) and [learn](https://cs50.readthedocs.io/cs50.dev/) about VS Code.
+   You can host a website using [GitHub](https://pages.github.com/) or [Netlify](https://www.netlify.com/).
+   You can host a web app using [AWS](https://aws.amazon.com/education/awseducate/), [Azure](https://azure.microsoft.com/en-us/free/students/), or [Google Cloud](https://cloud.google.com/edu/students).
+   You can ask questions in relevant online communities.
+   You can ask questions using AI-based tools like [OpenAI](https://chat.openai.com/) and [GitHub Copilot](https://github.com/features/copilot).
+   You can take any of our other CS50 courses.
+   You can join one of our many [communities](https://cs50.harvard.edu/communities).

## Cybersecurity

+   Today will be a high-level overview of some of the cybersecurity-related topics.
+   Cybersecurity is understanding how our data is *secure* or *not secure*.

## Passwords

+ One cybersecurity concern relates to our passwords.

+ Passwords are one method used to secure data online.

+ There are common passwords that people use:

  ```auto
  1. 123456
  2. admin
  3. 12345678
  4. 123456789
  5. 1234
  6. 12345
  7. password
  8. 123
  9. Aa123456
  10. 1234567890
  ```

+ If you have one of the passwords above, most likely, millions of people have the same password as you!

+ Adversaries in the world will start with this list.

+ Bad guys can also guess most of the heuristics you use to add symbols to your password.

+ Adversaries can use *brute-force attacks*, using a dictionary of passwords to simply try every possible password.

+ Your password is likely not as secure as you think it is.

## Phone Security

+ Many phones are secured by a four-digit code.

+ The most simple form of attack would be to brute-force attempt all possible passwords.

+ There are 10,000 possible passwords when using a four-digit code.

+ If it takes one guess per second, it will take 10,000 seconds to crack the password.

+ However, if a programmer creates a program to generate all possible codes, the time required would be minimal. Consider the following code in Python:

  ```auto
  from string import digits
  from itertools import product
  
  for passcode in product(digits, repeat=4):
      print(passcode)
  ```

+ It should be quite disconcerting that the code above could take only a few seconds (at most!) to discover your password.

+ We could improve our security by switching to a four-letter password. This would result in 7,311,616 possible passwords.

+ Including uppercase and lowercase characters would create over 78 million possibilities.

+ Consider how we could modify your code to discover these passwords:

  ```auto
  from string import ascii_letters
  from itertools import product
  
  for passcode in product(ascii_letters, repeat=4):
      print(passcode)
  ```

+ We could even add the ability to look at all possible eight-digit passwords with letters, numbers, and punctuations:

  ```auto
  from string import ascii_letters, digits, punctuation
  from itertools import product
  
  for passcode in product(ascii_letters + digits + punctuation, repeat=8):
      print(passcode)
  ```

+ Expanding to eight characters, including upper and lowercase letters, numbers, and symbols, would result in 6,095,689,385,410,816 possible combinations.

+ In the digital world, you simply want your password to be better than other peoples’ passwords such that others would be attacked far before you—as you are a much less convenient target.

+ A downside of using such a long password is the downside of having to remember it.

+ Accordingly, there are other defenses that could be employed to slow down an attacker. For example, some phone manufacturers lock out those who guess a password incorrectly.

+ Security is about finding a “sweet spot” between the trade-offs of enhanced security while maintaining convenience.

## Password Managers

+   Password managers can be used to create very challenging passwords and remember them for you.
+   The probability of a password secured by a password manager being broken is very, very low.
+   You’d hope that such password managers are secure. However, if one gains access to your password manager, they would have access to all your passwords.
+   In the end, you are far less likely to be at risk by those you live with—and much more likely to be at risk by the billions of other people on the internet.
+   As mentioned prior, you can make a decision based on a balance between security and convenience.

## Two-factor Authentication

+   Adding another means by which you must authenticate adds further security. However, there is a human cost as you might not have access to your second factor.
+   These are implemented as one-time passwords of sorts that are sent to an email, device, or phone number.
+   Always, security policies attempt to balance the needs of security and human convenience.

## Hashing

+ Your account information and other sensitive data should not be stored as raw text in an online database.

+ If a database becomes compromised and all credentials are stored in plain text, credentials for other services at other websites are likely also compromised.

+ Hence, hashing algorithms, as discussed earlier in this course, are used to store only hashed values of passwords.

+ One-way hashing allows online services to actually *never* store the original password typed by the user: Only the hashed value of these passwords. Accordingly, if there is a breach, only the hashed value will be known.

+ *Rainbow tables* are huge dictionaries that adversaries use to attempt to pre-hash possible passwords as a means by which to attempt to break the hash algorithm.

+ As an additional process to heightened security, programmers may sometimes introduce *salting* where it becomes unlikely that multiple users may have the same hash value to represent their passwords. You can imagine this as follows:

  ![salt and password being fed to an algorithm outputting a hash](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week10Slide106.png)

## Cryptography

+   Similar to hashing, a cipher algorithm can use a *public key* and text to create ciphertext.
+   In turn, a *private key* and the ciphertext can be fed to the algorithm to decrypt the text.

## Passkeys

+ Passkeys are a new technology only emerging in the most recent months.

+ Through private keys and a challenge being fed to an algorithm, websites can authenticate you through the unique signature created by your device.

  ![public key and challenge being provided to an alogirthm resulting in a signature](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week10Slide125.png)

+ Hence, passwords and usernames may soon become obsolete.

## Encryption

+   Encryption is a way by which data is obscured such that only the sender and intended receiver can be read.
+   Early in this course, we learned a very simple algorithm to “shift” the text by one or more characters as a rudimentary form of encryption.
+   *End-to-end encryption* is a way by which encrypting and decrypting happen on the same system without a middleman. This prevents the middleman or a malicious actor from being able to snoop on your data. Zoom and Apple Messages can both utilize end-to-end encryption.

## Deletion

+ Trashing a file on your computer or emptying the trash can does not actually delete the actual bits of the file on your computer.

+ Instead, remnants of the files are left.

  ![remnants of a file on a hard drive](https://picbox-1313243162.cos.ap-nanjing.myqcloud.com/cs50Week10Slide136.png)

+ *Secure deletion* is where the remnants of those files are turned into zeros and ones.

+ Still, some remnants may remain because of what is rendered inaccessible by the operating system.

+ *Full-disk encryption* allows your entire hard drive to be encrypted. Thus, your deleted files are less accessible to adversaries.

+ Considering encryption, it’s this same technology that adversaries use to create *ransomware* that can, quite literally, hold your hard drive for ransom.

## Summing Up

+   Use a password manager.
+   Use two-factor authentication.
+   Use (end-to-end) encryption.

