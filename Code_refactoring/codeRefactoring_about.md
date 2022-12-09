# CODE REFACTORING - CLEAN CODE


---


## LINKS

[Behavior-driven development](https://en.wikipedia.org/wiki/Behavior-driven_development)
[Refactoring](https://refactoring.guru/refactoring)


---


## CLEAN CODE

The main purpose of refactoring is to fight technical debt. It transforms a mess into clean code and simple design.


**1. Clean code is obvious for other programmers.**

    Poor variable naming, bloated classes and methods, magic numbers -you name it- all of that makes code sloppy and difficult to grasp.


**2. Clean code doesn’t contain duplication.**

    Each time you have to make a change in a duplicate code, you have to remember to make the same change to every instance. This increases the cognitive load and slows down the progress.


**3. Clean code contains a minimal number of classes and other moving parts.**

    Less code is less stuff to keep in your head. Less code is less maintenance. Less code is fewer bugs. Code is liability, keep it short and simple.


**4. Clean code passes all tests.**
   
    You know your code is dirty when only 95% of your tests passed. You know you’re screwed when you test coverage is 0%.


**5. Clean code is easier and cheaper to maintain!**



---


## TECHNICAL DEBT

Everyone does their best to write excellent code from scratch. There probably isn’t a programmer out there who intentionally writes unclean code to the detriment of the project. But at what point does clean code become unclean?

You can temporarily speed up without writing tests for new features, but this will gradually slow your progress every day until you eventually pay off the debt by writing tests.



---


## CUASES OF TECHNICAL DEBT

**1. Business pressure**

    Sometimes business circumstances might force you to roll out features before they’re completely finished. In this case, patches and kludges will appear in the code to hide the unfinished parts of the project.


**2. Lack of understanding of the consequences of technical debt**

    Sometimes your employer might not understand that technical debt has “interest” insofar as it slows down the pace of development as debt accumulates. This can make it too difficult to dedicate the team’s time to refactoring because management doesn’t see the value of it.


**3. Failing to combat the strict coherence of components**

    This is when the project resembles a monolith rather than the product of individual modules. In this case, any changes to one part of the project will affect others. Team development is made more difficult because it’s difficult to isolate the work of individual members.


**4. Lack of tests**

    The lack of immediate feedback encourages quick, but risky workarounds or kludges. In worst cases, these changes are implemented and deployed right into the production without any prior testing. The consequences can be catastrophic. For example, an innocent-looking hotfix might send a weird test email to thousands of customers or even worse, flush or corrupt an entire database.


**5. Lack of documentation**

    This slows down the introduction of new people to the project and can grind development to a halt if key people leave the project.


**6. Lack of interaction between team members**

    If the knowledge base isn’t distributed throughout the company, people will end up working with an outdated understanding of processes and information about the project. This situation can be exacerbated when junior developers are incorrectly trained by their mentors.


**7. Long-term simultaneous development in several branches**

    This can lead to the accumulation of technical debt, which is then increased when changes are merged. The more changes made in isolation, the greater the total technical debt.


**8. Delayed refactoring**

    The project’s requirements are constantly changing and at some point it may become obvious that parts of the code are obsolete, have become cumbersome, and must be redesigned to meet new requirements.

    On the other hand, the project’s programmers are writing new code every day that works with the obsolete parts. Therefore, the longer refactoring is delayed, the more dependent code will have to be reworked in the future.


**9. Lack of compliance monitoring**

    This happens when everyone working on the project writes code as they see fit (i.e. the same way they wrote the last project).


**10. Incompetence**

    This is when the developer just doesn’t know how to write decent code.


---


## WHEN TO REFACTOR

**1. Rule of Three**

    When you’re doing something for the first time, just get it done.

    When you’re doing something similar for the second time, cringe at having to repeat but do the same thing anyway.

    When you’re doing something for the third time, start refactoring.


**2. When adding a feature**

    Refactoring helps you understand other people’s code. If you have to deal with someone else’s dirty code, try to refactor it first. Clean code is much easier to grasp. You will improve it not only for yourself but also for those who use it after you.

    Refactoring makes it easier to add new features. It’s much easier to make changes in clean code.


**3. When fixing a bug**

    Bugs in code behave just like those in real life: they live in the darkest, dirtiest places in the code. Clean your code and the errors will practically discover themselves.

    Managers appreciate proactive refactoring as it eliminates the need for special refactoring tasks later. Happy bosses make happy programmers!


**4. During a code review**

    The code review may be the last chance to tidy up the code before it becomes available to the public.

    It’s best to perform such reviews in a pair with an author. This way you could fix simple problems quickly and gauge the time for fixing the more difficult ones.



---


## HOW TO REFACTOR

Refactoring should be done as a series of small changes, each of which makes the existing code slightly better while still leaving the program in working order.


**1. The code should become cleaner.**

*   If the code remains just as unclean after refactoring... well, I’m sorry, but you’ve just wasted an hour of your life. Try to figure out why this happened.


*   It frequently happens when you move away from refactoring with small changes and mix a whole bunch of refactorings into one big change. So it’s very easy to lose your mind, especially if you have a time limit.

*   But it can also happen when working with extremely sloppy code. Whatever you improve, the code as a whole remains a disaster.

*   In this case, it’s worthwhile to think about completely rewriting parts of the code. But before that, you should have written tests and set aside a good chunk of time. Otherwise, you’ll end up with the kinds of results we talked about in the first paragraph.


**2. New functionality shouldn’t be created during refactoring.**

*   Don’t mix refactoring and direct development of new features. Try to separate these processes at least within the confines of individual commits.

 
**3. All existing tests must pass after refactoring.**

There are two cases when tests can break down after refactoring:

*    **You made an error during refactoring.** This one is a no-brainer: go ahead and fix the error.

*    **Your tests were too low-level.** For example, you were testing private methods of classes.

*    In this case, the tests are to blame. You can either refactor the tests themselves or write an entirely new set of higher-level tests. A great way to avoid this kind of a situation is to write `behavior-driven development BDD-style tests`.



---




