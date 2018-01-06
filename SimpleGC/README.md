SimpleGC
========

Challenge description:
```
SimpleGC (107)
Solves: 47
memory management in C does not have to be hard

Files: Link

Difficulty: easy

Connect: nc 35.198.176.224 1337
```

This is a classical menu based challenge with six options:
 - Create player (assigned to a team)
 - Display player
 - Display team
 - Edit team
 - Delete player
 - Exit

We started out writing the skeleton for our pwn script, code to interact with the application and afterwards went to do some static analysis on the code. 

Reversing the create player function gives us the following structs that are used in the code:

```c

Group {
  char* name_ptr; // 24 bytes
  unsigned char refCount
}

User {
  unsigned int age;
  char* name_ptr; // at most 192 bytes
  char* grp_name_ptr; 
}
```

When we edit a player we are given the option to propagate
