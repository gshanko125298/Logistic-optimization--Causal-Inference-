# Unit testing
Unit testing is a technique in which particular module is tested to check by developer himself whether there are any errors. The primary focus of unit testing is test an individual unit of system to analyze, detect, and fix the errors.
Unit testing is a method for testing software that looks at the smallest testable pieces of code, called units, which are tested for correct operation. By doing unit testing, we can verify that each part of the code, including helper functions that may not be exposed to the user, works correctly and as intended.

The idea is that we are independently checking each small piece of our program to ensure that it works. This contrasts with regression and integration testing, which tests that the different parts of the program work well together and as intended.

In this post, you will discover how to implement unit testing in Python using two popular unit testing frameworks: the built-in PyUnit framework and the PyTest framework.

After completing this tutorial, you will know:

    Unit testing libraries in Python such as PyUnit and PyTest
    Checking expected function behavior through the use of unit tests
    Unit Tests vs. Integration Tests
The world of testing has no shortage of terminology, and now that you know the difference between automated and manual testing, it’s time to go a level deeper.

Think of how you might test the lights on a car. You would turn on the lights (known as the test step) and go outside the car or ask a friend to check that the lights are on (known as the test assertion). Testing multiple components is known as integration testing.

Think of all the things that need to work correctly in order for a simple task to give the right result. These components are like the parts to your application, all of those classes, functions, and modules you’ve written.

A major challenge with integration testing is when an integration test doesn’t give the right result. It’s very hard to diagnose the issue without being able to isolate which part of the system is failing. If the lights didn’t turn on, then maybe the bulbs are broken. Is the battery dead? What about the alternator? Is the car’s computer failing?

If you have a fancy modern car, it will tell you when your light bulbs have gone. It does this using a form of unit test.