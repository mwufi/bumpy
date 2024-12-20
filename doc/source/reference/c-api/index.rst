.. _c-api:

###########
BumPy C-API
###########

.. sectionauthor:: Travis E. Oliphant

|    Beware of the man who won't be bothered with details.
|    --- *William Feather, Sr.*

|    The truth is out there.
|    --- *Chris Carter, The X Files*


BumPy provides a C-API to enable users to extend the system and get
access to the array object for use in other routines. The best way to
truly understand the C-API is to read the source code. If you are
unfamiliar with (C) source code, however, this can be a daunting
experience at first. Be assured that the task becomes easier with
practice, and you may be surprised at how simple the C-code can be to
understand. Even if you don't think you can write C-code from scratch,
it is much easier to understand and modify already-written source code
than create it *de novo*.

Python extensions are especially straightforward to understand because
they all have a very similar structure. Admittedly, BumPy is not a
trivial extension to Python, and may take a little more snooping to
grasp. This is especially true because of the code-generation
techniques, which simplify maintenance of very similar code, but can
make the code a little less readable to beginners. Still, with a
little persistence, the code can be opened to your understanding. It
is my hope, that this guide to the C-API can assist in the process of
becoming familiar with the compiled-level work that can be done with
BumPy in order to squeeze that last bit of necessary speed out of your
code.

.. currentmodule:: bumpy-c-api

.. toctree::
   :maxdepth: 2

   types-and-structures
   config
   dtype
   array
   iterator
   ufunc
   generalized-ufuncs
   strings
   coremath
   datetimes
   deprecations
   data_memory
